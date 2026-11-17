---
title: "Addendum: Hexalith Documentation Standard PRD"
created: 2026-11-10
updated: 2026-11-11
---

# Addendum: Hexalith Documentation Standard PRD

This addendum supports `prd.md` and adds no requirements. It holds three things:

- A proposed module registry for a maintainer to confirm (§A).
- Mechanism notes for architecture (§B).
- Stranger-test notes for story writing (§C).

## A. Proposed module registry (unconfirmed)

This table proposes values for four of the registry's fields: category, quickstart blocks, packages, and CI owner. FR-2 lists the rest. Two things are still open: every category not marked confirmed (Open Question 3) and the quickstart blocks for Hexalith.Builds, Hexalith.AI.Tools, and Hexalith.BmadSkills (Open Question 5).

Column key:

- **Category:**
  - Confirmed: recorded in the brief's decision log.
  - Proposed: a guess based on the repository's role in the shared agent instructions.
  - ?: no basis for a guess yet.
- **Quickstart blocks.** These follow the current-state survey in the brief's addendum. A repository with an Aspire AppHost gets "Run it", one that publishes packages gets "Use the package", and a tooling repository gets "Use the tool". "None" means a "Start here" list. Open Question 14 still governs where "Run it" starts.
- **Packages.** Whether the repository publishes NuGet packages.
- **CI owner:**
  - CiCd: managed by Hexalith.CiCd.
  - Own: the repository's own CI.
  - Caller: a caller workflow.

| Repository | Category | Quickstart blocks (in order) | Packages | CI owner |
| --- | --- | --- | --- | --- |
| Hexalith.Agents | ? | Use the package | yes | CiCd |
| Hexalith.AI.Tools | proposed: technical | Use the tool | no | CiCd |
| Hexalith.BmadSkills | proposed: technical | Use the tool | no | caller |
| Hexalith.Builds | proposed: technical | Use the tool (note 1) | yes | own (note 2) |
| Hexalith.ChatBot | ? | Use the package, Run it | yes | CiCd |
| Hexalith.CiCd | confirmed: technical | none | no | own |
| Hexalith.Commons | proposed: technical | Use the package | yes (note 3) | CiCd |
| Hexalith.Conversations | ? | Use the package, Run it | yes | CiCd |
| Hexalith.Docs | confirmed: technical | none | no | caller |
| Hexalith.EventStore | proposed: technical | Use the package, Run it | yes | CiCd |
| Hexalith.Folders | ? | Use the package, Run it | yes | CiCd |
| Hexalith.FrontComposer | proposed: technical | Use the package, Run it | yes | CiCd |
| Hexalith.McpCli | confirmed: technical | Use the tool | yes | CiCd |
| Hexalith.Memories | confirmed: technical | Use the package, Run it | yes | CiCd |
| Hexalith.Parties | proposed: business | Use the package, Run it | yes | CiCd |
| Hexalith.Platform | ? | Run it (the "Try it" path) | no | CiCd |
| Hexalith.PolymorphicSerializations | proposed: technical | Use the package | yes | CiCd |
| Hexalith.Projects | proposed: business | Use the package, Run it | yes | CiCd |
| Hexalith.Tenants | proposed: business | Use the package, Run it | yes | CiCd |
| Hexalith.Timesheets | proposed: business | Use the package, Run it | yes | CiCd |
| Hexalith.Works | proposed: business | Use the package | yes | CiCd |

Notes:

1. Hexalith.Builds has an Aspire AppHost but is proposed as "Use the tool". It's the one exception to the AppHost rule in the column key (Open Question 5).
2. Only Hexalith.CiCd agents change Hexalith.Builds' own CI.
3. Hexalith.Commons also has per-package READMEs.

## B. Mechanism notes for architecture

These are options and constraints that the research and reviews surfaced. Architecture makes the final choices.

### B.1 Working within Hexalith.CiCd (FR-14, FR-15, FR-41 to FR-43, FR-48, FR-64)

Hexalith.CiCd's contract is in `references/Hexalith.CiCd/_bmad-output/specs/spec-cicd/`, which holds the SPEC, enforcement, pipeline stages, and module inventory.

- **Workflows.** Hexalith.CiCd renders and delivers these items for each managed module:
  - `.github/workflows/`
  - `.github/hexalith-ci.json`
  - The Builds pointer.
  - A marked CI/CD block in the agent entry points (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`). Agents following the documentation rules must not edit this block.

  Module agents' tokens can't push workflow changes.
- **When CI runs.** Module CI runs only on pushes to `main`. Agents push directly to `main`. Hexalith.CiCd is reducing required-status-check rulesets to rules that block only deletion and force-push.
- **Enforcement.** A red `main` blocks that module's nightly release ("main is red, nothing released").
- **Product gate.** Hexalith.CiCd's gate classification allows only product gates. Hexalith.CiCd accepted the docs check as a product gate on 2026-11-11, because the README is the package page.
- **Placement and local run.** See §B.2.
- **Releases.** A README-only change needs a release rule that covers it, or a dispatched release. Don't relabel docs changes as `fix:`.
  - Builds releases on every commit type except `docs`, `test`, and `style`.
  - Module releases skip `build(cicd)` and `build(deps)`. A `fix(deps)` commit forces one.
  - The options are a `docs(readme)` patch rule in the shared release config, or a one-time release that a maintainer dispatches for each repository.
- **Commit scopes.** Commit lint runs inside Hexalith.CiCd's guard. That's where to ban story, epic, and FR scopes (FR-14).

### B.2 Docs check (FR-5, FR-13, FR-41, FR-42, FR-45, FR-46, FR-64)

- **Existing configs.** Hexalith.EventStore has markdownlint-cli2 and lychee configs, and a `docs/page-template.md`, all reusable.
- **Registry reads.** The registry is machine-readable. From it, the docs check reads each repository's expected one-sentence description, badge sources, package IDs, SonarQube Cloud key, and quickstart blocks.
- **Placement.** The docs check is a stage in the shared CI, placed early because it's cheap. Each module's setup file in Hexalith.CiCd sets the module's docs check mode, for example `"docs": "warn" | "fail"`.
- **Local run.** Hexalith.CiCd's CAP-3 local pre-push command should include the docs check (FR-64).
- **Skeleton.** The markdownlint rule MD043 (`required-headings`) supports `*` and `?` wildcards, so the title can vary by repository.
- **lychee-action v2:**
  - Set `failIfEmpty: false`, because the default is `true`.
  - Authenticate with a token to avoid HTTP 429 (rate limit) responses, and retry on 429.
  - Map absolute self-links (`https://github.com/Hexalith/<repo>/blob/main/…`) to the commit's local files.
  - Pin the action to a commit SHA.
- **Central scheduled run.** GitHub turns off scheduled workflows in a public repository after 60 days without activity. So run the weekly check of external links and badge hosts from one repository that stays active. Open issues through a GitHub App that has explicit Issues permission, or post one report in Hexalith.Docs.
- **Candidate planning-content patterns.** Tune these against all 21 repositories in warn mode:
  - `_bmad-output`
  - `\bEpic\s+\d+`
  - `\bStory\s+\d+(\.\d+)*`
  - `\b(N?FR|UJ|SM)-\d+\b`
  - `actions/runs/\d+`
  - 40-character hexadecimal SHAs in prose. This is the one pattern that can be suppressed, and only for pinned actions and submodule commits.

### B.3 NuGet (FR-11, FR-12, FR-15)

- **Image allow list.** The allow list is nuget.org's published list of trusted image domains: 38 domains when `research-landscape.md` was written. It includes:
  - img.shields.io and sonarcloud.io
  - github.com, for workflow badges
  - raw.githubusercontent.com, media.githubusercontent.com, and camo.githubusercontent.com
  - cdn.jsdelivr.net

  The Codespaces badge's image URL isn't allowed, so use a text link instead.
- **Rendering.** The nuget.org site renders CommonMark through Markdig. It doesn't render raw HTML, relative links, or relative images.
- **Package description.** `Hexalith.Builds/Hexalith.Package.props` configures packing of the root README. The `Description` can be set per project or centrally. Hexalith.Commons projects that have their own README keep their own descriptions.
- **Verifying the republish.** Check that each package's latest version on nuget.org shows the expected README content. Then check that the number of republished packages matches the registry's package count. Record the result in the launch ledger.

### B.4 Compiled "Use the package" samples (FR-19)

- **Option 1.** Samples live in a compiled sample or test project and are injected into the README, as MarkdownSnippets does for Marten.
- **Option 2.** CI extracts the fenced C# blocks and compiles them.
- **Either way.** Compile against the package packed from the same commit and served from a local feed, so an API break fails the build in the same change.
- **Later, for "Run it".** Dapr's mechanical-markdown, once the brief's decision 10C is revisited.

### B.5 Dev container and agents (FR-5, FR-6, FR-63, Open Questions 13 and 15)

- **Opening the container.** Each path has a trade-off:
  - The devcontainer CLI needs Node.js on the host.
  - An agent running inside VS Code loses its session when VS Code reopens in the container.
  - Codespaces avoids the host entirely, but uses the newcomer's Codespaces quota.

  The spike tests each supported agent tool on a clean host and records the path that works.
- **Options for FR-63:**
  - The shared baseline exempts quickstart runs from its rule to "stop and report the missing baseline as a blocker".
  - The dev container's post-create step initializes the root submodules.
  - The quickstart AI prompt tells the agent it's running a quickstart, not contributing.
- **Platform's dev container.** It must reproduce today's setup:
  - Submodules at their pinned commits.
  - .NET SDK 10.0.403 or later.
  - Aspire CLI 13.6.4.
  - An isolated Dapr home with CLI 1.18.2 and runtime 1.18.7.
- **Action for the Platform migration.** The Platform README tells readers to export `HEXALITH_DAPR_HOME` with version 1.18.2 in its path, but the setup script creates a 1.18.7 home. Fix the README.

### B.6 SonarQube Cloud (FR-40)

- **Project keys.** Use one per repository, for example `hexalith_<repository-name>` [ASSUMPTION]. A maintainer decides whether to reuse the legacy projects for Hexalith.Commons and Hexalith.PolymorphicSerializations.
- **Missing token.** When no token is available, skip the scan instead of failing it. That happens with fork pull requests, or when the legacy `SONAR_TOKEN` is restricted.

## C. Stranger-test notes (FR-53, FR-55, FR-61)

- **What each run records:**
  - The model ID, the agent tool and its version, and the exact prompt.
  - Start and stop times.
  - Evidence of first success.
  - The friction log.
- **Friction log columns.** Step, elapsed time, what happened, and severity (red, amber, or green).
- **Why three runs with a 2-of-3 threshold.** In a 2026 benchmark, agents set up repositories from a bare environment only 39–57% of the time (see `research-landscape.md`).
- **The human stranger test** is a smoke test, not a statistical measurement. It uses the same record template as the agent runs, and the record identifies the tester by role.

## Related documents

- Current-state baseline and rejected alternatives: the brief's addendum, `_bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/addendum.md`.
- Research on comparable projects, with sources: `research-landscape.md`.
- Review findings behind this revision: the `review-*.md` and `reconcile-*.md` files in this folder.
