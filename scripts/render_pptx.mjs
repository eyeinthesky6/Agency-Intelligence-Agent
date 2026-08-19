#!/usr/bin/env node
/**
 * Render a client-review JSON file into a concise 6-slide PowerPoint.
 *
 * Usage:
 *   npm install
 *   node scripts/render_pptx.mjs path/to/client-review.json [output.pptx]
 */

import fs from "node:fs";
import path from "node:path";
import PptxGenJS from "pptxgenjs";

const input = process.argv[2];
if (!input) {
  console.error("Usage: node scripts/render_pptx.mjs <client-review.json> [output.pptx]");
  process.exit(2);
}

const output = process.argv[3] || input.replace(/\.json$/i, ".pptx");
const data = JSON.parse(fs.readFileSync(input, "utf8"));

const pptx = new PptxGenJS();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Agency Intelligence Agent";
pptx.subject = `Client intelligence review for ${data.client || "client"}`;
pptx.title = `${data.client || "Client"} — ${data.period || "Review"}`;
pptx.company = "Agency Intelligence Agent";
pptx.lang = "en-US";
pptx.theme = {
  headFontFace: "Aptos Display",
  bodyFontFace: "Aptos",
  lang: "en-US",
};

const C = {
  ink: "111827",
  muted: "6B7280",
  line: "E5E7EB",
  soft: "F3F4F6",
  accent: "2563EB",
  white: "FFFFFF",
  good: "047857",
  warn: "B45309",
};

const margin = 0.65;

function addHeader(slide, eyebrow, title, subtitle = "") {
  slide.addText(eyebrow.toUpperCase(), {
    x: margin, y: 0.42, w: 5.5, h: 0.22,
    fontFace: "Aptos", fontSize: 9, bold: true, color: C.accent,
    charSpacing: 1.5, margin: 0,
  });
  slide.addText(title, {
    x: margin, y: 0.72, w: 11.9, h: 0.55,
    fontFace: "Aptos Display", fontSize: 25, bold: true, color: C.ink,
    margin: 0, breakLine: false, fit: "shrink",
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: margin, y: 1.31, w: 11.7, h: 0.35,
      fontSize: 11, color: C.muted, margin: 0, fit: "shrink",
    });
  }
  slide.addShape(pptx.ShapeType.line, {
    x: margin, y: 1.76, w: 12.0, h: 0,
    line: { color: C.line, width: 1 },
  });
}

function bullets(slide, items, x, y, w, h, opts = {}) {
  const list = (items || []).filter(Boolean).slice(0, opts.max || 6);
  if (!list.length) {
    slide.addText("No material items recorded.", { x, y, w, h: 0.35, fontSize: 11, color: C.muted, italic: true, margin: 0 });
    return;
  }
  const runs = [];
  list.forEach((item) => {
    runs.push({
      text: String(item),
      options: { bullet: { indent: 14 }, hanging: 3, breakLine: true },
    });
  });
  slide.addText(runs, {
    x, y, w, h, fontSize: opts.fontSize || 15, color: C.ink,
    breakLine: false, valign: "top", margin: 0.05, paraSpaceAfterPt: 10,
    fit: "shrink",
  });
}

function card(slide, x, y, w, h, title, body, note = "") {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.06,
    fill: { color: C.white }, line: { color: C.line, width: 1 },
  });
  slide.addText(title, {
    x: x + 0.22, y: y + 0.18, w: w - 0.44, h: 0.3,
    fontSize: 11, bold: true, color: C.ink, margin: 0, fit: "shrink",
  });
  slide.addText(body || "—", {
    x: x + 0.22, y: y + 0.58, w: w - 0.44, h: h - 0.9,
    fontSize: 19, bold: true, color: C.ink, margin: 0, fit: "shrink", valign: "mid",
  });
  if (note) {
    slide.addText(note, {
      x: x + 0.22, y: y + h - 0.35, w: w - 0.44, h: 0.18,
      fontSize: 8.5, color: C.muted, margin: 0, fit: "shrink",
    });
  }
}

function addFooter(slide, n) {
  slide.addText(`${data.client || "Client"}  •  ${data.period || "Review"}`, {
    x: margin, y: 7.15, w: 6.5, h: 0.18, fontSize: 8.5, color: C.muted, margin: 0,
  });
  slide.addText(String(n), {
    x: 12.2, y: 7.15, w: 0.4, h: 0.18, fontSize: 8.5, color: C.muted, align: "right", margin: 0,
  });
}

// Slide 1 — client pulse
{
  const slide = pptx.addSlide();
  addHeader(slide, "Client intelligence", data.client || "Client", data.period || "Review period");
  slide.addText(data.headline || "Account pulse", {
    x: margin, y: 2.1, w: 12.0, h: 0.75, fontSize: 28, bold: true, color: C.ink, margin: 0, fit: "shrink",
  });
  bullets(slide, data.executive_summary, margin, 3.05, 11.9, 3.55, { max: 5, fontSize: 16 });
  addFooter(slide, 1);
}

// Slide 2 — performance/progress
{
  const slide = pptx.addSlide();
  addHeader(slide, "Performance", "Progress against what matters", "Use supplied metrics only; missing data stays missing.");
  const metrics = (data.metrics || []).slice(0, 6);
  if (!metrics.length) {
    bullets(slide, ["No comparable performance metrics were supplied for this review."], margin, 2.15, 11.8, 1.2, { fontSize: 17 });
  } else {
    metrics.forEach((m, i) => {
      const col = i % 3;
      const row = Math.floor(i / 3);
      card(slide, margin + col * 4.05, 2.05 + row * 2.15, 3.72, 1.78, m.name || "Metric", m.current || "—", m.previous ? `Previous: ${m.previous}` : (m.note || ""));
    });
  }
  addFooter(slide, 2);
}

// Slide 3 — market / competitors
{
  const slide = pptx.addSlide();
  addHeader(slide, "External intelligence", "What changed around the client", "Only material signals that affect decisions.");
  const signals = (data.signals || []).slice(0, 4);
  if (!signals.length) {
    bullets(slide, ["No material external change recorded for this period."], margin, 2.1, 11.8, 1.2, { fontSize: 17 });
  } else {
    signals.forEach((s, i) => {
      const y = 2.02 + i * 1.22;
      slide.addText(s.fact || "Signal", { x: margin, y, w: 5.35, h: 0.52, fontSize: 14, bold: true, color: C.ink, margin: 0, fit: "shrink" });
      slide.addText(s.impact || "", { x: 6.15, y, w: 5.9, h: 0.52, fontSize: 12, color: C.ink, margin: 0, fit: "shrink" });
      slide.addText(s.source || "", { x: 6.15, y: y + 0.56, w: 5.9, h: 0.18, fontSize: 8, color: C.muted, margin: 0, fit: "shrink" });
      slide.addShape(pptx.ShapeType.line, { x: margin, y: y + 0.92, w: 11.9, h: 0, line: { color: C.line, width: 1 } });
    });
  }
  addFooter(slide, 3);
}

// Slide 4 — learnings
{
  const slide = pptx.addSlide();
  addHeader(slide, "Learning", "What we learned", "Keep lessons separate from activity lists.");
  bullets(slide, data.learnings || data.actions_completed || [], margin, 2.08, 11.9, 4.5, { max: 6, fontSize: 16 });
  addFooter(slide, 4);
}

// Slide 5 — recommendations
{
  const slide = pptx.addSlide();
  addHeader(slide, "Recommendations", "The next three moves", "Ranked, evidence-backed and executable.");
  const recs = (data.recommendations || []).slice(0, 3);
  recs.forEach((r, i) => {
    const x = margin + i * 4.05;
    card(slide, x, 2.15, 3.72, 3.65, `${i + 1}. ${r.action || "Recommendation"}`, r.why || "", `Priority: ${r.priority || "—"}`);
  });
  if (!recs.length) bullets(slide, ["No recommendations recorded."], margin, 2.2, 11.5, 1.0, { fontSize: 17 });
  addFooter(slide, 5);
}

// Slide 6 — decisions / next 30 days
{
  const slide = pptx.addSlide();
  addHeader(slide, "Decision", "What we need from the client", "Turn the review into decisions, not applause.");
  bullets(slide, data.decisions_needed, margin, 2.05, 11.9, 3.2, { max: 6, fontSize: 17 });
  const completed = (data.actions_completed || []).filter(Boolean).slice(0, 4);
  if (completed.length) {
    slide.addText("RECENTLY COMPLETED", { x: margin, y: 5.6, w: 3.0, h: 0.22, fontSize: 9, bold: true, color: C.good, charSpacing: 1.2, margin: 0 });
    slide.addText(completed.join("   •   "), { x: margin, y: 5.96, w: 11.8, h: 0.65, fontSize: 10.5, color: C.muted, margin: 0, fit: "shrink" });
  }
  addFooter(slide, 6);
}

fs.mkdirSync(path.dirname(output), { recursive: true });
await pptx.writeFile({ fileName: output });
console.log(output);
