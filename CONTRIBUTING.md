# Contributing

Small, testable contributions are welcome: a fixture, a regression case, a clearer instruction, an installation report, or a documentation improvement.

## Before Editing

Open an issue for major scope changes. Keep the package focused on reference-driven frontend reconstruction rather than unrelated design, scraping, or backend tooling. Do not submit copied proprietary layouts/assets, secrets, production recordings, or fabricated benchmarks.

## Pull Request Checklist

1. Explain the problem and the smallest change that solves it.
2. Use original or appropriately licensed fixtures; record asset rights.
3. Add or update a deterministic test for helper behavior. For prompt changes, include a concrete scenario and expected observable behavior.
4. Run `python -m unittest discover -s tests -v` and `python tests/validate_repo.py` after installing the helper requirements.
5. Keep SKILL.md concise; place detail in references and preserve valid frontmatter.
6. Update documentation when flags, outputs, or compatibility change. Do not claim runtime support from an installer-only test.

CI checks structure, links, tests, and installation; maintainers review behavioral claims separately. A PR adding an evaluation plan is not proof of a passed evaluation. Read [the protocol](evals/README.md).

## Useful First Contributions

- Add a unit test for a malformed or unusual PNG input.
- Contribute an original responsive fixture with expected behavior.
- Report a reproducible installation issue with OS, Node, CLI, and agent versions.

Be respectful and specific in reviews. Explain failures without personal attacks. Never post private screenshots or credentials to reproduce an issue.
