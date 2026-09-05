# Stack Adapters

## Contract
- Apply the design and UX guidance across frontend languages, not only JavaScript stacks.
- Adapt to the repository's native rendering model instead of translating it into a new stack.
- This is language-agnostic guidance, not a claim that every runtime has been tested.
- A stack's presence in the table does not certify compatibility with every version or library.
- Native mobile implementation is outside the tested web scope; Flutter here means Flutter web.
- Desktop, embedded webviews, and hybrid native shells need separately stated validation scope.
- Never force React, Node, or Python into generated UI merely because tooling uses them.
- Keep automation dependencies separate from application runtime and build dependencies.

## Inspect Before Choosing An Adapter
- Read repository instructions, manifests, lockfiles, build scripts, and existing UI examples.
- Identify exact framework and language versions, package manager, and supported build targets.
- Locate route definitions, page shells, templates, components, styles, and asset pipelines.
- Determine server rendering, client rendering, hydration, streaming, and progressive enhancement.
- Inspect authentication, authorization, CSRF handling, validation, and state ownership.
- Identify existing localization, accessibility, design-token, icon, and component conventions.
- Reuse the team's test runner and normal development commands; do not guess framework versions.
- Choose the smallest native change consistent with the requested UI and repository boundaries.
- Do not upgrade dependencies, switch package managers, or add a second UI framework incidentally.

## Stack Map
| Stack | Native Surface And Preservation Checks |
| --- | --- |
| JS/TS React | JSX/TSX; preserve router, hooks, state, SSR/hydration, and server/client boundaries. |
| JS/TS Vue | SFCs or existing templates; preserve directives, reactivity, scoped CSS, and SSR. |
| JS/TS Svelte | Existing component syntax; inspect version before using runes, stores, or actions. |
| JS/TS Angular | Native templates/components; preserve forms, dependency injection, routing, and change detection. |
| JS/TS Astro | Astro templates and existing islands; preserve hydration directives and server-only execution. |
| JS/TS Web Components | Custom elements; preserve lifecycle, shadow/light DOM contracts, events, and form participation. |
| PHP Blade/Twig/WordPress | Native templates and theme conventions; preserve escaping, helpers, routes, nonces, and CSRF protections. |
| Python Django/Jinja | Native templates and configured autoescaping; preserve URL helpers, form errors, and CSRF tokens. |
| Ruby ERB/Hotwire | Rails templates/partials and Turbo/Stimulus; preserve authenticity tokens, frame IDs, and navigation lifecycle. |
| Go templates/templ | html/template or existing templ components; preserve contextual escaping, handlers, and generated-code workflow. |
| Java/Kotlin Thymeleaf/JSP | Existing server templates/tag libraries; preserve context-aware escaping, form binding, and security integration. |
| C# Razor/Blazor | cshtml/razor conventions; preserve encoding, antiforgery, binding, render modes, and circuit/component state. |
| Elixir HEEx/LiveView | HEEx components; preserve assigns, streams, stable DOM IDs, events, and live navigation. |
| Rust Leptos/Yew | Native component macros; preserve signals/hooks, ownership rules, feature flags, and SSR/hydration targets. |
| Dart Flutter web | Existing widgets and theme; preserve semantics, focus, navigation, responsive constraints, and web build target. |
| Scala | Inspect Play Twirl, Scala.js, Laminar, or the actual stack; preserve native templates, escaping, routes, and state. |
| Clojure/ClojureScript | Inspect Hiccup, Reagent, UIx, or the actual stack; preserve escaping behavior, reactive state, and build tooling. |
| Generic fallback | Identify the native renderer and browser output; preserve its escaping, routing, security, and state contracts. |

## Safe Native Implementation
- Extend existing pages, partials, components, or widgets instead of producing detached HTML mockups.
- Keep shared layout ownership intact and avoid duplicating shells, global styles, or providers.
- Preserve route helpers, base paths, URL encoding, query parameters, and active-navigation state.
- Keep form methods, field names, hidden fields, CSRF tokens, and server validation wiring intact.
- Preserve authorization checks; hiding a control is not an authorization mechanism.
- Preserve user-entered values, selected items, pagination, and state across expected transitions.
- Respect framework event syntax and lifecycle cleanup; do not attach unmanaged duplicate listeners.
- Retain SSR and hydration contracts; avoid browser-only APIs during server execution.
- Keep generated markup deterministic where hydration requires matching server and client output.
- Preserve streaming, deferred content, and progressive enhancement where the app uses them.
- Do not replace real data bindings or mutations with hardcoded sample values to match a screenshot.
- If demo data is necessary, label it and keep it separate from production application behavior.

## Escaping And Trust Boundaries
- Escape strings for their output context: HTML text, attributes, URLs, CSS, or JavaScript.
- Use framework interpolation and serialization helpers; do not invent universal escaping utilities.
- Inspect the actual engine's escaping defaults; template syntax alone does not prove safety.
- Do not mark untrusted input as raw HTML or disable escaping for visual convenience.
- If rich HTML is required, follow the application's established sanitization and trust policy.
- Keep dynamic values out of inline script/style contexts unless safely serialized for that context.
- Validate URL schemes and preserve established asset handling and content security policy.
- Use native SVG/icon integration; preserve accessible labels and do not introduce emoji.
- Do not silently scrub existing user content; document reference substitutions as deviations.

## Framework-Specific Discipline
- Follow the repository's React version, compiler configuration, and established component patterns.
- Do not add useMemo or useCallback automatically; memoize only for a demonstrated repository need.
- Use useEffectEvent, startTransition, or useDeferredValue only when supported and appropriate.
- Keep React server/client boundaries explicit; do not move secrets or server logic into client code.
- In other reactive stacks, use their native state and effect mechanisms rather than React analogies.
- For server templates, prefer existing progressive-enhancement patterns over new client bootstraps.
- For generated templates or bindings, edit source inputs and use the normal generation workflow.
- For canvas/widget-rendered web UI, verify the semantics tree and keyboard behavior explicitly.

## UX Across Stacks
- Implement relevant loading, empty, error, success, disabled, and pending interaction states.
- Preserve focus, keyboard activation, dialog behavior, and status announcements through updates.
- Use semantic browser elements where available and native accessibility APIs otherwise.
- Keep translations, pluralization, locale formatting, and RTL behavior in the existing system.
- Test realistic long content and responsive layouts rather than assuming one screenshot size.
- Reuse compact design tokens and meaningful icons; avoid arbitrary visual trends and fake statistics.
- Label no-reference work as brief-led creation and make no reference-fidelity claims.

## Validation And Environment Reporting
- Assess runtime/compiler availability separately from browser and screenshot-tool availability.
- A working browser does not prove that the native application can compile or run locally.
- A successful build does not prove that rendering, interactions, or visual quality are correct.
- Run the repository's applicable formatter, type/template checks, build, and tests when available.
- Run the actual application in a browser when possible; check relevant routes and UI states.
- Exercise SSR/hydration, forms, keyboard flows, navigation, responsive layouts, and locale cases.
- Record the commands, versions, browser/viewports, and results actually observed.
- If a runtime is unavailable, report compilation as not run, not passed or implicitly supported.
- If browser execution is unavailable, report visual and interaction checks as unverified.
- A static preview may aid design review but is not native integration or runtime validation.
- Do not silently install runtimes or rewrite the stack to make local validation easier.
- Report blockers, remaining checks, explicit deviations, and subjective design-review conclusions.
