---
title: "Review: epics-readiness of the Hexalith Documentation Standard PRD"
reviewed: prd.md (updated 2026-11-10), addendum.md
created: 2026-11-10
seat: epics-and-stories author; AI coding agents implementing one repository at a time
---

# Review: epics-readiness of the Hexalith Documentation Standard PRD

## Verdict

**Conditionally ready.** The PRD is well above average for downstream use. It has a tight glossary, one capability per FR, testable consequences, explicit assumptions, and a launch gate that maps to FRs. Epics for the foundations in Hexalith.Docs, Hexalith.Builds, and Hexalith.AI.Tools can be drafted now. The Level 1 migration epic (21 per-repository stories) and the launch-gate epic should wait for fixes to two critical findings and the high findings below.

- **ER-1.** As written, Platform can't reach Level 1.
- **ER-2.** The agent stranger test is on the Level 1 critical path, but it has no defined environment, harness, or operator.
- **ER-3.** No rule catalog connects the standard, the docs check, and the agent rules.
- **Sequencing and human-only steps.** Several prerequisites are implicit or missing, such as a public `Hexalith/.github`, per-repository release config, and shared CI for the seven repositories that have none. Human-only steps aren't tagged, so agents may try admin actions or stall on them.

Most FRs need no rewrite. The fixes are a few added FRs, a rule catalog, an owner and realization tag on each FR, and some explicit "depends on" lines.

Evidence beyond the PRD comes from the workspace (`references/*` submodules declared in the root `.gitmodules`). It was read-only, and no nested submodule was initialized.

## Findings

Severity: **critical** blocks a correct epic structure or the launch gate as specified. **High** forces the epics author to invent requirements or sequencing that change scope. **Medium** produces ambiguous acceptance criteria or rework. **Low** is polish.

### Critical

#### ER-1: Platform can't reach Level 1, so launch-gate item 2 depends on Level 2

- **Location:** FR-17, FR-57, FR-58, §7.3 item 2, addendum §A (Platform row); the same pattern affects Hexalith.CiCd and Hexalith.Docs.
- **Issue:**
  - **Platform.** FR-17 requires at least one quickstart block in every README, and a "Run it" block may be added only once it meets its time target. FR-57 excludes "Run it" blocks from Level 1. Platform publishes no packages and has no tool, and its only proposed block is "Run it", the "Try it" path. So Platform's Level 1 needs a Level 2 result (agent stranger test of "Try it"), and Level 2 depends on Platform deploying the chatbot (mid-December, R-1). Launch-gate item 2 ("all 21 reach Level 1") silently inherits the Level 2 timeline.
  - **Hexalith.CiCd.** It is proposed as "Use the tool" but has no content (Open Question 5), so no honest block exists.
  - **Hexalith.Docs.** FR-17 makes its Quickstart link to "Try it". FR-26 and NFR-3 forbid promising "Try it" before it passes the agent stranger test.
- **Fix:** Add an explicit Level 1 rule for repositories that have no publishable block yet. One option: a Quickstart section that states the status, with no time claim, plus a link to the development guide. That rule should be allowed for Platform until FR-58 and for CiCd until it has content. Make the Hexalith.Docs "Try it" link follow FR-26's gating. Or move Platform Level 1 explicitly after "Try it" in §7.4 and say so in §7.3.

#### ER-2: The agent stranger test gates Level 1 but is undefined as a deliverable

- **Location:** FR-19, FR-21, FR-51, FR-52, FR-53, FR-57; Glossary "Clean machine"; UJ-2; addendum §C.
- **Issue:**
  - FR-57 pulls FR-19 and FR-21 into Level 1, and both include "meets its 5-minute time target". Time targets are verified only by the agent stranger test. So about 19 Level 1 stories (14 "Use the package" and 5 "Use the tool") each need 3 timed fresh-agent runs. FR-54 doesn't list these blocks as triggers.
  - No FR delivers the test kit: the environment image, the launch procedure, the friction log template, the results file format and path, and the issue-filing step.
  - "Clean dev container" (FR-53) is undefined.
  - The Glossary's "Clean machine" excludes the .NET SDK. So a "Use the package" target measured on it would include installing the SDK, which contradicts UJ-2, where Karim is a .NET developer.
  - An implementing agent can't be its own "fresh agent session with no prior context". Someone or something has to launch that session, and the PRD doesn't say who or how.
  - "Try it" must run "on a clean machine", and nothing provisions one for an agent.
- **Fix:**
  - Add an FR (for example FR-53a "Stranger test kit" in Hexalith.Docs). It defines one environment per block type (for example, "Use the package" runs in a container with only the pinned .NET SDK), a scripted or documented launch of a headless agent session, the record format and path (absorbing FR-56), the friction log template from addendum §C, and who may start a run: a maintainer, or an automation with an API key.
  - Decide whether time targets for "Use the package" and "Use the tool" are a Level 1 condition or only SM-4. If they are Level 1, add them to FR-54's triggers.
  - Add "Clean dev container" to the Glossary.

### High

#### ER-3: No rule catalog, and the standard, docs check, and agent rules depend on each other in a circle

- **Location:** FR-1 (third bullet), FR-41, FR-44, FR-46, FR-47, FR-49 (third bullet), NFR-5.
- **Issue:** FR-1 and FR-49 require every enforced rule to name its docs check rule ID. FR-41 implements rules taken from the standard. No list of rule IDs exists, and FR-41 covers only six rule groups. Many testable rules aren't assigned to the docs check, to review, or to the stranger test:
  - FR-9's fixed heading text and Contributing link targets
  - the Packages section only when packages exist
  - the License SPDX identifier
  - FR-17's block names
  - FR-18's prerequisites-first rule
  - FR-22's AI prompt presence and the 10-line limit
  - FR-34's absence of local community files (otherwise an agent can re-add CONTRIBUTING without any signal)
  - FR-36's development guide presence
  - NFR-6's alt text
  - the "no table of contents" rule
  - FR-50's "domain module" wording in public docs

  An epics author can't size the docs check epic or write acceptance criteria for FR-1 without this list.
- **Fix:** Add a rule catalog, either to the standard or as an addendum section, and make it the first story of the foundations. Columns: rule ID, rule text, source FR, enforced by (docs check, review, or stranger test), applies to (README, docs, CONTRIBUTING, per-package), suppressible (yes/no, which settles FR-46), and introduced in warn mode (yes/no). Order the work as: catalog, then the docs check, then the standard citing the IDs.

#### ER-4: Hexalith.Docs can't pass its own docs check in fail mode

- **Location:** FR-1, FR-3, FR-4, FR-5, FR-7, FR-13, FR-17, FR-41 (scope `docs/**/*.md`), FR-46 (third bullet).
- **Issue:**
  - The standard (assumed `docs/documentation-standard.md`) must describe the banned internal-planning patterns and show banned badges and raw HTML. FR-46 makes internal-planning and badge rules unsuppressible, so the standard trips them.
  - Template files under `docs/` would be scanned as documentation pages, with placeholder links and all three quickstart blocks.
  - The dev container template's location isn't set. At the repository root it becomes Hexalith.Docs' own `.devcontainer/`.
  - The migration prompt's location isn't set either. FR-7 models it on a `.github/prompts/` file, but if it lands under `docs/`, it is scanned.
  - See ER-1 for the Hexalith.Docs "Try it" link.
- **Fix:** Fix template and prompt paths outside the scanned set, or add a non-suppression mechanism such as a docs check path exclusion listed in the catalog. For example: `templates/README.md`, `templates/development.md`, `templates/devcontainer/`, and `.github/prompts/migrate-to-level-1.prompt.md`. Let the standard show examples in a form the patterns don't match, or exempt the standard's file by rule-catalog design rather than by suppression.

#### ER-5: Missing prerequisites before any repository can switch to fail mode

- **Location:** FR-9 item 8, FR-25, FR-31, FR-33, FR-42, FR-45; §7.4; §10.
- **Issue:**
  - No FR creates `Hexalith/.github`. It appears only in §10 as needing admin rights.
  - In fail mode, every README's Contributing section links by absolute URL to the organization CONTRIBUTING, and the docs check fails on broken internal links (FR-45). So `Hexalith/.github` must exist, be public, and contain CONTRIBUTING before the first migration merges.
  - Links to the standard or guides in Hexalith.Docs fail for an unauthenticated lychee while Docs is private. FR-31 only says "before launch".
  - GitHub shows the organization profile README, and applies default community health files, only when `.github` is public. So FR-25 and FR-33 can't be verified while it is private.
  - Branch protection (FR-42) isn't available for a private repository on the Free plan, so Hexalith.Docs can't get its required check until it is public.
- **Fix:** Add an FR, or a §7.4 row, for creating `Hexalith/.github` as a public repository with community files before any migration. Split FR-31 into "`.github` public before migrations" and "Docs public before migrations, or before the first migration that links to it, after the FR-31 content review". Add explicit "Depends on" lines to FR-42 and FR-57.

#### ER-6: The republish mechanism lands in 16 repositories, not one shared config, and may need human approval

- **Location:** FR-15, R-11, addendum §B "Package republish", FR-7.
- **Issue:**
  - Addendum §B proposes a release rule "in Hexalith.Builds' shared release config". But semantic-release is configured per repository: `references/Hexalith.Tenants/.releaserc.json` uses the default `@semantic-release/commit-analyzer` with no `releaseRules`. So the docs-release trigger is a change to 16 package repositories.
  - `Hexalith.Builds/.github/workflows/domain-release.yml` runs the release in a protected environment (default `production`) and has a governed-release mode with release-authority inputs. A republish may therefore need a human approval per repository.
  - FR-7 doesn't say which Conventional Commit type and scope the migration PR must use to trigger the release (for example `docs(readme):`). The Builds commitlint config allows `docs` but doesn't restrict scopes.
- **Fix:**
  - Add an FR or story set, "Docs-only release trigger": one change per package repository (×16) to `.releaserc.json`, made before that repository's migration merges.
  - Require FR-7 to emit the trigger commit type and scope.
  - Mark the release approval as human-only.
  - Correct addendum §B.

#### ER-7: Seven repositories need shared CI adoption, but no FR covers it

- **Location:** FR-38 ("CI status, required"), FR-39, FR-40, FR-43; extract §C.1.
- **Issue:** FR-43 adds only the docs check to the repositories outside Builds CI: AI.Tools, BmadSkills, ChatBot, CiCd, McpCli, Platform, and Docs. But every README needs a CI status badge that reads a default-branch workflow. ChatBot, McpCli, and Platform build .NET code, so they also need the SonarQube Cloud badges, which require the Hexalith.Builds reusable CI (FR-40). None of these three runs any quality CI today. Adopting the shared CI there is a real CI migration with no FR. For repositories with no .NET code, it isn't stated whether the docs check workflow counts as the "CI status" badge source.
- **Fix:** Add an FR, "Shared CI in every in-scope repository": `domain-ci.yml` for repositories with .NET code, and the docs check workflow as the CI badge source for repositories without it. Name the per-repository list, and make it a prerequisite of those repositories' Level 1 stories.

#### ER-8: FR-19 hides a cross-repository CI mechanism with an open architecture decision

- **Location:** FR-19 (second bullet), FR-57, addendum §B "Compiled samples".
- **Issue:** "CI compiles the sample on every pull request that changes it or the package it uses" needs a mechanism in Hexalith.Builds, either snippet injection (Option 1) or extracting and compiling fenced blocks (Option 2), plus per-repository wiring in 14 "Use the package" repositories. The FR is filed under README content, so an epics author would bury the mechanism inside each migration story. The architecture choice is still open, and 14 Level 1 stories depend on it.
- **Fix:** Split out an FR in §4.7, for example "Compiled samples", owned by Hexalith.Builds. Make the architecture decision on Option 1 or 2 an explicit prerequisite. Keep FR-19 for block content only.

#### ER-9: FR-48 per-repository work is underestimated

- **Location:** FR-47, FR-48, addendum §B "Agent entry points".
- **Issue:** The workspace shows:
  - Hexalith.CiCd and Hexalith.Platform have no `AGENTS.md`, `CLAUDE.md`, or `.github/copilot-instructions.md`.
  - Hexalith.PolymorphicSerializations has no `.github/copilot-instructions.md`.
  - Hexalith.BmadSkills isn't in the workspace, so it can't be inspected locally.
  - Every module repository pins `Hexalith.AI.Tools` as a submodule. The new `hexalith-docs-instructions.md` therefore reaches a repository only after its submodule pointer moves, and the shared baseline forbids agents to update dependencies unless the task explicitly requires it.
  - The baseline tells agents to stop when the instructions file can't be found, which happens in a standalone clone without submodules.
- **Fix:** In FR-48, state the per-repository deliverables:
  - Create any missing entry points from the shared baseline.
  - Bump the `references/Hexalith.AI.Tools` pointer to the commit that contains the documentation rules. Make this an explicitly authorized dependency update.
  - Verify that the chain resolves in a fresh clone that initializes only root-declared submodules.

  Make FR-47 merged a prerequisite.

#### ER-10: Where a migrating agent works, and how it reads Hexalith.Docs artifacts, is unstated

- **Location:** FR-2, FR-3 to FR-7, UJ-5, FR-57.
- **Issue:** Templates are "copied once", and the migration prompt "reads" the module registry. An agent migrating Hexalith.Parties needs the standard, registry, templates, and prompt, which live in Hexalith.Docs. Hexalith.Docs is private and isn't a submodule of module repositories. The Hexalith.Docs workspace does declare 19 module repositories as root submodules, but not Hexalith.BmadSkills, and the shared baseline requires working "from the repository that owns the change". Without a stated working model, every per-repository story will improvise its setup.
- **Fix:** State the execution model in §7.4, or in FR-7 if it covers both cases:
  - **Option A:** run migrations from the Hexalith.Docs umbrella workspace and commit inside each `references/<repo>`, after adding Hexalith.BmadSkills to the root `.gitmodules`.
  - **Option B:** the agent works in a standalone clone and fetches the Docs artifacts by absolute URL or `gh`, which requires Docs to be readable.

  Name the commit boundary: one PR per repository, opened in that repository.

#### ER-11: Human-only steps aren't tagged, so agents may attempt or stall on them

- **Location:** §10, FR-2, FR-15, FR-28 to FR-35, FR-40, FR-42, FR-45, FR-52, FR-55, FR-57, Open Questions 1 to 8.
- **Issue:** Admin rights are listed once in §10. Individual consequences don't say "a human does this", so an agent implementing FR-28 or FR-35 will try `gh repo edit` or the API with whatever token it has. The full list is in the table under "Human-only and admin steps" below.
- **Fix:** Add a `[HUMAN]` tag (a decision, or an admin or third-party right) to each consequence that needs one. Split each such FR into "agent prepares" (a script, a list, or a dry-run report) and "human applies". The table below can go into the PRD as-is.

#### ER-12: FR-57 bundles too much for one per-repository story, and §7.1 disagrees with it

- **Location:** FR-57, §7.1 second bullet, FR-15.
- **Issue:**
  - One "Level 1 for repo X" story would cover a lot: README rewrite, development guide, operations page, deleting local community files and moving their content, badges, the NuGet `Description` in project files, entry points with the submodule bump, compiled-sample wiring, the switch to fail mode, admin metadata, a republish, package-page verification, and possibly stranger tests. That is too big for an agent session or a single review (R-4).
  - §7.1 counts FR-9 to FR-22 (including FR-20 "Run it") and FR-33 as Level 1. FR-57 excludes "Run it" and doesn't mention FR-33 or FR-40, although FR-39 depends on FR-40.
- **Fix:** Define the per-repository unit as about three stories:
  1. A content migration PR, which agents do: FR-9 to FR-14, FR-16 to FR-19, FR-21, FR-22, FR-34, FR-36 to FR-39, FR-48, and fail mode.
  2. Repository settings, which a human applies: FR-28, FR-35, branch protection.
  3. Republish and verify: FR-15.

  Align §7.1 with FR-57, and list FR-40 per repository as a dependency.

### Medium

#### ER-13: Rule FRs and story FRs aren't distinguished

- **Location:** FR-9 to FR-14, FR-16 to FR-18, FR-22, FR-34, FR-38, FR-39, FR-51.
- **Issue:** These FRs are rules. Each is realized three times: stated in the standard (FR-1), enforced by the docs check (FR-41), and applied per repository (FR-57). An epics author may turn each one into its own story ×21, which would produce about 300 stories.
- **Fix:** Tag each FR with a realization type: `story`, `rule (stated FR-1 / enforced FR-41 / applied FR-57)`, `gate`, or `human`. The table under "FR ownership and multiplicity" below is a draft.

#### ER-14: The docs check has no source for the per-repository facts it needs

- **Location:** FR-9 item 5, FR-11, FR-16, FR-38, FR-39, FR-41, FR-42, FR-46, FR-2.
- **Issue:** The script must know facts it can't infer:
  - whether the repository publishes packages (for the conditional Packages section and the required NuGet badge)
  - which package the NuGet badge reads in a multi-package repository
  - the SonarQube Cloud project key (for "same repository")
  - the expected quickstart blocks
  - where per-package READMEs live (Commons uses `src/libraries/*/README.md`)

  The module registry is a Markdown table in Hexalith.Docs, and the docs check runs in Hexalith.Builds. The identity checks in FR-2, FR-11, and FR-28 (README = About = registry = front door) aren't assigned to any check.
- **Fix:** Add a docs check configuration schema (one file per repository: mode, suppressions with reasons, packages, primary package, Sonar key, per-package README glob). Or make the registry machine-readable, for example a YAML file rendered into the standard. Add a registry consistency check, or a story that compares README, About (`gh repo view --json description`), registry, and front door.

#### ER-15: The registry has no one-sentence descriptions yet

- **Location:** FR-2, FR-11, FR-25, FR-28, addendum §A.
- **Issue:** Addendum §A has category, blocks, and packages, but no one-sentence description column. Drafting 21 descriptions of 120 characters or fewer, and having a maintainer confirm them, comes before FR-11 in every migration and before FR-25 and FR-28. Only the category has a stated confirmation point.
- **Fix:** Add a description column to the proposal, and make FR-2's human confirmation cover descriptions as well as categories. Make it a prerequisite for the migration waves and the front door.

#### ER-16: The docs check workflow has no versioning or self-test policy

- **Location:** FR-41, FR-42, FR-44, R-5.
- **Issue:** Callers of Hexalith.Builds workflows reference `@main` in 71 places, plus 24 different commit SHAs. If the docs check is called at `@main`, one rule change fails all 21 fail-mode repositories at once. FR-44's actionable findings have no verification fixtures.
- **Fix:** Add consequences to FR-41: callers pin a tag or SHA (matching the addendum's own advice for lychee), rules change through a versioned release, and Hexalith.Builds keeps fixture READMEs, one per rule ID, with expected findings. Those fixtures are how an agent proves FR-44.

#### ER-17: FR-40 omits the human setup, fork pull requests, and legacy projects

- **Location:** FR-40, FR-39, UJ-4.
- **Issue:**
  - SonarQube Cloud needs an organization, a GitHub binding, a token, and an organization secret, all human steps.
  - Each repository must bump its CI caller reference to pick up the scanner.
  - Pull requests from forks get no secrets. Unless the shared CI skips the Sonar step there, Tomás's first pull request (UJ-4) fails CI.
  - Commons and PolymorphicSerializations have legacy SonarCloud badge sets (4 and 11 badges), so their projects may already exist under other keys.
- **Fix:** Add consequences: "Sonar analysis is skipped, without failing, on pull requests that lack the token", "the project key follows `<convention>`", and "legacy projects are reused or deleted, a human decision". Tag the setup `[HUMAN]` and list the per-repository caller bumps.

#### ER-18: Some consequences need human judgment but aren't labeled

- **Location:**
  - FR-7, fifth bullet (move versus delete)
  - FR-8, first bullet ("explains")
  - FR-12, fifth bullet (rendered page has no raw markup)
  - FR-15, third bullet ("an agent verifies", by an unspecified method)
  - FR-17, second bullet ("most likely to take first")
  - FR-27 ("shows the current UI")
  - FR-49, second bullet ("only rules an agent can't infer")
  - FR-57, fifth bullet ("accurate")
  - NFR-1
- **Issue:** An agent can't prove these with a command. FR-15 and FR-12 can be made agent-verifiable, for example with a Playwright snapshot of the nuget.org page or by fetching the package README through the NuGet API.
- **Fix:** Label each one `[REVIEW]` with the deciding role. For FR-12 and FR-15, specify the method and the evidence file.

#### ER-19: Community file contents are unspecified and their verification is partly unworkable

- **Location:** FR-33, FR-34, SM-7.
- **Issue:**
  - FR-33 names six files but not their content: which issue templates, whether `config.yml` has contact links, the Code of Conduct version, where support happens (Discussions? issues?), the SECURITY wording, and the pull request template checklist. An epics author would invent all of it.
  - "Community Standards page shows all six as present" may not be checkable for SUPPORT, because GitHub's checklist doesn't list SUPPORT. Confirm which items the checklist and `GET /repos/{owner}/{repo}/community/profile` report.
  - SM-7 says "complete", which isn't the same as "all six".
  - `Hexalith/.github` isn't an in-scope repository, so the front door and the organization CONTRIBUTING are never docs-checked for links, NuGet-safe rules, or internal planning content.
- **Fix:** Add content consequences or a decision (Open Question 9: the support channel). Use an API-based verification and name the fallback for SUPPORT. Run the docs check in `Hexalith/.github` (README skeleton rules off).

#### ER-20: The AI prompt pattern is shaped for "Run it"

- **Location:** FR-6, FR-22, FR-19.
- **Issue:** Steps 3 and 4 ("wait until services report healthy", "return the dashboard URL") don't apply to "Use the package" or "Use the tool". A "Use the package" block has a command (`dotnet add package`) and a code sample, so "wraps exactly one command" is ambiguous there.
- **Fix:** Define one pattern variant per block type in FR-6, or state that "Use the package" prompts wrap `dotnet add package` and then have the agent paste and run the sample.

#### ER-21: FR-23 mixes Platform's deliverables with this initiative's work

- **Location:** FR-23, FR-24, FR-55, §6 first bullet.
- **Issue:**
  - "One command deploys the chatbot and every service it needs" is Platform's work, which §6 puts out of scope. An epics author can't own it but must depend on it.
  - FR-24 depends on Platform supporting Kubernetes deployment, and that dependency isn't stated.
  - FR-55 doesn't say whether the outside tester uses the command or the AI prompt.
- **Fix:** Mark these consequences `[DEPENDENCY: Platform]`, and give this initiative only the README block, the tests, and the front door link. State which path the human stranger test uses.

#### ER-22: The development guide's scope conflicts with the README skeleton

- **Location:** FR-9 item 8, FR-36.
- **Issue:** Every README must link to "the repository's development guide", but FR-36 requires a guide only in repositories that "contain code", and that term is undefined. Docs, CiCd, AI.Tools, and BmadSkills are unclear.
- **Fix:** Define "contains code", or require a development guide in all 21 repositories, with a minimal variant for repositories without code.

#### ER-23: FR-54's triggers and the result records aren't operational

- **Location:** FR-54, FR-56, FR-15 (third bullet), FR-52 (third bullet).
- **Issue:**
  - Nothing detects "a change to a published quickstart's command or prerequisites", so FR-54 relies on memory.
  - FR-56 gives only "under `_bmad-output/`", with no path or schema.
  - FR-15's package-page records and FR-52's calibration decisions have no home at all.
- **Fix:** Have the docs check report a PR that changes a Quickstart section, as a finding or a label. Fix one evidence path, for example `_bmad-output/evidence/stranger-tests/<date>-<repo>-<block>.md`, and one ledger for Level 1 and republish status. That ledger is also the evidence for launch-gate items 2 and 3.

#### ER-24: Two sources of the rules, with no owner keeping them in sync

- **Location:** FR-1, FR-47, NFR-5.
- **Issue:** NFR-5 says the standard states each rule once, but FR-47 restates the rules in Hexalith.AI.Tools. The AI.Tools authoring rule forbids linking out to the standard. No FR says which source wins, or who updates the second one when a rule changes.
- **Fix:** Declare the standard authoritative. Add a consequence that every rule change updates both files in the same release window, matched through rule IDs, and have the docs check rule catalog list the rule IDs the agent file covers.

#### ER-25: FR-45 needs a cross-repository token, and badge URLs contradict "external links never block"

- **Location:** FR-45.
- **Issue:** The central scheduled run opens issues in 21 repositories, which needs a GitHub App or token that a human must create. Badge URLs point to external hosts (shields.io, sonarcloud.io, nuget.org) but are checked on every run in fail mode, so a flaky badge host can block merges. The FR's own statement promises the opposite.
- **Fix:** Tag the token `[HUMAN]`. Either move badge-host reachability to the scheduled run, or accept the risk and say so (R-5).

#### ER-26: FR-32 understates urgency and ownership

- **Location:** FR-32, §7.3 item 6.
- **Issue:** Hexalith.BmadSkills is already one of the 20 public current repositories, so any exposure exists now, not "at launch". "Someone reviews" names no owner. A secret scan (for example gitleaks) can be done by an agent, but revoking credentials and deciding on a history rewrite are human tasks. The repository isn't in the workspace `.gitmodules`.
- **Fix:** Make FR-32 week-one work, split it into an agent scan report and a human "revoke and decide", and name the maintainer as owner.

#### ER-27: Vocabulary drift

- **Location:** throughout.
- **Issue:** Glossary terms have synonyms, or terms are used without a definition:
  - **"First chat message"** (Glossary "Try it", FR-23 statement, FR-24, UJ-1) means the newcomer's message, but the timer stops at **first success**, the chatbot's reply (FR-51, SM-1). FR-24's "reaches a first chat message" is the clearest case.
  - **"About text"** (Glossary, FR-2, FR-11) versus **"About description"** (FR-2, FR-28).
  - **"Reviewer"** (FR-7, R-4) and **"someone"** (FR-32) versus **Maintainer**.
  - **"Operator"** (FR-24, FR-37, Glossary "Operations page"), **"first visitor"** or **"visitor"** (§4.4, FR-25, FR-28, FR-29, FR-30), and **"security researcher"** (FR-35) aren't defined.
  - **"Clean dev container"** (FR-53) versus **Clean machine** and **Dev container**.
  - **"Migration change"** (FR-7), **"migration pull request"** (FR-57), and **"Level 1 migration"** (FR-15, FR-42, FR-48, §7.4, Open Question 6) use an undefined term, "migration".
  - **"Documentation rules file"** (FR-49) versus **Documentation rules**. **"Shared agent instructions"** (Glossary) versus **"shared Hexalith instructions"** (FR-47). **"Agent entry points"** (FR-48) is undefined.
  - **"Working call"** (UJ-2, FR-19), **"sample call"** (FR-19), **"working sample call"** (Glossary, FR-51), and **"first successful call"** (Glossary, FR-51).
  - **"Guide hub"** (§4.4, FR-31) versus **"Hexalith.Docs guides"** (FR-25), **"cross-module guides"** (FR-8), and **"overview guide"** (FR-8, §7.1).
  - **"Shared CI"** (§1, §4.6, FR-40, §7.4) versus **"the Hexalith.Builds reusable CI"** (FR-40) versus **"reusable workflows"** (FR-43). None is defined.
  - **"Package page"** (UJ-2, §4.2, FR-12, FR-15, SM-5) is undefined. It means the nuget.org package page.
  - **"Dashboard URL"** (FR-6) versus **"the URL"** (UJ-1).
  - **Module** says each current repository is a module, and the 20 current repositories exclude Docs. But the registry gives Docs a category, and FR-25 and FR-28 require a category for every in-scope repository.
  - **SM-7's "Community Standards page is complete"** versus FR-33's "shows all six as present".
- **Fix:**
  - Add Glossary entries for migration, operator, visitor (or replace it with Newcomer), package page, shared CI, agent entry points, and clean dev container.
  - Replace "first chat message" with "first success" wherever it stops a timer.
  - Pick "About description".
  - Make Docs either a module or "an in-scope repository with a category".

### Low

#### ER-28: Thin FRs to merge into their parent stories

- **Location:** FR-26, FR-43, FR-44, FR-46, FR-49, FR-50, FR-51, FR-56.
- **Issue:** These FRs can't stand alone as stories:
  - FR-26 is a gate on FR-25.
  - FR-43 is a repository list for FR-42.
  - FR-44 and FR-46 are acceptance criteria of FR-41.
  - FR-49 constrains FR-47.
  - FR-50 is a wording rule for FR-1 and FR-47.
  - FR-51 is standard content.
  - FR-56 is part of the stranger test kit (ER-2).
- **Fix:** Keep the IDs, but note "realized within FR-x" so the epics author doesn't create stories for them.

#### ER-29: FR-58's scope disagrees with Open Question 5

- **Location:** FR-58 (second bullet), Open Question 5, FR-20.
- **Issue:** "Each module with an Aspire AppHost" includes Hexalith.Builds, which is proposed as "Use the tool". FrontComposer already has a `.devcontainer/`, and FR-20 doesn't say whether it is replaced or kept.
- **Fix:** Scope FR-58 to the registry's "Run it" rows, and say what happens to existing dev containers.

#### ER-30: FR-11 doesn't say where `Description` lives or how Commons is handled

- **Location:** FR-11 (third bullet), FR-16.
- **Issue:** Nothing says whether the NuGet `Description` is edited per project file or in a repository-level props file. Commons packages pack per-package READMEs, so "packs the README" is ambiguous for them.
- **Fix:** Name the property's location, and state the rule for Commons packages.

#### ER-31: Destination for internal planning content in `docs/`

- **Location:** FR-8 (third bullet), FR-13, FR-14.
- **Issue:** Backlogs and evidence files under `docs/` (extract §C.2) must leave `docs/`, but FR-14 gives destinations only for release history and runbooks.
- **Fix:** Add a bullet: internal planning content moves to `_bmad-output/` in the same repository, or is deleted if a reviewer decides so.

#### ER-32: No operations page template, and dev container pins aren't enforced

- **Location:** FR-37, FR-5, NFR-5.
- **Issue:** FR-37 has no template, unlike FR-4. FR-5's pinned versions drift once copied, and the docs check doesn't read `.devcontainer/`. Platform's prerequisites are pinned exactly (Aspire CLI 13.6.4, Dapr 1.18.2/1.18.7), so drift can break "Run it".
- **Fix:** Add an operations page template. Either accept dev container drift (R-9) or add a docs check rule for the pinned versions.

#### ER-33: The pilot repository isn't named

- **Location:** §7.4, UJ-5, FR-7.
- **Issue:** UJ-5 uses Hexalith.Works, but nothing makes the pilot a gate before the migration waves.
- **Fix:** Add a §7.4 step: the migration prompt is proven on one or two pilot repositories (for example Works, plus a simple package repository such as PolymorphicSerializations) before the waves start.

## Human-only and admin steps

These steps should carry a `[HUMAN]` tag. Agents may prepare inputs, as the last column shows, but must not apply them.

| Step | FR | Right or decision needed | Agent can prepare |
|---|---|---|---|
| Confirm categories and one-sentence descriptions | FR-2, OQ3 | Maintainer decision | Draft the registry |
| Choose quickstart blocks for Builds, CiCd, AI.Tools, BmadSkills | FR-17, OQ5 | Maintainer decision | Proposal |
| Name reviewers and weekly capacity | FR-57, OQ6, R-4 | Maintainer decision | n/a |
| Create `Hexalith/.github` and make it public | FR-25, FR-33 (ER-5) | Organization owner | Content PR |
| Approve publishing Docs `_bmad-output/`, then change visibility | FR-31 | Maintainer decision, organization owner | Content inventory |
| Archive decisions, then archiving | FR-29, OQ2 | Maintainer decision, organization owner | Candidate list with last-push dates |
| Pin repositories (UI only, as far as known) | FR-30, OQ4 | Maintainer decision, organization owner | Proposal |
| Set About descriptions and topics | FR-28 | Repository admin | `gh repo edit` script, dry run |
| Check About descriptions for typos | FR-28 | Maintainer review | Spell-check report |
| Enable private vulnerability reporting | FR-35 | Repository admin, or an organization default | API script, dry run |
| Branch protection with docs check required | FR-42 | Repository admin | Script, dry run |
| SonarQube Cloud organization, GitHub binding, token, organization secret | FR-40 | SonarQube Cloud admin, organization owner | Setup checklist |
| Cross-repository token or GitHub App for the scheduled link check | FR-45 | Organization owner | Workflow |
| Approve protected-environment releases (republish) | FR-15 (ER-6) | Release owner, nuget.org rights | Release PRs, verification |
| Review and merge each migration PR | FR-57 | Maintainer | The PR and its decision list |
| Revoke exposed credentials; decide on a history rewrite | FR-32, OQ8 | Credential owner, maintainer | Scan report |
| Decide on calibration (each target stays or changes) | FR-52 | Maintainer decision | Baseline results |
| Recruit an outside tester and run the human stranger test | FR-55 | Outside tester | Protocol, friction log template |
| Decide what "Try it" needs (key, account, mailbox) | FR-23, OQ1 | Platform maintainer | n/a |
| Decide to launch | §7.3 | Maintainer | Launch-gate evidence checklist |

## FR ownership and multiplicity (draft)

**Repository counts** come from addendum §A:

- 16 repositories publish packages.
- 14 have a "Use the package" block.
- 5 have a "Use the tool" block.
- 12 have an AppHost (11 modules plus Platform).

**Realization types:**

- **S**: one or a few stories.
- **R**: a rule. It is stated in FR-1, enforced by FR-41 where possible, and applied per repository in FR-57.
- **G**: a gate.
- **H**: a human step.

| FR | Owning repository or place | Multiplicity | Type | Depends on |
|---|---|---|---|---|
| 1 | Docs | 1 | S | rule catalog (ER-3) |
| 2 | Docs | 1 | S + H | OQ3 |
| 3, 4 | Docs | 1 each | S | 41 |
| 5 | Docs | 1 | S | n/a |
| 6, 8 | Docs | 1 each | S | 1 |
| 7 | Docs | 1, plus a pilot | S | 1 to 4, 41 |
| 9, 10, 12, 13, 14, 17, 18, 22 | each in-scope repository | ×21 | R | 1, 41 |
| 11 | each repository, project files, GitHub About | ×21 | R + H | 2 |
| 15 | each package repository (`.releaserc.json`), nuget.org | ×16 | S + H | migration merged, ER-6 |
| 16 | Commons | 1 | S | 41 |
| 19 | Builds (mechanism), each "Use the package" repository | 1 + ×14 | S + R | ER-8 decision |
| 20 | each "Run it" repository | ×11 (Level 2) | S | 5, 53 |
| 21 | each "Use the tool" repository | ×5 | R | 53 if time targets are in Level 1 |
| 23, 24 | Platform | 1 each | S + G | Platform (external) |
| 25 (+26, 27) | `Hexalith/.github` | 2 (before and after "Try it") | S | 2, ER-5; 53 for the link |
| 28 | GitHub settings | ×21 | H | 2 |
| 29, 30, 31 | organization settings | 1 each | H | OQ2, OQ4 |
| 32 | BmadSkills | 1 | S + H | n/a |
| 33 | `Hexalith/.github` | 1 to 2 | S | ER-5 |
| 34 | the 5 repositories with a local CONTRIBUTING, plus EventStore's Code of Conduct | ×5 | R | 33 |
| 35 | GitHub settings | ×22 | H | 33 (SECURITY) |
| 36 | each repository with code | ×about 18 | S (inside migration) | 4 |
| 37 | McpCli, Works, and others as found | ×about 3 to 5 | S (inside migration) | n/a |
| 38, 39 | each repository | ×21 | R | 40, ER-7 |
| 40 | Builds, SonarQube Cloud, each .NET repository | 1 + ×about 17 | S + H | ER-7 |
| 41 (+44, 46) | Builds | 1 epic | S | rule catalog |
| 42 (+43) | Builds (input), each repository (caller), branch protection | 1 + ×21 + ×21 H | S + H | 41 |
| 45 | Builds | 1 | S + H | 41 |
| 47 (+49, 50) | AI.Tools | 1 | S | rule catalog |
| 48 | each repository (entry points, submodule bump) | ×21 | S (inside migration) | 47 |
| 51 | Docs (standard) | n/a | R | n/a |
| 52 | Docs records, each existing quickstart | 1 | S + H | 53 |
| 53 (+54, 56) | Docs (kit) | 1 | S | ER-2 |
| 55 | outside tester | 1 to 2 | H + G | 23, 26 |
| 57 | each repository | ×21 (about 3 stories each, ER-12) | G | all of the above |
| 58 | Platform, each "Run it" repository | 1 + ×11 | G | 20, 23, 24 |

## Missing FRs an epics author would otherwise invent

Each of these is covered by the finding in parentheses.

1. A rule catalog with rule IDs, enforcement, and suppressibility (ER-3).
2. A stranger test kit: environments, launch procedure, templates, and the record path (ER-2).
3. Creating `Hexalith/.github` as a public repository before migrations (ER-5).
4. A docs-only release trigger per package repository (ER-6).
5. Shared CI adoption in the seven repositories outside Builds CI (ER-7).
6. Compiled samples as a Hexalith.Builds mechanism (ER-8).
7. A docs check configuration schema, a machine-readable registry, and a consistency check (ER-14).
8. Versioning and fixture tests for the docs check (ER-16).
9. An execution model for migrating agents, including adding BmadSkills to the workspace (ER-10).
10. A Level 1 and republish status ledger, and the launch-gate evidence checklist (ER-23, §7.3).
11. An operations page template (ER-32).
12. Content requirements for community files, and a support channel decision (ER-19).

## Proposed epic outline (sanity check)

The epics are ordered by dependency. Each line ends with its FR IDs and, where they apply, the findings it absorbs. Epics 1 to 6 can run in parallel after Epic 0, except where an arrow shows otherwise. Epic 9 is gated on Epics 1 to 8.

0. **Decisions and organization prerequisites** (mostly human): confirm the registry (categories and descriptions), Open Question 5 block choices, reviewers, create a public `Hexalith/.github`, set up SonarQube Cloud, create the cross-repository token, approve the Docs content, and make the BmadSkills scan urgent. FR-2 (confirmation), FR-31 (content review), FR-32; ER-5, ER-11, ER-26.
1. **Standard foundations in Hexalith.Docs**: the rule catalog, the standard, the module registry (machine-readable), the AI prompt pattern variants, time targets, vocabulary, and the overview guide. FR-1, FR-2, FR-6, FR-8, FR-50, FR-51; ER-3, ER-14, ER-20.
2. **Docs check in Hexalith.Builds** (after Epic 1's rule catalog): the job, the configuration schema, actionable findings, suppressions, the mode input, versioning, fixtures, and the central weekly link check. FR-41, FR-42 (input), FR-44, FR-45, FR-46; ER-4, ER-16, ER-25.
3. **Templates and migration prompt in Hexalith.Docs** (after Epic 2): README, development guide, dev container, and operations page templates; then the migration prompt and its execution model. FR-3, FR-4, FR-5, FR-7; ER-4, ER-10, ER-32.
4. **Shared CI, quality signals, and release plumbing**: adopt shared CI where it is missing, the SonarQube Cloud scanner (skipped on fork PRs), compiled samples, and the docs-only release rule in each package repository. FR-19 (mechanism), FR-40, FR-15 (mechanism); ER-6, ER-7, ER-8, ER-17.
5. **Documentation rules for agents in Hexalith.AI.Tools**: the topical file, the 100-line budget, sync with the standard. FR-47, FR-49, FR-50; ER-24.
6. **Organization community files and front door v1** (after Epic 0): the community files, private vulnerability reporting, the front door without the "Try it" link, About descriptions and topics. FR-25, FR-28, FR-33, FR-35; ER-19.
7. **Warn-mode rollout** (×21 caller PRs, after Epic 2): FR-42 (warn mode), FR-43.
8. **Stranger test kit and baseline** (November): FR-53, FR-54, FR-56, FR-52 (with the human calibration decision); ER-2, ER-23.
9. **Level 1 migration** (pilot first, then waves). For each repository: (a) the content PR, (b) repository settings `[HUMAN]`, and (c) republish and verify. This covers FR-9 to FR-14, FR-15, FR-16, FR-17 to FR-19, FR-21, FR-22, FR-34, FR-36 to FR-39, FR-48, and FR-57; ER-1, ER-9, ER-12, ER-13, ER-22, ER-31, ER-33.
10. **Platform "Try it" and Kubernetes how-to** (depends on Platform, which is external): FR-20 (Platform), FR-23, FR-24, with "Try it" agent stranger test iterations; ER-21.
11. **Front door v2 and launch gate**: the "Try it" link, the optional demo, pins, applying the archive list, Docs visibility, branch protection everywhere, the human stranger test, the launch-gate checklist, and the launch decision. FR-26, FR-27, FR-29, FR-30, FR-31, FR-42 (enforcement), FR-55, §7.3.
12. **Level 2 "Run it" per module** (before or after launch): FR-58, FR-20, FR-5 (per repository); ER-29.

**Structure check.** Every FR from FR-1 to FR-58 lands in at least one epic. Only Epic 9 multiplies ×21, so the per-repository story count is about 63, plus about 16 release-rule PRs and 21 warn-mode caller PRs. Epic 0 is the only epic that must start entirely with humans. Without ER-1's fix, Epic 9 can't close for Platform before Epic 10. Without ER-2's fix, Epic 9 can't close for the 19 repositories with "Use the package" or "Use the tool" blocks before Epic 8.
