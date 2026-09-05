# Icons and Motion

Read the section needed for the current feature, not every library. Use the existing framework, versions, package manager, icon style, and dependencies. These recipes are implementation guidance, not a preinstalled animation engine or a claim that every version is tested.

## shadcn/ui and SVG Icons

shadcn/ui components use the project's selected icon library. Inspect `components.json` (including `iconLibrary` when present), existing component imports, and installed packages. Lucide is common, but do not replace an already consistent alternative just to follow an example. Do not invent a `shadcn-icons` import or assume component aliases such as `@/components/ui/button` exist without checking.

When a React project needs a new icon family and the user permits the dependency, Lucide's `lucide-react` is a suitable option. Import individual icons instead of a whole dynamic catalog. Match size, stroke, alignment and contrast. Decorative icons should be hidden from assistive technology; icon-only buttons need action-oriented labels. Never use emoji as icons or as substitutes for unavailable packages.

```tsx
import type { MouseEventHandler } from "react";
import { Search } from "lucide-react";

export function SearchButton({ onClick }: { onClick: MouseEventHandler<HTMLButtonElement> }) {
  return (
    <button type="button" aria-label="Search" onClick={onClick}>
      <Search size={20} aria-hidden="true" />
    </button>
  );
}
```

The native button above illustrates semantics only; use the project's shadcn Button and existing classes when available, preserving focus styles and target size. For Vue/server templates/other stacks, use the appropriate icon package or licensed static SVG. Do not introduce React for an icon. Retain third-party license notices for copied SVG assets.

## Choose One Animation Approach per Feature

| Need | Preferred approach |
|---|---|
| Small hover/focus/color transition | Existing CSS or native framework transitions |
| React presence, layout, gestures | Existing Framer Motion or modern Motion for React |
| Sequenced timelines, SVG movement, coordinated scroll | GSAP and only required plugins |
| Non-React browser UI | CSS/WAAPI, native transitions, GSAP, or Motion JavaScript as appropriate |

Never let CSS, GSAP and Motion compete over the same property on the same element. If both engines already exist, keep ownership explicit; do not rewrite unrelated features. Dependencies cost bundle size and maintenance. A static reference does not justify gratuitous entrance effects, parallax, cursor followers or scroll hijacking.

## GSAP Lifecycle and Reduced Motion

For React, use `useGSAP` from `@gsap/react` when available and approved. It scopes animations through GSAP context and cleans up recorded effects. Use `revertOnUpdate: true` for effects reconstructed by changing dependencies; wrap animation-creating delayed callbacks in `contextSafe`, and separately remove listeners/timers. Import/register ScrollTrigger only when the feature uses it.

```tsx
"use client";
import type { ReactNode } from "react";
import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(useGSAP);

export function Entrance({ children }: { children: ReactNode }) {
  const root = useRef<HTMLDivElement>(null);
  useGSAP(() => {
    const mm = gsap.matchMedia();
    mm.add("(prefers-reduced-motion: no-preference)", () => {
      gsap.from(root.current, { y: 12, duration: 0.35, ease: "power2.out" });
    });
    return () => mm.revert();
  }, { scope: root });
  return <div ref={root}>{children}</div>;
}
```

This example leaves content visible without JavaScript and skips movement for reduced motion. Motion must fit the brief; do not wrap every section automatically. For non-React integrations, use `gsap.context()` or `gsap.matchMedia()` in the framework's client lifecycle and revert on teardown. `matchMedia()` already creates a context; an extra manual wrapper is unnecessary.

Use `gsap.matchMedia()` for responsive/reduced-motion variants, not deprecated `ScrollTrigger.matchMedia()`. Clean up owned ScrollTriggers, not global `ScrollTrigger.killAll()` in a component. Refresh scroll geometry after consequential image/font/layout changes. Test resize, repeated navigation/mount/unmount, and media-preference changes for duplicated listeners, pin spacers, or stale transforms.

## Motion / Framer Motion

For new React adoption, current Motion docs use package `motion` and imports from `motion/react` (check installed React/version requirements). If the project already uses `framer-motion`, preserve its imports and supported APIs unless a migration is explicitly in scope. Do not mix imports or install both packages by habit.

```tsx
"use client";
import type { ReactNode } from "react";
import { motion, MotionConfig } from "motion/react";

export function Action({ children }: { children: ReactNode }) {
  return (
    <MotionConfig reducedMotion="user">
      <motion.button type="button" whileTap={{ scale: 0.98 }}>
        {children}
      </motion.button>
    </MotionConfig>
  );
}
```

Wire real actions and use existing providers/components in the application; this example only demonstrates animation policy. `MotionConfig reducedMotion="user"` disables transform/layout animation but does not disable every opacity or color transition. Use `useReducedMotion` for bespoke parallax, autoplay, large transitions, or an explicit no-animation requirement. Keep focus/keyboard semantics independent of gestures.

For exit animations, use the installed package's `AnimatePresence`, stable keys, and proper mount ownership. `useAnimate` supplies scoped selectors and automatic unmount cleanup, but timers/listeners and async continuation still need deliberate handling. Retain controls for standalone `animate()` and cancel/stop according to intended cleanup; those operations have different style semantics.

Keep DOM access and hooks on the client. Avoid initially hiding essential server-rendered content until hydration. Import selected features; measure production bundles before claiming an optimization. Consider `LazyMotion` or mini entry points only when supported and useful, not as speculative infrastructure.

## Verification Contract

- Record the icon package/version and chosen animation engine, rationale and property ownership.
- Run actual type/build checks where the runtime is available; sample snippets are not proof of integration.
- Exercise normal motion, reduced motion, resize, repeated navigation and unmount. Check focus visibility, layout shift, content reachability and absence of console errors.
- Compare screenshots in matched, documented stable states. Keep separate evidence for animated behavior; a disabled-animation screenshot cannot prove timing or cleanup.
- If a library/tool is unavailable, report unverified integration or propose an approved fallback. Do not claim GSAP/Framer Motion ran just because this guide was read.

## Official References

- [shadcn configuration schema](https://ui.shadcn.com/schema.json)
- [Lucide React](https://lucide.dev/guide/packages/lucide-react)
- [GSAP React lifecycle](https://gsap.com/resources/React/)
- [GSAP matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/)
- [Motion React installation](https://motion.dev/docs/react-installation)
- [Motion accessibility](https://motion.dev/docs/react-accessibility)
- [Motion useAnimate](https://motion.dev/docs/react-use-animate)
