---
title: "Extract: brief inputs for the Hexalith Documentation Standard PRD"
created: 2026-11-09
sources:
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/addendum.md
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/.memlog.md
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/inputs/initial-brief.md
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/brief.md (context, for diffing)
---

# Extract: brief inputs for the PRD

Source tags: **[ADD]** addendum.md, **[MEM]** .memlog.md (line number), **[INIT]** initial-brief.md, **[BRIEF]** brief.md, **[WS]** observed in this workspace (not from the sources). All decisions were accepted on 2026-11-09.

Short-name to full-name map ([WS] from this repo's `.gitmodules`, plus [BRIEF] for BmadSkills): agents = Hexalith.Agents, aitools = Hexalith.AI.Tools, bmadskills = Hexalith.BmadSkills, builds = Hexalith.Builds, chatbot = Hexalith.ChatBot, cicd = Hexalith.CiCd, commons = Hexalith.Commons, conversations = Hexalith.Conversations, eventstore = Hexalith.EventStore, folders = Hexalith.Folders, frontcomposer = Hexalith.FrontComposer, mcpcli = Hexalith.McpCli, memories = Hexalith.Memories, parties = Hexalith.Parties, platform = Hexalith.Platform, polymorphicserializations = Hexalith.PolymorphicSerializations, projects = Hexalith.Projects, tenants = Hexalith.Tenants, timesheets = Hexalith.Timesheets, works = Hexalith.Works, xppmodel = Itaneo org (out of scope). Hexalith.Docs (this repository) and `Hexalith/.github` (not yet created) are extra and are not among the 20.

---

## A. Accepted decisions

| # | Topic | Accepted option (gist) | Concrete rules and thresholds |
|---|---|---|---|
| 1 | Deploy in minutes | **B: dev container + `aspire run`**, with an AI prompt on top | `.devcontainer/` pins .NET, the Aspire CLI, Dapr, and Docker-in-Docker. Open it in VS Code, or in Codespaces with one click, then run `aspire run`. The command is `aspire run` everywhere. The AI prompt is **10 lines or fewer** and wraps only that command. It checks prerequisites (or opens the dev container), runs the command, waits for services to be healthy, returns the dashboard URL, and explains the first call. Rule: "If a prompt needs more than about 10 lines, fix the command, not the prompt." Targets: "Try it" runs **on Docker, on the user's own machine**, and the time target applies to it. Platform gets a **Kubernetes how-to, with no time target**. **Azure, AWS, and Scaleway come after launch.** Contingency: consider option C (prebuilt images) later, for the "Try it" path only, if B misses the 20-minute target. |
| 2 | README skeleton and quickstarts | **C: one skeleton where only the quickstart varies** | Each module is labeled **business** or **technical**; the label is used in the module list on the org page. Each repository picks **one or more of three quickstart blocks**: "Use the package", "Run it", "Use the tool". Example: eventstore uses "Use the package" for its SDK and "Run it" for its server. The skeleton itself is in B.1. |
| 3 | Front door | **A + B: org profile README (`Hexalith/.github/profile/README.md`) + Hexalith.Docs for cross-module guides** | The profile **fits on one screen**. It says what Hexalith is, links "Try it" to the Platform quickstart, and lists every module with its category (business or technical), a one-line description, and a link. Cross-module guides (concepts, architecture, how modules fit together) live in Hexalith.Docs. Every repository gets an About description and topics. Revisit a website once there are enough docs to justify one. |
| 4 | GitHub README and NuGet page | **A: one NuGet-safe README per repository** (Hexalith.Builds already packs it) | Absolute HTTPS links and images, no raw HTML, badges only from hosts nuget.org allows. "Linting enforces these rules." commons keeps its per-package READMEs; other repositories don't have to adopt them. Revisit C (generate at pack time) only if a single page would mislead users of a repository's packages. |
| 5 | Quality indicators | **The three required badges plus SonarQube Cloud** | Rule: **"no badge without a pipeline that produces it."** NuGet version (Shields): required when the repository publishes packages. CI build status (GitHub Actions workflow badge): required. License (Shields): required. SonarQube Cloud quality gate and coverage: accepted (add the scanner once to the Hexalith.Builds reusable CI; one Sonar project per repository; an organization token). Skeleton cap: up to five badges. |
| 6 | Contributor docs and policies | **C: hybrid** | Org defaults in `Hexalith/.github` (CONTRIBUTING, code of conduct, SECURITY, SUPPORT, issue and PR templates) plus `docs/development.md` in each repository for build, test, and debug steps. Delete each repository's own CONTRIBUTING so the org default applies. Move runbooks now in READMEs into `docs/development.md`. Enable GitHub private vulnerability reporting so SECURITY.md points to a real channel. Move release history to CHANGELOG.md or GitHub Releases. The shared CONTRIBUTING links to each repository's development guide. |
| 7 | Keeping docs consistent | **B + C: agent rules in aitools + docs-check job in builds reusable CI** | The docs check runs markdownlint-cli2, lychee, and a small script for required sections, length, and forbidden content (`_bmad-output`, epic and story IDs, FR/NFR IDs). It **starts as a warning and becomes required in each repository after migration**. An agent migrates each repository with the audit-and-migration prompt. |
| 8 | "Try it" while Platform is in progress | **A (wait to announce), with D (demo video or GIF) optional** | Docs work starts now; don't hold back the docs (repositories and packages are already public). **Don't announce until "Try it" works** (meets its time target). Optional demo video/GIF on the org page "shows the chatbot in 30 seconds". |
| 9 | Rollout | **A, split into two levels of "done" plus cleanup** | Level 1 "Clean" for all 20 current repositories: writing work agents can do with the audit prompt and templates; human review is the bottleneck. Level 2 "Try-able" starts with the Platform "Try it" path, which is the launch gate. Cleanup includes archiving, which can be undone. |
| 10 | Time targets and measurement | **Targets 5 / 15 / 20 minutes or less; human stranger test (B) is the launch gate, agent stranger test (D) runs routinely** | Full detail in section E. |
| 11 | Planning folders | **Keep `_bmad-output/` public in every repository, never link it from READMEs or docs** | Decided in conversation, without an options analysis. [MEM 55]: applies "including Hexalith.Docs and this brief" (user chose "a"). |

### Rejected alternatives (one line each)

- **1A** Better docs for today's path: 30–60+ minutes of installs; "deploy in minutes" stays false.
- **1C** Prebuilt images + `docker compose up` (ghcr.io, Aspire-generated compose): new image pipeline per service, Dapr sidecars in compose, version matrix. Deferred as the fallback for "Try it" only.
- **1D** Azure `azd up` to Azure Container Apps: needs a paid subscription; 10–20 minutes of provisioning.
- **2A** Same sections for every repository: forces "deploy" onto libraries and tooling, creating filler.
- **2B** Separate template per kind of repository: several files to keep in sync.
- **2 (first proposal)** Four kinds (Library, Module, Application, Tooling): rejected; the user groups repositories as business or technical modules instead.
- **3C** Docs website (GitHub Pages with docfx or MkDocs): build, hosting, upkeep; over-engineering for now.
- **3D** Platform README as front door: today a release log aimed at maintainers.
- **4B** Hand-written README per package (as commons does): more files that drift. (commons may keep its own.)
- **4C** Generate the package README at pack time: build tooling to write and maintain. Revisit only if one page misleads.
- **5** OpenSSF Scorecard: "Later" (renders on NuGet only through Shields).
- **5** Coverity Scan: dropped (fragile service, overlaps with Sonar for C#, renders on NuGet only through Shields, no customer or certification needs it; [MEM 29] user "2 no").
- **5** Codacy, Codecov: dropped (overlap with Sonar).
- **6A** Org defaults only: no room for repository-specific steps. **6B** Copy files into each repository: 20 times the edits, copies drift.
- **7A** Written standard only: people and agents won't read it. **7D** Vale prose linting: noisy, skip for v1. **7E** Org rulesets with required workflows: need a paid GitHub plan (plan unknown).
- **8B** Interim "Try it" on a single module (for example Tenants): not the chatbot experience; poor first impression. **8C** Hosted demo instance: hosting and LLM costs, abuse, tenant isolation, operations.
- **9B** Launch set limited to chatbot dependencies: still 17 repositories. **9C** Waves by kind: order seems arbitrary. **9D** Opportunistic updates: never finishes.
- **10A** No number: untestable. **10C** Automated CI smoke test: Docker-in-Docker with Dapr and Keycloak in CI is heavy and flaky; add only for "Try it" and only if quickstarts keep breaking after launch.

---

## B. Launch-scope checklists (FR candidates)

IDs below are added for traceability; the wording is the addendum's.

### B.1 Foundations in Hexalith.Docs

- FD-1 The standard, on one page.
- FD-2 The README skeleton, with three quickstart blocks: "Use the package," "Run it," and "Use the tool".
- FD-3 A `docs/development.md` template.
- FD-4 A dev container template.
- FD-5 The AI-prompt pattern: 10 lines or fewer, wrapping exactly one command.
- FD-6 An audit-and-migration prompt, modeled on `builds/.github/prompts/audit-hexalith-ci-cd.prompt.md`.
- FD-7 Cross-module guides.

**README skeleton: 150 lines or fewer, with these sections in order:**

1. Title and a one-sentence description of **120 characters or fewer**. The description matches the GitHub About text and the NuGet description.
2. Up to **five** badges.
3. What the module does and who it's for, in **five lines or fewer**.
4. Quickstart: one or more quickstart blocks that **fit on one screen**.
5. A packages table, if the repository publishes packages.
6. Documentation links into `docs/`.
7. A "Part of Hexalith" link to the front door.
8. A link to contributing guidance.
9. License.

**Quickstart blocks:**

| Block | What the reader does | Examples |
|---|---|---|
| Use the package | Adds the NuGet package and pastes a short code sample | commons, polymorphicserializations |
| Run it | Runs `aspire run` in the dev container, then makes a first call | memories, eventstore, tenants, parties |
| Use the tool | Installs the tool and runs a first command | mcpcli, builds, cicd, aitools |

### B.2 `Hexalith/.github` (public)

- GH-1 The organization profile (`profile/README.md`).
- GH-2 CONTRIBUTING, with a link to each repository's `docs/development.md`.
- GH-3 CODE_OF_CONDUCT.
- GH-4 SECURITY, with GitHub private vulnerability reporting turned on.
- GH-5 SUPPORT.
- GH-6 Issue and PR templates.

### B.3 Shared CI in Hexalith.Builds

- CI-1 The SonarQube Cloud scanner, with the quality gate and coverage.
- CI-2 A docs-check job that runs markdownlint-cli2, lychee, and a script that checks for required sections, length, and forbidden content. It starts as a warning and becomes required for each repository once that repository is migrated.

### B.4 Hexalith.AI.Tools

- AI-1 Documentation rules in the shared agent instructions (today `aitools/hexalith-*-instructions.md` contain no README rules).

### B.5 Level 1 "Clean" checklist (all 20 current repositories)

- L1-1 The README follows the skeleton and meets its target of 150 lines or fewer.
- L1-2 The README is NuGet-safe: it uses absolute links, avoids raw HTML, and only shows badges from hosts that nuget.org allows.
- L1-3 The one-sentence description matches the GitHub About text and the NuGet description, and topics are set.
- L1-4 The README, CONTRIBUTING, and `docs/` contain no internal planning content: no epics, stories, FR/NFR IDs, or links to `_bmad-output`.
- L1-5 `_bmad-output/` stays public but is never linked from docs.
- L1-6 Repository-level CONTRIBUTING files are removed, so the organization defaults apply.
- L1-7 Runbooks move to `docs/development.md`.
- L1-8 Release history moves to CHANGELOG.md or GitHub Releases.
- L1-9 All links and badges work.
- L1-10 Every `docs/` page linked from the README is accurate. `docs/` folders are cleaned, not reorganized.

### B.6 Level 2 "Try-able"

- L2-1 The Platform "Try it" quickstart on Docker is the launch gate. It ends with a first chat message.
- L2-2 Each module's "Run it" quickstart is added as soon as it meets its time target.
- L2-3 Platform gets a Kubernetes deployment how-to, with no time target.

### B.7 Organization cleanup

- OC-1 After review, archive the repositories listed under Archive candidates (section C.5). Archiving can be undone.
- OC-2 Before launch, check Hexalith.BmadSkills for sensitive data. It contains 106 `.claude.json` files under `skills/reports/` that were copied from eval runs.
- OC-3 Make Hexalith.Docs and `Hexalith/.github` public.
- OC-4 Pin the key repositories.
- (Expectation, not a task) After launch, stars will probably concentrate on Platform, the repository behind "Try it."

### B.8 Requirements stated only in decision text (not in the checklists)

- Every repository gets an About description **and topics** (decision 3). Homepage is not addressed although the baseline notes none is set.
- The org profile fits on one screen, says what Hexalith is, links "Try it" to the Platform quickstart, and lists every module with category, one-line description, and link (decision 3).
- Each quickstart gets an AI prompt of 10 lines or fewer with the five behaviors listed in decision 1.
- The dev container pins .NET, the Aspire CLI, Dapr, and Docker-in-Docker, and opens in VS Code or Codespaces (decision 1). No checklist item adds `.devcontainer/` to each runnable repository; only the template (FD-4) is listed.
- SECURITY.md must point to a real channel: private vulnerability reporting enabled (decision 6).
- Linting enforces the NuGet-safe rules (decision 4), i.e. the docs check must detect relative links, raw HTML, and non-allow-listed badge hosts.
- One Sonar project per repository and an organization token (decision 5).
- Optional demo video or GIF on the org page (decision 8).
- Baseline time measurement "now" (decision 10; [BRIEF] timeline: November).

**Counts:** 11 decisions. 33 checklist items (Foundations 7, `.github` 6, Shared CI 2, AI.Tools 1, Level 1 10, Level 2 3, Org cleanup 4), plus 9 skeleton sections and 9 decision-text requirements in B.8.

---

## C. Current-state baseline (2026-11-09)

Source: read-only survey of local clones plus GitHub org data [ADD]. Every repository is MIT-licensed. "CQL+DR" = CodeQL + dependency review via Hexalith.Builds shared workflows.

### C.1 Repositories

| Repo | README lines | README role today | Badges | NuGet | Quality CI |
|---|---|---|---|---|---|
| agents | 6 | stub | – | yes | CQL+DR |
| aitools | 61 | agent instructions | – | no | none |
| bmadskills | none | – | – | no | none |
| builds | 1275 | build runbook (~935 lines on local tools) | version tag | yes | CQL+DR |
| chatbot | 175 | epic changelog + local setup | – | yes | none |
| cicd | 2 | stub | – | no | none |
| commons | 557 | product intro, per-package READMEs | License, Discord, Build, NuGet, Coverity, Codacy, Sonar×4 | yes | CQL+DR |
| conversations | 157 | contract/evidence log | – | yes | CQL+DR |
| eventstore | 203 | product intro (best example) | stars, NuGet, Build, Docs, License | yes | CQL+DR, coverage |
| folders | 54 | submodule setup | – | yes | CQL+DR, coverage gate |
| frontcomposer | 26 | dependency pinning | – | yes | CQL+DR, Stryker |
| mcpcli | 631 | operator runbook | – | yes | none |
| memories | 138 | quick start + operations | – | yes | CQL+DR, coverage |
| parties | 341 | product intro + appended content | – | yes | CQL+DR, coverage |
| platform | 608 | release/evidence log (SHAs, run IDs) | – | no (source releases) | none |
| polymorphicserializations | 182 | product intro | License, Discord, Build, NuGet, Coverity, Codacy, Sonar×11 | yes | CQL+DR |
| projects | 1 | title only | – | yes | CQL+DR, coverage |
| tenants | 175 | product intro (good example) | CI, NuGet, License | yes | CQL+DR, coverage gate |
| timesheets | 149 | agent hooks + build | – | yes | CQL+DR, coverage |
| works | 131 | release procedure | – | yes | CQL+DR |
| xppmodel (Itaneo) | 2 | stub | – | no (Python) | none |

Derived: repos without NuGet = aitools, bmadskills, cicd, platform (+ xppmodel). Repos with quality CI "none" = aitools, bmadskills, chatbot, cicd, mcpcli, platform (+ xppmodel). Category labels known so far [MEM 30]: memories, cicd, docs, mcpcli are **technical**; full business/technical assignment for all repos is not recorded.

### C.2 Findings that shape the standard

- **The README is the NuGet package page.** `builds/Hexalith.Package.props` packs the root README into every package. projects' README is only a title, so `Hexalith.Projects.Contracts` 1.2.3 on nuget.org shows only a title. Only commons ships per-package READMEs (`commons/src/libraries/*/README.md`).
- **READMEs have no shared purpose:** product intro, contributor runbook, or release/evidence log. [MEM 8]: only ~5 of 20 READMEs are presentable (best: eventstore, tenants).
- **Internal planning content leaks:** epic and story references, FR/NFR IDs, links to `_bmad-output`, backlogs and evidence files under `docs/`, sprint rules in `memories/CONTRIBUTING.md`.
- **AI agents write most docs.** Nearly every repo has agent files; `aitools/hexalith-*-instructions.md` has no README rules; agents tend to add content after the License section.
- **Badges don't match tooling.** Two repos show Coverity, Codacy, and SonarCloud badges, but no workflow runs those scans. The Sonar analyzer is only a compile-time package (`builds/Hexalith.Build.props:40`).
- **Broken links:** badges point to deleted workflows (commons, eventstore); a license badge points to the wrong repo; one link points to a nonexistent sample path.
- **Community health files missing:** no `Hexalith/.github` repo; no repo has SECURITY.md, SUPPORT.md, issue templates, or a PR template; only eventstore has a code of conduct. [BRIEF only]: five repos have a CONTRIBUTING file, 23 to 680 lines.
- **GitHub About metadata is thin:** no repo has topics or a homepage; some descriptions missing; several contain typos.
- [BRIEF only]: five repositories have a quickstart, and nobody has timed any of them.

### C.3 Runtime and deploy

- **Common start command:** 11 repos plus platform have an Aspire AppHost: chatbot, conversations, eventstore, folders, frontcomposer, memories, parties, projects, tenants, timesheets, builds, and `platform/apphost.cs`.
- **Platform prerequisites** (per platform README): .NET SDK 10.0.403 or later; Aspire CLI 13.6.4 exactly; Docker; an isolated Dapr home with CLI 1.18.2 and runtime 1.18.7 (machine-wide `dapr init` doesn't qualify); submodules at exact commits. The README exports `HEXALITH_DAPR_HOME` with 1.18.2 in the path, but the setup script creates 1.18.7 (mismatch).
- **AI-prompt quickstart precedent:** mcpcli README "Quick start: Claude Code sets it up for you", ~20 lines, needs a handoff folder, a gateway URL, and a token from an "environment owner". Shows the idea works and how prompts grow when the command is complex.
- **No container images and one dev container:** no CI publishes images; only frontcomposer has `.devcontainer/`.
- **Dependencies:** platform's submodules cover 17 repos; chatbot's cover 16.
- [MEM 36 only]: `platform/apphost.cs` (17 lines) adds Docker, Kubernetes, Redis, Keycloak, Dapr plus a Composition project; the platform README status still says "empty Aspire AppHost scaffold"; the chatbot README describes M365 mailbox intake. The "Try it" end state and its prerequisites (auth, LLM key, mailbox) are unverified.
- [MEM 48]: Platform is on track to deploy the chatbot by mid-December.

### C.4 Organization

- 67 non-archived repositories, 60 public. Only 20 public repositories are current modules (commits pushed in November 2026). [MEM 40]: the others are "untouched since mid-2026 or earlier".
- Hexalith.Docs is **private**; it must become public to be the guide hub.
- [MEM 50]: GitHub stars baseline 2026-11-09 = 0 across all current public repos (1 on the legacy Hexalith repo).

### C.5 Archive candidates (awaiting review)

40 public repos that aren't current modules:

- 5 apparent forks of third-party projects: semantic-kernel, ollama, open-webui, qdrant, kernel-memory.
- 2 `_OLD` repos: Documents_OLD, Security_OLD.
- 3 templates: Templates, MyNewModule, MyNewPackage (not inspected; decide whether to keep).
- About 30 older modules, some next to their replacements (EventStores beside EventStore; FrontShell beside FrontComposer).

### C.6 Existing levers

- **Hexalith.Builds is the de facto enforcement layer.** 16 repos use its reusable workflows (`domain-ci.yml`, `codeql.yml`, `commitlint.yml`, and others). It also holds `ci-cd-standards.md` (no documentation rules yet), `audit-hexalith-ci-cd.prompt.md`, `Hexalith.Package.props`, and the module templates.
- **cicd** was set up to harmonize workflows but contains none.
- **eventstore** has `docs/page-template.md` plus markdownlint-cli2 and lychee configs, but no workflow runs them.
- **frontcomposer** has a docfx site.

---

## D. Research digest: rules that constrain requirements

**GitHub**

- GitHub looks for the README in `.github/`, then root, then `docs/`; truncates past 500 KiB; builds an Outline TOC from headings; resolves relative links against the current branch.
- A **public** `.github` repo can supply org defaults: CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, SUPPORT, ACCESSIBILITY, FUNDING, and issue, PR, and discussion templates.
- LICENSE can't be an org default (each repo keeps its own LICENSE).
- Org defaults don't appear in clones or packages.
- Issue templates are all-or-nothing per repository (any repo-local template replaces all org defaults).
- Community Standards checklist: description, README, code of conduct, contributing, license, security policy, issue templates, PR template, content reports.
- [MEM 14 only]: template repositories copy once, with no sync.

**README conventions**

- Standard Readme: short description of 120 characters or fewer that matches the GitHub and package descriptions; TOC required above 100 lines; License last as an SPDX identifier.
- Google docguide: a README is a short summary that links to the full docs. Diátaxis (tutorials, how-to, reference, explanation) for organizing sub-documents.

**NuGet package README**

- `PackageReadmeFile` must point to a Markdown file, and the file must be packed explicitly.
- nuget.org renders CommonMark via Markdig: no raw HTML; relative links and images don't render (NuGetGallery issue #8876, open since 2021).
- Image allow-list includes img.shields.io, sonarcloud.io, codecov.io, coveralls.io, GitHub workflow badges, raw.githubusercontent.com; excludes scan.coverity.com, api.scorecard.dev, bestpractices.dev (Coverity and Scorecard can go through Shields; bestpractices.dev through Shields is [unverified]).
- **Fixing a broken package page means publishing a new package version.**
- Separate package READMEs are common but not explicitly recommended by Microsoft.

**Badges**

- NuGet version/downloads (Shields): free, renders on nuget.org. GitHub Actions workflow status: free for public repos, renders. SonarQube Cloud (renamed from SonarCloud on 2024-10-29, same domain): free OSS plan since 2026-01-27, renders. CodeQL: no dedicated badge; use the workflow badge with advanced setup.
- Shields caches and retires badges when services change: fewer badges, fewer stale ones.

**Enforcement tooling**

- markdownlint-cli2 for Markdown structure and style; lychee-action v2 for links (gaurav-nelson markdown-link-check was archived 2026-04-20).
- Vale (vale-action v3 can flag only added lines) is skipped for v1.
- Reusable workflows via `workflow_call`, already used through Hexalith.Builds.
- Org rulesets and required workflows need GitHub Team or Enterprise; Hexalith's plan is unknown.

**Writing style** (Microsoft and Google style guides)

- Most important point first. Second person, active voice. Keep it short. Sentence-case headings and numbered steps. Descriptive link text and alt text. Write for a global audience.

---

## E. Time targets and measurement method (decision 10, in full)

**Conditions.** Targets apply to a **first run on a clean machine**. The machine starts with **Docker and VS Code installed**, or with **only a browser if you use Codespaces**. **The timer starts on the README and stops at the first success.**

| Journey | Success event | Target |
|---|---|---|
| Use the package | working sample call | **5 minutes or less** |
| Run a module | first successful call | **15 minutes or less** |
| "Try it" on Platform | first chat message | **20 minutes or less** |

All three targets are tagged **[ASSUMPTION: calibrate against a measured baseline]**.

**Measurement options considered:**

| Option | Description | Verdict |
|---|---|---|
| A. No number | — | Rejected: untestable |
| B. Human stranger test | Someone who has never used Hexalith follows the quickstart on a clean machine, with a timer | **Accepted as the launch gate** |
| C. Automated CI smoke test | Runs the quickstart and checks health | Deferred: Docker-in-Docker with Dapr and Keycloak in CI is heavy and flaky; add only for "Try it" and only if quickstarts keep breaking after launch |
| D. Agent stranger test | A fresh AI agent gets only the README and the AI prompt in a clean dev container | **Accepted, runs routinely**; cheap, repeatable, tests the AI-prompt path (a launch feature); doesn't replace a human |

**Rules:**

- **Phuong Duong (GitHub: `tinouit`)** runs the human stranger test **once Platform is finished**.
- Each person can be a stranger only once, so the **baseline and all iterations use the agent test (D)**.
- **Measure a baseline now** to calibrate the targets ([BRIEF]: in November).
- If "Try it" can't meet 20 minutes while building from source, switch to prebuilt images (decision 1 option C).
- [BRIEF] success criterion 1 phrases the gate as `github.com/Hexalith` to first chat message in 20 minutes or less "on a clean machine with Docker". [BRIEF] criterion 3: the agent gets only the **Platform** README and the AI prompt, and completes "Try it". [BRIEF] risk: if the human test fails, a second outside tester is needed.

---

## F. Open questions, risks, assumptions, deferred items

### F.1 Memlog items that do NOT appear in brief.md (flagged)

1. **Hexalith.Docs is itself a module and must follow the standard** [MEM 30]. The brief's "all 20 current repositories" excludes it (it is private and not in the survey table), so its own Level 1 compliance is unstated.
2. **Category assignments** [MEM 30]: memories, cicd, docs, and mcpcli are **technical modules**. No complete business/technical list exists anywhere; the PRD needs one for the org profile.
3. **Planning-folder rule covers Hexalith.Docs and this brief** [MEM 55]: when Hexalith.Docs goes public, its `_bmad-output/` (brief, addendum, memlog, this PRD) becomes public. brief.md omits the planning-folder rule entirely; it is in addendum decision 11 only.
4. **Platform/chatbot state** [MEM 36]: `platform/apphost.cs` is 17 lines (Docker, Kubernetes, Redis, Keycloak, Dapr, Composition project). The platform README still says "empty Aspire AppHost scaffold". The chatbot README describes **M365 mailbox intake**. The "Try it" end state and prerequisites are **unverified**. brief.md only keeps the generic open question.
5. **Implementation rules left out of brief.md on purpose** [MEM 58]: the `aspire run` command, the **10-line** AI-prompt cap, and the planning-folder rule live only in the addendum. Other addendum-only constraints the PRD must carry: the 120-character description rule, the 9-section skeleton including the "Part of Hexalith" link, the NuGet allow-list, markdownlint-cli2 + lychee, private vulnerability reporting, CHANGELOG/Releases, Codespaces, and "timer starts on the README".
6. **Stars baseline detail** [MEM 50]: 0 across current repos, **1 on the legacy Hexalith repo**. The brief says only "up from 0".
7. **Stars-target framing** [MEM 53]: "within a year of launch, i.e. by end of 2027". The brief keeps only "by the end of 2027".
8. **"Template repos copy once with no sync"** [MEM 14]: relevant to how templates (README skeleton, dev container, `docs/development.md`) propagate. Not in brief or addendum.
9. **"Only ~5 of 20 READMEs are presentable (best: eventstore, tenants)"** [MEM 8]: baseline quality figure not in brief.
10. **Overridden or refined decisions**:
    - Deploy target was first accepted as "**local-only**" [MEM 27–28]. It was later refined from the user's words "Docker or Kubernetes now; Azure, AWS and Scaleway in future" [MEM 44] into Docker "Try it" + Kubernetes how-to (no time target), confirmed [MEM 54].
    - BmadSkills `.claude.json` was first "out of brief scope" [MEM 13], then an open question [MEM 57], then moved into org cleanup scope [MEM 58].
    - Contributors were not in the user's original audience [MEM 19] and were added via scope [MEM 24].
    - The four-kinds proposal became category + quickstart blocks [MEM 31, 33].
    - The "four quickstart blocks" drift was fixed to three [MEM 59].
11. **Rigor level** [MEM 35]: "Calibrate to launch-grade rigor" (stakes: nobody outside the team has tried Hexalith; docs block the public launch).
12. **Launch window** [MEM 45]: end of 2026 is "~7 weeks from 2026-11-09".
13. **Facilitator caveat** [MEM 53]: "docs convert visitors, outreach brings them". The brief merges this into "depends on outreach".
14. **Brief length** [MEM 60]: ~1,550 words, ~250 over the 1–2 page aim; the user was informed. Process note only.

### F.2 Open questions (still open)

- What does a newcomer need for "Try it" besides Docker? Possibly an LLM provider key, a sign-in account (Keycloak), or a mailbox (M365). This affects the 20-minute target and must appear in the quickstart. [BRIEF, MEM 36, 57]
- Which stale repos and forks get archived? The list awaits review. The 3 templates aren't inspected. [BRIEF, ADD]
- Hexalith's GitHub plan is unknown, which decides whether rulesets and required workflows are possible. [ADD]
- Whether bestpractices.dev badges render through Shields: [unverified]. Coverity status: [unverified]. [ADD]
- Business/technical label for every repo (see F.1 #2).
- Which repositories are "key" to pin (OC-4): not specified.
- Which topics to set (L1-3): not specified.
- CHANGELOG.md or GitHub Releases: either is allowed, with no rule for choosing.

### F.3 Risks [BRIEF, ADD]

- **Platform completion** is the main risk: "Try it" can't pass until Platform deploys the chatbot (reported on track for mid-December).
- **Single human stranger test:** single-use per person; if it fails, a second outside tester is needed.
- **Build time:** building Platform from source pulls in 17 repos and might exceed 20 minutes. Prebuilt images would then be needed, and that work isn't in this plan.
- **Review capacity:** human review of 20 repos is the bottleneck.
- Docs-check tuning can block PRs (decision 7C con).
- AI prompt: results vary by agent, the agent runs commands on the user's machine, and the prompt needs testing (decision 1 con).
- Codespaces has a limited free quota; Docker-in-Docker is heavy; first run builds from source (decision 1B cons).
- Demo video goes stale as the UI changes (decision 8D con).
- Stars depend on outreach, which is outside the initiative.

### F.4 Assumptions

- Time targets are assumptions to calibrate against a measured baseline.
- Platform deploys the chatbot and all needed services when finished; the "Try it" end state is a chatbot the newcomer can use [MEM 38].
- The repos and packages are already public, so improving docs before the announcement carries no exposure risk (decision 8).
- Agents can do Level 1 writing with the audit prompt and templates (decision 9).

### F.5 Deferred or out of scope (with revisit triggers)

- Azure, AWS, Scaleway deployment: after launch (vision).
- Documentation website: revisit "once there are enough docs to justify one".
- Hosted demo: out.
- Prebuilt container images (1C): only if "Try it" misses 20 minutes, and then for the "Try it" path only.
- Package README generated at pack time (4C): only if a single page would mislead.
- OpenSSF Scorecard: later.
- Automated CI smoke test (10C): only for "Try it", only if quickstarts keep breaking after launch.
- Vale, org-wide rulesets, Coverity, Codacy (and Codecov): out.
- Reorganizing existing `docs/` folders: out (clean only).
- xppmodel (Itaneo org): out.
- Outreach: outside the initiative.
- Research defaults not adopted: ACCESSIBILITY, FUNDING, discussion templates, and "content reports" from the Community Standards checklist.

---

## G. Qualitative intent a requirements structure might drop

- **"Written for people."** Documentation must be clear and easy to read [INIT]. The user's own goal: "simple, crystal-clear documentation" [MEM 18].
- **"Concise at the top level."** The README and its table of contents give an overview only; details go in linked sub-documents [INIT].
- **"Self-sufficient README."** It must contain everything needed to understand the repository, "without being too long" [INIT].
- **Framing shift** [MEM 20]: from a README style guide to **time-to-first-success**. The core outcome is easy adoption via quickstarts that get a newcomer using Hexalith in minutes "with a simple prompt to deploy".
- **Honesty is a rule.** No badge without a pipeline. Never announce "Try it" until it passes a timed stranger test. "The front door never promises something the product doesn't do" (8A).
- **Command plus prompt** suits a product people use through a chatbot. Newcomers can let their own agent do the setup.
- **Fix the command, not the prompt.** Prompt length is a smell test for command complexity (the mcpcli ~20-line precedent).
- **Built for documentation written by agents.** Rules sit where agents read them, and CI catches what agents miss. AI agents are a secondary reader who need "explicit rules and short, reliable commands".
- **Self-serve.** Developers want something working "in minutes, without asking anyone". Contributors should open a first PR "without reverse-engineering the build".
- **Value is consistency, not novelty.** "None of this is technically hard to copy."
- **Launch-grade rigor** [MEM 35].
- **Minimalism.** Fewer badges means fewer stale ones; no website, hosted demo, or images until demand justifies them.
- **Voice** (research): most important point first, second person, active voice, sentence-case headings, numbered steps, descriptive link and alt text, global audience. Vale is skipped, so tone is enforced only by agent rules and review.
- **Visitor perspective.** Make it obvious which 20 repos are current; don't present an order that "seems arbitrary to a visitor" (9C con).
- **"Date moves, not the gate."** If the end-of-2026 date and "Try it works" conflict, the date moves.

---

## H. Contradictions and ambiguities

1. **Where the timer starts.** Addendum decision 10: "starts on the README". Brief criterion 1: "from `github.com/Hexalith`" (the org page). The gate's start point differs.
2. **Clean-machine definition.** Addendum: Docker **and VS Code**, or **only a browser** with Codespaces. Brief: "a clean machine with Docker". Codespaces as a supported "Try it" path is never stated in brief.md or the checklists.
3. **Agent test environment.** Addendum: "README and the AI prompt in a clean dev container". Brief: "only the Platform README and the AI prompt", with no environment and no time limit stated. "Routinely" has no defined cadence or trigger.
4. **Repository count.** [MEM 7] says "21 module repos ... (plus xppmodel)". Elsewhere it is 20. The addendum table has 21 rows (20 + xppmodel). [MEM 30] says Hexalith.Docs follows the standard, but it is outside the 20. `Hexalith/.github` will also be a new public repo. The in-scope set for Level 1 and the docs check (20, 21, or 22) is ambiguous.
5. **Badge count and mandatoriness.** "Up to five badges" plus "three required + SonarQube Cloud". It is unclear whether Sonar quality gate and coverage are one badge or two, and whether Sonar is required for repos with little or no .NET code (aitools, bmadskills, cicd). The NuGet badge is required only "when the repository publishes packages".
6. **"A running pipeline backs every badge" vs License and NuGet-version badges.** These are Shields badges with no CI pipeline behind them. The honesty rule needs a definition that admits them.
7. **"Run it" time target at launch.** Brief criterion 2 says "Run it" quickstarts take 15 minutes or less at launch. L2-2 says each module's "Run it" is added only once it meets its target, so none is required at launch. It is also unclear who measures package and module targets, since the human test runs once, for Platform only.
8. **NuGet page success criterion vs package versions.** Brief criterion 5: "Every NuGet package page shows the module's description and quickstart". The research says fixing a page requires publishing a new package version. Releasing every package before launch is implied but appears in no checklist, timeline, or scope.
9. **NuGet description matching.** L1-3 requires the README sentence to match "the NuGet description", but a repository ships several packages that may have different descriptions. commons keeps per-package READMEs: do those follow the skeleton or pass the docs check?
10. **Docs check reach.** The docs check lives in the Hexalith.Builds reusable CI, but only 16 repos use those workflows. Six of the 20 have no quality CI (aitools, bmadskills, chatbot, cicd, mcpcli, platform). Wiring the remaining repos is unplanned. Brief criterion 4 says all 20 "pass the docs check", but it doesn't say the check is in "required" mode for all 20 at launch.
11. **TOC.** [INIT] mentions "the README and its table of contents". Standard Readme requires a TOC above 100 lines, and the skeleton allows 150 lines but has no TOC section (GitHub generates an Outline automatically).
12. **"Self-sufficient README" [INIT] vs "short summary that links to full docs".** Two principles are in tension. The skeleton resolves it through limits (150 lines, 5-line intro, one-screen quickstart), but "fits on one screen" is not measurable as written (it applies to the quickstart and the org profile).
13. **Contributing link target.** Repo CONTRIBUTING files are deleted and org defaults "don't appear in clones or packages". Skeleton item 8 doesn't say whether the link goes to the org CONTRIBUTING (absolute URL) or `docs/development.md`.
14. **Runbook destination.** "Runbooks move to `docs/development.md`" fits build runbooks (builds ~935 lines). mcpcli's operator runbook (631 lines) and works' release procedure aren't development content, and no home is defined for operator docs.
15. **Quickstart-block examples vs reality.** cicd is listed under "Use the tool" but "contains none" (a 2-line stub with no workflows). builds has an AppHost but is listed under "Use the tool". aitools "Use the tool" has no defined first command.
16. **Kubernetes scope.** The brief's vision says "deploys with one command to Docker or Kubernetes", but the launch deliverable is only a K8s "how-to" with no time target. No acceptance check is defined for it.
17. **"The organization page shows only current repositories"** (brief criterion 7). This could mean the profile README list or the org's repository listing. Archived repos remain visible in the listing, and pinning (OC-4) has no list. "Every one of them has the shared community files" could be satisfied implicitly by org defaults, unless a repo keeps local files (issue templates are all-or-nothing).
18. **Stars target date.** "Within a year of launch" [MEM 53] and "by the end of 2027" [BRIEF] diverge if the launch slips past end of 2026, which the brief explicitly allows. "Across the organization" doesn't say whether legacy or archived repos count (1 star on the legacy Hexalith repo).
19. **Brief-only baseline facts.** "Five repositories have a CONTRIBUTING file, 23 to 680 lines" and "Five repositories have a quickstart" are in brief.md but not in the addendum survey, so which repos is unknown.
20. **Terminology** [WS, outside the three sources]. The shared agent baseline `references/Hexalith.AI.Tools/hexalith-llm-instructions.md` calls the split "technical modules" vs "**domain** modules". The brief uses "business". The agent-rule update (AI-1) should reconcile this.
21. **Forbidden-content detection.** "Epic and story IDs, FR/NFR IDs" have no defined patterns. Moving "backlogs and evidence files under `docs/`" may conflict with "cleaned, not reorganized" when evidence is referenced elsewhere.
22. **Dev container rollout.** FD-4 provides a template, but no checklist item adds `.devcontainer/` to each runnable repo (only frontcomposer has one). "Run it" and "Try it" depend on it.
