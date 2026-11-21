---
title: Reconciliation of the documentation spine against PRD, addendum and epics
reviewed: ARCHITECTURE-SPINE.md (updated 2026-11-21) and .memlog.md (2026-11-21T07:11)
inputs:
  - ../../../prds/prd-docs-2026-11-09/prd.md (final, 2026-11-20)
  - ../../../prds/prd-docs-2026-11-09/addendum.md (2026-11-20)
  - ../../../epics.md
also-consulted:
  - references/Hexalith.CiCd architecture-cicd-2026-11-07 spine (AD-14, AD-15) and spec-cicd enforcement.md and pipeline-stages.md
  - references/Hexalith.Platform architecture-platform-2026-09-27 spine (AD-4)
  - the Docs tree as it stands (docs/, templates/, scripts/, docs/module-registry.json, .github/workflows/documentation.yml) and the pinned module checkouts
date: 2026-11-21
---

# Reconciliation: spine against PRD, addendum and epics

## Verdict

**Not ready.** Coverage is broad: all 66 FRs appear in the capability map, and OQ-14, the one Open Question assigned to Architecture, is answered. Six problems are structural, though:

- AD-9's sample-runner mechanism contradicts the CiCd custom-action contract, so it breaks the PRD's "work within Hexalith.CiCd" boundary.
- AD-6 and AD-8 contradict each other on how the checker finds package READMEs.
- The suppression model cannot express FR-46.
- The spine never says where a migration agent works.
- The FR-63 exemption sits in a file that a fresh clone lacks.
- The front door and the community files have no definition as checked pages.

Several quiet requirements were dropped: the NFR-7 budget, NFR-9 maintainer-only changes, the convention for an ignored secret file, the ASP.NET Core 10 runtime, and the `hexalith-module` tool pin. The memlog's list of PRD updates to offer upstream (line 58) is incomplete.

Counts: 1 critical, 7 high, 15 medium, 18 low.

## Open Questions owned by Architecture (PRD §12)

| OQ | Owner | Disposition in spine | Status |
| --- | --- | --- | --- |
| 14: which Platform-owned composition and first call for each business module's "Run it" | Architecture | AD-10 answers it: `dotnet tool run hexalith-module -- run --manifest module/hexalith.module-manifest.v2.json` from the module workspace in the dev container, ending with one McpCli call. Without a v2 manifest or McpCli coverage, "Run it" stays reserved. Memlog lines 45 and 61. | **Answered**, but the answer contradicts PRD text that the memlog does not list for upstream update (M-8). It also depends on a tool pin that the spine does not record (H-6). |

These Open Questions are owned elsewhere but touch the spine:

- **Deferred explicitly:** OQ-3, OQ-11, OQ-15, OQ-18 and OQ-19.
- **Pre-empted for another owner:** OQ-10 (Builds and CiCd), where AD-6 is marked [ADOPTED] for placement, and OQ-13 (AI.Tools), answered by AD-12. The memlog records both (lines 43 and 48).
- **Not mentioned:** OQ-1, OQ-5, OQ-16 and OQ-20. OQ-20 governs AD-4's create/list operation and AD-10's "one McpCli call" (L-13).

## Deliberate deviations and their memlog record

| Deviation | PRD/addendum text | Memlog record | Offered upstream (line 58)? |
| --- | --- | --- | --- |
| Registry rules move from the per-repository check to Docs CI (AD-6) | FR-2, FR-11, FR-39, FR-41 put them in the docs check in the shared CI | Lines 42, 53 | **No** (H-2) |
| markdownlint-cli2 is not adopted, and lychee runs only weekly (AD-7, Deferred) | FR-41: "runs markdownlint-cli2, lychee, and a script". Addendum §B.2: MD043, lychee-action v2 | Lines 44, 60 | **No** (M-7) |
| Links to other Hexalith repositories are checked only at migration and weekly (AD-7) | FR-45: "Every run checks internal links within the Hexalith organization" | Line 44 | Line 58 wrongly says FR-45 "already matches" (M-7) |
| "Run it" uses `hexalith-module run`, not `aspire run` (AD-10) | FR-5, FR-6, FR-20, glossary "Setup command", UJ-3 | Line 45 | FR-20 only (M-8) |
| The first "Run it" call goes through McpCli only (AD-10) | FR-20: "the first call the block shows" | Line 61 | Partly (with FR-20) |
| Suppressions live in a module-owned `.github/hexalith-docs.json` (AD-8) | FR-46: "the repository's docs check configuration" | Line 51 [ASSUMPTION] | n/a. The model has gaps (H-3) |
| The profile and the CONTRIBUTING list are generated, and About is checked only by the weekly report (AD-14) | FR-2, FR-28: a docs check rule verifies About and the front door | Line 54 [ASSUMPTION] | No (L-8) |
| Contributor Covenant 3.0 (Stack) | FR-33 [ASSUMPTION: 2.1] | Lines 30, 58 | **Yes** |
| A shared Builds sample runner replaces the pilot scripts (AD-9) | Addendum §B.4: the pilot hooks are the FR-19 evidence | Line 46 [ASSUMPTION] | n/a. It conflicts with CiCd (C-1) |
| Prompts live in `templates/` | FR-3 [ASSUMPTION: `templates/` and `.github/prompts/`] | Not recorded | No (L-7) |
| Commit-lint ban covers every planning ID in subjects and scopes (AD-11) | FR-14: story, epic and FR *scopes* | Line 47 says scopes only | No (L-2) |

## Findings

### Critical

#### C-1: The AD-9 sample hook "calls" a Builds tool, which CiCd forbids

- **Input.** PRD §7 non-goal: "Changing CI/CD outside Hexalith.CiCd". Addendum §B.1 "Working within Hexalith.CiCd" points to the CiCd contract. Addendum §B.4 names the module-owned hooks as the FR-19 evidence.
- **Spine.** AD-9 says: "Each publisher's module-owned `after-unit-tests` hook packs same-revision Release outputs and calls that tool", where the tool is a Builds tool. CiCd AD-14 says: "No action rebuilds the module or calls Builds". CiCd's enforcement.md section "Hoisting shared code" moves shared logic "into Builds, as a shared stage or action". Its jscpd duplicate scan fails on a fragment found in two or more modules, and 14 near-identical hooks would trip it.
- **Records.** The spine's Inherited invariants table omits CiCd AD-14. Memlog line 57 lists the CiCd amendments needed (AD-10/16/17, AD-12, AD-15, guard commitlint) but not AD-14.
- **Fix.** Make the README-sample runner a Builds CI step enabled by a `hexalith-ci.json` knob that CiCd renders, as was done for the docs check, or record a CiCd AD-14 amendment. Add CiCd AD-14 to the Inherited table.

### High

#### H-1: AD-8's checked pages need the registry, which AD-6 forbids the checker to read

- **Input.**
  - FR-16: "The module registry identifies which package IDs use a project-specific README."
  - Glossary, Checked pages: these include per-package READMEs.
  - FR-9: "Packages, if the repository publishes packages" and "a link to the development guide if the module registry records one".
- **Spine.** AD-8: "Fail mode judges ... every package README the registry assigns". AD-6: Builds' `docs_check.py` "never reads the registry". The per-repository checker therefore cannot find these pages, and it cannot decide whether the Packages section or the development-guide link is required. Memlog line 52 calls today's `.csproj`-adjacent scope only "the pilot subset".
- **Fix.** Define checked package READMEs and the conditional sections from facts the checkout proves, such as each packable project's `PackageReadmeFile` and the presence of `docs/development.md`. Have Docs CI verify that the registry agrees.

#### H-2: Moving registry rules to Docs CI loses module-level enforcement and Level 1 evidence

- **Input.**
  - FR-41: the shared-CI script covers "the one-sentence description and registry consistency".
  - FR-39: badge parameters "against the module registry".
  - Glossary, fail mode: a finding "turns `main` red, and the nightly release skips the repository".
  - FR-57: "The docs check passes in fail mode".
  - FR-64: the local result matches CI.
  - FR-43: BmadSkills and `Hexalith/.github` run the check too.
- **Spine.** AD-6 judges these rules in Docs CI against Docs' own submodule pins, and they never gate a module. The spine does not say:
  - which Docs commit and pin prove a repository's accepted revision at Level 1;
  - how a migration agent runs the registry rules locally before handing over (UJ-5 step 3);
  - how BmadSkills (an external checkout, not a submodule) and `Hexalith/.github` (not a submodule) are judged.
- **Records.** Memlog lines 42 and 53 record the move, not these consequences, and the move is missing from the line-58 upstream list.
- **Fix.** Add to AD-6:
  - Level 1 needs a green Docs CI run at a Docs commit that pins the accepted revision, with the run recorded in the ledger.
  - The registry rules can run locally against a working module checkout.
  - BmadSkills and `.github` are covered either by an explicit Docs-side check of their approved revision or by a recorded exception.

#### H-3: The suppression model cannot express FR-46 and drops its visibility controls

- **Input.**
  - FR-46: every suppression carries a reason, and the job summary shows the suppression count. "The planning-content and badge rules can't be suppressed, with one exception: the commit-SHA pattern ... for pinned actions and submodule commits".
  - SM-C2: track the suppression count across repositories.
  - FR-13: the standard may quote the patterns through an exemption recorded in the rule table.
- **Spine.** AD-8 has three problems:
  - Suppressions are `{file, rule, reason}` with no line or matched value. Planning content has no rule ID of its own: it sits inside D-LOCATION, together with release-history and runbook placement. The one permitted SHA exception would therefore silence every planning-content finding, and every location finding, in that file.
  - The wording "D-BADGE ... findings admit a suppression only for a pinned action or submodule SHA" lets D-BADGE be suppressed, which is looser than FR-46.
  - There is no job-summary count and no cross-repository tally. The file is module-owned, so the agents being policed can edit it.

  Docs' own standard could not quote the patterns under this model.
- **Fix.**
  - Give planning content its own rule ID.
  - Scope the SHA exception to `{file, line or sha, rule, reason}`.
  - Make D-BADGE unsuppressible.
  - Require a suppression count in the job summary and a cross-repository tally in the weekly report.
  - Record the rule-table exemption that lets the standard quote the patterns.

#### H-4: The spine never says where a migration agent edits, checks and commits

- **Input.** UJ-5 and FR-7: the agent "works from the Hexalith.Docs workspace" and "runs the local docs check until it's clean (FR-64)". Hexalith baseline (CI/CD section):
  - `check.py` runs "from the module root in a standalone clone".
  - "Never initialize nested submodules in an umbrella workspace to run the checker".
  - "Launch Claude Code from the module root so the project-local `Edit` denies protect whole-owned files".
- **Spine.** Silent. In the Docs workspace, `references/<Module>/references/Hexalith.Builds` is a nested submodule. The module-local `.claude/settings.json` denies do not apply there: Commons, for example, denies `Edit(/.github/workflows/**)` relative to its own root.
- **Fix.** Add a rule: a migration reads the standard and registry from the Docs workspace, but edits, runs `check.py` and commits in a standalone clone of the module, launched at the module root.

#### H-5: The AD-12 exemption is placed where a fresh clone cannot see it

- **Input.**
  - FR-63: in a fresh clone *without submodules*, the entry points must not stop the agent.
  - R-14: 16 repositories' entry points stop when `references/Hexalith.AI.Tools` is missing.
  - FR-48: a check script confirms the chain in a fresh clone.
- **Spine.** AD-12: "AI.Tools' baseline limits its 'stop and report a missing baseline' rule". In a fresh clone, the agent reads only the repository's own `AGENTS.md`, `CLAUDE.md` and `copilot-instructions.md`, and the AI.Tools file is absent.
- **Fix.** State that the exemption is part of the normalized entry-point text in every in-scope repository, outside the CiCd marker block. AI.Tools owns that text. Each migration propagates it, and the FR-48 and FR-63 checks verify it.

#### H-6: AD-10 depends on a `hexalith-module` tool pin that has no upstream

- **Input.** FR-20 and OQ-14: the composition a business module uses. Platform AD-4 ("Mode selection" and "Platform identity" rules):
  - The Platform tool must be pinned in the workspace's `.config/dotnet-tools.json`.
  - Every workspace other than Platform declares `references/Hexalith.Platform` directly.
  - The Platform identity pins a supported tool-version range.

  FR-18 and NFR-4: commands run as written.
- **Spine.** AD-10 prescribes `dotnet tool run hexalith-module`, but AD-13 gives that tool's version no upstream, and the module seed lists neither `.config/dotnet-tools.json` nor `references/Hexalith.Platform`. The checkouts disagree:

  | Checkout | `hexalith-module` tool pin |
  | --- | --- |
  | Parties | `hexalith.builds.module.cli` 6.3.0 |
  | Platform | 6.3.0 |
  | EventStore | 5.2.1 |
  | Tenants, Memories | no tool manifest |
  | Projects | manifest without `hexalith-module` |
- **Fix.** Add the tool pin to AD-13 ("within the range the Platform identity pins") and to the module seed, together with the direct `references/Hexalith.Platform` declaration. Make D-PREREQUISITES compare the pin with that range.

#### H-7: The front door and the community files have no checked-page or rule-profile definition

- **Input.**
  - FR-13: the front door and the community files contain no planning content.
  - FR-25: the front door "passes the docs check, with the skeleton rules turned off".
  - FR-59: `.github` runs the check "with the skeleton rules turned off".
  - Launch gates 5 and 6.
- **Spine.** AD-8 defines checked pages only as the root README, package READMEs and pages it links to. `profile/README.md` and CONTRIBUTING, SECURITY, SUPPORT and the templates are not covered. The configuration surface has a mode (`docs` knob or caller) and per-file suppressions, but no way to turn a rule set off. CiCd AD-2 forbids the checker from naming a module, so the difference must come from configuration.
- **Fix.** Define a page list and disabled rules in caller-supplied configuration, such as `.github/hexalith-docs.json` or a checker argument. Name `.github`'s checked pages explicitly.

### Medium

#### M-1: The registry cannot tell a reserved "Run it" from a published one

- **Input.**
  - FR-17: a registry entry for "Run it" reserves the block until it qualifies under FR-58. Until then, the README links to the development guide.
  - FR-58: the block is published once it passes the 15-minute agent test.
- **Spine.** AD-10 gates publication on a v2 manifest and McpCli coverage only, not on the FR-58 qualification. The registry (`quickstarts: [...]`) has no state per block. The Docs CI rule "quickstart order" therefore cannot tell a missing block from a reserved one. Platform lists only "Run it".
- **Fix.** Add a per-block status (`reserved` or `published`) to the registry. AD-10 should publish a block only with FR-58 ledger evidence.

#### M-2: Platform dev container pins were dropped or loosened

- **Input.**
  - Addendum §B.5: Platform selects "SDK 11.0.100 with `latestPatch`, the ASP.NET Core 10 runtime and Aspire CLI 17.0.0", uses a single absolute `HEXALITH_DAPR_HOME`, and says "Record the catalog used for each timed trial". The Platform README also lists the .NET 10 ASP.NET Core runtime.
  - FR-5: the template pins *exact* versions, including Docker-in-Docker.
- **Spine.** AD-13 and the Stack omit the ASP.NET Core 10 runtime. The `dotnet:…-11.0-resolute` image ships only .NET 11. Docker-in-Docker is pinned only to feature major `4`, although the memlog has 4.1.3. AD-4 and AD-13 drop the Dapr-home variable and the per-trial catalog record.
- **Fix.**
  - Add the ASP.NET Core 10 runtime to AD-13 and the Stack, with Platform as its upstream.
  - Pin exact feature versions.
  - Name `HEXALITH_DAPR_HOME`.
  - Add the Builds catalog revision to the trial record.

#### M-3: D-PREREQUISITES' Aspire comparison cannot be computed per commit

- **Input.** FR-5: a docs check rule verifies the dev container pins. The Aspire comparison is implied by D-PREREQUISITES.
- **Spine.** AD-13: the Aspire CLI version equals the `Aspire.AppHost.Sdk` version "of the AppHost that runs the block". For modules run through Platform's model, that AppHost sits in `references/Hexalith.Platform`. The checker runs "before submodule init" (memlog line 39), and AD-6 limits it to what the checkout proves.
- **Fix.** State which checked-in value the per-commit rule compares, for example the module's `aspire.config.json` or tool manifest. Otherwise assign the Platform-AppHost comparison to Docs CI against its pins.

#### M-4: AD-4's trial-record fields are a subset of FR-53 and FR-56

- **Input.**
  - FR-53: tool, version and model ID are designated before three trials, and a different configuration starts a new set. The candidate README is rendered at an immutable commit. Record entry URL, revision, exact prompt and outcome.
  - FR-56: clean environment, starting page and model ID.
  - Addendum §C: record whether the published content matches the tested path.
- **Spine.** AD-4 records "actual prerequisites, tester role, duration, tool version and friction". An agent could read this as the complete list.
- **Fix.** Make AD-4 reference the FR-56 field list. Add the same-configuration rule and the immutable candidate revision.

#### M-5: The NFR-9 maintainer-only rule for dev containers and entry points is missing

- **Input.** NFR-9: "Dev container files and agent entry points take effect on a newcomer's machine, so only a maintainer may change them". Prompts keep installs inside the container or the clone. OQ-19 concerns only the guard *mechanism*.
- **Spine.** The ownership table and seed mark `.devcontainer/` as module-owned. AD-12 lets agents edit entry points outside the marker block. The only reference is the deferral of OQ-19 to CiCd.
- **Fix.** State the rule independently of OQ-19: a maintainer must review changes to `.devcontainer/**` and to the entry points, for example through CODEOWNERS. AI prompts change nothing outside the container or the clone.

#### M-6: There is no cross-repository convention for the ignored secret file

- **Input.**
  - FR-6: the reader enters the secret "in an environment file that Git excludes and replies 'done'".
  - FR-18 and NFR-8: secrets never go in a prompt, the chat or a commit.
  - FR-61: "A run fails if the agent asks for a secret in chat".
  - Story 3.14: a privately supplied McpCli credential.
- **Spine.** AD-12 says secrets "follow D-PROMPT", but the spine fixes no file name, ignore entry or template line. Twenty-one READMEs, prompts and `.gitignore` files would each invent one.
- **Fix.** Fix one file name, such as `.env.local`, its `.gitignore` entry in the templates and the dev container, and the kit's stop-on-chat-secret rule.

#### M-7: The link-checking and tooling deviations are not flagged for upstream update

- **Input.**
  - FR-41: "runs markdownlint-cli2, lychee, and a script".
  - FR-45: "Every run checks internal links within the Hexalith organization".
  - Addendum §B.2: MD043 and the lychee-action v2 settings.
- **Spine.** AD-7 checks only self-links per commit. The Deferred list drops markdownlint-cli2. These choices are recorded at memlog lines 44 and 60. Line 58, however, claims FR-45 "already matches D-LINK", which is inaccurate for links to other Hexalith repositories, and it omits FR-41.
- **Fix.** Add FR-41 and FR-45 to the PRD upstream-update list, worded as "per commit, self-links only".

#### M-8: AD-10 contradicts more PRD text than the memlog lists

- **Input.**
  - FR-5: after the container starts, `aspire run` succeeds in a repository that has an AppHost.
  - FR-6: both the "Run it" and "Try it" prompt steps say `Run aspire run`.
  - FR-20: "run `aspire run`".
  - The glossary's "Setup command", and UJ-3.
  - The current tree: D-QUICKSTART ("starts Aspire") and `templates/quickstart-prompts.md`.
- **Spine.** AD-10 replaces this with `hexalith-module run` for every module except Platform, and Platform AD-1 freezes module AppHosts. Memlog line 58 offers only FR-20 for update.
- **Fix.** List FR-5, FR-6, the glossary, UJ-3, D-QUICKSTART and the prompt template as items to update, and restate FR-5's dev-container acceptance as "`hexalith-module run` succeeds".

#### M-9: The scan scope is unbounded, and NFR-7 is missing

- **Input.**
  - Glossary and FR-13: the check reports on other `docs/` pages, and `_bmad-output/` is never scanned.
  - FR-3: templates sit outside the checked pages.
  - R-13: about 430 of 970 pages match the patterns, and Platform holds about 2,600 evidence files.
  - NFR-7: the check adds 2 minutes or less on EventStore. Story 3.11 measures it.
- **Spine.** AD-8: "Other pages report only", with no bound. No exclusion of `_bmad-output/`, `_bmad/` or `references/` is stated, and NFR-7 appears nowhere.
- **Fix.** Report only on other `docs/**` pages. Never scan `_bmad-output/`, `_bmad/`, `references/` or submodule paths. Record the NFR-7 budget as a constraint on AD-6.

#### M-10: The AI.Tools rules file and the FR-48 reachability chain are underspecified

- **Input.**
  - FR-47: [ASSUMPTION] the file is `hexalith-docs-instructions.md`, self-contained and referenced from `hexalith-llm-instructions.md`.
  - FR-49: 100 lines or fewer.
  - FR-48: a check script run during each migration verifies the chain. `[HUMAN]` The `references/Hexalith.AI.Tools` pointer update is authorized by a person. The rules merge before the first migration.
- **Spine.** AD-8's Docs test checks "the pinned ... AI.Tools submodules" but names no file. AD-5's list of human-only acts omits the pointer authorization. No reachability script is placed in the seed.
- **Fix.**
  - Name the rules file and its budget.
  - Add the AI.Tools pointer update to AD-5's human-only acts.
  - Add the reachability check to `scripts/` in the seed.

#### M-11: No AD governs SonarQube Cloud, though Docs CI checks the key

- **Input.**
  - FR-40: one project per repository, an organization token, and a skipped (not failed) scan without a token.
  - Addendum §B.6: key `hexalith_<repository-name>` [ASSUMPTION], and skip when `SONAR_TOKEN` is unavailable.
  - FR-39: the key is the repository's own.
- **Spine.** The capability map lists SonarQube under AD-6 and AD-7, which say nothing about scanning. AD-6 has Docs CI judge the "Sonar key" with no convention. The registry already uses `Hexalith_Hexalith.Commons`, which differs from the addendum's form.
- **Fix.**
  - Fix the key convention, or defer it explicitly with OQ-18.
  - Record the skip-without-token rule as Builds CI behavior delivered through CiCd.

#### M-12: FR-54's Quickstart-change report was dropped

- **Input.** FR-54: "The docs check reports changes to Quickstart sections, so the test can be triggered".
- **Spine.** Omitted. Under AD-1 and AD-6, a per-commit checker cannot see the previous revision.
- **Fix.** Assign it to Docs CI. When a submodule pin advances, report any Quickstart section that changed between the old and new pinned revisions.

#### M-13: The delivery boundaries lack a per-repository Level 1 row

- **Input.** FR-57 is the done state for 19 of the 36 stories (Epic 3).
- **Spine.** The delivery boundaries cover "Pilot ready for adoption" only. Gate 9 (Kubernetes, FR-24) is also absent.
- **Fix.** Add a row for "Repository at Level 1": hosted fail-mode run at the accepted revision, green Docs CI at the matching pin, readability checklist, and republish verified or marked inapplicable. Add a row for the untimed Kubernetes qualification.

#### M-14: No seed includes a LICENSE

- **Input.**
  - FR-60: an MIT LICENSE at the root of all 21 repositories, and the docs check fails a repository without one.
  - FR-38: the License badge is required.
- **Spine.** Neither seed lists `LICENSE`. Docs has none: its README says "A repository license for this guide hub is pending", and the registry has `licenseFile: null`.
- **Fix.** Add `LICENSE` (MIT) to both seeds and flag Docs' missing file as a Level 1 blocker.

#### M-15: The migration-time link check has no mechanism or evidence

- **Input.**
  - FR-57: "every external link on checked pages works when the migration lands".
  - FR-45: each migration verifies every external link once.
- **Spine.** AD-7: "Each migration checks links to other Hexalith repositories, external destinations and badge images". The spine names no tool (lychee is limited to the weekly job) and no ledger field.
- **Fix.** Let the weekly report script run in single-repository mode for migrations, and record the result in the ledger.

### Low

#### L-1: Pilot-only wording in AD-2 and AD-3 is narrower than FR-42 and FR-15

AD-2 says "Promote each pilot to fail mode", while FR-42 requires all 21 repositories in fail mode at launch. AD-3 says "For every pilot package, verify the nuspec README", while FR-15 covers every registry package ID (101).

**Fix.** Generalize the wording to each migrated repository and each package ID. The pilot remains the example.

#### L-2: AD-11 states the commit-lint ban as fact while OQ-11 is open

AD-11 says "CiCd's commit lint enforces this", while the Deferred list says the timing belongs to CiCd. The rule is also broader than FR-14 (subjects plus any planning ID, against scopes in FR-14), and memlog line 47 records scopes only.

**Fix.** Mark the enforcement "pending CiCd (OQ-11)" and record the broadened scope as a decision.

#### L-3: The "human starts the release" step is ambiguous under nightly auto-dispatch

- **Input.** FR-15 `[HUMAN]`: a maintainer starts one release per repository. R-11: one patch per repository.
- **Spine.** AD-5 lists "starting a package release" as a human act. CiCd's nightly central process dispatches adopted modules, so a landed `docs(readme)` commit releases that night.

**Fix.** Say the human act is landing the `docs(readme)` commit, or a manual dispatch, and that maintainers batch README fixes to avoid extra versions.

#### L-4: Standalone callers pin Builds by release tag

AD-6 has standalone callers pin Builds by release tag [ASSUMPTION]. The inherited AD-1 row says the check "never fetches ... another repository", yet `.github` and BmadSkills must fetch Builds.

**Fix.** Pin a tag plus commit SHA, and except the pinned checker from the no-fetch sentence.

#### L-5: The conventions omit "no raw HTML" and the image allowlist

- **Input.** FR-12 and addendum §B.3: no raw HTML; badge hosts only from nuget.org's list; a text link for Codespaces. Memlog line 33: nuget.org strips HTML comments even inside code blocks.
- **Spine.** The Links convention covers only absolute URLs.

**Fix.** Add a NuGet-safe row covering no raw HTML or HTML comments, allowlisted hosts and no Codespaces badge.

#### L-6: The conventions carry no writing-style or accessibility rule

- **Input.**
  - NFR-1: second person, active voice, sentence-case headings, numbered steps, a global audience.
  - NFR-6: alt text and descriptive link text.
  - FR-9: fixed heading text.
  - FR-50: "business module" equals "domain module".
- **Spine.** The conventions cover only vocabulary, without the equivalence to "domain module".

**Fix.** Add one convention row that points to D-README, D-RENDER and D-IDENTITY for headings, style and alt text, and states the domain-module equivalence.

#### L-7: The location of prompts is an unrecorded deviation

FR-3 [ASSUMPTION] puts prompts in `.github/prompts/`. The seed and the current tree keep them in `templates/`.

**Fix.** Record the decision in the memlog and the upstream-update list.

#### L-8: About-text verification became non-gating without an upstream note

FR-2 and FR-28 have a docs check rule verify About. AD-14 checks it only in the weekly report, because About is not in any checkout. This is recorded as an assumption at memlog line 54.

**Fix.** Add the item to the upstream-update list, and make About verification part of migration review (Story 5.1).

#### L-9: The seed's dev container path differs from FrontComposer's

The registry records FrontComposer at `.devcontainer/ide-parity/devcontainer.json`, and FR-5 says to align it. The seed fixes `.devcontainer/devcontainer.json`.

**Fix.** Say D-PREREQUISITES reads the path the registry records, or require migration to the seed path.

#### L-10: AD-10's EventStore, Memories and McpCli clause is unclear

It does not say whose dev container FR-20's block opens, the repository's or Platform's. McpCli's registry block is "Use the tool", not "Run it".

**Fix.** State that these technical modules' "Run it" points to the Platform dev container and workspace, and drop McpCli from the clause.

#### L-11: The AD-9 runner is CI-only

CiCd AD-15 says "Hooks never run locally", so an agent cannot reproduce a sample failure through `check.py`. AD-9 is also silent on samples in per-package READMEs that sit outside a "Use the package" block (FR-16, Story 3.1).

**Fix.** Make the runner invocable standalone, and say whether samples in package READMEs are executed.

#### L-12: File-level findings have no defined line

FR-9, FR-34 and FR-60 produce findings for files that are absent or forbidden, but the convention says only that "line starts at 1".

**Fix.** Specify `line: 1` for file-level findings.

#### L-13: Some Open Questions are unreferenced

OQ-20 (the Projects create operation behind AD-4 and AD-10) is unreferenced. So are:

- OQ-16, the BMAD `project_knowledge` setting that writes into `docs/` (FR-13 durability);
- OQ-1, the "Try it" prerequisites;
- OQ-5, the quickstart blocks for Builds, AI.Tools and BmadSkills.

**Fix.** List them under Deferred with their owners.

#### L-14: The seed comment on the exposure review invites detail

The comment "launch ledger, exposure review" could invite item-level findings into Docs' `_bmad-output/`, which becomes public. The file itself says only aggregate status belongs there.

**Fix.** Annotate the seed with "exposure review status only, findings private (AD-5)".

#### L-15: The capability map has no NFR rows

NFR-7, NFR-8 and NFR-9 bind several units: Builds, every module and the kit.

**Fix.** Add an NFR column or rows.

#### L-16: AD-1 hard-codes the count of 21

AD-1 says "Verify all 21 repositories are represented", while PRD §8.5 adds new repositories with a registry row.

**Fix.** Phrase it as every in-scope repository (21 at launch).

#### L-17: The weekly report's write path and token are undefined

AD-7 "publishes one report in Docs" without saying where (job summary, artifact, committed file or issue) or with which permissions. Docs CI today runs with `contents: read`. Addendum §B.2 requires token authentication and retry on HTTP 429 for lychee.

**Fix.** Fix the destination, the minimal permissions and the token used for rate limits.

#### L-18: Per-rule fixtures have no fixed location

FR-41 says "Every rule ID has a test fixture", and Story 2.1 asks for positive and negative fixtures. The spine assigns checker rules to Builds and registry rules to Docs, but places no fixtures.

**Fix.** State that fixtures live with the rule's implementation: Builds tests for checker rules, Docs `scripts/tests/` for registry rules. Review-only rule IDs are exempt.

## Items checked and found consistent

- The 21-repository scope, 19 direct submodules and the BmadSkills external checkout (AD-1, FR-7).
- Ownership of the CiCd perimeter and the marker block (inherited CiCd AD-4, FR-7, FR-48).
- Warn mode before fail mode, and a new rule warning for one release (AD-2, AD-8, FR-42, §8.5).
- The finding shape `{file, line, rule, hint}` (FR-44).
- Offline self-links resolved against the checkout (FR-45).
- The same-revision fresh-consumer sample (AD-3, FR-19).
- The `docs(readme)` patch rule and a republish only after the Builds tag carries it (AD-11, FR-15, addendum §B.1).
- Platform-only composition (Platform AD-1, AD-10).
- McpCli as the only module-operation surface (Platform AD-11, FR-23).
- A private exposure record with public status only (AD-5, FR-65).
- Testers identified by role, and no tokens in evidence (FR-56, FR-65, NFR-8).
- The profile rendered only from confirmed registry values (AD-14, FR-2).
- Registry status values matching `scripts/validate_registry.py`.
- Stack pins matching the Platform checkout (`global.json` 11.0.100 `latestPatch`) and `documentation.yml` (ubuntu-24.04, checkout v7.0.1 SHA).
- Prebuilt images, CI smoke test, chat, Kubernetes topology and website deferred with their PRD §8.2 triggers.
