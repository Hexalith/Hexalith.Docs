---
name: Hexalith documentation standard
type: architecture-spine
purpose: build-substrate
altitude: initiative
paradigm: distributed ownership with a shared validation pipeline
scope: documentation authoring, package distribution, first-run evidence and publication
status: final
created: 2026-11-11
updated: 2026-11-21
binds: [hub, migration, package, first-run, publication]
sources:
  - ../../prds/prd-docs-2026-11-09/prd.md
  - ../../prds/prd-docs-2026-11-09/addendum.md
  - ../../epics.md
  - ../../../../references/Hexalith.CiCd/_bmad-output/planning-artifacts/architecture/architecture-cicd-2026-11-07/ARCHITECTURE-SPINE.md
  - ../../../../references/Hexalith.Platform/_bmad-output/planning-artifacts/architecture/architecture-platform-2026-09-27/ARCHITECTURE-SPINE.md
companions: [.memlog.md]
---

# Hexalith documentation architecture

## Design paradigm

**Distributed ownership with a shared validation pipeline.** Docs owns the standard and module registry. Each module owns the README its users see. Builds owns the reusable checker and packaging mechanics. CiCd owns the managed configurations and their delivery. The agent baseline belongs to AI.Tools. Platform owns local composition and McpCli owns the operator interface.

| Owner | Owns | Lives in |
| --- | --- | --- |
| Hexalith.Docs | Standard and rule catalog, registry, templates, renderer, cross-repository checks, link report, stranger-test kit, launch ledger | `docs/`, `templates/`, `scripts/`, `tools/`, `_bmad-output/implementation-artifacts/` |
| Each module | README, package READMEs, development and operations pages, dev container, LICENSE | Its repository, outside the CiCd perimeter |
| Hexalith.Builds | Checker, README-sample step, packing, release rules, module tool | `Github/lib/`, `Tools/`, `schemas/` |
| Hexalith.CiCd | `docs`, `readmeSamples` and suppression settings, rendered workflows, commit lint, nightly release | `setup/<Repo>.yml` and the files it renders |
| Hexalith.AI.Tools | Canonical entry-point text and documentation rules | Shared instruction files |
| Hexalith.Platform, Hexalith.McpCli | Module run, local composition, first operation | Platform tool, `Hexalith.McpCli` |
| Hexalith/.github | Organization profile, community files | `profile/README.md`, community files |

## Inherited invariants

| Inherited | From | Binds here |
| --- | --- | --- |
| CiCd AD-1 | Hexalith.CiCd spine | A commit's CI result depends only on that commit. `hexalith-ci.json` is complete, so every documentation knob is rendered explicitly (amendment pending). |
| CiCd AD-2 | Hexalith.CiCd spine | Builds code names no module. All variation comes from `hexalith-ci.json` and the perimeter. |
| CiCd AD-3 | Hexalith.CiCd spine | Documentation settings are set in CiCd `setup/<Repo>.yml`. Unknown keys fail. |
| CiCd AD-4, AD-7 | Hexalith.CiCd spine | Module agents never edit `.github/workflows/`, `hexalith-ci.json`, `dependabot.yml`, the Builds gitlink or the `hexalith-cicd` marker block. Their tokens can't push workflows. |
| CiCd AD-10, AD-16, AD-17 | Hexalith.CiCd spine | Releases come from commit analysis. Amendment pending: the module `docs(readme)` patch rule (AD-11). |
| CiCd AD-11 | Hexalith.CiCd spine | The checker and Docs tooling are Python 3.12 or later, standard library only. `run:` steps invoke scripts. Downloaded binaries are SHA-256 checked. |
| CiCd AD-12 | Hexalith.CiCd spine | The docs check runs in the prepare step after the stage-1 guard. The README-sample step joins stage 3 (amendment pending). |
| CiCd AD-14 | Hexalith.CiCd spine | No hook action calls Builds. The CI job holds only the pull-only registry pair. |
| CiCd AD-15 | Hexalith.CiCd spine | `check.py` runs the same docs check locally. There is no pre-push hook. |
| CiCd AD-18 | Hexalith.CiCd spine | The nightly run dispatches every adopted module's release, subject to release eligibility, CI and dispatch results. Publication requires per-package evidence (AD-11). |
| CiCd AD-20 | Hexalith.CiCd spine | Documentation adds no Builds workflow. Standalone callers reuse the checker script. |
| CiCd AD-21 | Hexalith.CiCd spine | `SONAR_TOKEN` is a legacy secret that adoption removes. |
| Platform AD-1 | Hexalith.Platform spine | Only Platform's Aspire model composes multi-module environments. No quickstart starts a module-owned AppHost. |
| Platform AD-4 | Hexalith.Platform spine | The module workspace initializes only direct `references/*` submodules. EventStore, Memories and McpCli run from the Platform workspace. |
| Platform AD-11 | Hexalith.Platform spine | Hexalith.McpCli is the only module-operation surface. Legacy CLI and MCP hosts are frozen (AD-18). |

## Invariants and rules

### AD-1 — One standard and one module registry [ADOPTED]

- **Binds** the guide hub, agent rules, organization profile and migration tooling.
- **Prevents** an unconfirmed module description or package count from becoming a public claim.
- **Rule** Record rule IDs in the standard and module facts in one JSON registry. JSON can be read with the Python standard library. Distinguish unknown, proposed and human-confirmed values. Verify all 21 repositories are represented. BmadSkills remains one of the 21 while its owner supplies an immutable external revision. Treat its existing empty package list as pending until the owner verifies the inventory at that revision (AD-16).

### AD-2 — CI validates the checked-out revision [ADOPTED]

- **Binds** local runs, hosted checks and management of shared CI config.
- **Prevents** an edit on another repository's default branch from changing yesterday's result.
- **Rule** Use the same released checker, mode and checkout locally and in hosted CI. CiCd agents configure the 17 managed modules through CiCd setup and maintain Builds and CiCd in their own CI. Docs, BmadSkills and the additional organization repository `Hexalith/.github` set their mode in their caller workflows. Begin in warning mode. AD-6 defines the inputs, AD-7 the link checks and AD-8 the evidence for promotion.

### AD-3 — Test the material a reader receives [ADOPTED]

- **Binds** the package example, packing, release selection and verification.
- **Prevents** green library tests from concealing an unusable README or an old package page.
- **Rule** A fresh consumer must run the displayed code against packages built from that revision. For every pilot package, verify the nuspec README entry against its intended source, including project-specific documentation. Eligible module migrations use the README release rule. AD-11 specifies the Builds and paired McpCli release routes. Record the released version, package count and verified public README before claiming a successful republish.

### AD-4 — Platform owns the timed local journey [ADOPTED]

- **Binds** the cold-host kit, Platform setup and the user-facing Try it link.
- **Prevents** a warm developer checkout or partial topology from certifying the 20-minute target.
- **Rule** Qualify both routes on the same immutable candidate Platform README before publishing its “Run it” block or the organization’s “Try it” link.
  - For each route, the maintainer predeclares the supported agent tool, version and model. Start three independent unaided clean sessions with the route’s exact printed prompt. Record entry URL, candidate SHA, effective toolchain (AD-13), role, elapsed times, first result and friction. Keep secrets and personal identifiers out of the record. Each route requires two passes within its own target.
  - “Run it” ends at the documented first successful call within 15 minutes. “Try it” includes readiness of all seven MVP modules and a McpCli create/list that returns the same project in the same tenant within 20 minutes. A restore or a read-only query cannot establish that result.
  - Before promotion, compare the candidate with the instructions proposed for publication. A change to the prompt, commands, prerequisites or path requires repeating the affected qualification. A changed agent configuration starts a new set. After both passes, publish the link. The maintainer confirms an eligible outside tester and backup and declares the command or prompt path in advance. The tester starts at the public organization page on their own clean machine and, unaided, reaches the same create/list result within 20 minutes including prerequisites. Both the documented command and the prompt must demonstrate that result (FR-23). A failed human trial requires fixes, agent requalification and the backup tester. The separate Kubernetes how-to requires one fresh agent’s successful untimed run (FR-24).

### AD-5 — Publication requires human evidence [ADOPTED]

- **Binds** the launch ledger, repository visibility and exposure review.
- **Prevents** private findings, credentials or unsupported readiness claims appearing in public guides.
- **Rule** The security maintainer reviews already-public planning content immediately, including the BmadSkills originals and backups identified in FR-32. Cover both planning trees at the reviewed revision and reconcile intervening changes before closure. Review Docs before a visibility change. Verify secret scanning and push protection for all 21 repositories and the organization community repository. Keep item-level findings and remediation in the private review record. The ledger records reviewed revisions, counts, role and status. Changing visibility, enabling safeguards, starting a package release, accepting an outside test and deciding launch require the corresponding owner.

### AD-6 — Each check judges only what its own commit pins

- **Binds** the Builds checker, Docs CI, standalone callers and the registry rules (FR-11, FR-38, FR-39, FR-41, FR-43, FR-64, NFR-7).
- **Prevents** a module's result changing because Docs or another repository changed, two implementations of one rule, and a red Docs build for every module not yet migrated.
- **Rule**
  - Builds' `docs_check.py` is the only per-repository checker. It runs in the CI prepare step after the stage-1 guard and before restore, in the mode the `docs` knob sets, and `check.py` calls the same function [ADOPTED]. It adds at most 2 minutes to an EventStore CI run.
  - Its checked pages come from the checkout alone: the root README, every `README.md` beside a `.csproj` under `src/`, and the docs pages the root README links to directly. It never reads the registry.
  - The own-CI and caller routes in AD-2 run the same script from a Builds checkout pinned to a release tag, with a committed page profile of `module`, `hub` or `org` that selects the applicable rules [ASSUMPTION].
  - Docs CI owns every rule that needs the registry: verbatim description, quickstart order, package IDs, the package-README set, badge sources and Sonar key. The Docs acceptance commit fixes the rules, registry and source identities. Use its 19 direct gitlinks, its own tree for Docs, and a BmadSkills commit approved by its owner and recorded in the Docs evidence. Run the same Docs check locally on those inputs. Determine each candidate’s mode from its committed configuration under AD-2. In fail mode an unresolved required input or a failing registry rule prevents acceptance. Other rows report.
  - For Level 1, record the Docs acceptance commit and passing Docs check, plus the candidate’s hosted fail-mode result at the same source revision. For Docs itself the workflow run identifies that Docs commit. Record its SHA in subsequent evidence to avoid a self-referential commit.

### AD-7 — Links are checked offline per commit and online on schedule [ADOPTED]

- **Binds** D-LINK, the checker, migrations and the scheduled report (FR-45).
- **Prevents** a rate limit or flaky host turning a module red, and a broken self-link passing.
- **Rule**
  - Per commit, the checker resolves relative paths, in-page fragments and self-links against the checkout, without network access. Self-links are `https://github.com/Hexalith/<self>/{blob,tree,raw}/main/…` and `https://raw.githubusercontent.com/Hexalith/<self>/{main,refs/heads/main}/…`. A self-link to any other ref is a finding.
  - On every Docs registry check, resolve cross-repository source-file links and fragments offline at the source revisions recorded by AD-6. For the organization repository, record its immutable revision alongside the external inputs. Report missing target revisions or paths and keep the affected migration open. Resolve default-branch file URLs against those pinned trees. An explicitly immutable target is checked at its stated revision. Live-only resources such as badges and release pages go to the online check. A module check alone covers only its own tree.
  - One Docs link script checks live links to other Hexalith repositories, external destinations and badge images. It uses lychee, deduplicates by URL, and also runs in single-repository mode as each migration's online check [ASSUMPTION].
  - The scheduled run goes every Monday at 06:00 UTC with Docs' own `GITHUB_TOKEN` and `issues: write`. It updates one pinned report issue in Docs and the job summary, and fails only on its own errors. It also reads live default branches and reports drift from the pinned revisions.

### AD-8 — One rule catalog and one finding contract

- **Binds** the standard's rule table, checker output, AI.Tools rules, suppressions and fail-mode promotion (FR-42, FR-44, FR-46, FR-47, FR-49).
- **Prevents** a finding citing an undefined rule, an agent suppressing the rule that polices it, and a new rule turning fail-mode repositories red on delivery.
- **Rule**
  - Rule IDs take the form `D-<NAME>` and exist only in the table in `docs/documentation-standard.md`. An ID enters the table before any Builds release emits it. Planning content gets its own ID, `D-PLANNING`, split from D-LOCATION [ASSUMPTION]. Builds findings and AI.Tools rules cite only catalog IDs. A Docs test checks the pinned Builds and AI.Tools submodules against the table.
  - A finding is one JSON line `{file, line, rule, level, hint}` with `level` set to `report` or `fail` [ASSUMPTION]. Docs CI findings add `repository`.
  - A finding fails a run only when the repository's mode is `fail`, its level is `fail`, it sits on a checked page and no suppression matches.
  - Managed modules get suppressions only from CiCd setup, rendered into `hexalith-ci.json`. Own-CI and caller repositories commit theirs in `.github/hexalith-docs.json` [ASSUMPTION]. An entry is `{file, rule, match, reason}`, where `match` is the exact suppressed text. Only a `D-PLANNING` match on a 40-character SHA of a pinned action or submodule commit can be suppressed. D-BADGE can't. The job summary prints the suppression count, and the weekly report totals them across repositories.
  - A new or widened rule ships at `report` level. Builds raises it to `fail` in a later release, and only after the weekly report shows zero findings for it in every fail-mode repository.
  - Before the first promotion, the Docs maintainer records one warning-mode calibration of the candidate planning-content patterns against all 21 source revisions (FR-13). Record the checker and rule revision, source SHA, findings and disposition for each repository, including an owner-approved BmadSkills checkout. A missing source or missing rule coverage leaves calibration open. Changed patterns require a fresh calibration.
  - Each repository runs in hosted warning mode before migration. After its maintainer reviews the findings, the configuration owner in AD-2 enables fail mode. The ledger links the shared calibration and the successful hosted fail-mode run at the accepted revision. For Level 1, also record the disposition of every applicable mandatory rule. A report-only or manual rule needs affirmative review evidence. An unresolved mandatory finding blocks acceptance even if the hosted job passed.

### AD-9 — README samples run as one Builds step

- **Binds** "Use the package" blocks, package READMEs, CI stage 3 and package verification (FR-16, FR-19, D-QUICKSTART). Extends AD-3.
- **Prevents** 14 publishers writing 14 extraction scripts, a hook action calling Builds, a consumer restoring an old package from nuget.org, and a displayed sample that no test runs.
- **Rule**
  - Builds' reusable `ci.yml` runs one native README-sample step in stage 3, after unit tests and before the `after-unit-tests` hook. The step runs when the `readmeSamples` knob CiCd renders is `true` [ASSUMPTION].
  - The step packs the stage-2 Release outputs into a temporary feed at a version no public feed carries. Each consumer's `NuGet.Config` clears every other source. Consumers target the framework of the repository's SDK major.
  - A sample is one or more consecutive `csharp` blocks, followed directly by exactly one `text` block holding the expected output. Samples sit in the root README's "Use the package" block or under a package README's `## Usage` heading [ASSUMPTION]. Earlier blocks become type files, and the last block holds the top-level statements. Each sample prints its documented result, and output must match line by line. A prompt block never directly follows a `csharp` block.
  - The pilots' hook scripts stay until the Builds release ships. Then each hook drops its sample step. Level 1 requires same-revision hosted execution of each displayed package sample. Package and tool quickstarts each require one successful unaided candidate run before first publication (FR-57). A tool-only publisher verifies its documented first command and every package ID under AD-11.

### AD-10 — "Run it" runs through Platform and ends with a McpCli call

- **Binds** every module's "Run it" block, its prompt and the registry's quickstart field (FR-20, FR-58, Open Question 14).
- **Prevents** a README starting a frozen module AppHost, a second composition path, an unpinned module tool, or a first call through a legacy surface.
- **Rule**
  - For a module run from its own workspace, eligibility requires `module/hexalith.module-manifest.v2.json`, a direct `references/Hexalith.Platform` gitlink and `Hexalith.Builds.Module.Cli` pinned in `.config/dotnet-tools.json` at the version that Platform revision pins.
  - The block opens the repository dev container, runs `dotnet tool restore`, then `dotnet tool run hexalith-module -- run --manifest module/hexalith.module-manifest.v2.json` from the module workspace. EventStore, Memories and McpCli instead use the Platform checkout, its pinned tool and the target manifest under its direct `references/` gitlink.
  - The block ends with one call through the McpCli build that the Platform tool produces for that run, and shows its expected output.
  - Platform’s own route starts its AppHost with `aspire run` in the Platform dev container. Its candidate checkout supplies the toolchain and direct dependency pins. No module quickstart or prompt uses `aspire run`.
  - The registry lists planned blocks, and the ledger records each block's qualification. Rehearse a proposed block on an immutable candidate commit. The default-branch README links to the development guide until its block qualifies. Platform publishes after both AD-4 qualifications.

### AD-11 — Documentation commits and the release start

- **Binds** migration commits, republishing, commit lint and verification of the nightly release (FR-13, FR-14, FR-15). Extends AD-3 and AD-5.
- **Prevents** agents relabeling documentation as `fix:`, an unreviewed README reaching nuget.org through the nightly release, and planning IDs reaching release notes.
- **Rule**
  - Migration work lands as `docs:` commits, which never release.
  - After the maintainer reviews the candidate migration and before final Level 1 acceptance, the module owner makes or explicitly approves the single `docs(readme): …` commit. That commit authorizes the module patch for the next eligible nightly dispatch (AD-5). Verify the actual release result. Make it only after the delivered Builds tag contains the `docs(readme)` rule. The release record lists any non-docs commits the patch carries, and the owner accepts them.
  - The Builds maintainer includes the migrated READMEs for `Hexalith.Builds.Evidence.Cli` and `Hexalith.Builds.Module.Cli` in the next qualifying Builds release. Its selector excludes docs, test and style changes. If that release would miss the FR-15 stabilization deadline, record the gap in the launch forecast for owner disposition. For the paired McpCli release, Platform owns the stable tool and McpCli owns Abstractions (Platform AD-11). McpCli currently stages and publishes both IDs together. Hold a documentation-triggered republish until the owners reconcile that workflow with Platform AD-11 and identify one authorized publisher and one release receipt per ID.
  - No commit subject or scope carries a story, epic, FR or other planning ID. CiCd's commit lint gains this rule by amendment (Open Question 11). Until then, migration review enforces it.
  - Reconcile the release’s package IDs with the confirmed inventory at the Docs acceptance revision. For each expected ID verify the intended latest listed stable version, its nuspec README against the mapped source at the release tag, and the rendered page and links. Record version and verified/expected count. Missing IDs keep the publisher’s Level 1 acceptance open.

### AD-12 — Quickstart runs never stop on the contributor baseline

- **Binds** the canonical entry-point text, the three entry points in every repository, quickstart prompts and the dev container post-create step (FR-22, FR-48, FR-63, NFR-9, D-PROMPT).
- **Prevents** a newcomer's agent halting in a fresh clone that lacks `references/Hexalith.AI.Tools`, entry points with three different writers, and prompts that frame the task differently.
- **Rule**
  - AI.Tools owns the canonical normalized text of `AGENTS.md`, `CLAUDE.md` and `.github/copilot-instructions.md`. Each repository carries that text byte for byte, plus only the `hexalith-cicd` marker block. Docs CI compares each pinned repository's entry points with the canonical text at Docs' pinned AI.Tools revision.
  - That text limits "stop and report a missing baseline" to repository work, and states that running a README quickstart isn't repository work.
  - Every quickstart prompt opens with the line `You are running a Hexalith quickstart.`
  - The dev container `postCreateCommand` initializes only root-declared submodules, without recursion.
  - Only a maintainer changes entry points or dev container files. A migration installs the canonical text and the template verbatim. Guard protection stays with CiCd (Open Question 19).
  - Secrets go into a git-ignored `.env.local` at the repository root or a hidden prompt, never into a prompt or a commit [ASSUMPTION].

### AD-13 — Every environment pin has one upstream

- **Binds** dev container templates, prerequisite lists and the stranger-test kit (FR-5, FR-18, D-PREREQUISITES). Extends AD-4 to every dev container.
- **Prevents** a dev container and its repository disagreeing on SDK, Aspire or Dapr versions, and a README listing versions no file enforces.
- **Rule**
  - The base image is `mcr.microsoft.com/devcontainers/dotnet` at an exact tag whose .NET major equals the SDK major in `global.json`. The checker compares the two from the checkout.
  - Dev container files never state Aspire or Dapr versions. `postCreateCommand` runs `dotnet tool restore` and Platform's setup with the pinned module tool. Setup installs the Dapr CLI and runtime that the tool's catalog requires into the single home named by `HEXALITH_DAPR_HOME`, which install and run share. It installs the Aspire CLI that matches the Aspire version pinned by the AppHost that runs the block [ASSUMPTION].
  - Setup also installs any extra runtime the Platform README lists.
  - Prerequisite lists restate the installed versions. Record the Platform and effective Builds catalog SHAs, module-tool version, and declared and observed SDK, Aspire, Dapr CLI and Dapr runtime versions. The catalog must match the Builds gitlink of the Platform candidate. A sibling checkout with another SHA or a different installed version disqualifies the trial. Install and run use the same Dapr home.

### AD-14 — Pages derived from the registry are generated

- **Binds** the organization profile catalog, About descriptions and the organization CONTRIBUTING development-guide list (FR-25, FR-28, FR-33, FR-36).
- **Prevents** the profile, About text and registry drifting apart through hand edits, and two owners of the profile.
- **Rule**
  - `Hexalith/.github` pins Docs as a submodule and runs the Docs renderer in its own CI [ASSUMPTION].
  - The renderer writes only between `hexalith-docs` begin and end markers in `profile/README.md` and `CONTRIBUTING.md`, using only confirmed descriptions and categories. The `.github` CI fails when committed text differs from rendered text.
  - A maintainer sets each GitHub About description from the registry. The weekly report flags differences.

### AD-15 — Migrations work in the owning repository and name their inputs

- **Binds** every migration story and the migration prompt (FR-7, FR-57).
- **Prevents** an agent editing one checkout while checking another, nested submodule initialization, and migrations following different template revisions.
- **Rule**
  - A migration edits and commits in the owning repository's checkout. It validates messages with that repository's pinned commit lint.
  - Run the local per-repository check from the same Builds commit as the candidate’s hosted release tag using its committed mode, configuration and source checkout. If the Docs sibling differs, use a separate checkout of that released checker. Record its SHA and hosted run URL. If the pinned release lacks the checker, the configuration owner must deliver a compatible release before the check can qualify. The Docs registry check runs separately on the AD-6 inputs.
  - Each migration records, in its ledger row, the Docs commit whose templates and registry it followed and the AI.Tools revision its entry points came from.

### AD-16 — Shared state has one write path

- **Binds** the registry, the launch ledger and trial records (FR-2, FR-56). Extends AD-1 and AD-5.
- **Prevents** parallel agents overwriting each other's rows, agents confirming their own descriptions, and a registry row disagreeing with its pinned checkout.
- **Rule**
  - A registry row changes only in the Docs commit that advances that module's gitlink, or in a maintainer commit. Only a maintainer commit sets a status to `confirmed`. Agents write `proposed` values or `null`.
  - The registry distinguishes pending inventory from an owner-confirmed empty list. Record confirmation status and the owner-approved source revision with the inventory. A changed inventory requires renewed confirmation. Legacy rows without that evidence remain pending even where schema v1 stores zero. Until confirmed, show the repository as pending in the ledger and capacity forecast. Only a confirmed empty inventory makes package evidence inapplicable. An unresolved inventory prevents closing the migration or declaring the forecast complete.
  - The ledger has one row per registry repository. Only that repository's migration or the maintainer edits it.
  - Each trial writes its own record under `_bmad-output/implementation-artifacts/trials/`, and the row links to it [ASSUMPTION].

### AD-17 — SonarQube Cloud appears only where CiCd delivers it

- **Binds** Sonar analysis, Sonar badges and the registry `sonarKey` (FR-38, FR-39, FR-40).
- **Prevents** a module adding its own Sonar token or workflow, divergent project keys, and a badge that reads no live analysis.
- **Rule**
  - Sonar analysis runs only through a path CiCd admits. FR-40 needs that CiCd amendment first.
  - The registry `sonarKey` is the only key source, in the existing `Hexalith_<RepositoryName>` form [ASSUMPTION].
  - A README shows Sonar badges only once its registry `sonarKey` is set. The Docs maintainer sets it after CiCd delivers analysis.
  - A managed module's CI badge names only the CiCd-rendered `ci.yml`.

### AD-18 — Legacy surface packages carry a notice, not a quickstart

- **Binds** the package READMEs of frozen CLI and MCP surfaces, the registry and republishing (FR-15, FR-16).
- **Prevents** a republished README presenting a frozen surface as current, and those IDs dropping out of the package count.
- **Rule** The registry flags each package ID of a legacy surface that Platform AD-11 freezes [ASSUMPTION]. That package's README is a short notice that it is obsolete, naming Hexalith.McpCli. Its ID stays in the republish count. No quickstart, sample or profile entry names it.

### Dependency direction

Arrows point from a repository to what it depends on at build or run time. No module CI reads Docs or the registry. CiCd writes only its perimeter files into each module (CiCd AD-4). That write isn't a dependency, so it isn't drawn.

```mermaid
flowchart TD
    Module[Module repository CI] -->|runs pinned checker and README-sample step| Builds[Hexalith.Builds]
    CiCd[Hexalith.CiCd] -->|pins release tag| Builds
    Docs[Hexalith.Docs CI] -->|reads pinned submodule revisions| Module
    Docs -->|checks cited rule IDs| Builds
    Docs -->|reads canonical entry-point text| AITools[Hexalith.AI.Tools]
    Org[Hexalith/.github CI] -->|pins Docs and runs renderer| Docs
    Module -->|Run it| Platform[Hexalith.Platform and McpCli]
```

## Flow of changes and evidence

```mermaid
flowchart LR
    Docs[Docs standard and registry] --> Module[Module README and sample]
    CiCd[CiCd configuration] --> Builds[Versioned Builds checks]
    Module --> Builds
    Builds --> Package[NuGet package]
    Package --> Verify[Compare published README]
    Verify --> Ledger[Launch ledger]
    Platform[Platform and McpCli] --> Trial[Timed first operation]
    Trial --> Ledger
    Review[Maintainer exposure review] --> Ledger
```

## Consistency conventions

| Concern | Convention |
| --- | --- |
| Rule IDs | `D-<NAME>` from the standard's table. Never numbered, renamed or reused. |
| Findings | One JSON line `{file, line, rule, level, hint}`. `file` is a repository-relative POSIX path, `line` starts at 1, `hint` is one imperative sentence. |
| Registry | `docs/module-registry.json`: integer `schemaVersion`, camelCase keys, one row per repository. Status values are `confirmed` or `proposed`, plus `unconfirmed` for an absent category. Unknown facts are `null`, never guessed. |
| Quickstart names | "Use the package", "Run it" and "Use the tool", in registry order. "Start here" when a repository has none. |
| Sample shape | Consecutive `csharp` blocks followed by one `text` block of expected output (AD-9). |
| Prompts | Ten lines or fewer. They open with `You are running a Hexalith quickstart.` and use the same setup command and first-success check as the manual steps. |
| Secrets | A git-ignored `.env.local` at the repository root, or a hidden prompt. Never pasted, logged or committed. |
| Commits | Conventional Commits, validated by the owning repository's pinned commit lint. `docs:` for migration work, `docs(readme)` only for the owner's release commit. No planning IDs. |
| Links | READMEs use absolute HTTPS links and images, because NuGet renders no relative links. In-page `#fragment` links are allowed. Docs pages may link relatively inside their repository. |
| Vocabulary | "Business module" and "technical module" (D-IDENTITY). |
| Evidence | Ledger rows keyed by registry repository name. Testers identified by role. Local results labeled apart from published evidence. Dates in `YYYY-MM-DD`. No tokens. |
| Tooling | Python 3.12 or later, standard library only. `unittest` tests under `scripts/tests/`. No network access in per-commit checks. |

## Stack

| Name | Version |
| --- | --- |
| Python for the checker and Docs tooling | 3.12 or later, standard library only |
| .NET SDK | 11.0.100 in every module `global.json`, with `rollForward` set per repository |
| Aspire | 17.0.0 at Platform `abb62da8`; older Platform pins in module workspaces use 13.6.5 |
| Hexalith.Builds.Module.Cli (`hexalith-module`) | 6.4.4 pinned by Platform `abb62da8` |
| Hexalith.McpCli | Stable Abstractions 3.0.0. For trials the Platform tool builds McpCli from the candidate source pin (currently `e79b7f8b` at `abb62da8`). Record the source and loaded artifact identity. |
| Dapr CLI and runtime | Platform `abb62da8` pins Builds `fe68718b`: CLI 1.19.1, runtime 1.19.1. Docs sibling `e1380b81`: CLI 1.19.1, runtime 1.19.2. Use AD-13 for trials |
| Builds release with the checker and `docs(readme)` rule | Pilots pin v6.4.4. Use a release containing both the checker and the module README selector |
| Dev container base image | `mcr.microsoft.com/devcontainers/dotnet:3.0.1-11.0-resolute` |
| Dev container features | docker-in-docker 4.1.3, python 1.8.1 |
| lychee, for the Docs link script only | v0.24.2 |
| GitHub-hosted runner for Docs workflows | ubuntu-24.04 |
| actions/checkout | v7.0.1 (`3d3c42e5aac5ba805825da76410c181273ba90b1`) |
| Contributor Covenant | 3.0 |

## Structural seed

```text
Hexalith.Docs/
  README.md                         # Start here
  LICENSE                           # to add after rights are confirmed
  docs/
    documentation-standard.md       # rule catalog and readability checklist
    module-registry.json            # 21 rows, schemaVersion 1
    overview.md                     # cross-module guide
    stranger-test.md                # clean-host trial instructions
  templates/                        # README, development, operations, prompts, migration; dev container to add
  scripts/                          # registry validator, published-README verifier; registry rules, renderer and link script to add
    tests/
  tools/stranger-test.py            # trial kit
  .github/workflows/documentation.yml   # registry validation; cross-repository checks and weekly link report to add
  references/                       # root submodules, read-only pins
  _bmad-output/implementation-artifacts/  # launch ledger, trials/, exposure review, sprint status
```

```text
<Module>/
  README.md                                    # checked page (D-README)
  LICENSE
  src/**/<Package>/README.md                   # checked when beside a .csproj
  docs/development.md, docs/operations.md
  .devcontainer/devcontainer.json              # maintainer-owned, pins per AD-13
  .config/dotnet-tools.json                    # pins hexalith-module for "Run it" (AD-10)
  module/hexalith.module-manifest.v2.json      # enables "Run it" (AD-10)
  AGENTS.md, CLAUDE.md, .github/copilot-instructions.md  # canonical text plus CiCd marker block (AD-12)
  .github/workflows/, .github/hexalith-ci.json  # CiCd-owned, never edited by module agents
  .env.local                                   # git-ignored, never committed
```

```mermaid
flowchart LR
    subgraph GitHub
        ModCI[Module CI: docs check, tests, README samples]
        Nightly[CiCd nightly dispatch]
        Release[Module release.yml]
        DocsCI[Docs CI: registry and cross-repository rules]
        Weekly[Docs weekly link report]
        Org[Hexalith/.github profile and community files]
        Live[Module default branches]
    end
    Nightly --> Release
    Release --> NuGet[nuget.org package pages]
    ModCI -.->|after CiCd admits a Sonar path| Sonar[SonarQube Cloud]
    Weekly --> NuGet
    Weekly --> Org
    Weekly --> Live
    Newcomer[Clean host: Docker and VS Code, or Codespaces] -->|dev container| Platform[Platform local composition]
    Platform --> McpCli[Hexalith.McpCli first operation]
```

## Delivery boundaries

| Result | Required evidence | Responsible owner |
| --- | --- | --- |
| Guide ready for public access | Confirmed registry values, exposure disposition, links work signed out | Docs and security maintainers |
| Pilot ready for adoption | AD-8 calibration and hosted fail evidence, sample output, badge and package checks, maintainer review | Module owners |
| Hosted checks enabled | Released checker, committed mode and successful hosted result at the candidate revision | Configuration owner under AD-2 |
| Package page current | Latest stable version and rendered README verified per package ID | Release maintainer |
| First operation ready | Two of three for each route at the same candidate (15 and 20 minutes). Both precede the public link | Platform and launch maintainer |
| Launch decision | Outside tester passes from the live link and all ten PRD §8.3 conditions are evidenced | Launch maintainer |

## Capability → architecture map

| Capability (FRs) | Lives in | Governed by |
| --- | --- | --- |
| Standard, registry, templates and guides (FR-1 to FR-8, FR-62) | Docs `docs/`, `templates/` | AD-1, AD-8, AD-13, AD-15, AD-16 |
| README and package pages (FR-9 to FR-16, FR-60) | Each module | AD-3, AD-6, AD-8, AD-9, AD-11, AD-18 |
| Quickstarts and prompts (FR-17 to FR-22) | Module README and dev container | AD-9, AD-10, AD-12, AD-13 |
| "Try it", Kubernetes and chat (FR-23, FR-24, FR-66) | Platform, McpCli, Docs kit | AD-4, AD-10, Platform AD-1, Platform AD-11 |
| Front door and organization (FR-25 to FR-32, FR-65) | `Hexalith/.github`, Docs | AD-5, AD-14 |
| Community files and contributor docs (FR-33 to FR-37, FR-59) | `Hexalith/.github`, each module | AD-14, D-COMMUNITY |
| Quality signals (FR-38 to FR-40) | Module README, Builds CI, SonarQube Cloud | AD-6, AD-7, AD-17 |
| Docs check (FR-41 to FR-46, FR-64) | Builds checker, CiCd settings, Docs CI | AD-2, AD-6, AD-7, AD-8 |
| Agent rules (FR-47 to FR-50, FR-63) | AI.Tools | AD-8, AD-12 |
| Time targets and stranger tests (FR-51 to FR-56, FR-61) | Docs `tools/`, ledger and trial records | AD-4, AD-5, AD-16 |
| Rollout levels (FR-57, FR-58) | Ledger, CiCd setup | AD-2, AD-5, AD-10, AD-15 |

## Upstream amendments and open conflicts

| Owner | Item | Needed by |
| --- | --- | --- |
| Hexalith.CiCd | AD-1 and AD-3: add `docs`, `readmeSamples` and documentation suppressions to the complete knob list, always rendered | Hosted docs check on the pilots |
| Hexalith.CiCd | AD-10, AD-16, AD-17: admit the module `docs(readme)` patch rule | First republish |
| Hexalith.CiCd | AD-12: add the README-sample step to stage 3 | AD-9 Builds release |
| Hexalith.CiCd | Commit-type convention: ban planning IDs in subjects and scopes (Open Question 11) | Before the waves |
| Hexalith.CiCd | AD-7, AD-12, AD-14, AD-21: admit a Sonar analysis path, or descope FR-40 | Sonar badges |
| Hexalith.CiCd | Guard protection for entry points and dev container files (Open Question 19) | First published block |
| Platform and McpCli | Reconcile the current paired publisher with inherited Platform AD-11 and record the responsible workflow and release receipt per stable ID | Before authorizing the McpCli README republish |
| Hexalith.Builds | Finding `level`, page profiles, self-link resolver, README-sample step, `D-PLANNING`, a release that contains `aaf27a2c` | Pilot fail mode |
| PRD | FR-5, FR-6, FR-20, UJ-3 and the glossary: module `aspire run` replaced by AD-10. FR-33: Contributor Covenant 3.0. FR-41: no markdownlint-cli2, registry rules in Docs CI. FR-45: ratify checkout-only module runs plus the paired offline Docs check for pinned sibling targets (AD-7). Migration and weekly runs cover live targets. The literal every-run requirement remains open until the PRD owner agrees. FR-46: managed suppressions live in CiCd setup | Next PRD update |
| Hexalith.Docs | Extend registry validation, ledger and forecast consumers for inventory confirmation and source revision (AD-16). Deliver the pinned-source link check and 21-repository calibration evidence | Before inventory exclusions or first pilot promotion |
| Hexalith.Docs | `templates/quickstart-prompts.md` still uses `aspire run` and lacks the fixed first line. `docs/development.md` says Python 3.11 | Story 1.3 acceptance |
| Hexalith.Platform | The Platform README at `abb62da8` lists ASP.NET Core runtime 10 alongside SDK 11.0.100. Retain that documented prerequisite until Platform verifies cold setup and Aspire CLI provisioning. | Story 1.4 |

## Deferred

- **December decision points.** They use the ledger and measured review capacity.
- **Prebuilt images.** A measured cold-start bottleneck triggers the PRD's prebuilt-image decision (FR-52).
- **Automated "Run it" smoke test in CI.** The agent stranger test remains the verification until the brief's decision 10C is revisited.
- **Chat qualification.** It waits for ChatBot in Platform (FR-66).
- **Maintainer confirmations.** Registry descriptions and categories, supported agent tools and versions, and repository visibility (Open Questions 3 and 15).
- **markdownlint-cli2.** Not adopted, so the per-commit path needs no Node. Revisit if rule coverage needs a Markdown parser.
- **Kubernetes topology and how-to content.** Platform owns them (Platform AD-1). This spine fixes only the untimed qualification (FR-24).
- **Cloud providers and a documentation website.** Outside launch scope.
- **Weekly-job keepalive.** Activity in Docs keeps the scheduled job enabled. Add a keepalive only if GitHub disables it.
- **Legacy SonarQube Cloud projects.** A maintainer decides whether to reuse them (Open Question 18).
