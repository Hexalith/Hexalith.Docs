---
title: "Reconciliation: brief addendum vs PRD draft"
created: 2026-11-10
source: _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/addendum.md
targets: prd.md, addendum.md (this folder)
decision-log: .memlog.md (this folder)
---

# Reconciliation: brief addendum vs PRD draft

Line references are `BA:Lnn` for the brief addendum and `PRD:Lnn` / `PA:§x` for this folder's `prd.md` / `addendum.md`. Items that `.memlog.md` logs as a `decision` or `assumption` are marked **deliberate** and are not reported as gaps.

**Result:** 96 of 111 scoped items carried (decisions 1-11, all launch checklists, skeleton, quickstart table, badge rules, decision 10 rules, adopted research constraints). 15 are partial, weakened, dropped or contradicted. A further 5 baseline facts behind the decisions were checked as extras (4 carried, 1 partial). 1 advisory item was not adopted by the brief.

## Coverage table

Status: **C** carried, **C*** carried via a deliberate (memlog) change, **P** partial or weakened, **D** dropped, **X** contradicted.

### Decisions 1-11 (BA:L19-31, L288-463)

| # | Item | PRD | Status |
|---|---|---|---|
| 1 | D1: `aspire run` in a dev container. "Try it" on Docker, K8s how-to for Platform, Azure/AWS/Scaleway later | FR-5, FR-20, FR-23, FR-24, §2.2, §6 | C |
| 2 | D1: "If a prompt needs more than about 10 lines, fix the command, not the prompt" | FR-6 (verbatim), SM-C3 | C |
| 3 | D1: the prompt checks prerequisites or opens the dev container, runs the command, waits for healthy, returns the dashboard URL, explains the first call | FR-6 steps 1-5 | C |
| 4 | D1: "Try it" runs "on Docker, on the user's own machine, and the time target applies to it" | Only R-8. FR-23, FR-53, FR-55 and SM-1 use "clean machine", whose definition includes Codespaces | P (Gap 3) |
| 5 | D1: consider prebuilt images (C) later, for "Try it" only, if B misses 20 minutes | §6, §7.2, R-3 | C |
| 6 | D2: one skeleton, business/technical label, one or more of three blocks. The rejected four-kind taxonomy is not used | FR-2, FR-9, FR-17, FR-50 | C |
| 7 | D2: the category labels the org-page list, and the blocks follow what the reader does first | FR-25, FR-17 | C |
| 8 | D3: front door = org profile plus Hexalith.Docs guides, no website | FR-25, FR-8, §6 | C |
| 9 | D3: the profile fits one screen and has what Hexalith is, "Try it" to the Platform quickstart, and every module with category, one-line description and link | FR-25 (60-line assumption), FR-23 | C |
| 10 | D3: cross-module guides cover "concepts, architecture, how modules fit together" | FR-8 requires only ≥1 overview guide, and architecture isn't named | P (Gap 7) |
| 11 | D3: every repository gets an About description and topics | FR-28 | C |
| 12 | D3: revisit a website once there are enough docs | §6 | C |
| 13 | D4: one NuGet-safe README with absolute HTTPS links and images, no raw HTML, allowed hosts. "Linting enforces these rules" | FR-12, FR-41 | C |
| 14 | D4: commons keeps per-package READMEs, and "other repositories don't have to adopt them" | FR-16: "No other in-scope repository adds per-package READMEs before launch" | X (Gap 8) |
| 15 | D4: "Revisit C only if a single page would mislead users" | §6 lists it as a non-goal with no trigger. §7.2 says only two items have triggers | D (Gap 11) |
| 16 | D5: NuGet version, CI, License, SonarQube Cloud. Drop Coverity and Codacy | FR-38 | C |
| 17 | D5: Sonar scanner added once to the Builds reusable CI, one project per repository, an organization token | FR-40 | C |
| 18 | D5: OpenSSF Scorecard verdict "Later" | §6 lists it as a non-goal with no revisit | P (Gap 11) |
| 19 | D6: org defaults in `Hexalith/.github` plus `docs/development.md` per repository | FR-33, FR-36 | C |
| 20 | D6: delete each repository's CONTRIBUTING | FR-34 (broadened to all six files) | C |
| 21 | D6: move README runbooks to `docs/development.md` | FR-14, FR-36, FR-37 (operator content goes to `docs/operations.md`, memlog L23) | C* |
| 22 | D6: enable private vulnerability reporting so SECURITY points to a real channel | FR-35 | C |
| 23 | D6: release history goes to CHANGELOG.md or GitHub Releases | FR-14 | C |
| 24 | D7: agent rules in aitools plus a docs check in the builds CI | FR-41 to FR-50 | C |
| 25 | D7: the check "becomes required in each repository after migration" | FR-42: fail mode at migration, but the required status check is set only "at launch" | P (Gap 10) |
| 26 | D7: an agent migrates each repository with the audit-and-migration prompt | FR-7, UJ-5 | C |
| 27 | D8: docs now, announce only when "Try it" works, demo optional | FR-26, FR-27, §7.3, R-1 | C |
| 28 | D8: "The front door never promises something the product doesn't do" | FR-26 (near verbatim), NFR-3 | C |
| 29 | D9: every current repository at Level 1, Level 2 starting with Platform, cleanup | FR-57, FR-58, FR-29 to FR-32 (21 repositories, memlog L13) | C* |
| 30 | D9: Level 1 is agent writing work, and "human review is the bottleneck" | §4.10, R-4, FR-57 | C |
| 31 | D10: targets of 5, 15 and 20 minutes | FR-51 | C |
| 32 | D10: clean machine = Docker + VS Code, or only a browser with Codespaces | Glossary (tightened to "no Hexalith toolchain", memlog L18) | C* |
| 33 | D10: "The timer starts on the README and stops at the first success" | FR-51 ("Try it" starts at the front door, memlog L17) | C* |
| 34 | D10: calibrate against a measured baseline ("measure a baseline now") | FR-52 | C |
| 35 | D10: Phuong Duong (`tinouit`) runs the human stranger test | FR-55, §10 say "an outside tester". The name is gone | D (Gap 6) |
| 36 | D10: each person is a stranger once, so the baseline and iterations use the agent test | §4.9, R-2, FR-52 | C |
| 37 | D10 option D: the agent test gets only the README and the prompt "in a clean dev container" | FR-53: dev container for 3 blocks, but "on a clean machine for 'Try it'" | P (Gap 12) |
| 38 | D10: "an agent test runs routinely" | FR-54 lists event triggers only, with no periodic or post-launch cadence | P (Gap 1) |
| 39 | D10: add the CI smoke test (C) only for "Try it", only if quickstarts keep breaking after launch | §6, §7.2 (no detection mechanism, see Gap 1) | C |
| 40 | D10: if "Try it" can't meet 20 minutes from source, "switch to prebuilt images" | R-3: "a scope decision on prebuilt images … is raised" | P (Gap 13) |
| 41 | D11: `_bmad-output/` stays public in every repository and is never linked | FR-13, FR-31, FR-56 | C |

### Foundations in Hexalith.Docs (BA:L35-43)

| # | Item | PRD | Status |
|---|---|---|---|
| 42 | The standard, on one page | FR-1 | C |
| 43 | README skeleton with three quickstart blocks | FR-3, FR-9, FR-17 | C |
| 44 | `docs/development.md` template | FR-4 | C |
| 45 | Dev container template | FR-5 | C |
| 46 | AI-prompt pattern of ≤10 lines wrapping exactly one command | FR-6 | C |
| 47 | Audit-and-migration prompt modeled on `builds/.github/prompts/audit-hexalith-ci-cd.prompt.md` | FR-7 (the path exists at `references/Hexalith.Builds/.github/prompts/`) | C |
| 48 | Cross-module guides | FR-8 (see #10) | P (Gap 7) |

### README skeleton and limits (BA:L45-55)

| # | Item | PRD | Status |
|---|---|---|---|
| 49 | ≤150 lines | FR-10 | C |
| 50 | Title plus a one-sentence description ≤120 characters that matches the About text and the NuGet description | FR-9 §1, FR-11 (NuGet "starts with", memlog L28) | C* |
| 51 | Up to five badges | FR-38 | C |
| 52 | What and who in ≤5 lines | FR-9 §3, FR-10 | C |
| 53 | Quickstart blocks that fit on one screen | FR-10 (40 lines, assumption), FR-17 | C |
| 54 | Packages table if the repository publishes packages | FR-9 §5, FR-10 | C |
| 55 | Documentation links into `docs/` | FR-9 §6 | C |
| 56 | "Part of Hexalith" link to the front door | FR-9 §7 | C |
| 57 | Link to contributing guidance | FR-9 §8 (absolute URL, memlog L23) | C* |
| 58 | License | FR-9 §9 (SPDX, MIT, nothing after it) | C |

### `Hexalith/.github` (BA:L57-64)

| # | Item | PRD | Status |
|---|---|---|---|
| 59 | `profile/README.md` | FR-25 | C |
| 60 | CONTRIBUTING "with a link to each repository's `docs/development.md`" | FR-33: "explains how to find and follow each repository's development guide" | P (Gap 9) |
| 61 | CODE_OF_CONDUCT | FR-33 | C |
| 62 | SECURITY with private vulnerability reporting on | FR-33, FR-35 | C |
| 63 | SUPPORT | FR-33 | C |
| 64 | Issue and PR templates | FR-33, FR-34 | C |
| 65 | Public | FR-31 | C |

### Shared CI and AI.Tools (BA:L66-73)

| # | Item | PRD | Status |
|---|---|---|---|
| 66 | SonarQube Cloud scanner with quality gate and coverage | FR-40 | C |
| 67 | Docs check: markdownlint-cli2, lychee, and a script (sections, length, forbidden content). Warn first, then required per repository | FR-41, FR-42 (required timing, see #25) | C |
| 68 | Documentation rules in the shared agent instructions | FR-47 to FR-50 | C |

### Level 1 "Clean" (BA:L75-86)

| # | Item | PRD | Status |
|---|---|---|---|
| 69 | Skeleton and ≤150 lines | FR-9, FR-10, FR-57 | C |
| 70 | NuGet-safe (absolute links, no raw HTML, allowed badge hosts) | FR-12 | C |
| 71 | Description matches About and NuGet, topics set | FR-11, FR-28 | C* |
| 72 | No epics, stories, FR/NFR IDs or `_bmad-output` links in the README, CONTRIBUTING or `docs/` | FR-13 (broadened in the glossary) | C |
| 73 | `_bmad-output/` public, never linked | FR-13 | C |
| 74 | Repository CONTRIBUTING files removed | FR-34 | C |
| 75 | Runbooks move to `docs/development.md` | FR-14 (split, memlog L23) | C* |
| 76 | Release history goes to CHANGELOG.md or GitHub Releases | FR-14 | C |
| 77 | **All** links and badges work | FR-39, FR-45, FR-57. External links are excluded from fail mode, and FR-57 doesn't verify them | P (Gap 2) |
| 78 | Every `docs/` page linked from the README is accurate. `docs/` folders are cleaned, not reorganized | FR-57, FR-8, §6 | C |

### Level 2 "Try-able" (BA:L88-92)

| # | Item | PRD | Status |
|---|---|---|---|
| 79 | Platform "Try it" on Docker is the launch gate and ends with a first chat message | FR-23, FR-58, §7.3 (first success = the chatbot's reply, see Changed specifics) | C |
| 80 | Each module's "Run it" is added once it meets its target | FR-17, FR-20, FR-58 (memlog L20) | C* |
| 81 | Platform K8s how-to with no time target | FR-24 | C |

### Organization cleanup (BA:L94-101)

| # | Item | PRD | Status |
|---|---|---|---|
| 82 | Archive the reviewed candidates. Archiving can be undone | FR-29 | C |
| 83 | Check Hexalith.BmadSkills: 106 `.claude.json` under `skills/reports/` | FR-32 | C |
| 84 | Make Docs and `.github` public | FR-31 | C |
| 85 | Pin the key repositories | FR-30 | C |

### Quickstart block table (BA:L324-328)

| # | Item | PRD | Status |
|---|---|---|---|
| 86 | Use the package: add the NuGet package and paste a short sample (commons, polymorphicserializations) | FR-19, PA §A | C |
| 87 | Run it: `aspire run` in the dev container, then a first call (memories, eventstore, tenants, parties) | FR-20, PA §A | C |
| 88 | Use the tool: install, then a first command (mcpcli, builds, cicd, aitools) | FR-21, PA §A, OQ-5 | C |

### Badge rules (BA:L362-376, L250-263)

| # | Item | PRD | Status |
|---|---|---|---|
| 89 | NuGet version, required when the repository publishes packages | FR-38 | C |
| 90 | CI status, required | FR-38, FR-39 | C |
| 91 | License, required | FR-38, FR-39 | C |
| 92 | Sonar quality gate and coverage | FR-38 (2 badges, required where CI builds .NET, memlog L21), FR-40 | C* |
| 93 | Coverity dropped | FR-38, §6 | C |
| 94 | Codacy and Codecov dropped | FR-38, §6 | C |
| 95 | "No badge without a pipeline that produces it" | FR-39, recast as "live source" (memlog L21) | C* |
| 96 | Badges only from nuget.org-allowed hosts | FR-12 | C |

### Research digest constraints the brief adopted (BA:L191-282)

| # | Item | PRD | Status |
|---|---|---|---|
| 97 | LICENSE can't be an org default | No FR requires a root LICENSE file. Hexalith.Docs has none today (verified) | D (Gap 4) |
| 98 | Org defaults don't appear in clones or packages | FR-9 §8 (absolute URL) | C |
| 99 | Issue templates are all-or-nothing | FR-34 | C |
| 100 | Community Standards checklist (description, README, CoC, contributing, license, security, issue templates, PR template, content reports) | FR-33 checks "all six". SM-7 requires a "complete" page | P (Gap 14) |
| 101 | Standard Readme: ≤120-character description matching GitHub and the package, License last as SPDX | FR-11, FR-9 §9 | C |
| 102 | GitHub builds the outline, so no TOC section | FR-9 (assumption) | C |
| 103 | `PackageReadmeFile` packed explicitly (Builds packs the root README) | §10, FR-15 | C |
| 104 | nuget.org: no raw HTML, no relative links or images, image allow-list | FR-12, PA §B | C |
| 105 | Fixing a page means publishing a new version | FR-15 (memlog L15) | C* |
| 106 | Fewer badges go stale less often | FR-38 (≤5) | C |
| 107 | markdownlint-cli2, lychee-action v2 (archived markdown-link-check not used) | FR-41, PA §B | C |
| 108 | Vale skipped for v1 | §6, NFR-1 | C |
| 109 | Reusable workflows via `workflow_call` | FR-41, FR-43 | C |
| 110 | Org rulesets and required workflows need a paid plan | §6, PA §B (branch protection on Free) | C |
| 111 | Writing style: important point first, second person, active voice, short, sentence case, numbered steps, descriptive link and alt text, global audience | NFR-1, NFR-6 | C |

### Extras: baseline facts behind the decisions (not counted above)

| # | Item | PRD | Status |
|---|---|---|---|
| E1 | Agents add content after License (BA:L145) | FR-9, FR-47 | C |
| E2 | Badges point to deleted workflows or the wrong repository (BA:L147) | FR-39 | C |
| E3 | Platform prerequisites: exact versions, isolated Dapr home, submodules at exact commits, `HEXALITH_DAPR_HOME` 1.18.2 vs 1.18.7 mismatch (BA:L154-161) | FR-5 pins versions only | P (Gap 5) |
| E4 | mcpcli's ~20-line prompt shows how prompts grow (BA:L162) | FR-6, SM-C3 | C |
| E5 | "Sixteen repositories use its reusable workflows" (BA:L182) | FR-43's list implies 14 | C (number mismatch, see Changed specifics) |
| Adv | GitHub reads `.github/README.md` before the root README (BA:L197). Not adopted by the brief | none | advisory |

## Gaps

### Gap 1: "Routinely" lost its cadence, so the 10C revisit trigger can't fire (medium)

- **Source:** "A human stranger test is the launch gate, and an agent test runs routinely." (BA:L30). "Add C … only if quickstarts keep breaking after launch." (BA:L462)
- **PRD:** FR-54 (PRD:L673-678) runs the test only at the baseline, before publishing, after a change to a quickstart's command or prerequisites, and before launch. Nothing runs after launch unless someone edits the quickstart. Dependency or toolchain drift in the 17 repositories Platform pulls in, or a new package version, wouldn't trigger a run. The §7.2 trigger "if quickstarts keep breaking after launch" (PRD:L768) has no data source and no threshold.
- **Fix:** add a periodic consequence to FR-54. For example, run "Try it" and every published "Run it" block monthly and on every Platform release. Define "keep breaking" in §7.2, for example two failed periodic runs in a quarter.

### Gap 2: Level 1 doesn't verify that all links work (medium)

- **Source:** "All links and badges work." (BA:L85)
- **PRD:** FR-57 (PRD:L702-713) relies on "the docs check passes in fail mode". FR-45 (PRD:L577-580) excludes external links from fail mode and from PR blocking. So a repository can reach Level 1, and the launch gate can pass, with broken external links in the README or `docs/`.
- **Fix:** add to FR-57: "a full link check including external links passes at migration merge, and any remaining failure is listed with a reason". Add to §7.3: "no open external-link issue on an in-scope repository's README".

### Gap 3: "Try it" on the user's own machine is only a risk mitigation (medium)

- **Source:** "The 'Try it' quickstart runs on Docker, on the user's own machine, and the time target applies to it." (BA:L307)
- **PRD:** The glossary's clean machine (PRD:L86) includes "only a browser" with Codespaces. FR-23, FR-53, FR-55 and SM-1 all say "clean machine". Only R-8 (PRD:L828) says the gate is measured locally, and memlog L18 intends that. The launch gate could therefore be passed in Codespaces.
- **Fix:** in FR-55 and SM-1, say "on a local clean machine with Docker and VS Code (not Codespaces)". In FR-23, say the one command deploys "on Docker on the newcomer's machine".

### Gap 4: No FR requires a LICENSE file (medium)

- **Source:** "LICENSE can't be a default." (BA:L208). "Every repository is MIT-licensed." (BA:L109, which covers the 20 current repositories only)
- **PRD:** FR-9 §9 says the License section gives MIT. FR-39 says the License badge "reads the repository's LICENSE file". SM-7 requires a complete Community Standards page, which includes a license. But no FR requires each in-scope repository to have a root LICENSE file. Hexalith.Docs, which becomes public under FR-31, has no LICENSE today (checked: its root has only AGENTS.md, CLAUDE.md, `_bmad`, `_bmad-output` and `references`).
- **Fix:** add a consequence to FR-57 (or a new FR in §4.5): "every in-scope repository has a root LICENSE file (MIT)". Make the docs check verify it, and include Hexalith.Docs explicitly.

### Gap 5: The dev container's scope omits the Platform prerequisites that made option A slow (medium)

- **Source:** The baseline requires "an isolated Dapr home with CLI 1.18.2 and runtime 1.18.7 (a machine-wide `dapr init` doesn't qualify)" and "submodules checked out at exact commits", and notes the `HEXALITH_DAPR_HOME` version mismatch (BA:L154-161). Decision 1B removes "the prerequisite pain" (BA:L293).
- **PRD:** FR-5 (PRD:L152-159) pins tool versions, and "`aspire run` succeeds … with no further installation". It says nothing about:
  - obtaining Platform's 17 submodules at pinned commits (clone or init step, and its time)
  - isolating the Dapr home
  - removing the version mismatch

  FR-23's "one command" may silently rely on an unlisted clone or submodule step.
- **Fix:** add to FR-5 and FR-23: the dev container initializes only root-declared submodules at their pinned commits, non-recursively, per workspace policy, and configures the Dapr home. The block lists the clone command, and the timer counts it. Every version comes from one source, so README, script and container can't disagree.

### Gap 6: The named human stranger tester was dropped (low)

- **Source:** "Phuong Duong (GitHub: `tinouit`) runs the human stranger test once Platform is finished." (BA:L460, also in brief.md's timeline)
- **PRD:** FR-55 and §10 (PRD:L841) say "An outside tester who is available once Platform deploys the chatbot", which reads as unassigned. The launch gate loses its committed owner.
- **Fix:** name the tester in §10 or FR-55. If the omission is deliberate, for privacy in a public repository, log that in `.memlog.md`. Consider adding "the designated tester isn't exposed to Hexalith before the test".

### Gap 7: Cross-module guide scope narrowed (low)

- **Source:** "Cross-module guides (concepts, architecture, how modules fit together) live in Hexalith.Docs." (BA:L344)
- **PRD:** FR-8 (PRD:L192) requires at least one overview guide [ASSUMPTION]. It covers what Hexalith is, the business/technical split, and how Platform combines modules. Architecture isn't required.
- **Fix:** name architecture as a required topic of the overview guide, which can stay one page, or state that architecture is deferred.

### Gap 8: Per-package READMEs went from optional to forbidden (low)

- **Source:** "commons keeps its per-package READMEs. Other repositories don't have to adopt them." (BA:L359)
- **PRD:** FR-16 (PRD:L284): "No other in-scope repository adds per-package READMEs before launch." That's a prohibition, not an option, and no memlog entry records it.
- **Fix:** reword it as "don't have to add them, and any that are added follow FR-16". If the prohibition is intended, log it as a decision.

### Gap 9: The org CONTRIBUTING no longer links to each development guide (low)

- **Source:** "CONTRIBUTING, with a link to each repository's `docs/development.md`" (BA:L60). "the shared CONTRIBUTING links to each repository's development guide" (BA:L384)
- **PRD:** FR-33 (PRD:L454) says it "explains how to find and follow each repository's development guide".
- **Fix:** "CONTRIBUTING links by absolute URL to each in-scope repository's development guide, or to the module registry row that does."

### Gap 10: "Required" per repository at migration is now "required at launch" (low)

- **Source:** "It starts as a warning and becomes required for each repository once that repository is migrated." (BA:L69, L405)
- **PRD:** FR-42 (PRD:L555-556) switches to fail mode at migration, but the required status check is set only "at launch". FR-57 doesn't include branch protection. A failing, non-required check doesn't block merges, so regressions can land between migration and launch.
- **Fix:** add to FR-42 and FR-57: "the Level 1 migration adds the docs check as a required status check on the default branch".

### Gap 11: Revisit triggers dropped (low)

- **Source:** Decision 4: "Revisit C only if a single page would mislead users of a repository's packages." (BA:L360). Decision 5: OpenSSF Scorecard "Later" (BA:L372)
- **PRD:** §6 (PRD:L743-744) lists both as non-goals with no trigger. §7.2 (PRD:L765) says "Two items have defined revisit triggers", but the website trigger in §6 makes three.
- **Fix:** list all revisit triggers in §7.2: website, pack-time README generation, OpenSSF Scorecard, prebuilt images, and the CI smoke test.

### Gap 12: Agent test environment changed for "Try it" without a log entry (low)

- **Source:** "a fresh AI agent gets only the README and the AI prompt in a clean dev container" (BA:L456)
- **PRD:** FR-53 (PRD:L668) runs "Try it" "on a clean machine". This is probably better, because the prompt's step 1 opens the dev container. But it isn't in the memlog (L24 omits the environment).
- **Fix:** log it as a decision. Also resolve the related conflict listed under Deliberate changes to confirm, item 1.

### Gap 13: The prebuilt-image contingency is softer than decision 10 (low)

- **Source:** "If 'Try it' can't meet its 20-minute target while building from source, switch to prebuilt images (option C of decision 1)." (BA:L463)
- **PRD:** R-3 (PRD:L823): "a scope decision on prebuilt images for 'Try it' is raised. That work isn't in this plan." This matches brief.md's risk wording and decision 1's "consider C later", so the brief is internally inconsistent.
- **Fix:** confirm the softer wording, and name the owner and deadline for that scope decision (for example, at calibration under FR-52).

### Gap 14: Community Standards completeness differs between FR-33 and SM-7 (low)

- **Source:** The Community Standards checklist covers description, README, code of conduct, contributing, license, security policy, issue templates, PR template, and content reports (BA:L213).
- **PRD:** FR-33 (PRD:L455) checks that "all six" community files are present. SM-7 (PRD:L803) requires the page to be "complete for all 21", which also needs a license (Gap 4) and content reporting enabled. No FR enables content reports.
- **Fix:** add license and content reports to FR-33 (and FR-57), or narrow SM-7 to the six files.

### Advisory (not adopted by the brief)

- GitHub shows `.github/README.md` in preference to the root README (BA:L197), while Builds packs the root README. A stray `.github/README.md` would split the GitHub and NuGet pages. Consider a docs check rule that fails if `.github/README.md` exists in an in-scope repository. This doesn't apply to `Hexalith/.github` itself, whose front door is `profile/README.md`.

## Deliberate changes to confirm

1. **Clean machine without a .NET SDK, applied to "Use the package"** (memlog L18, glossary PRD:L86, FR-51 PRD:L650). **Medium.**
   - A .NET developer's 5-minute "Use the package" timer now includes installing the .NET 10 SDK.
   - Meanwhile FR-53 (PRD:L668) measures that block "in a clean dev container", which pins the SDK.
   - The target and its test therefore measure different start states. Either the 5-minute target is unreachable on the FR-51 machine, or the test doesn't measure FR-51.
   - Recommend defining the start state per journey: "Use the package" and "Use the tool" with a .NET SDK present, and "Run it" and "Try it" with Docker and VS Code only.
2. **The "Try it" link appears once the agent stranger test passes** (memlog L25, FR-26). **Low.**
   - Decision 8A says "the public announcement waits until the Platform quickstart meets its time target" (BA:L412).
   - A link on the public org page is a visible promise made before the human launch gate.
   - It's probably acceptable, because the agent test enforces the time target. Confirm that the link isn't treated as the announcement.
3. **The "Try it" timer starts at the front door** (memlog L17, FR-51). **Low.**
   - The agent stranger test (FR-53, SM-2) starts at the Platform README.
   - So only the single human test measures the full FR-51 journey, and FR-26 opens the link on a test that skips the front door leg.
   - Accept this, or add "starts at `github.com/Hexalith`" to the agent test for "Try it".

The other memlog changes look sound and need no action: 21 repositories, the operations page split, NuGet descriptions that "start with" the one-sentence description, the live-source badge definition, compiled "Use the package" samples, republishing every package, and "Run it" kept out of the launch gate.

## Changed specifics

| Specific | Brief addendum | PRD | Logged? |
|---|---|---|---|
| Repository count | 20 current (BA:L29, L75) | 21 in-scope, including Docs (glossary, FR-57) | yes (memlog L13) |
| "Try it" timer start | README (BA:L441) | `github.com/Hexalith` (FR-51) | yes (L17) |
| "Try it" first success | "first chat message" (BA:L90, L447) | "the chatbot replies to the newcomer's first message" (FR-23, glossary) | no. A sensible tightening, but confirm it |
| NuGet description | "matches" (BA:L47, L79) | "starts with" the sentence, plus an optional package-specific sentence (FR-11) | yes (L28) |
| Runbook destination | `docs/development.md` (BA:L83) | development guide plus `docs/operations.md` (FR-14, FR-37) | yes (L23) |
| Local community files removed | CONTRIBUTING (BA:L82, L388) | all six files, no exceptions (FR-34). EventStore's local CoC goes | no. Consistent with the all-or-nothing caveat |
| Per-package READMEs | others "don't have to adopt" (BA:L359) | others must not add any before launch (FR-16) | no (Gap 8) |
| Org CONTRIBUTING | "a link to each repository's `docs/development.md`" (BA:L60) | "explains how to find and follow" (FR-33) | no (Gap 9) |
| Docs check "required" | per repository, after migration (BA:L69) | required status check "at launch" (FR-42) | partly (L22) (Gap 10) |
| Agent test environment | "clean dev container" (BA:L456) | dev container for 3 blocks, "clean machine" for "Try it" (FR-53) | no (Gap 12) |
| Agent test cadence | "routinely" (BA:L30) | event triggers only (FR-54) | partly (L24) (Gap 1) |
| Prebuilt-image contingency | "switch to prebuilt images" (BA:L463) | "a scope decision … is raised" (R-3) | no (Gap 13) |
| Human tester | Phuong Duong (`tinouit`) (BA:L460) | "an outside tester" (FR-55, §10) | no (Gap 6) |
| Cross-module guides | concepts, architecture, how modules fit (BA:L344) | ≥1 overview guide (FR-8) | assumption, PRD only |
| Sonar badges | "SonarQube Cloud" (count open) | 2 badges, required where CI builds .NET (FR-38) | yes (L21) |
| One screen (quickstart) | "fit on one screen" (BA:L50) | ≤40 lines of Markdown (FR-10) | assumption, PRD only |
| One screen (front door) | "fits on one screen" (BA:L343) | ≤60 lines, "Try it" in the first 10 (FR-25) | assumption, PRD only |
| Demo | "shows the chatbot in 30 seconds" (a pro, BA:L415) | "30 seconds or less", with a text alternative (FR-27) | no. Fine |
| Pins | "Pin the key repositories" | up to 6, Platform first (FR-30) | assumption, PRD only |
| "Use the tool" target | none (BA:L443-447) | 5 minutes (FR-21, FR-51) | assumption, with OQ-7 |
| K8s how-to acceptance | none | agent test on Docker Desktop K8s or kind (FR-24) | assumption, PRD only |
| Repositories outside the Builds workflows | "Sixteen repositories use its reusable workflows" (BA:L182) | FR-43 lists 6 current repositories plus Docs as not using them, which implies 14. The list matches the "Quality CI: none" column, not workflow usage | no. Verify per repository |
| Allow-list pointer | 38-domain allow-list (research) | FR-12 says "`addendum.md` §B lists them". PA §B names only 7 examples | no. Point to the source list |
| Audit prompt path | `builds/.github/prompts/audit-hexalith-ci-cd.prompt.md` | `Hexalith.Builds/.github/prompts/audit-hexalith-ci-cd.prompt.md` (FR-7) | same file. Verified it exists |

**Unchanged and verified:**

- README ≤150 lines.
- Description ≤120 characters.
- ≤5 badges.
- What and who in ≤5 lines.
- AI prompt ≤10 lines, wrapping exactly one command.
- Time targets of 5, 15 and 20 minutes.
- 106 `.claude.json` files under `skills/reports/`.
- 17 repositories pulled in by Platform.
- markdownlint-cli2, lychee (lychee-action v2), SonarQube Cloud.
- `Hexalith/.github/profile/README.md`, `docs/development.md`, `.devcontainer/`, `_bmad-output/`, CHANGELOG.md.
- Azure, AWS and Scaleway after launch.
- Kubernetes how-to with no time target.

**Qualitative intent:**

- "Fix the command, not the prompt" (FR-6, SM-C3) and "the front door never promises something the product doesn't do" (FR-26) are carried nearly verbatim.
- "No badge without a pipeline" survives as "live source" (FR-39).
- "Human review is the bottleneck" (R-4) and "archiving can be undone" (FR-29) are kept.
- "Don't hold back the docs" survives as R-1. Its reason, that today's docs are already public, was dropped, which is harmless.
