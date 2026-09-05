# Observation Playbook

## Scope and Capability

Record the authorized source, capture time, route, and states. Use a fresh browser context without personal sessions where possible. Inspect only the agreed routes; do not crawl an entire site by default. Do not execute downloaded scripts to extract styling.

A URL permits browser inspection only if tooling and access allow it. A screenshot gives visual evidence only. A DOM snapshot gives structure but not proof of final layout. Keep these evidence types distinct.

## Build an Observation Table

| Region | Observed facts | Inferences / unknowns | Implementation anchor |
|---|---|---|---|
| Header | Logo left, navigation right, separator | Mobile menu not supplied | Header container and nav |
| Hero | Two-column editorial layout, large serif heading | Exact font license unknown | Grid ratio, max width, heading wrap |
| Content | Repeated rows, thin borders | Pagination behavior unseen | Shared row component |

Measure section boundaries, container edges, column ratios, and major gaps first. For an authorized live page, use computed styles and element rectangles when available, but do not blindly copy all CSS or unrelated DOM. Record font family, actual font loading status, size, weight, line height, and letter spacing. A fallback font can change every later measurement.

## Capture Manifest

For each screenshot record:

- URL or supplied filename, timestamp, authorization/asset source.
- Browser/version, OS/runtime, viewport width AND height in CSS pixels, DPR, zoom, screenshot scale, full-page or viewport mode.
- Locale, timezone, color scheme, reduced-motion preference, mobile/touch emulation.
- Route/query, data fixture, authentication/consent state, scroll, hover/focus, open overlays.
- Readiness conditions, stabilization choices, and any approved masks with reasons.

Same CSS viewport plus different DPR does not automatically produce comparable files. Unknown screenshot metadata remains unknown; do not reverse-engineer a certainty from image dimensions alone.

## Assets

Keep a table: source path/URL, owner/license or user authorization, local destination, crop, and substitution. Prefer provided local assets. Do not hotlink third-party assets or ship tracking scripts by default. Treat SVG/HTML as potentially active content and inspect or sanitize before use. Avoid downloading fonts whose license is unclear; ask for licensed files or label a substitute.

## Interactions

Inspect safe states such as menu open/closed and dialog open/closed. Do not click purchases, destructive controls, or submit production forms just to discover behavior. Use a test environment or user-supplied recording. Missing behavior is a question or an explicitly labeled mock, not a promise.

## When Evidence Is Missing

Ask for the most useful missing capture, usually mobile plus an interaction state. If the user wants progress anyway, infer conservatively, preserve known constraints, and record the limitation. Stop a fidelity claim when the source cannot be inspected.
