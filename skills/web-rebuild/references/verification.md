# Visual Verification

## Comparable Captures First

Capture reference and candidate with the same browser/version, OS, viewport, DPR, screenshot scale, zoom, color scheme, locale, and state. Fix these before interpreting a diff. Record unknown reference metadata.

Await `document.fonts.ready`, then check that the intended fonts are actually present rather than fallback. Wait for relevant images to decode and have nonzero intrinsic dimensions. Scroll predictably to trigger lazy content, then return to the recorded position. Prefer explicit UI-ready conditions; arbitrary sleeps and `networkidle` alone are unreliable.

Stabilize clocks, data, consent banners, carets, animations, carousels, and hover/focus consistently. Playwright's `animations: "disabled"` fast-forwards finite animations and cancels infinite ones; it is not an arbitrary frame freeze. Inspect canvas/video separately. Record masks in advance, never mask the UI under evaluation to improve the score.

Capture matched viewport images for precise comparison and full-page views for coverage. Different full-page heights indicate a real layout difference or noncomparable capture; inspect that before numerical comparison. Never stretch images to make dimensions agree.

## Offline PNG Helper

Install `scripts/requirements.txt` in an approved environment. From the skill directory:

```bash
python scripts/compare_images.py reference.png candidate.png --output comparison --threshold 16 --max-mismatch-ratio 0.02
```

Arguments:

| Argument | Meaning |
|---|---|
| `reference`, `candidate` | Local, single-frame PNGs of identical dimensions |
| `--output` | New directory; existing directories are refused to protect prior evidence |
| `--threshold` | Integer 0-255; a pixel differs when its maximum RGB-channel difference is strictly greater than this value |
| `--max-mismatch-ratio` | Finite number 0-1; pass when differing pixels / total pixels is at most this value |

Defaults are strict: threshold 0, ratio 0. Choose task-appropriate tolerances before a comparison. Values in examples are not endorsed universal targets.

The helper composites transparency onto white, ignores embedded color-profile transformations, converts to RGB, and supports at most 4,000,000 pixels per input. It refuses mismatched sizes, animated/non-PNG files, invalid thresholds, existing output directories, and oversized images. Use viewport or agreed region captures for larger pages; the helper intentionally has no resizing or automatic masking feature.

Outputs:

- `side-by-side.png`: reference left, candidate right.
- `overlay.png`: equal blend, useful for spotting displaced edges.
- `difference.png`: absolute RGB difference, not a perceptual score.
- `report.json`: file hashes, size, threshold, differing pixel count/ratio, mean absolute channel error, and pass/fail.

Exit codes: `0` within the declared image tolerance, `1` outside it, `2` invalid input or output failure. Stdout emits the JSON report on a completed comparison; diagnostics go to stderr. The helper reads only the two files and writes only its output directory, uses no network, and does not execute anything from an image. Review image provenance and keep Pillow patched.

A zero diff of a file against itself is only a control test. A screenshot-only implementation could score well and still be unusable. This metric does not measure aesthetic quality, reference authorization, accessibility, DOM semantics, real interactions, or model performance. Different OS/font rendering can cause legitimate differences.

## Correction Budget

Before each round list the top three mismatches. Fix structure and typography before details, recapture, and record whether those mismatches improved. Stop at the agreed budget (default three rounds), if evidence is unavailable, or if progress stalls. Never replace the source image with the candidate baseline just to obtain a pass.

For adaptation, assess unchanged regions against the source and changed regions against the approved brief. Report separately; a whole-image pixel score can penalize deliberate changes and is not an appropriate single success metric.

## Independent Gates

Test agreed routes/states at reference widths, an intermediate width, and around observed breakpoints. Check 320-CSS-pixel reflow, 200% text enlargement, long content, focus visibility, keyboard order, dialog focus return, accessible names, form errors, and reduced motion. Allow deliberate horizontally scrollable two-dimensional content such as a data table, but not accidental whole-page overflow.

Run available build/lint/tests and safe local interaction checks. Automated accessibility checks complement manual keyboard and targeted assistive-technology checks; do not turn an axe pass into a blanket WCAG claim.

Conclude `verified` only for the documented scope when all agreed gates pass. Otherwise report `partial`, `blocked`, or `unverified` with remaining work.
