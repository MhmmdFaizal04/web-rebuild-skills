# Prompts and Practice

Install the skill first using the root README. These prompts go into your coding agent, not into a terminal. Replace placeholders and supply files you have rights to reuse.

## 1. Authorized URL

> Use web-rebuild in faithful mode. Recreate <AUTHORIZED_URL> in the existing project. I have rights to reuse the supplied assets. Preserve the section order, typography, copy, and observed interactions. Compare 320x900, 768x1024, and 1440x1000 captures with matching source states. Stop after three correction rounds and report remaining differences.

## 2. Adapt a Reference

> Use web-rebuild in adaptation mode. Keep the attached reference's grid and spacing rhythm, but use my provided logo, palette, and copy. Do not reuse the reference brand or third-party images. Track intentional changes separately from defects and keep the current framework.

## 3. Screenshot Without Browser Access

> Use web-rebuild with this 1440x1000 screenshot. Browser access is unavailable. Implement the visible layout and infer a mobile version, but label responsiveness and interactions unverified. Do not invent measured similarity or executed tests.

## 4. Correct an Existing Attempt

> Use web-rebuild to compare the supplied reference and our current local page. Do not redesign it. Fix container widths and typography first, preserve existing functionality, and show evidence for each correction round.

## 5. New UI Without a Reference

> Use web-rebuild in brief-led creation mode. Build a furniture catalog for our existing Laravel Blade application. Use supplied products and brand assets. No emoji, fabricated testimonials, or generic gradient hero. Preserve routes, CSRF, form validation, and native templates. Propose a coherent visual direction and test empty/error/loading states, mobile reflow, and keyboard flow. Do not claim reference fidelity.

## 6. Keep the Existing Language

> Use web-rebuild to recreate these authorized screenshots in our Go templ project. Preserve handlers and contextual escaping. Use the existing CSS and icon system, no new React app and no emoji. If Go compilation or browser access is unavailable, say which checks were not run.

## 7. Token-Conscious Layout Fix

> Use web-rebuild to correct the spacing in this existing TSX page. Keep token use lean: reuse our components and tokens, inspect relevant files with enough context, and summarize results without pasting complete files. Preserve the agreed desktop/mobile, keyboard, and regression checks. Recheck screenshots if the code changes.

This is the default efficiency policy, not an extra skill or a special CLI flag. Ask for a detailed explanation when needed; correctness takes priority over a shorter answer.

## 8. URL + Icons + Motion

> Use web-rebuild in faithful mode for <AUTHORIZED_URL>. Keep this TypeScript/shadcn project and configured icon family. Inspect actual source animation; prefer our installed Framer Motion rather than adding another engine. Preserve reduced motion and keyboard semantics. Build a separate candidate, compare desktop/mobile captures under matched conditions, and report missing evidence. Do not treat a source/control screenshot pair as proof of reconstruction.

For a public, original practice URL use https://mhmmdfaizal04.github.io/web-rebuild-skills/reference.html . It deliberately has no GSAP/Motion animation; adding elaborate effects in faithful mode would be a deviation. Use an explicit adaptation brief to request new motion.

## Original Practice Fixture

[Fieldnotes Studio](../skills/web-rebuild/assets/reference.html) is an original MIT-licensed HTML reference with no external assets, scripts, or network dependencies. It has an editorial two-column hero, staggered project artwork, in-page navigation, and keyboard-operable native disclosures.

Find it in the installed skill's `assets/reference.html`. Open it in a browser, or serve the installed assets directory locally:

```bash
python -m http.server 4173 --bind 127.0.0.1 --directory "<SKILL_DIR>/assets"
```

Then visit `http://127.0.0.1:4173/reference.html`. This server is optional, serves only the specified directory, and should not expose a folder containing private files.

Capture reference views at 320x900, 768x1024, and 1440x1000. Ask the agent to rebuild from the captures into a separate project; do not give it the fixture source if evaluating screenshot reconstruction. You can give source access for a migration exercise, but record that as a different task.

Expected checks:

- Preserve editorial hierarchy, asymmetric hero, color roles, section order, and copy in faithful mode.
- Stack hero below 768 CSS pixels and keep project artwork and captions readable without page overflow.
- Make navigation anchors and the disclosure functional with keyboard access.
- Keep code editable; a screenshot background is not a reconstruction.
- Record source/candidate browser settings, visual differences, and untested areas.

CI captures this fixture and exercises the image helper; it does not generate a reconstruction using an AI model. [Evaluation protocol](../evals/README.md) explains how to run that separate experiment fairly.
