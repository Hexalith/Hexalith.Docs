# Reconciliation: documentation spine against the CiCd and Platform parent spines

Review date: 2026-11-21. Read-only review. No other file was changed.

## Scope and evidence

- Spine under review: `ARCHITECTURE-SPINE.md` (draft, updated 2026-11-21). Covers its Inherited invariants table, AD-6 to AD-14, Stack and Structural seed.
- CiCd parent spine: `references/Hexalith.CiCd/.../architecture-cicd-2026-11-07/ARCHITECTURE-SPINE.md`, read at the local checkout `d868b82`. Diffed against `origin/main` `6b3d5c5`, whose AD-7 and AD-18 edits do not touch documentation.
- Platform parent spine: `references/Hexalith.Platform/.../architecture-platform-2026-09-27/ARCHITECTURE-SPINE.md` at `b0159ad4`.
- Builds code: `git show 2c33b2d7:` (origin/main) for `Github/lib/docs_check.py`, `ci_pipeline.py`, `ci_config.py`, `local_check.py`, `release_version.py`, `schemas/hexalith.ci.v1.json`, `.github/workflows/ci.yml` and `README.md`. Tool code read at `v6.3.0` for `ModuleCommandApplication.cs`, `CompositionPrerequisiteProbe.cs` and `SupportedPlatformPins.cs`. Dapr pins read at `6b6eb4ee`, `dc225a69`, `fe68718b` (`v6.4.4`), `08dc4d27` and `2c33b2d7`.
- Platform reality: `README.md`, `.config/dotnet-tools.json` (`hexalith.builds.module.cli` 6.3.0), `global.json` (11.0.100, latestPatch), `apphost.cs` (`Aspire.AppHost.Sdk@17.0.0`), `hexalith-platform.json` (tool range `[6.3.0, 7.0.0-0)`), `eng/builds-tuple.json`. Platform's Builds gitlink is `08dc4d27`.
- Commons `origin/main` (`258f9d2`): `.github/actions/after-unit-tests/action.yml`, `scripts/validate-consumer-package-references.py`, `scripts/pack-release-packages.py`. PolymorphicSerializations `origin/main`: hook and `scripts/validate-readme-sample.py`.
- CiCd `origin/main`: `setup/*.yml`, `setup/README.md` ("README checks and the package pilots"), `rendered/Hexalith.Commons/.github/hexalith-ci.json`, `builds-version` (`v6.4.4`).

## Verdict

**Not reconciled.** Every inherited ID is correct. Most named commands, paths and knob values match the code. However:

- Three new rules contradict binding CiCd ADs, and the spine does not flag any of them:
  - AD-9: a hook calls a Builds tool (CiCd AD-14).
  - SonarQube Cloud runs in module CI (CiCd AD-7, AD-14 and AD-21).
  - AD-8: suppressions live in a module-owned file (CiCd AD-2, AD-3 and AD-8).
- AD-13 names a Dapr upstream that the Platform tool does not use (Platform AD-4). It breaks at the next Builds tag.
- Four CiCd amendments are needed beyond the one the spine flags: AD-1 completeness, the AD-3 knob list, the AD-12 stage order and the commit-type convention.

## Summary

| # | Severity | Parent AD or code location | Category | One line |
| --- | --- | --- | --- | --- |
| F1 | High | CiCd AD-14, AD-8, AD-9, AD-20 | True conflict | AD-9: the module hook "calls that [Builds] tool", but no custom action may call Builds |
| F2 | High | CiCd AD-14, AD-7, AD-12, AD-21 | True conflict | SonarQube Cloud in module CI needs a token in the CI job. Only the pull-only pair is allowed there, and `SONAR_TOKEN` is a legacy secret that adoption removes |
| F3 | High | CiCd AD-2, AD-3, AD-8 | True conflict | AD-8: a module-owned `.github/hexalith-docs.json` steers a Builds gate. Per-module variation must come only from `hexalith-ci.json` and the perimeter |
| F4 | High | Platform AD-4; tool `CompositionPrerequisiteProbe` | Accuracy | AD-13: "Dapr from the Builds catalog the checkout pins" is not what the pinned tool checks. It diverges at the first tag containing `2c33b2d7` |
| F5 | Medium | CiCd AD-12; Builds `ci.yml`, `ci_pipeline.main` | Paraphrase and unflagged amendment | The inherited row says "stage 1". The code runs the check in the prepare step after the stage-1 guard, as AD-6 says |
| F6 | Medium | CiCd AD-1, AD-3; `ci_config.py:128-133`, `ci_pipeline.py:171` | Unflagged amendment | `docs` is optional and the reader defaults it to `off`, but the schema default is `warn`. AD-1 allows only `aspire` and `job-timeout-minutes` to be omitted, and AD-3's knob list lacks `docs` |
| F7 | Medium | CiCd AD-2 | Paraphrase | AD-2 is restated as "hexalith-ci.json and the checkout". The original says "and the perimeter", and the widening hides F3 |
| F8 | Medium | Platform AD-4 | Paraphrase and omission | "Run it" eligibility omits the direct Platform gitlink, the pinned `hexalith-module` within Platform's range, and `dotnet tool restore` |
| F9 | Medium | Platform AD-11 | Omission | "Ends with one McpCli call" doesn't say which McpCli. Platform allows only the run-scoped build or a Platform-published stable version |
| F10 | Medium | CiCd AD-10, AD-18 | Conflict in mechanism | AD-8's "one Builds minor release" warning period can be skipped by the nightly auto-bump to the newest tag |
| F11 | Medium | CiCd Consistency conventions (Commit types), AD-4 absent-glob | Unflagged amendment | AD-11 says "CiCd's commit lint enforces" the planning-ID ban, but the commit-type convention is closed. The ban appears only under Deferred |
| F12 | Medium | CiCd AD-10, AD-18, AD-19 | Flagged amendment, timing | The pending `docs(readme)` amendment becomes effective automatically on the first acceptable tag. Builds' own rules exclude `docs` |
| F13 | Medium | CiCd AD-21, AD-20; baseline | Omission | Only 6 modules are in CiCd `setup/`. The spine doesn't say how unadopted modules get the per-commit check |
| F14 | Medium | `docs_check.py` vs spine AD-6 and AD-8 | Code mismatch and internal contradiction | Fail mode should judge "package READMEs the registry assigns", but the checker can't read the registry. The code judges every `src/libraries` README and no docs pages |
| F15 | Low | CiCd AD-1 | Paraphrase | "Depends only on that commit" overstates AD-1. At run time the guard and drift check read CiCd |
| F16 | Low | CiCd AD-4, AD-7 | Paraphrase, incomplete | The perimeter list omits the `.gitmodules` section, `permissions.deny` and the absent-glob commitlint and semantic-release configs |
| F17 | Low | CiCd AD-11 | Attribution | Docs-tooling stdlib-only is a Docs choice. CiCd AD-11 binds only Builds and CiCd logic |
| F18 | Low | CiCd AD-3, AD-6, Consistency conventions; Docs gitlink | Unagreed caller and reality | CiCd as a "standalone caller" needs a CiCd decision. Docs' own Builds pin `6b6eb4ee` is not a tag and lacks `docs_check.py` |
| F19 | Low | `docs_check.py`; CiCd AD-12 order | Code gap | D-LINK isn't implemented, and the check runs before submodule initialization |
| F20 | Low | Poly `validate-readme-sample.py`; spine AD-9 | Code mismatch | The Poly pilot sample has two `csharp` blocks and one `text` block, which the AD-9 sample shape can't express |
| F21 | Low | Platform AD-10, "Local tool and readiness" | Omission | Readiness and `down` cleanup ownership are not referenced by AD-4 or AD-10 |
| F22 | Low | CiCd gate rule (CAP-10, `gate-classification.md`) | Omission | The README check and the README sample need a product-gate classification |
| F23 | Low | CiCd AD-19 | Omission | Builds' hand-written `hexalith-ci.json` has no `docs`, so Builds' README is never checked |
| F24 | Info | Platform AD-9 | Omission | AD-9 "Builds owns all versions, including local Sentry, placement and scheduler images" supports AD-13. Cite it |

## Inherited invariants, row by row

| Row | ID correct | Faithful | Note |
| --- | --- | --- | --- |
| CiCd AD-1 | Yes | Overstated | F15 |
| CiCd AD-2 | Yes | No: "checkout" replaces "perimeter" | F7, F3 |
| CiCd AD-3, AD-10 | Yes | Yes, but incomplete | `docs` is missing from AD-3's knob list and from AD-1's omittable list (F6) |
| CiCd AD-4, AD-7 | Yes | Partial | F16 |
| CiCd AD-10, AD-16, AD-17 | Yes | Yes. The pending amendment is flagged | Add AD-18 for central dispatch. Timing in F12 |
| CiCd AD-11 | Yes | Attributed beyond scope | F17 |
| CiCd AD-12 | Yes | No: "stage 1" is wrong. The hook sentence conflicts with AD-14 | F5, F1 |
| CiCd AD-15 | Yes | Yes | `local_check.py:172` calls `ci_pipeline.check_documentation` after the guard. Hooks never run locally, so the README sample is CI-only |
| CiCd AD-20 | Yes | Yes, as a self-restriction | The runner's location must also satisfy the AD-20 end state (F1) |
| Platform AD-1 | Yes | Yes | |
| Platform AD-4 | Yes | Partial | F8, F4 |
| Platform AD-11 | Yes | Yes | It omits the publication and run-scoped McpCli rules (F9) |

## Findings

### F1 — High — The README sample hook calls Builds (CiCd AD-14, AD-8, AD-9, AD-20)

- **Spine says.** AD-9: "One standard-library Builds tool … Each publisher's module-owned `after-unit-tests` hook packs same-revision Release outputs and calls that tool." The inherited CiCd AD-12 row says "The README sample runs from the `after-unit-tests` hook." The dependency diagram has `Module CI -->|runs pinned checker and sample tool| Builds`.
- **Conflict.**
  - CiCd AD-14 says: "No action rebuilds the module or calls Builds."
  - CiCd's allowed-dependency rule under its diagram says: "custom actions never call Builds."
  - The AD-8 guard deny list rejects any custom-action `uses:` of `Hexalith/Hexalith.Builds`.
  - CiCd AD-9 makes `references/Hexalith.Builds` "data only: MSBuild props and the local check". Running a tool from the gitlink inside a hook breaks this too.
  - CiCd AD-20's end state keeps in `Github/` and `Tools/` "only what those workflows and `check.py` use". A runner that only module hooks call would be deleted at the final deletion.
  - Today's pilots comply because they use their own module scripts (Commons `scripts/validate-consumer-package-references.py`, Poly `scripts/validate-readme-sample.py`). Commons packs with `--no-build`. The spine's target design is what breaks the rules.
  - Vendoring one runner copy per module is not a way out. AD-9 wants one runner, and CiCd `scan.yml` (jscpd, cross-module) flags the copies.
- **Fix.** Make the runner a Builds-native step of the reusable `ci.yml`, in stage 4 next to the `after-unit-tests` hook. Enable it with a rendered `hexalith-ci.json` knob, for example `docs.samples` listing README paths. Have Builds code pack Release outputs with `--no-build`. Place the runner in `Github/lib/` beside `docs_check.py`. Record this as pending CiCd amendments (AD-3 knob, AD-12 stage order, AD-14 note) and a minor Builds API change (AD-10). Until then, keep the module-owned scripts as the sanctioned interim and correct the AD-12 row.

### F2 — High — SonarQube Cloud in module CI has no compliant path (CiCd AD-14, AD-7, AD-12, AD-21)

- **Spine says.**
  - The deployment diagram has `ModCI --> Sonar[SonarQube Cloud]`.
  - The capability map row "Quality signals (FR-38 to FR-40)" lives in "Builds CI, SonarQube Cloud" and is governed by AD-6 and AD-7. Neither AD covers Sonar.
  - AD-6 has Docs CI judge the "Sonar key".
  - The PRD's FR-40 says "The shared CI runs the SonarQube Cloud scanner … using an organization token."
  - Deferred covers only reuse of legacy projects (OQ-18).
- **Conflict.**
  - CiCd AD-14: "Every secret its job references is readable by all of that job's steps, so the CI job and `nightly-hook` hold only the pull-only registry pair." Its stated goal is to prevent "a secret reaching every test in the CI job".
  - CiCd AD-12's closed stage list has no scan stage.
  - CiCd AD-21 treats `SONAR_TOKEN` as a legacy org secret, "never CiCd or Builds", removed from each repo at adoption.
  - CiCd AD-1 has rendered callers pass only named secrets.
  - So a Sonar scanner in the shared CI contradicts several CiCd ADs. No docs AD records this.
- **Fix.** Add an AD, or at least a Deferred entry, that marks FR-40 blocked on a CiCd decision. Options:
  - a separately scoped Sonar job or workflow. CiCd's Deferred "Hook and job secrets" notes this needs a spec change to the one-CI-job constraint, like the AD-12 approved manual qualification job;
  - keyless SonarQube Cloud automatic analysis, which gives no .NET coverage;
  - dropping the Sonar badges from launch.

  Remove the `ModCI --> Sonar` arrow and the "Builds CI" placement until CiCd decides.

### F3 — High — Module-owned suppressions steer a shared gate (CiCd AD-2, AD-3, AD-8)

- **Spine says.** AD-8: "Suppressions live only in the module-owned `.github/hexalith-docs.json` as `{file, rule, reason}` entries [ASSUMPTION]." A finding fails only "with no matching suppression".
- **Conflict.**
  - CiCd AD-2: "All variation comes from `hexalith-ci.json` and the perimeter."
  - CiCd AD-3: setup files are "the only per-module input". It prevents "free-form knobs; overrides that silently never apply".
  - CiCd AD-8 prevents "module-owned audit or gate bypasses; module code or module config steering the guard".
  - The precedent is test exclusions, which live in CiCd setup (`tests.exclude`) and not in a module file ("There is no plain skip", AD-13).
  - A module file that turns a fail-mode finding into a pass is a module-owned gate bypass. The spine tags it [ASSUMPTION] but never notes that it conflicts with a parent AD. Its AD-2 paraphrase (F7) obscures the conflict.
- **Fix.** Put suppressions in CiCd setup, for example `docs: {mode, suppressions: [{file, rule, reason}]}`. They are then schema-validated, rendered into `hexalith-ci.json` and changed only by CiCd agents. Alternatively, get an explicit CiCd AD-2 and AD-3 amendment that admits a docs-only module file with a closed schema. Either way, list it as a pending CiCd amendment.

### F4 — High — AD-13's Dapr upstream is not what the Platform tool checks (Platform AD-4)

- **Spine says.** AD-13: "Dapr CLI and runtime come from the Builds catalog the checkout pins." The Stack row says "1.19.1 at `dc225a69`; CLI 1.19.1 and runtime 1.19.2 at `2c33b2d7`."
- **Reality.**
  - The `hexalith-module` prerequisite probe (`Hexalith.Builds.Tooling/Runtime/CompositionPrerequisiteProbe.cs`) compares the CLI and runtime in `HEXALITH_DAPR_HOME` with the pinned tool's own catalog. At `v6.3.0`, `SupportedPlatformPins.DaprRuntimeVersion` is "1.19.1".
  - Platform AD-4: the Platform identity "pins the Builds catalog commit and a supported Platform-tool version range".
  - CiCd AD-10 moves a module's Builds gitlink nightly in lockstep, independently of the workspace's tool pin.
  - Today all sources agree on 1.19.1: tool `v6.3.0`, module gitlinks at `v6.4.4` (`fe68718b`), and Platform's Builds gitlink `08dc4d27`.
  - The first tag containing `2c33b2d7` (runtime 1.19.2) will reach module gitlinks by auto-bump while module tool pins stay at 6.3.0. A dev container that follows AD-13 then installs runtime 1.19.2, and the tool refuses it.
  - Platform's own README still prescribes CLI 1.18.2 and runtime 1.18.7 (README lines 519-557). Its prerequisites already disagree with its pinned tool.
- **Fix.** For "Run it" blocks and their dev containers, take Dapr and the Aspire CLI from the catalog of the `hexalith-module` version pinned in the workspace `.config/dotnet-tools.json`. That pin must lie within the Platform identity's accepted range, per Platform AD-4. Keep "the Builds gitlink" as the upstream only for CI (CiCd AD-12: "the one Dapr version pinned in Builds"). Have D-PREREQUISITES compare the dev container against the tool catalog, and add the stale Platform README to the D-PREREQUISITES findings.

### F5 — Medium — The docs check is not in stage 1 (CiCd AD-12)

- **Spine says.** Inherited row: "The docs check runs in stage 1." AD-6, correctly: "It runs in the CI prepare phase before restore." The memlog's pending amendment says "AD-12 stage 1 gains the docs check."
- **Reality.** In Builds `.github/workflows/ci.yml` at `2c33b2d7`:
  - The first step is "Stage 1 guard owned CI/CD content" (`$/Github/guard`).
  - The next step is "Validate and prepare module" (`$/Github/ci-prepare`). There, `ci_pipeline.main` with `--phase prepare` calls `check_documentation` before `initialize_submodules`.
  - Then come SDK setup and "Stage 2 restore and Release build".
  - The prepare step also runs with `solution: none`.
  - The Builds README agrees: "After the guard, the reusable CI prepare stage …".
- **Conflict.** The AD-12 stage list is closed. The inherited row misstates it, and the planned amendment targets the wrong stage.
- **Fix.** Change the row to: "The docs check runs after the guard and before restore, in the prepare step, including with `solution: none`." Amend CiCd AD-12's order to match, and list that amendment as pending.

### F6 — Medium — The `docs` knob breaks CiCd AD-1 completeness and is missing from AD-3's knob list

- **Reality.**
  - `schemas/hexalith.ci.v1.json` declares `docs` with enum `off|warn|fail`, default `warn`, outside `required` ("Previously delivered documents may omit this field").
  - `ci_config.py:128-133` accepts omission.
  - `ci_pipeline.check_documentation` reads `prepared.document.get("docs", "off")`.
  - The Builds README says "Older configurations with no setting skip this check."
  - The CiCd `setup/README.md` on `origin/main` says the render "materializes `docs: warn`."
- **Conflict.**
  - CiCd AD-1: "every knob is written out, so no reader applies a default or accepts a missing key". Only `aspire` and `job-timeout-minutes` may be omitted.
  - The reader's omitted value (`off`) also differs from the schema default (`warn`).
  - CiCd AD-3's knob list doesn't include `docs`.
  - The spine cites CiCd AD-3 and AD-10 as if they already house the knob.
- **Fix.** Add to the pending-amendment list:
  - AD-3 gains the `docs` knob (`off|warn|fail`, schema default `warn`, a minor release under AD-10);
  - AD-1's omittable list gains `docs`, where omission means `off` only in pre-contract documents.

  Alternatively, make `docs` required in the next contract.

### F7 — Medium — CiCd AD-2 is paraphrased unfaithfully

- **Spine says.** "Per-repository variation comes from `hexalith-ci.json` and the checkout."
- **Original.** "All variation comes from `hexalith-ci.json` and the perimeter."
- **Conflict.** "The checkout" admits any module-owned file as an input to Builds behavior. That is exactly what F3 relies on.
- **Fix.** Restore "and the perimeter". If F3's suppression file survives, cite the CiCd amendment that admits it.

### F8 — Medium — "Run it" eligibility omits Platform AD-4's workspace requirements

- **Spine says.**
  - Platform AD-4 row: "The module workspace initializes only direct `references/*` submodules …"
  - AD-10: run `dotnet tool run hexalith-module -- run --manifest module/hexalith.module-manifest.v2.json`. A repository without a v2 manifest, or whose operations McpCli doesn't serve, keeps the block reserved.
- **Reality.**
  - The command is valid: `run` exists at tool `v6.3.0`, `--manifest` is required, and mode defaults to `source`.
  - Platform AD-4 also requires every non-Platform workspace that runs the tool to declare `references/Hexalith.Platform` directly. The tool must be pinned in `.config/dotnet-tools.json`, where it "alone sets the single mode property". The Platform identity pins the Builds catalog and the tool range. The tool fails when it finds an initialized nested submodule.
  - Current workspaces show the gap:

    | Workspace | v2 manifest | Platform gitlink | `hexalith-module` pin |
    | --- | --- | --- | --- |
    | Parties | Yes | Yes | 6.3.0 |
    | Tenants | Yes | Yes | None |
    | Projects | Yes | Yes | None (pins only `hexalith.frontcomposer.cli`) |
    | Folders | No | Yes | None |

  - Platform's README always runs `dotnet tool restore` first.
- **Fix.** Extend AD-10's eligibility to: a v2 manifest, a direct `references/Hexalith.Platform` gitlink, and a `hexalith-module` pin within that Platform identity's `toolVersionRange`. Prefix the command with `dotnet tool restore`. Restate the Platform AD-4 row to include the Platform-identity and tool-pin rules.

### F9 — Medium — Which McpCli makes the first call (Platform AD-11)

- **Spine says.** AD-10: "The block ends with one Hexalith.McpCli call and its expected output."
- **Platform AD-11.**
  - Only the Platform publication workflow publishes stable `Hexalith.McpCli`, after staging validation. McpCli's own pipeline publishes only prerelease tool versions.
  - "In source and package modes the Platform tool builds a run-scoped, never-published McpCli."
  - An operation is executable only when the gateway's metadata endpoint serves it.
- **Reality.** The Platform README says the tool builds McpCli only for the McpCli manifest (it reports the path in diagnostic `HXI010`, field `mcpcli`). "Package mode builds no McpCli." Connected execution "arrives in Epic 3".
- **Fix.** State that the call uses the run-scoped McpCli the Platform tool reports for that run, against that run's gateway. Forbid READMEs from installing a prerelease `Hexalith.McpCli` package. Tie AD-10's "reserved" state to Platform's connected-execution milestone, so a reserved block is the expected state today.

### F10 — Medium — The new-rule warning period can be skipped by the auto-bump (CiCd AD-10, AD-18)

- **Spine says.** AD-8: "A new rule reports as a warning in fail-mode repositories for one Builds minor release before it can fail [ASSUMPTION]."
- **Conflict.** The nightly auto-bump moves `builds-version` to "the newest acceptable tag in the current major that is not in `builds-skip`". A fail-mode module can therefore jump from a tag before the rule to a tag where the rule already fails. This happens when two minors ship in one day, after a `builds-skip` entry, or after a rollback. This is the kind of minor-release breakage AD-10 prevents.
- **Fix.** Make failure depend on a value that CiCd sets, rather than on release adjacency. For example, `docs: fail` could judge only a rule-set version named in setup, so that new rules stay warnings until CiCd promotes the rule set. Alternatively, fail-capable rules could land only in a Builds major.

### F11 — Medium — The planning-ID commit ban is stated as enforced, but the CiCd convention is closed

- **Spine says.** AD-11: "No commit subject or scope carries a story, epic, FR or other planning ID, and CiCd's commit lint enforces this." Deferred: "Commit lint scope ban. Delivery timing belongs to Hexalith.CiCd (Open Question 11)."
- **Conflict.**
  - CiCd's "Commit types" convention fixes commitlint as "Builds' commitlint config as it is today, plus one rule rejecting `[skip ci]`-family markers and `skip-checks` trailers".
  - Module commitlint configs are absent-glob entries in CiCd AD-4, so the ban can live only in the Builds guard's config. That requires a CiCd convention amendment.
  - The memlog records this amendment, but AD-11 and the inherited table don't.
- **Fix.** In AD-11, write "[pending CiCd amendment: commit-type convention and the Builds guard commitlint config]". Add the matching row to the inherited table.

### F12 — Medium — The flagged `docs(readme)` amendment activates automatically, and Builds is excluded

- **Spine says.** Inherited row: "Amendment pending: the module `docs(readme)` patch rule (AD-11) admits one docs type." AD-11: "Dispatch a republish only after the delivered Builds tag contains the `docs(readme)` rule."
- **Reality.** `release_version.py` at `2c33b2d7`, lines 44-48, adds `{"type": "docs", "scope": "readme", "release": "patch"}` to the module rules only. The `builds` selection still excludes `docs`, `test` and `style`. No tag contains `aaf27a2c` yet (`v6.4.4` is `fe68718b`).
- **Conflict (timing).** CiCd AD-10 and AD-18 auto-bump the 6 managed modules to the first acceptable tag that contains `aaf27a2c`. From that night, CiCd AD-10's text ("In modules, `feat`, `fix` and `perf` release …") contradicts delivered behavior.
- **Gap.** Under CiCd AD-10 and AD-19, Builds' own package READMEs are never republished by a `docs(readme)` commit.
- **Fix.**
  - Require the CiCd AD-10 amendment to merge before that Builds tag is accepted, or add the tag to `builds-skip` until it does.
  - Add CiCd AD-18 to the row, because central nightly dispatch is the release path.
  - Note in AD-11 that Builds' READMEs refresh only with Builds' next releasing commit.

### F13 — Medium — Rollout to unadopted modules (CiCd AD-21, AD-20; baseline)

- **Reality.** CiCd `origin/main` `setup/` lists only AI.Tools, Commons, Conversations, McpCli, PolymorphicSerializations and Works.
  - For any other module, the baseline says "Until a module adopts CiCd, its existing required CI gates apply."
  - Module agents can't push workflows (CiCd AD-7).
  - The legacy Builds workflows are frozen (CiCd AD-20).
- **Gap.** AD-2 ("Enroll modules through CiCd …") and AD-6's standalone-caller list don't say what unadopted modules get. In practice they get only the Docs-CI rules judged on pinned submodule revisions. FR-57 rollout levels depend on the CiCd AD-21 sequence.
- **Fix.** State that the per-commit check reaches a module only after CiCd adoption (AD-21), with no legacy-workflow interim. Make adoption a precondition of the "Pilot ready" and "Hosted checks enabled" delivery boundaries.

### F14 — Medium — AD-8's checked-page scope can't be implemented under AD-6, and the code differs

- **Spine says.** AD-6: the checker "never reads the registry". AD-8: fail mode judges "the root README, every package README the registry assigns, and docs pages the root README links to directly. Other pages report only." It also adds suppressions.
- **Reality.**
  - `docs_check.readmes()` yields the root `README.md` and every `README.md` beside a `.csproj` under `src/libraries`.
  - `check()` fails on any finding in any of these files, so there is no checked-page distinction.
  - It reads no docs pages and supports no suppressions.
  - Its rules are only D-README, D-LENGTH (more than 150 lines) and D-BADGE. All three are in `docs/documentation-standard.md`.
- **Fix.** Define checked package READMEs by a rule the checker can evaluate alone, such as packable projects or the nuspec `readme` entry. Alternatively, have CiCd render the assigned list into `hexalith-ci.json`. Add the docs-page scope and suppressions to the Builds backlog, and mark AD-8 as not yet implemented beyond the finding contract.

### F15 — Low — CiCd AD-1 is overstated

- **Spine says.** "A commit's CI result depends only on that commit."
- **Original.** AD-1 materializes the configuration in the commit, and "At run time Builds reads CiCd only for the guard and the release drift check."
- **Fix.** Write: "The module commit materializes its CI configuration. The docs check adds no run-time read of CiCd, the registry or another repository."

### F16 — Low — The CiCd AD-4 perimeter is listed incompletely

- **Gap.** The row omits the Builds `.gitmodules` section, `.claude/settings.json` `permissions.deny`, and the absent-glob entries (`commitlint.config.*`, `.commitlintrc*`, `.releaserc*`, `release.config.*`). The last group matters for F11.
- **Fix.** Cite the AD-4 table instead of enumerating it, or complete the list.

### F17 — Low — CiCd AD-11 is attributed beyond its scope

- **Gap.** CiCd AD-11 binds "all Builds and CiCd logic". It also allows PEP 723 with `uv` for CiCd tools that hold no secret. The Docs rule "standard library only" is a Docs decision. That is acceptable, but it is not inherited.
- **Fix.** Split the row: Builds checker and runner (inherited) and Docs tooling (own convention).

### F18 — Low — The standalone-caller assumption needs CiCd's agreement and a tagged pin

- **Spine says.** AD-6: "A standalone caller (Docs, BmadSkills, CiCd, `Hexalith/.github`) runs that script from a Builds checkout pinned to a release tag [ASSUMPTION]."
- **Conflict and reality.**
  - CiCd's global checks are a closed list (AD-3), and its workflows are fixed (`deliver.yml`, `nightly.yml`, `scan.yml`).
  - CiCd reads Builds only at `builds-version` through a clone. Its `references/` submodules are for agent context only.
  - Docs' own `references/Hexalith.Builds` is `6b6eb4ee` (`v6.3.1-10-g6b6eb4ee`). That is not a release tag, and `Github/lib/docs_check.py` doesn't exist there.
- **Fix.** Mark CiCd as a caller "subject to CiCd decision". Record that Docs must move its Builds gitlink to the first tag containing `aaf27a2c` before it can run the checker.

### F19 — Low — Per-commit link checking isn't in the checker yet

- **Gap.**
  - AD-7 (tagged [ADOPTED]) has the checker resolve relative paths, fragments and self `blob/main` links offline. `docs_check.py` at `2c33b2d7` has no D-LINK.
  - The check runs before `initialize_submodules`, and it reads the working tree (`Path.read_text`, `os.walk`). Links into gitlinked directories therefore won't resolve.
- **Fix.** Tag AD-7's per-commit half as pending Builds work. Specify that D-LINK resolves against the git tree, so a gitlink entry counts as an existing directory.

### F20 — Low — The AD-9 sample shape doesn't fit the PolymorphicSerializations pilot

- **Reality.** Poly's `validate-readme-sample.py` requires two `csharp` blocks (`Models.cs`, `Program.cs`) and one `text` block under "Quick Start". AD-9 says "each `csharp` block … is followed directly by one `text` block".
- **Fix.** Either allow N `csharp` blocks followed by one `text` block, or plan Poly's README restructuring in the migration.

### F21 — Low — Readiness and cleanup ownership are not referenced (Platform AD-10, "Local tool and readiness")

- **Gap.** AD-4 measures "through readiness". Platform defines readiness through the runner: a default 10-minute startup deadline and declared readiness, where process-running is not readiness. The runner also owns cleanup (`down --manifest`, with `--run-id` on HXR024).
- **Fix.** Measure readiness from the tool's ready report. End "Run it" and the stranger-test kit with `down`. Cite Platform AD-10.

### F22 — Low — Gate classification (CiCd CAP-10 gate rule)

- **Gap.** The gate rule keeps only product checks: compilation, tests, security and dependency scans, commit format and package publishing. The README check and the README sample need an explicit classification. D-BADGE inspects workflow file names, which is close to the deleted "workflow YAML" category.
- **Fix.** Ask CiCd to classify both, under package publishing or as an added product-documentation category.

### F23 — Low — Builds' own README is unchecked (CiCd AD-19)

- **Reality.** Builds' hand-written `.github/hexalith-ci.json` at `2c33b2d7` has no `docs` key. With the reader default `off`, Builds' README is never checked, although the registry includes Builds. Only CiCd agents change Builds.
- **Fix.** Add an action item for CiCd agents: set `docs: warn` in Builds' hand-written config when the contract ships.

### F24 — Info — Cite Platform AD-9

Platform AD-9 ("Builds owns all versions, including local Sentry, placement and scheduler images; file AppHost pins must agree with that catalog") is the Platform rule behind AD-13's single-upstream principle. Cite it in AD-13 and in the inherited table.

## Verified as matching

- All inherited IDs exist and name the right topics: CiCd AD-1, 2, 3, 4, 7, 10, 11, 12, 15, 16, 17, 20 and Platform AD-1, 4, 11.
- `Github/lib/docs_check.py` exists on Builds main and is stdlib-only. Its standalone CLI is `--root`, `--mode warn|fail` and `--repository`.
- The finding contract matches: one JSON line `{file, line, rule, hint}` (`docs_check.check`).
- `docs` knob values are `off|warn|fail`, with schema default `warn`. Warn mode never fails, and fail mode raises before submodule initialization and restore.
- `check.py` runs the same function: `local_check.run` calls `ci_pipeline.check_documentation` after the guard.
- The badge rule checks a same-repository workflow file in the checkout, offline (AD-2 and AD-7, badge part).
- `docs(readme)` gives a module patch release (`release_version.py` line 45). The first tag after `v6.4.4` that contains `aaf27a2c` doesn't exist yet, as the Stack row states.
- `dotnet tool run hexalith-module -- run --manifest module/hexalith.module-manifest.v2.json` is a valid command at tool 6.3.0, with default mode `source`. Platform pins `hexalith.builds.module.cli` 6.3.0. Parties, Tenants and Projects have `module/hexalith.module-manifest.v2.json`.
- Platform pins match the Stack: `global.json` SDK 11.0.100 with `latestPatch`, and `apphost.cs` `Aspire.AppHost.Sdk@17.0.0`. The Platform spine's own Stack table (10.0.401, Aspire 13.5.4) is stale. The docs spine correctly follows Platform's configuration (its AD-4).
- The Dapr pins at the named revisions are correct: `dc225a69`, `6b6eb4ee`, `fe68718b` and `08dc4d27` all have 1.19.1/1.19.1; `2c33b2d7` has runtime 1.19.2 and CLI 1.19.1.
- `.github/actions/after-unit-tests/action.yml` is the correct CiCd AD-14 path. The Commons and Poly hooks are composite and call only module scripts. Commons packs with `--no-build`. CiCd setup enables `hooks: [after-unit-tests]` for both pilots.
- `actions/checkout` v7.0.1 `3d3c42e5…` matches Builds `ci.yml`. The Python 3.12 floor is enforced in `ci_pipeline.main`.
- Platform AD-1 and AD-4: technical modules (EventStore, Memories, McpCli) run from the Platform workspace with `references/<Module>/module/…v2.json` manifests, as the Platform README's table shows.

## Notes outside this review's scope

- Builds `2c33b2d7` edits the frozen `domain-ci.yml` and `domain-release.yml` files. CiCd AD-20 forbids changing them until the last module has moved. This is a Builds and CiCd matter, unrelated to the docs spine.
- Platform's README prerequisites (Dapr 1.18.2/1.18.7) disagree with its pinned tool catalog (1.19.1). That is a D-PREREQUISITES finding for Platform once the rule exists.
