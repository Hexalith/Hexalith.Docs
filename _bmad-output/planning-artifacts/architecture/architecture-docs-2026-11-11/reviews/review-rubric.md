---
title: Rubric review of the Hexalith documentation architecture spine
reviewed: ARCHITECTURE-SPINE.md (updated 2026-11-21, status draft)
companion: .memlog.md (updated 2026-11-21T07:11)
reviewer: independent rubric walker (good-spine checklist)
date: 2026-11-21
---

# Rubric review: Hexalith documentation architecture spine

## Verdict

**Not ready to finalize. Revise, then re-run the gate.** The spine ratifies most of the settled reality, including the registry, rule IDs, finding format, `docs` knob, `docs(readme)` rule and Platform-only composition. The capability map covers all 66 FRs. Before agents in 21 repositories build from it, these problems need fixing:

- AD-9 contradicts an inherited CiCd invariant (critical).
- AD-6 and AD-8 contradict each other on which pages fail mode judges.
- Several real divergence points have no owner: SonarQube Cloud, legacy CLI/MCP package READMEs, the entry-point exemption text, and republishing Builds and McpCli.
- The scheduled job and its secrets are underspecified.

Counts: 1 critical, 7 high, 8 medium, 8 low.

## Method and evidence

I read the spine and its memlog in full. I also read the PRD (FR-1 to FR-66, NFRs, §8 to §12), PRD addendum §B.2 to §B.6, `epics.md`, the parent CiCd spine (architecture-cicd-2026-11-07, AD-1 to AD-21, conventions, stack) and the Platform spine (AD-1, AD-4, AD-9, AD-10, AD-11).

For brownfield, I inspected:

- `docs/`, `templates/`, `scripts/`, `tools/` and `.github/workflows/documentation.yml`
- `_bmad-output/implementation-artifacts/`: launch ledger, exposure review and sprint status
- `.gitmodules` and the submodule pins
- Builds `origin/main`: `Github/lib/docs_check.py`, `ci_pipeline.py`, `local_check.py`, `release_version.py`, `schemas/hexalith.ci.v1.json` and `Props/Directory.Packages.props`
- the PolymorphicSerializations and Commons `after-unit-tests` hooks and the README-sample script
- module `global.json`, v2 manifests, `.config/dotnet-tools.json`, `.gitmodules` and `CLAUDE.md` entry points

Nothing was executed except read-only git and file inspection. I loaded no agent skill from `references/`.

## Checklist verdicts

| # | Checklist item | Verdict | Findings |
| --- | --- | --- | --- |
| 1 | Fixes the real divergence points for the level below, and misses none | **Partial** | It fixes the registry shape, rule-ID catalog, finding line, knob, commit vocabulary, Run-it path and pin upstreams. It misses SonarQube Cloud, legacy-surface package READMEs, suppression document shape, the README heading contract, the sample unit, the canonical entry-point text, the Dapr home and the standalone checker CLI. See R-03, R-04, R-05, R-07, R-10, R-11, R-16 and R-18. |
| 2 | Every AD's Rule is enforceable and prevents its divergence | **Partial** | AD-6 and AD-8 contradict each other (R-02). The AD-13 Aspire comparison can't run anywhere (R-06). The AD-8 grace period is defeated by the nightly auto-bump (R-09). The AD-12 Rule edits the wrong text (R-07). |
| 3 | Nothing under Deferred lets two units diverge | **Mostly pass** | OQ-19 (dev container and entry-point ownership), the legacy Sonar projects and the weekly keepalive leave small gaps (R-23, R-03, R-12). |
| 4 | Named technology is current and evidenced | **Pass with gaps** | The SDK 11.0.100, Aspire 17.0.0, Dapr 1.19.1/1.19.2, base image, lychee, runner and Contributor Covenant entries are evidenced in the memlog and confirmed in the checkouts. The feature majors, actions/checkout and the missing Sonar or installer versions are gaps (R-22). |
| 5 | Ratifies rather than contradicts brownfield | **Partial** | It ratifies the registry, validator, standard, kit, ledger and Docs workflow. It contradicts the hosted-passing PolymorphicSerializations sample (R-05), the quickstart prompt templates (R-13), the Python floor in `docs/development.md` and Docs' own Builds pin (R-18). |
| 6 | Covers the spec's capabilities (FR-1 to FR-66) | **Pass (coverage) / Partial (governance)** | Every FR falls in a map row (table below). FR-40, the FR-15 republish of Builds and McpCli, the FR-54 change report and the FR-48 check owner have no governing AD (R-03, R-08, R-15, R-07). |
| 7 | No new AD weakens or contradicts an inherited one | **Fail** | AD-9 contradicts CiCd AD-9 and AD-14 (R-01). The Sonar placement conflicts with CiCd AD-14 and AD-21 (R-03). AD-13 is ambiguous against Platform AD-4 (R-06). The Inherited table presents pending amendments as inherited facts (R-14). |
| 8 | Every owned dimension is decided, deferred or an open question, especially the operational envelope | **Partial** | Environments, runners and the dev container base are decided. The weekly job has no schedule, output channel, token or failure signal. SonarQube Cloud and its secret are undecided. Docs pin cadence, triage ownership and commit lint for unmanaged repos are missing. There is no open-question or amendment register (R-03, R-12, R-15). |

Other checks: rationale leaking into rules is low (R-20). Some ADs are really seed or process (R-20). There is redundancy between ADs (R-19). The mermaid diagrams are syntactically valid, with semantic issues (R-21).

## Findings

Severity: **critical** means building to the spine breaks an inherited invariant across many repositories. **High** means independently built units will diverge, or a launch gate can't be met. **Medium** means a likely divergence or an unenforced rule. **Low** means clarity, hygiene or evidence.

### R-01 (critical): AD-9 makes module hooks call Builds, which CiCd forbids

- **Checklist:** 7, 1
- **Location:** AD-9 Rule (lines 104–108); Inherited table row "CiCd AD-12" (line 47); dependency diagram edge `Module -->|runs pinned checker and sample tool| Builds` (line 146)
- **Issue:** AD-9 says: "Each publisher's module-owned `after-unit-tests` hook packs same-revision Release outputs and calls that [Builds] tool." The parent spine, which is final, forbids this in three places:
  - Line 93: "custom actions never call Builds".
  - CiCd AD-14: "No action rebuilds the module or calls Builds".
  - CiCd AD-9: "The module's `references/Hexalith.Builds` is data only: MSBuild props and the local check".

  The guard deny list also rejects `uses: Hexalith/Hexalith.Builds`. All 14 publishers would implement this path. They would either violate the invariant (calling `python3 references/Hexalith.Builds/...` from a hook) or keep diverging per-module scripts, which is the outcome AD-9 exists to prevent.
- **Suggested fix:** Make the README-sample runner a step of Builds' reusable `ci.yml` in stage 4, after unit tests and before the `after-unit-tests` hook. Enable it with a new optional `hexalith-ci.json` knob, for example `readmeSamples`, rendered by CiCd. That is a minor Builds release under CiCd AD-3 and AD-10. Builds' own package-mode outputs feed it, so no module action calls Builds. Module hooks keep only module-specific checks. If CiCd prefers the hook design, record it as a required amendment to CiCd AD-9 and AD-14, owned by the CiCd maintainer, before any publisher adopts it. Move the row from "Inherited" to "Requires parent amendment" (see R-14).

### R-02 (high): AD-6 and AD-8 disagree on the checked package READMEs

- **Checklist:** 2, 5
- **Location:** AD-6 Rule (line 90): the checker "never reads the registry". AD-8 Rule (line 102): fail mode judges "every package README the registry assigns".
- **Issue:** The only per-repository checker that has modes can't know which READMEs the registry assigns. Today `docs_check.py` judges the root README plus any `README.md` beside a `.csproj` under `src/libraries`. The registry assigns READMEs outside that tree:
  - `src/Hexalith.Conversations.Contracts/README.md`
  - `src/Hexalith.FrontComposer.Cli/README.md` and `src/Hexalith.FrontComposer.Testing/README.md`
  - ten `src/Hexalith.Memories.*/README.md`

  Builds implementers and migration agents will each choose differently: registry list, `src/libraries` glob or csproj metadata. Either the fail-mode page set silently shrinks, or the checker breaks CiCd AD-1 and AD-2.
- **Suggested fix:** Define the package-README set from the checkout. For example: every README a packable project packs, read from `PackageReadmeFile` or the packed path in its csproj, which the checker can evaluate without restore, or the nuspecs in Release mode. Add a Docs CI registry rule that `projectReadmes` equals that derived set at the pinned revision. Reword AD-8 to "every package README the checkout packs".

### R-03 (high): SonarQube Cloud (FR-40) has no architecture home and conflicts with CiCd

- **Checklist:** 1, 6, 7, 8
- **Location:** Capability map row "Quality signals (FR-38 to FR-40)… AD-6, AD-7" (line 270); seed diagram `ModCI --> Sonar` (line 243); Deferred "Legacy SonarQube Cloud projects" (line 288); Stack (no scanner entry)
- **Issue:**
  - AD-6 covers only checking the Sonar key against the registry. AD-7 doesn't govern the scanner. Nothing fixes where the scanner runs, how the token reaches it, the fork or no-token skip, or the key formula.
  - CiCd AD-14 allows only the pull-only registry pair in the CI job ("so the CI job and `nightly-hook` hold only the pull-only registry pair"). CiCd AD-21 lists `SONAR_TOKEN` among the legacy org secrets to restrict.
  - Key conventions already diverge. Addendum §B.6 proposes `hexalith_<repository-name>`, while the registry records `Hexalith_Hexalith.Commons` and `Hexalith_Hexalith.PolymorphicSerializations`. Badges (FR-38), registry rows, the Docs CI key rule and the Builds scanner will disagree.
- **Suggested fix:** Add an AD, or an explicit open question owned by CiCd and Builds, with a named deadline before the pilots. It should fix:
  1. Scanner placement: a dedicated job or hook that receives the token by name, which needs a CiCd AD-14 amendment.
  2. One key formula. The registry stores the derived key.
  3. The skip-not-fail behavior without a token.
  4. The org token's name and scope.
  5. The scanner version in Stack.

  Link the legacy-projects deferral to this decision, because it changes the keys.

### R-04 (high): Package READMEs of frozen legacy CLI and MCP surfaces are unresolved

- **Checklist:** 1, 7
- **Location:** Inherited table row "Platform AD-11" (line 52): "No README documents a legacy module CLI or MCP host"; AD-3 Rule (line 72); capability map rows FR-9 to FR-16
- **Issue:** The registry inventories `Hexalith.EventStore.Admin.Cli` and assigns package READMEs for `Hexalith.Memories.Cli` and `Hexalith.Memories.Mcp`. Platform AD-11 explicitly names EventStore.Admin.Cli obsolete. The registry also inventories `Hexalith.FrontComposer.Mcp`. The current `src/Hexalith.Memories.Cli/README.md` documents `dotnet tool install --global Hexalith.Memories.Cli` and `memories --help`.

  AD-3 and FR-15 require these READMEs to be verified and republished, and FR-10 requires a Packages row for each. The inherited row forbids documenting them. The baseline exempts only `Hexalith.FrontComposer.Cli` and Memories `tools/MigrateEmbeddingVectors`. Each migration agent (EventStore, Memories, FrontComposer) will resolve this differently: delete the README, keep it, or mark it obsolete.
- **Suggested fix:** Add a rule:
  - A frozen legacy surface's package README and Packages row say only that the package is obsolete, name Hexalith.McpCli as the replacement, and document no commands.
  - The registry marks such IDs, for example with `legacySurface: true`.
  - Republish still applies, or a maintainer instead chooses nuget.org deprecation per FR-29.

  Reword the inherited row to Platform AD-11's actual scope and list the named exemptions.

### R-05 (high): AD-9's sample shape contradicts the passing pilot and leaves the sample unit ambiguous

- **Checklist:** 5, 1, 2
- **Location:** AD-9 Rule (line 108); Conventions "Sample shape" (line 179); memlog line 40
- **Issue:**
  - **Pilot contradiction.** The hosted-passing PolymorphicSerializations sample uses two `csharp` fences followed by one `text` fence. These are `Models.cs` and `Program.cs` in commit `aba0bbc`. `scripts/validate-readme-sample.py` requires exactly two code fences and one output fence, and addendum §B.4 confirms "runs the two displayed fences". AD-9 ("each `csharp` block … followed directly by one `text` block … a consumer for each pair") would fail that pilot. Memlog line 40 misstates both pilots as "one csharp block".
  - **Prompt and output collision.** `templates/quickstart-prompts.md` puts AI prompts in ` ```text ` fences. A prompt placed right after a sample fence would be read as the expected output.
  - **Package README scope.** Per-package READMEs (FR-16) needn't follow the skeleton, so the runner's scope there ("Use the package" heading, or every `csharp` fence) is undefined. Commons package READMEs contain illustrative, non-runnable snippets.
  - **Package references.** Which packages the consumer references is unspecified. The pilot hard-codes them.
- **Suggested fix:**
  - Define the sample unit as one or more consecutive `csharp` fences, each carrying its file name in the info string (for example ` ```csharp Models.cs `), followed by exactly one ` ```text ` output fence.
  - Give prompts a distinct fence, for example ` ```text prompt ` or ` ```prompt `, and update the template.
  - The consumer references exactly the packages named by the block's `dotnet add package` commands.
  - In package READMEs, run only fences under a "Use the package" heading.
  - Correct the memlog event.

### R-06 (high): AD-13's pins can't be checked as written, and the Dapr source is ambiguous

- **Checklist:** 2, 7, 4
- **Location:** AD-13 Rule (line 132); Stack rows "Dapr CLI and runtime" and "Dev container features" (lines 194, 197); AD-4 (line 78)
- **Issue:**
  1. **The Aspire comparison can't run anywhere.** The Aspire CLI version must equal the `Aspire.AppHost.Sdk` of the AppHost that runs the block, which for business modules is Platform's `apphost.cs`.
     - In module CI, the per-commit checker runs in the prepare phase *before* submodule initialization (`ci_pipeline.main`: `check_documentation` precedes `initialize_submodules`). CiCd AD-12 checks out only Builds, so the Platform submodule is never present.
     - Docs CI initializes only root-declared submodules, so it sees Docs' own Platform pin, not each module's nested `references/Hexalith.Platform`.
  2. **The Dapr source is ambiguous.** "Dapr … from the Builds catalog the checkout pins" has two candidates for blocks run through `hexalith-module`:
     - the module's own Builds gitlink, which CiCd's nightly lockstep moves;
     - the catalog pinned by the Platform identity, which Platform AD-4 says the tool uses and enforces in package mode.

     Addendum §B.5 already records them differing: `dc225a69` gives 1.19.1/1.19.1, while `2c33b2d7` gives CLI 1.19.1 and runtime 1.19.2. This is the disagreement AD-13 claims to prevent.
  3. **Docker-in-Docker isn't exact.** FR-5 requires exact Docker-in-Docker pins, but Stack lists the feature as `4`, a major only. Its upstream isn't named.
  4. **"SDK matches `global.json`" is undefined.** The image tag carries `11.0`, while `global.json` says `11.0.100` with `latestPatch`.
- **Suggested fix:**
  - For any block run through Platform, take Aspire and Dapr from the Platform identity: the Platform submodule's `apphost.cs` and its pinned Builds catalog. Use the module's Builds gitlink only for blocks that don't use Platform.
  - Assign the check to Docs CI. Compare against Docs' Platform and Builds pins, and add a registry rule that each module's Platform gitlink equals Docs' Platform pin, or make it a migration-time check with recorded evidence.
  - Define the SDK comparison as major.minor plus feature band.
  - Pin features exactly, with the Docs template as their upstream.

### R-07 (high): AD-12 changes the wrong text, and the canonical entry-point baseline has no owner

- **Checklist:** 2, 1, 6
- **Location:** AD-12 Rule (line 126); capability map "Agent rules (FR-47 to FR-50, FR-63)" (line 272)
- **Issue:** The rule that stops a newcomer's agent ("If no permitted location exists, stop and report the missing baseline as a blocker") lives in each repository's own `CLAUDE.md`, `AGENTS.md` and `.github/copilot-instructions.md`. It appears at line 22 in Commons, Parties, PolymorphicSerializations and AI.Tools, outside the `hexalith-cicd` marker block. It doesn't live in `hexalith-llm-instructions.md`, which a fresh clone lacks.

  AD-12 changes only "AI.Tools' baseline". It names no canonical source for the normalized entry-point text, no propagation to 21 repositories plus the superproject, and no check that copies stay identical. Independent migration agents will word the exemption differently, breaking the "normalized text" contract. R-14 in the PRD is not mitigated until every copy changes. The owner of the FR-48 chain-check script is also unnamed.
- **Suggested fix:**
  - Name one canonical entry-point baseline file in AI.Tools.
  - Every migration copies it verbatim outside the marker block, and the exemption keys on the sentinel line `You are running a Hexalith quickstart.`
  - The FR-48 migration check, owned by a Docs script in `scripts/`, also verifies normalized equality of all three entry points with the canonical text at the pinned AI.Tools revision.

### R-08 (high): AD-11's republish path can't release Builds or McpCli packages

- **Checklist:** 1, 6, 7
- **Location:** AD-11 Rule (line 120); AD-3 (line 72); Delivery boundaries "Package page current" (line 257)
- **Issue:**
  - **Builds.** Builds' release rules (`release_version.py`, `builds` selection: `!(docs|test|style)`, matching CiCd AD-10) never release on any `docs` commit. A `docs(readme)` change in Builds therefore republishes nothing for `Hexalith.Builds.Evidence.Cli` and `Hexalith.Builds.Module.Cli`.
  - **McpCli.** Per Platform AD-11, stable `Hexalith.McpCli` versions come only from Platform's publication workflow after staging validation. McpCli's own pipeline publishes only prerelease tool versions.
  - **Effect.** FR-15 and launch gate 4 need all 101 IDs. An agent migrating Builds or McpCli has no compliant path and is pushed toward `fix:`, which AD-11 forbids.
- **Suggested fix:** Add explicit paths:
  - **Builds:** the README change ships with the next releasing Builds commit, or a `docs(readme)` patch rule for the `builds` selection is added as a CiCd AD-10 amendment.
  - **McpCli:** the `Hexalith.McpCli` page is verified after the next Platform publication, and `Hexalith.McpCli.Abstractions` follows the module rule.

  Record the expected path per registry row, for example in a `republishPath` field or a ledger note.

### R-09 (medium): The new-rule grace period lasts as little as one night

- **Checklist:** 2
- **Location:** AD-8 Rule, last sentence (line 102)
- **Issue:** "A new rule reports as a warning … for one Builds minor release before it can fail." CiCd's nightly auto-bump (AD-10, AD-18) moves every module to the newest acceptable tag each night, and Builds releases on every non-docs commit. Two minors in a week give a grace of hours. Delivery-wait then fails the night when a fail-mode module turns red. The rule also needs per-rule metadata that no AD defines.
- **Suggested fix:** New rules ship in Builds with a per-rule warn-only flag. A separate, explicit Builds change removes the flag only after the Docs weekly report shows zero findings for that rule in every fail-mode repository, or after a fixed recorded date. This matches PRD §8.5 ("then starts failing in a later release").

### R-10 (medium): The suppression document has no defined shape, schema, granularity or rule ID

- **Checklist:** 1, 2
- **Location:** AD-8 Rule (line 102); seed `.github/hexalith-docs.json` (line 229)
- **Issue:**
  - **Shape and schema.** Only the entry fields `{file, rule, reason}` are fixed, not the top-level structure. Builds reads this file, so the CiCd Schemas convention applies: a required `schema: "hexalith.<name>.v<N>"` and a Builds schema file.
  - **Granularity.** File plus rule would suppress *every* planning-content finding in a file. FR-46 and addendum §B.2 allow only the 40-hex SHA pattern, and only for pinned actions or submodules.
  - **Rule ID.** No planning-content rule ID exists. The standard folds it into D-LOCATION, and memlog line 51 cites D-ENFORCEMENT. Eligibility can't be keyed on an ID.
  - **Summary count.** FR-46's suppression count in the job summary has no home.
- **Suggested fix:**
  - Fix the shape as `{"schema":"hexalith.docs.v1","suppressions":[{"file","rule","match","reason"}]}` with `schemas/hexalith.docs.v1.json` in Builds.
  - Give planning content its own ID, for example D-PLANNING, and the SHA pattern a separate suppressible ID.
  - State that the job summary prints the suppression count.

### R-11 (medium): The standalone-caller contract is unspecified

- **Checklist:** 1, 2, 8
- **Location:** AD-6 Rule (line 90): "A standalone caller (Docs, BmadSkills, CiCd, `Hexalith/.github`) runs that script from a Builds checkout pinned to a release tag [ASSUMPTION]"; Inherited row "CiCd AD-20"
- **Issue:**
  - **CLI isn't public API.** The `docs_check.py` CLI (`--root`, `--mode`, `--repository`) isn't Builds public API. CiCd AD-10 lists only the `check.py` command line, so a Builds minor can break four callers.
  - **Pin mechanism.** It is unstated whether callers pin by gitlink or by checkout ref, and who bumps the pin.
  - **Docs' own pin.** Docs' Builds pin (`6b6eb4ee`, v6.3.1-10) isn't a release tag and has no `docs_check.py`. `documentation.yml` runs with `submodules: false`, and `docs/development.md` documents a command that fails at that pin.
  - **Hexalith/.github.** Under CiCd AD-2 there is no generic way to judge `profile/README.md` and the community files with skeleton rules off (FR-25, FR-59).
  - **CiCd.** If CiCd places the check inside its delivery-gating global checks, a README finding blocks delivery to all 17 modules.
  - **Coverage holes.** BmadSkills (external checkout) and `Hexalith/.github` (not a Docs submodule) are never judged by Docs CI registry rules. Only the non-gating weekly report sees them.
- **Suggested fix:**
  - Add the `docs_check.py` CLI to Builds' public API as a CiCd amendment, including generic page-set and rule-profile options such as `--pages` and `--profile organization`.
  - Standalone callers pin Builds by gitlink at an acceptable tag, and the repository owner bumps it.
  - CiCd runs its own docs check outside the delivery-gating checks.
  - State the BmadSkills and `.github` coverage as an accepted gap, or add a gating path.

### R-12 (medium): The operational envelope for the weekly job, Docs pins and commit lint is missing

- **Checklist:** 8, 3
- **Location:** AD-7 (line 96), AD-14 (line 138), Deferred "Weekly-job keepalive" (line 286), Consistency "Commits" (line 181), Structural seed `documentation.yml` (line 217)
- **Issue:**
  - **Weekly report.** It has no schedule and no output channel ("publishes one report in Docs": a commit to `main`, an issue or a job summary?). Its job permissions are unstated. It has no token for lychee and GitHub API reads (addendum §B.2 notes HTTP 429 without one), no failure signal or triage owner, and no retention. If GitHub disables the schedule, nothing detects it, and FR-45's external checks stop silently.
  - **Docs pins.** Docs CI judges registry rules only at Docs' pinned submodule revisions, but no AD sets pin-bump cadence or ownership. A module's change can turn Docs red at bump time with no stated triage owner.
  - **Commit lint.** Docs, BmadSkills and `.github` aren't managed by CiCd and have no commitlint config (Docs has none tracked). The "validated by the owning repository's pinned commit lint" convention can't be met there.
- **Suggested fix:** Add an Operations subsection:
  - a weekly cron (UTC)
  - `permissions: contents: read`, plus `issues: write` if the report is a rolling issue
  - one rolling issue, or an artifact plus job summary, owned by the Docs maintainer
  - `GITHUB_TOKEN` passed to lychee
  - a last-run-age check in Docs CI, as in CiCd's 26-hour check, instead of relying on activity
  - a Docs pin-bump cadence and owner, with bumps through a PR that runs Docs CI
  - standalone repositories running Builds' commitlint config from their pinned Builds checkout

### R-13 (medium): AD-10 departs from the PRD and templates without recording it, and is ambiguous for Platform-root modules

- **Checklist:** 5, 1, 8
- **Location:** AD-10 Rule (line 114)
- **Issue:**
  - **Setup command.** FR-6 ("Run `aspire run`"), FR-20, FR-23, the glossary "Setup command", D-QUICKSTART ("starts Aspire") and `templates/quickstart-prompts.md` all say `aspire run`. AD-10 prescribes `dotnet tool run hexalith-module -- run --manifest …` for modules. The memlog lists this as a PRD update to offer, but the spine doesn't record the amendment, and agents copying the template will diverge.
  - **Dev container.** For EventStore, Memories and McpCli, the Rule says both "opens the repository dev container" and "start from a Platform checkout", so it's unclear whose dev container is used.
  - **Preconditions.** The reserved-block condition omits two prerequisites:
    - `hexalith-module` in `.config/dotnet-tools.json`, which is absent in Agents, McpCli, Memories, Projects and Tenants;
    - a direct `references/Hexalith.Platform`, which Platform AD-4 requires.
- **Suggested fix:**
  - State that business-module "Run it" uses `hexalith-module run` and that only Platform uses `aspire run`. Record the PRD, standard and template amendment.
  - EventStore, Memories and McpCli "Run it" open the Platform dev container.
  - Add both missing preconditions to the reserved-block rule.

### R-14 (medium): The Inherited invariants table mixes inherited facts with pending amendments

- **Checklist:** 7
- **Location:** Inherited table (lines 39–52)
- **Issue:**
  - **Pending amendments shown as facts.** The CiCd AD-12 row ("docs check runs in stage 1; README sample runs from the `after-unit-tests` hook") and the AD-15 row (`check.py` runs the docs check) aren't in the parent spine. Memlog line 57 lists them as amendments for the CiCd maintainer, along with the commitlint scope ban. Only the AD-10/16/17 row says "Amendment pending".
  - **Rows that extend their source.** The CiCd AD-11 row extends a Builds/CiCd rule to Docs tooling. The Platform AD-11 row is stronger than its source (see R-04).
  - **Omitted owned paths.** The CiCd AD-4 and AD-7 row omits CiCd-owned `.claude/settings.json` `permissions.deny`, the Builds `.gitmodules` section and the commitlint `absent-glob` paths.
- **Suggested fix:** Split the table into "Inherited as written" and "Requires parent amendment", with owner and status. Complete the owned-path list.

### R-15 (medium): There is no register of open questions and upstream amendments

- **Checklist:** 8, 6
- **Location:** The document as a whole (only Deferred exists, lines 276–289)
- **Issue:** The spine creates PRD deviations without surfacing them:
  - AD-7 checks only self-links per commit. FR-45 says every run checks internal links across the organization.
  - Under AD-6, registry-rule findings don't turn a module's `main` red, unlike FR-42 and the glossary's fail-mode consequence.
  - The setup command differs from FR-6, FR-20 and FR-23 (R-13).
  - FR-33 assumes Contributor Covenant 2.1, while Stack says 3.0.
  - FR-41 names markdownlint-cli2 and lychee in the docs check, which the spine drops.
  - FR-54's "docs check reports changes to Quickstart sections" has no owning unit.
  - The CiCd amendments in R-01, R-08, R-09 and R-11 aren't listed.
- **Suggested fix:** Add an "Upstream amendments and open questions" section. Give each item an owner (PRD, standard, CiCd, Builds) and a needed-by date.

### R-16 (medium): The README's machine-checkable contract isn't fixed

- **Checklist:** 1
- **Location:** Consistency conventions (lines 171–185); AD-8; seed `README.md # checked page (D-README)`
- **Issue:** The Builds checker, the templates, the AI.Tools rules and 21 migrations must agree on several things the spine leaves open:
  - exact heading text and levels (the template uses `##` sections and `###` blocks; the pilot uses `## Quick Start`)
  - H1 title handling
  - how "Start here" lists are recognized
  - where a quickstart block ends, for the 30-line limit
  - the prompt fence's identity

  FR-9 marks fixed heading text an [ASSUMPTION] and leaves it to the standard, but no artifact is named as authoritative for the strings.
- **Suggested fix:** Add a conventions row: heading strings and levels are those in `templates/readme.md` (authoritative, verbatim; H1 title, H2 sections, H3 blocks). Blocks end at the next H2 or H3. Prompts use the distinct fence from R-05.

### R-17 (low): AD-7's self-link remapping is incomplete

- **Checklist:** 2
- **Location:** AD-7 Rule (line 96)
- **Issue:** Only `https://github.com/Hexalith/<self>/blob/main/` is resolved offline. READMEs must use absolute images, typically `https://raw.githubusercontent.com/Hexalith/<self>/main/…`, and may use `/tree/main/` links. Broken self-images and self-trees would pass per commit.
- **Suggested fix:** List every remapped prefix: `blob/main/`, `tree/main/`, `raw.githubusercontent.com/Hexalith/<self>/main/`, and `#fragment` on each.

### R-18 (low): Brownfield contradictions and an unnamed Dapr home

- **Checklist:** 5
- **Location:** Conventions "Tooling"; AD-4, AD-12, AD-13; Structural seed
- **Issue:**
  - `docs/development.md` says "Python 3.11 or later", while the spine requires 3.12.
  - The same page runs `references/Hexalith.Builds/Github/lib/docs_check.py`, which is absent at Docs' Builds pin.
  - `templates/quickstart-prompts.md` lacks the AD-12 sentinel line and uses `aspire run`.
  - `tools/stranger-test.py` and addendum §B.5 use `HEXALITH_DAPR_HOME` and `~/.hexalith`, but AD-4 and AD-13 say only "one Dapr home". The dev container template, Platform tool and kit could choose different variables (`DAPR_RUNTIME_PATH`, `--runtime-path`).
- **Suggested fix:** Ratify `HEXALITH_DAPR_HOME` in the conventions. List the brownfield files that must change with the spine (development guide, prompt templates, Docs Builds pin).

### R-19 (low): ADs overlap

- **Checklist:** other (redundancy)
- **Location:** AD-2 compared with AD-6, AD-7 and AD-8; AD-3 compared with AD-9 and AD-11; AD-4 compared with AD-13
- **Issue:**
  - AD-2 restates local and CI parity, offline per-commit checks and warn-to-fail promotion. AD-6, AD-7 and AD-8 state them more precisely, and AD-2's wording ("Promote each pilot") is narrower than FR-42.
  - AD-3 restates the sample and README release rule.
  - AD-4 and AD-13 both fix the pin sources and "one Dapr home".

  Agents may cite the weaker wording.
- **Suggested fix:** Keep the ADOPTED IDs, but trim AD-2, AD-3 and AD-4 Rules to what later ADs don't say. Alternatively, add "Refined by AD-n" and make the later AD authoritative on conflict.

### R-20 (low): Rationale and seed leak into rules

- **Checklist:** other (rationale, seed)
- **Location:**
  - AD-1: "JSON can be read with the Python standard library"
  - Conventions "Links": "because NuGet renders no relative links"
  - AD-9: "pilot scripts are prototypes and retire once the tool ships", which is transition, not invariant
  - AD-3 and AD-4: evidence-recording sentences that duplicate FR-56 and the "Evidence" convention
  - AD-5: mostly a human delivery gate, duplicating "Delivery boundaries"
- **Suggested fix:** Move the rationale to the memlog. Move evidence fields to Conventions. Consider moving AD-5 into Delivery boundaries and keeping only its invariant: item-level findings never enter a public file.

### R-21 (low): Diagrams are syntactically valid but semantically off

- **Checklist:** other (diagram validity)
- **Location:** Dependency diagram (lines 144–154); flow diagram (lines 158–169); seed diagram (lines 234–248)
- **Issue:** All three `flowchart` blocks are syntactically valid on inspection: node IDs, bracketed labels with `/`, `:` and `,`, edge labels and the subgraph. Semantic problems:
  - The legend says arrows mean "reads or runs", but `CiCd -->|writes perimeter files only| Module` is a write.
  - `Module -->|runs pinned checker and sample tool| Builds` encodes R-01.
  - The weekly report's reads of live default branches and badge hosts aren't drawn.
  - In the seed, `ModCI -->|dispatched release| NuGet` is wrong: releases come from module `release.yml`, dispatched by CiCd nightly, not from CI.
  - `ModCI --> Sonar` encodes R-03.
- **Suggested fix:** Correct the legend or the edge. Draw the release via CiCd nightly and module `release.yml`. Add `Weekly --> Module live main`. Redraw the sample and Sonar edges after R-01 and R-03 are resolved.

### R-22 (low): Version evidence gaps

- **Checklist:** 4
- **Location:** Stack (lines 189–201)
- **Issue:**
  - The dev container features are listed as majors (`docker-in-docker 4`, `python 1`). The memlog's exact 4.1.3 and 1.8.1 date from 11 November and weren't re-verified on 21 November.
  - `actions/checkout v7.0.1 (3d3c42e5…)` has no memlog version entry. It is evidenced only by the CiCd spine Stack and the existing workflow.
  - No version or installer is fixed for the Aspire CLI or Dapr CLI inside the dev container, or for the SonarQube scanner.
  - The Builds release row is a placeholder, which is acceptable while untagged; v6.4.4 is the latest tag and doesn't contain `aaf27a2c`.

  Confirmed current: SDK 11.0.100 (every module `global.json` checked), Aspire 17.0.0 (Platform `apphost.cs`), Dapr runtime 1.19.2 and CLI 1.19.1 (Builds main `Props`), the base image, lychee v0.24.2, ubuntu-24.04 and Contributor Covenant 3.0.
- **Suggested fix:** Pin exact feature versions and re-verify them. Add a memlog version entry for actions/checkout. Add installer and version rows for the Aspire and Dapr CLIs and the Sonar scanner, or defer them explicitly.

### R-23 (low): Deferred items leave ownership windows

- **Checklist:** 3
- **Location:** Deferred "Guard protection of dev container files and agent entry points" (line 287); "Legacy SonarQube Cloud projects" (line 288)
- **Issue:**
  - If CiCd later brings `.devcontainer/` or entry points into its perimeter (OQ-19), dev containers and exemption text written by module agents under AD-12 and AD-13 become drift that the guard overwrites.
  - The legacy-Sonar deferral leaves registry keys and badges unstable (see R-03).
- **Suggested fix:** State the interim owner (module) and that a CiCd perimeter decision supersedes it, with the migration path. Tie the Sonar deferral to the R-03 decision.

### R-24 (low): Capability map rows cite governance that doesn't govern

- **Checklist:** 6
- **Location:** Capability map (lines 262–274)
- **Issue:** Several rows cite the wrong governance, and some FR consequences have no governing AD:
  - "Community files and contributor docs" cites D-COMMUNITY, a rule ID rather than an AD. The local-CONTRIBUTING check under FR-34 belongs to the checker (AD-6, AD-8).
  - FR-36 ("an agent following only the development guide builds and tests green") has no governing AD.
  - FR-40 (R-03), FR-54 (R-15) and the FR-15 republish of Builds and McpCli (R-08) are uncovered in practice.
  - FR-48's chain-check script has no owner (R-07).
- **Suggested fix:** Cite ADs only, and add the missing ones or open questions noted above.

## Capability map coverage (FR-1 to FR-66)

| FR range in map | FRs | Covered | Governance gap |
| --- | --- | --- | --- |
| FR-1 to FR-8, FR-62 | 9 | Yes | none |
| FR-9 to FR-16, FR-60 | 9 | Yes | FR-15 for Builds and McpCli (R-08); legacy package READMEs (R-04) |
| FR-17 to FR-22 | 6 | Yes | FR-20 setup command (R-13) |
| FR-23, FR-24, FR-66 | 3 | Yes | none |
| FR-25 to FR-32, FR-65 | 9 | Yes | front door check path (R-11) |
| FR-33 to FR-37, FR-59 | 6 | Yes | FR-36 has no AD (R-24) |
| FR-38 to FR-40 | 3 | Yes | FR-40 has no AD (R-03) |
| FR-41 to FR-46, FR-64 | 7 | Yes | FR-46 summary count (R-10) |
| FR-47 to FR-50, FR-63 | 5 | Yes | FR-48 check owner, entry-point text (R-07) |
| FR-51 to FR-56, FR-61 | 7 | Yes | FR-54 change report (R-15) |
| FR-57, FR-58 | 2 | Yes | none |
| **Total** | **66** | **66 of 66** | |

## What already works

Keep these.

- The determinism split works. Module CI judges only the checkout. Docs CI judges registry rules at its own pins. The weekly report reads live state and never gates.
- Standard-library Python, and keeping markdownlint off the per-commit path, ratify CiCd AD-11 and the existing Builds checker.
- The ADOPTED tags on AD-6 (prepare phase, knob, `check.py` parity), the finding line `{file, line, rule, hint}` and the `docs(readme)` patch rule match Builds `origin/main` exactly. Evidence: `docs_check.py`, `ci_pipeline.check_documentation`, `local_check.py`, `schemas/hexalith.ci.v1.json` (`docs: off|warn|fail`, default `warn`) and `release_version.py`.
- The registry conventions match `docs/module-registry.json` and `scripts/validate_registry.py`: `schemaVersion` 1, 21 rows, `confirmed`/`proposed`/`unconfirmed`, nulls for unknowns.
- AD-10's reliance on v2 manifests matches the checkouts. The v2 manifest is present in Agents, Conversations, EventStore, McpCli, Memories, Parties, Projects and Tenants, and absent in ChatBot, Folders, FrontComposer, Timesheets and Works.
