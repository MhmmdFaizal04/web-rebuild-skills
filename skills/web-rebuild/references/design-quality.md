# Design Quality

## Scope And Mode
- Apply these rules to authored web UI across languages and frameworks.
- Treat visual quality as an evidence-led design review, not an automated guarantee.
- Select and name one mode before implementation; do not blur their success criteria.
- Reference-led rebuild: use supplied screenshots, URLs, assets, and interaction evidence.
- Brief-led creation (no reference): use the user's audience, goals, content, and constraints.
- In brief-led creation, label design choices as proposals; make no fidelity claims.
- For mixed tasks, identify which regions are reference-led and which are newly designed.
- Ask about consequential ambiguities; otherwise state bounded, reversible assumptions.

## Evidence Before Styling
- Inspect the existing product, design system, assets, and representative viewports first.
- Identify hierarchy, density, alignment, typography, rhythm, imagery, and interaction tone.
- Distinguish observed facts from inferred responsive behavior and missing interaction states.
- Preserve the product's visual language unless the brief explicitly calls for a redesign.
- Establish the primary user task and its path before adding decorative treatments.
- Use actual content length and asset proportions when judging layout and hierarchy.
- Do not invent branding, testimonials, customer logos, awards, or performance claims.
- Record missing assets or unavailable fonts and the visible effect of any substitutes.

## No Emoji In Authored Output
- Do not introduce emoji in authored UI, icons, text, or code examples.
- Do not use emoji as bullets, status markers, placeholders, or decorative accents.
- Use a semantic SVG icon or a concise text label when a pictorial cue is useful.
- Do not silently remove or rewrite emoji already present in user-owned content.
- Preserve existing user content unless its modification is authorized; flag conflicts.
- If a reference contains emoji to recreate, substitute semantic SVG or text by default.
- Record that substitution as an explicit reference deviation, including its location.
- Preserve a reference emoji only when the user specifically requests its preservation.
- A user-owned source string is not permission to introduce emoji in unrelated new copy.
- Do not sanitize runtime user input merely to enforce an authored-design preference.

## Intentional Visual Language
- Choose an aesthetic from the reference or brief, not a reusable landing-page formula.
- Avoid arbitrary generic gradients, glass effects, bento layouts, and decorative blobs.
- Such treatments require a concrete reference or brief rationale; they are not defaults.
- Do not impose universal color bans; select colors for context, contrast, and brand fit.
- Avoid interchangeable hero slogans, repetitive feature cards, and gratuitous oversized type.
- Give each section a purpose; remove ornamental components that compete with real tasks.
- Use meaningful imagery with appropriate crop, loading behavior, and alternative text.
- Keep visual emphasis proportional to importance rather than making every element loud.
- Follow the existing system's conventions instead of introducing a competing component kit.

## Small Coherent Token Set
- Reuse existing tokens before defining new ones; avoid a large speculative design system.
- Specify a compact palette with semantic roles for surfaces, text, borders, and feedback.
- Define a readable type hierarchy, line heights, content widths, and font fallbacks.
- Use a small spacing scale and consistent rules for radii, borders, shadows, and motion.
- Explain the few consequential token decisions using reference or brief evidence.
- Check tokens together in realistic screens, not only in isolated swatches or components.
- Keep one-off exceptions rare and justified by content or interaction requirements.
- Ensure themes and high-contrast settings do not erase controls or meaningful boundaries.

## Icons And Labels
- Use an existing icon set or a coherent SVG family with consistent stroke and proportions.
- Choose icons for meaning, not decoration; pair unfamiliar symbols with visible text.
- Prefer native controls and semantic HTML where supported by the rendering stack.
- Give icon-only controls accessible names that describe the action, not the icon's shape.
- Hide decorative SVGs from assistive technology; avoid duplicate spoken labels.
- Keep icons legible at small sizes and test their alignment with adjacent text.
- Provide usable pointer targets without enlarging every visible glyph.
- Never encode status or required actions solely through color, icon shape, or animation.

## UX And Accessibility
- Design the primary flow and relevant loading, empty, error, success, and disabled states.
- Distinguish a genuine empty state from a failed request and offer an appropriate next step.
- Keep validation near the field, preserve entered values, and explain how to recover.
- Provide clear pending feedback and guard against accidental duplicate submissions.
- Make controls keyboard operable with visible focus and a logical traversal order.
- For dialogs, manage focus entry, containment, escape behavior, and return to the trigger.
- Use appropriate landmarks, heading order, form labels, and accessible status announcements.
- Expose selected, expanded, invalid, and busy states through native semantics or suitable ARIA.
- Respect reduced motion; do not make animation necessary to understand or complete a task.
- Check text and non-text contrast, zoom, reflow, touch use, and assistive-technology behavior.
- Do not claim accessibility conformance solely from a screenshot or an automated scan.

## Responsive And International UX
- Test narrow and wide layouts with realistic content; avoid screenshot-only fixed positioning.
- Let hierarchy and reading order survive wrapping, stacking, long titles, and missing media.
- Account for navigation, tables, dialogs, sticky controls, and overflow at small widths.
- Keep copy localizable; avoid concatenated sentences and text embedded in decorative images.
- Format dates, numbers, currency, and plural forms through the project's locale facilities.
- Allow translated text expansion; do not assume English string lengths or Latin-only fonts.
- Support the project's RTL requirements with logical properties and correct reading order.
- Mirror directional affordances where meaningful, not logos or every icon indiscriminately.

## Data And Honest Presentation
- Use supplied or real application data when available and authorized.
- Label fabricated preview data as sample or demo data where it could be mistaken for real.
- Never add fake statistics, social proof, activity feeds, or conversion claims as decoration.
- Do not present a static mock interaction as working persistence or a connected service.
- Explain unavailable integrations and keep placeholder actions visibly distinguishable.

## Review And Handoff
- Compare reference-led work at matching viewports and relevant UI states when possible.
- Review brief-led work against audience needs and the agreed brief, not imagined fidelity.
- Inspect hierarchy, spacing, typography, icon consistency, content, and interaction clarity.
- Exercise keyboard flows and relevant responsive, error, long-content, and RTL cases.
- Report the checks actually run, their environments, and any unverified states.
- Keep an explicit deviation list for substitutions, including reference emoji replacements.
- Treat screenshot diffs and automated checks as evidence, not proof of tasteful design.
- State subjective design judgments as judgments; seek user review for consequential choices.
