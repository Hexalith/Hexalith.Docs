---
title: "Addendum: Hexalith Documentation Standard PRD"
created: 2026-11-10
updated: 2026-11-20
---

# Addendum: Hexalith Documentation Standard PRD

This addendum supports `prd.md` and adds no requirements. It holds three things:

- A proposed module registry for a maintainer to confirm (§A).
- Mechanism notes for architecture (§B).
- Stranger-test notes for story writing (§C).

## A. Proposed module registry (unconfirmed)

The following table records the planning baseline. The working inventory is now `docs/module-registry.json` in Hexalith.Docs. Use its source and confirmation fields for current migration work.

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
- **When CI runs.** The delivered pilot CI workflows run for pushes and pull requests targeting `main` and support manual dispatch. CiCd owns their configuration.
- **Enforcement.** A red `main` blocks that module's nightly release ("main is red, nothing released").
- **Product gate.** Hexalith.CiCd's gate classification allows only product gates. Hexalith.CiCd accepted the docs check as a product gate on 2026-11-11, because the README is the package page.
- **Placement and local run.** See §B.2.
- **Releases.** Both pilots pin Builds v6.4.4 (`fe68718b`). The module-only `docs(readme)` patch selector landed later, in `aaf27a2c`. Builds must release it and CiCd must deliver that version to the pilots before maintainers can use a README-only change to republish. [Builds change](https://github.com/Hexalith/Hexalith.Builds/commit/aaf27a2c)
- **Commit scopes.** Commit lint runs inside Hexalith.CiCd's guard. That's where to ban story, epic, and FR scopes (FR-14).

### B.2 Docs check (FR-5, FR-13, FR-41, FR-42, FR-45, FR-46, FR-64)

- **Placement.** Builds invokes `check_documentation` during CI preparation. It checks that READMEs are readable UTF-8 files, flags those longer than 150 lines and checks same-repository workflow badge targets. FR-41 defines the full rule set. Once a compatible version is delivered, CiCd renders `docs: warn` and can promote a pilot to `docs: fail` after maintainer review. [CiCd setup](https://github.com/Hexalith/Hexalith.CiCd/blob/3422bc15/setup/README.md)
- **Local run.** The shared local pre-push check invokes the same `check_documentation` function. [CI preparation](https://github.com/Hexalith/Hexalith.Builds/blob/2c33b2d7/Github/lib/ci_pipeline.py) · [Local check](https://github.com/Hexalith/Hexalith.Builds/blob/2c33b2d7/Github/lib/local_check.py)
- **Remaining rule coverage.** FR-41 also requires checks against each repository’s registered description, badge sources, package IDs, SonarQube Cloud key and quickstart blocks. EventStore provides reusable markdownlint-cli2 and lychee configurations and a page template.
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
- **Verifying the republish.** Run `python3 scripts/verify_published_readmes.py --module <pilot> --version <release>` from Docs. It compares each ID’s latest listed stable archive and nuspec-declared README with its mapped source. Inspect rendering and links on the corresponding NuGet pages, then enter the release version and verified count in the ledger.

### B.4 Executable “Use the package” samples (FR-19)

The pilot after-unit-tests hooks pack the current revision, check each archive’s selected README, and run the displayed code in a fresh consumer. Commons covers the repository and core-package examples. PolymorphicSerializations runs the two displayed fences and checks the documented result. These hooks provide the hosted evidence for FR-19. The docs checker in §B.2 has its own delivery and acceptance criteria. [Commons hook](https://github.com/Hexalith/Hexalith.Commons/blob/258f9d20/.github/actions/after-unit-tests/action.yml) · [Serialization hook](https://github.com/Hexalith/Hexalith.PolymorphicSerializations/blob/c6d0dfce/.github/actions/after-unit-tests/action.yml)

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
- **Platform’s dev container.** Read the SDK and Aspire pins from the tested Platform revision. At `a74abe17`, Platform selects SDK 11.0.100 with `latestPatch`, the ASP.NET Core 10 runtime and Aspire CLI 17.0.0. Keep dependencies at the revisions selected by that checkout. [Platform setup](https://github.com/Hexalith/Hexalith.Platform/blob/a74abe17/README.md)
- **Dapr setup.** Platform now uses a single absolute `HEXALITH_DAPR_HOME` for installation and execution. Resolve the CLI and runtime independently from the selected Builds catalog. Platform’s pinned Builds revision `dc225a69` selects 1.19.1 for both. The sibling Builds checkout at `2c33b2d7` selects CLI 1.19.1 and runtime 1.19.2. Record the catalog used for each timed trial. [Platform’s pinned catalog](https://github.com/Hexalith/Hexalith.Builds/blob/dc225a69/Props/Directory.Packages.props) · [Sibling catalog](https://github.com/Hexalith/Hexalith.Builds/blob/2c33b2d7/Props/Directory.Packages.props)

### B.6 SonarQube Cloud (FR-40)

- **Project keys.** Use one per repository, for example `hexalith_<repository-name>` [ASSUMPTION]. A maintainer decides whether to reuse the legacy projects for Hexalith.Commons and Hexalith.PolymorphicSerializations.
- **Missing token.** When no token is available, skip the scan instead of failing it. That happens with fork pull requests, or when the legacy `SONAR_TOKEN` is restricted.

## C. Stranger-test notes (FR-53, FR-55, FR-61)

- **What each run records:**
  - The candidate commit, entry URL and exact prompt. Use a README rendered at that commit for prepublication trials; record whether the published content matches the tested path.
  - The tool, version and model ID designated before the three timed trials. Start each trial with a fresh session and clean environment on that configuration.
  - Start and stop times.
  - Evidence of first success.
  - The friction log.
- **Friction log columns.** Step, elapsed time, what happened, and severity (red, amber, or green).
- **Untimed evidence.** For a Level 1 package or tool block, record a successful unaided first result. For the separate Kubernetes gate, record one independent, unaided execution of the how-to and its McpCli result. The 15-minute Platform first call and the 20-minute create/list journey each have their own timed qualification.
- **Why three runs with a 2-of-3 threshold.** In a 2026 benchmark, agents set up repositories from a bare environment only 39–57% of the time (see `research-landscape.md`).
- **The human stranger test** is a smoke test, not a statistical measurement. It uses the same record template as the agent runs, and the record identifies the tester by role.

## Related documents

- Current-state baseline and rejected alternatives: the brief's addendum, `_bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/addendum.md`.
- Research on comparable projects, with sources: `research-landscape.md`.
- Review findings behind this revision: the `review-*.md` and `reconcile-*.md` files in this folder.
