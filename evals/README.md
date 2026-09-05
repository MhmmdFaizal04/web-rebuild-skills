# Evaluation Protocol

## Current Evidence

No end-to-end model benchmark has been run for this initial version. CI results cover specification validation, packaging/installability, documentation links, offline helper tests, and a synthetic Chromium capture pipeline. These are not evidence of reconstruction superiority.

The sixteen cases in [cases.json](cases.json) are a manual evaluation plan. Only the original Fieldnotes HTML fixture is currently supplied. Cases requiring injection text, delayed assets, additional interaction states, or variants need controlled fixtures prepared before execution; their presence in the plan does not imply automated coverage.

## Compare Fairly

1. Pin model/version, agent version, skill commit, tools, browser/OS, fixtures, and budget.
2. Use the same task with no skill, this skill, and a relevant licensed competitor (for example Anthropic frontend-design). Do not copy competitor content into this repo.
3. Keep development examples separate from held-out layouts. Do not let a screenshot-only condition read the reference HTML source.
4. Run at least three repetitions per case and condition. Record all results, failures, time, and tokens/cost when available. Never post only the best run.
5. Agree visual thresholds before seeing outputs. Use expert/manual review alongside pixels; changed regions in adaptation need brief-based assessment.
6. Inspect actual code, tool traces, screenshots, and interactions. Agent self-reports alone are not ground truth.

## Record Per Run

| Field | Value |
|---|---|
| Case ID, run ID, condition | |
| Model/agent/tools/skill commits | |
| Reference rights, fixture hash, source access level | |
| Viewport/DPR/environment/state matrix | |
| Visual threshold, differences and approved deviations | |
| Build, editability, interaction and a11y checks | |
| Correctly reported limitations / fabricated claims | |
| Iterations, time, tokens/cost | |
| Artifact paths and independent reviewer | |
| Result and failures | |

Safety gates override a good screenshot score. A screenshot used as the entire page, fabricated browser evidence, unauthorized network action, or ignored scope is a failure. A truthful blocked result in a missing-evidence case can be the correct behavior.

## Reproduce Deterministic Checks

In a development checkout or remote workspace:

```bash
python -m pip install -r skills/web-rebuild/scripts/requirements.txt
python -m unittest discover -s tests -v
python tests/validate_repo.py
```

The optional browser smoke additionally needs the pinned Playwright dependency/browser from CI:

```bash
python -m pip install playwright==1.62.0
python -m playwright install chromium
python tests/browser_smoke.py
```

It writes into a new `artifacts/` directory, captures the fixture twice per viewport, and compares an intentionally altered capture. It refuses to overwrite existing artifacts. Review Actions artifacts for outputs; they contain only this public synthetic fixture, never user pages.

## v0.2 Design and Stack Cases

New cases cover no-emoji authored UI, brief-led creation, native server-template preservation, and an unavailable/unknown renderer. These are evaluation definitions, not completed model benchmarks. The one user-reported successful activation is useful feedback, not a controlled test of all stacks.

## Token-Economy Evaluation (Not Yet Run)

Compare current skill with its token-economy policy versus the same skill/task without that policy, using identical models, tools, fixtures, acceptance gates and budgets. Run at least three repetitions per condition. Include simple fixes, complex rebuilds, stale captures and a budget failure. Record all attempts and input/output/cached/reasoning tokens when exposed, tool/image context, cost, retries and quality. Missing provider usage must be `not measured`, not inferred from word counts.

CI checks package structure and evaluation definitions, not model adherence or token savings. Ponytail's published benchmarks are not this project's results. A cheaper failed reconstruction is not an improvement over a correct one.

## URL and Animation Evidence

`tests/url_smoke.py` starts an explicitly scoped loopback fixture server. With `CHECK_PUBLIC_REFERENCE=1`, it also inspects only the fixed original GitHub Pages reference. Run after installing the CI Playwright dependencies/browser and `python tests/browser_smoke.py`. It writes `artifacts/url-inspection/report.json`, source/control/mutated images, and comparison artifacts; it does not overwrite previous outputs. A same-page control is intentionally not called a candidate reconstruction. External access can fail independently of the skill, and PR runs use loopback only.

New manual cases cover configured icons without emoji, animation lifecycle/reduced motion, and blocked source URLs. Library recipes have been checked against official docs, not runtime-tested across GSAP/Motion versions. CI is not executing a model or checking the quality of model-generated cloning.
