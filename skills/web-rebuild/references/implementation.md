# Implementation Playbook

## Preserve the Project

Read the existing package scripts, routing, styles, tokens, and representative components. Prefer the current framework and build pipeline. Introduce dependencies only when their benefit is concrete and approved under the host's permissions. Preserve user work and keep the patch scoped to the requested routes.

## Work From Large to Small

| Pass | Match | Typical failure |
|---|---|---|
| Structure | Section order, max widths, grid ratios, alignment | Correct colors on the wrong layout |
| Typography | Loaded font, weight, size, line height, wrapping | Substituted font changing page rhythm |
| Spacing | Section rhythm, padding, gaps | Arbitrary margins compensating for structural errors |
| Assets | Aspect ratio, crop, object position | Right image with the wrong crop |
| Details | Border, shadow, icon stroke, color | Polishing while major regions still drift |
| Behavior | Real links and safe local states | Beautiful controls that do nothing |

Use content-driven breakpoints, flex/grid, max/min widths, and semantic HTML. Absolute positioning is suitable for deliberate decoration, not every content block. Preserve meaningful DOM order. Avoid fixed heights that clip translated or enlarged text.

## Faithful Versus Adaptation

In faithful mode do not add fashionable gradients, cards, rounded corners, animations, or sections absent from the source. In adaptation mode track each requested change and retain other constraints. A deliberate color change is not a mismatch; an accidental column-width change still is.

Existing design tokens may be reused or mapped. If the reference conflicts with the current design system, make that tradeoff explicit instead of silently replacing global tokens. Isolate route-specific styles where appropriate.

## Interactions and Accessibility

Use buttons for actions, links for navigation, real labels for inputs, and appropriate dialog primitives when already installed. Support keyboard interaction, visible focus, focus return, and Escape where expected. Do not fake a login or payment integration. Demo forms should clearly say they are local mocks and should not send data to production endpoints.

If the source is inaccessible, fix the issue and record the visual/behavioral deviation. Do not copy illegible contrast or keyboard traps for fidelity. Respect reduced motion; avoid adding motion just to make the demo look impressive.

## Completion Is Not Just a Build

A successful build does not prove matching screenshots, functional interactions, or accessibility. Each requires its own recorded evidence. When blocked by unavailable assets or tooling, leave a clear limitation rather than fabricated precision.
