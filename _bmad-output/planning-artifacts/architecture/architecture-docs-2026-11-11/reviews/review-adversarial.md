# Adversarial review of the documentation architecture spine

- **Spine:** `ARCHITECTURE-SPINE.md` (updated 2026-11-21), AD-1 to AD-14 plus inherited invariants
- **Lens:** construct two units one level down that obey every AD to the letter and still build incompatibly; flag Rules that can be satisfied while their Prevents still happens
- **Inputs read:** spine, `.memlog.md`, `epics.md` (36 stories), `docs/documentation-standard.md`, `docs/module-registry.json`, `templates/*`, `scripts/*.py`, `tools/stranger-test.py`, launch ledger, exposure review, CiCd spine AD-3/AD-4/AD-10/AD-17/AD-18, Builds `Github/lib/docs_check.py` at `2c33b2d7`, entry points and tool manifests in the pinned `references/*` checkouts
- **Date:** 2026-11-21

## Verdict

**Not yet safe for 21 parallel agents.** The spine names an owner for every repository, but it does not say who writes the shared state the repositories converge on: registry rows, ledger rows, entry-point text, release start and fail-mode promotion. Two data shapes are also left open: the sample/prompt fence grammar and the finding/suppression envelope. The review finds 5 critical, 11 high, 6 medium and 1 low hole. Twelve ADs can be satisfied while their Prevents still happens (see the table at the end).

## Critical

### H-01 Registry rows have no write path during parallel migrations

- **Units:** Tenants migration (3.19) adds `docs/development.md`, `docs/operations.md`, `.devcontainer/devcontainer.json` and a Sonar badge. Memories migration (3.15) changes a `PackageReadmeFile` mapping. Agents migration (3.8) is told to "Confirm its category". Story 1.2 maintainer confirms descriptions at the same time.
- **How they diverge while complying:** AD-1 makes Docs the owner of one registry, but no AD says who changes a row, when, or in which commit relative to the module's gitlink. Agent A opens a Docs PR that sets `development: "docs/development.md"` before the gitlink advances, so `validate_registry.py --check-sources` fails because the file is missing at the pinned revision. Agent B advances the gitlink without touching the row, so the Docs CI registry rules flag the new README facts, for example a Sonar badge while the row has `sonarKey: null`. Agent C, executing "Confirm its category", writes `categoryStatus: "confirmed"` itself. AD-1 only requires the statuses to be *distinguished*, so an agent can produce the unconfirmed public claim AD-1 exists to prevent. All three agents re-serialize a 739-line JSON file, which causes whole-file conflicts.
- **ADs:** AD-1, AD-6, AD-14.
- **Proposed rule:** A module's registry row changes only in the Docs commit that advances that module's gitlink to a revision on its `main`, formatted by one Docs serializer that Docs CI enforces. Only a maintainer's commit sets a status to `confirmed`, and Docs CI requires `confirmedBy` (role) and `confirmedOn` beside every confirmed value.

### H-02 Docs CI can gate every Docs commit on every module's conformance, and no AD sets a per-row mode

- **Units:** The Docs half of Story 2.1, which implements the registry rules (verbatim description, quickstart order, package IDs and counts, badge sources, Sonar key), against every other Docs-side story: 1.2 confirmations, 4.1 ledger, 6.3 Conversations pin, and each gitlink advance from H-01.
- **How they diverge while complying:** AD-6 says Docs CI "owns" these rules and judges the pinned revisions. It does not say whether a finding fails Docs CI.
  - **Implementer X gates.** Docs turns red on its first merge because 19 unmigrated READMEs fail the verbatim-description and quickstart-order rules, and every Docs PR is blocked. Agents can then turn it green only by editing the registry to match the README, which reverses AD-1's authority, or by leaving gitlinks behind. Confirming a new description also turns Docs red until the module changes and Docs advances its gitlink, which is circular.
  - **Implementer Y only reports.** The registry rules then never gate anything, and D-IDENTITY drift becomes permanent.
- **ADs:** AD-6, AD-1, AD-2.
- **Proposed rule:** Docs CI fails a registry-conformance finding only when two conditions hold: the row's module runs `docs: fail` in the `hexalith-ci.json` at its pinned gitlink (for standalone callers, the mode their committed caller passes), and the Docs commit changes that row or that gitlink. Every other registry finding reports without failing.

### H-03 AD-12's exemption sits in a file that a fresh clone lacks, and entry points have three writers

- **Units:**
  - AI.Tools migration (3.4) against a newcomer's agent in a fresh module clone.
  - Story 2.3 (owners "AI.Tools, CiCd and maintainers": "Install short rule-ID guidance") against 3.4 ("Make the short documentation rules reachable from the three agent entry points") against each 3.x migration agent.
- **How they diverge while complying:**
  - **The exemption is in the wrong file.** The halting sentence ("If no permitted location exists, stop and report the missing baseline as a blocker") is in the shared entry-point text of every repository. It appears in 32 `AGENTS.md`/`CLAUDE.md` copies under `references/` and does not appear in `hexalith-llm-instructions.md`. AI.Tools can add the exemption to its baseline exactly as AD-12 says, yet a newcomer's agent reads `CLAUDE.md` first, finds no baseline and halts. The Prevents happens.
  - **Three writers.** AI.Tools could edit the baseline. CiCd could use its marker block, which reaches 17 managed repositories. Every migration agent may edit the entry points, because AD-12 only forbids edits *inside* the marker. That produces 21 paraphrases and breaks the "normalized text" invariant the entry points themselves state.
- **ADs:** AD-12, CiCd AD-4.
- **Proposed rule:** The quickstart exemption and the pointer to the documentation rules live in the normalized entry-point text that AI.Tools authors. Each repository adopts that text byte for byte, and Docs CI compares the pinned copies with AI.Tools' pinned source. Documentation rules reach agents only through `hexalith-llm-instructions.md` (or a topical file beside it), never through the CiCd marker block or module-local text, and migrations do not otherwise edit entry points.

### H-04 Nightly dispatch releases every merged `docs(readme)` commit, although AD-5 says the owner starts a release

- **Units:** The Commons migration agent, which merges several `docs(readme):` fix-ups over two days, against CiCd nightly (CiCd AD-18), which dispatches `release.yml` for every adopted module at 02:17 UTC. Story 2.2's "Exercise docs-only release selection" adds to the problem.
- **How they diverge while complying:** Every merged `docs(readme)` commit produces a patch release that night. Unreviewed README text reaches nuget.org, the ledger's "verified republish" target moves every day, and each patch also carries any accumulated commits that do not release on their own (`build:`, `refactor:`, `build(deps):`). AD-5 is satisfied to the letter, because nobody started a release by hand, but the owner gate it describes is gone. AD-11's instruction to "dispatch a republish" assumes a manual dispatch that does not exist.
- **ADs:** AD-5, AD-11, AD-3, CiCd AD-18.
- **Proposed rule:** Merging a `docs(readme)` commit to `main` counts as starting the release. It lands only as one squashed commit in a PR the module owner approves after review, and all intermediate migration commits use `docs:`. The release record lists any non-docs commits the patch carries, and the owner accepts them.

### H-05 The checker must judge "every package README the registry assigns" but "never reads the registry"

- **Units:** Builds checker (2.1) against Memories (3.15), Conversations (3.10) and FrontComposer (3.13). The same gap affects each publisher's sample hook (AD-9 lets the hook pass the README paths).
- **How they diverge while complying:** The checker at `2c33b2d7` scopes package READMEs by a heuristic: a `README.md` beside a `.csproj` under `src/libraries`. That is the only way to honour both AD-6 and AD-8. The registry, however, assigns 13 package READMEs under `src/<Project>/` (Memories 10, Conversations 1, FrontComposer 2). Those READMEs are never judged, even after the module moves to fail mode. Under AD-9, the Memories hook can pass only the root README to the tool, so the samples in its package READMEs never run, which is the "displayed sample that no test runs" AD-9 prevents.
- **ADs:** AD-6, AD-8, AD-9, AD-3.
- **Proposed rule:** The checked package README set is the `PackageReadmeFile` of each packable project in the checkout. The checker and the sample tool both derive the set from there: the tool takes only the package directory and reads each nuspec `readme` entry. Docs CI checks that the registry's `projectReadmes` equals that set.

## High

### H-06 The registry cannot express a reserved "Run it" block

- **Units:** The Docs CI quickstart-order rule against these migrations:
  - Timesheets (3.20), Folders (3.12) and FrontComposer (3.13), which have no v2 manifest but list "Run it" in the registry.
  - ChatBot (3.9), whose manifest is `module/build.module-manifest.v2.json`, not the literal path in AD-10.
  - Tenants and Parties, which have manifests but whose operations McpCli does not yet serve (Platform stories 3.4 to 3.8).
  - Agents, which has a manifest while the registry omits "Run it".
- **How they diverge while complying:** `quickstarts` is a flat list, and the PRD treats a listed "Run it" as a reservation. A Docs CI implementer who requires the README blocks to equal the list turns about 10 rows red, or pushes agents to publish "Run it" to pass, which violates AD-10. The ChatBot agent can rename the manifest, use a non-literal path, or reserve the block. AD-10's condition (a manifest exists and McpCli serves the operations) is not D-QUICKSTART's condition (the block meets its time target), so an agent can publish a block that was never timed.
- **ADs:** AD-10, AD-6, D-QUICKSTART.
- **Proposed rule:** Each registry quickstart entry carries `status: published|reserved`, and the README blocks must equal the published entries in order. Only a Docs maintainer changes `reserved` to `published`, citing the ledger qualification. The "Run it" manifest path is exactly `module/hexalith.module-manifest.v2.json`.

### H-07 The warning grace is counted in Builds minors, and widened rules get none

- **Units:** A Builds agent that adds a rule, or that widens scope as AD-8 requires (from the pilot subset to registry-assigned READMEs and linked docs pages) or as the PRD's pattern tuning requires, against CiCd nightly auto-bump (CiCd AD-10, AD-18) and the pilots already in fail mode.
- **How they diverge while complying:** Builds releases a minor on any `feat` and is dispatched every night, and the auto-bump moves every module to the newest acceptable tag. The grace therefore lasts about one night. A module whose delivery was held (by `builds-skip` or a red delivery) jumps from N-1 to N+1 and gets no grace at all. A change to an *existing* rule, such as a wider scope or a tuned pattern, is not a "new rule", so it turns the pilots red on delivery, and a red `main` halts their releases (PRD glossary). The rule is satisfied and the Prevents still happens.
- **ADs:** AD-8, AD-2.
- **Proposed rule:** Any Builds change that can add findings, whether a new rule, a new pattern or a wider page scope, emits level `warning` in fail mode. A later, separate Builds change flips it to blocking, made no sooner than 14 days after the first delivery that reported it.

### H-08 A finding cannot say whether it blocks, Docs CI findings have no repository base, and D-BADGE has two implementers

- **Units:** Builds checker, `check.py` locally, AI.Tools guidance and the Docs CI registry rules.
- **How they diverge while complying:** In fail mode, a finding on a report-only page, a finding in its grace period and a suppressed finding all print the same four-key line. Agents then either fix pages that are out of scope or add suppressions to silence them, and the summary cannot show the suppression count that FR-46 requires. A Docs CI implementer can emit `file: "references/Hexalith.Tenants/README.md"` or `file: "README.md"`, and a module agent cannot map either reliably. D-BADGE is judged by the checker (the workflow target exists) and by Docs CI (the badge source matches the registry), and the two may treat suppressions differently. AD-6 lists "two implementations of one rule" as a Prevents, yet D-BADGE has two by design.
- **ADs:** AD-8, AD-6.
- **Proposed rule:**
  - Every finding adds `level` (`error`, `warning`, `report` or `suppressed`), computed only by the emitter.
  - Docs CI findings set `file` relative to the Docs root (`references/<Repo>/…`).
  - A new "Checked by" column in the standard names exactly one implementer per rule ID, and a rule split across checkers gets two IDs.

### H-09 The suppression shape lets an agent silence a whole rule

- **Units:** Builds checker (parser), 21 migration agents (writers) and AI.Tools rules (instructions).
- **How they diverge while complying:** The file envelope is undefined: one agent can write a bare array, another `{"suppressions": [...]}`, another a versioned object. Entries carry no line and no match, so `{file: "README.md", rule: "D-LENGTH"}` lifts the 150-line cap for good. "Planning-content" is not a rule ID. The PRD addendum allows a suppression only for the 40-hex SHA pattern, but the checker cannot tell that pattern from any other D-LOCATION finding. A suppression whose reason says "pinned action SHA" therefore silences all planning content in the file. The rule is satisfied and the Prevents still happens.
- **ADs:** AD-8, D-ENFORCEMENT.
- **Proposed rule:** `.github/hexalith-docs.json` is `{schemaVersion: 1, suppressions: [{file, rule, match, reason}]}`, and unknown keys fail. `match` is the exact offending text and is mandatory. Only the planning rule's 40-hex SHA pattern and a reviewed D-LENGTH section exception accept a suppression, and the CI summary prints the suppression count.

### H-10 New rule IDs reach modules before the catalog sees them

- **Units:** A Builds agent who adds `D-X` to the checker, CiCd nightly, which delivers it within a day, and the Docs test of AD-8. That test runs only when Docs advances its own Builds gitlink, which today is `6b6eb4ee`: not a tag, and without `docs_check.py`.
- **How they diverge while complying:** Modules emit `D-X` for weeks while the table lacks it, which is the undefined rule ID AD-8 prevents. In the opposite order, the table gains an ID that nothing emits. The same timing gap applies to AI.Tools.
- **ADs:** AD-8.
- **Proposed rule:** A rule ID enters the Docs table before any Builds or AI.Tools change emits it. Docs keeps its Builds gitlink at exactly the tag that its pinned CiCd `builds-version` names, and Docs CI fails when the two differ.

### H-11 The sample grammar is under-specified

- **Units:** Builds sample tool (2.2) against three groups:
  - The PolymorphicSerializations pilot (3.2). Its "two displayed fences" produce one result: a model fence with no output, then a usage fence.
  - Commons.UniqueIds, whose sample prints generated IDs.
  - Every migration that copies `templates/quickstart-prompts.md`, where prompts are ` ```text ` fences "directly below the reader's manual steps".
- **How they diverge while complying:**
  - The tool pairs each `csharp` fence with the next `text` fence. The serialization model fence has none, so the agent either inserts an empty `text` block, which confuses readers, or merges the fences.
  - A prompt placed below the manual steps is read as expected output.
  - Nondeterministic output (ULIDs, timestamps) leads 21 agents to invent 21 placeholder syntaxes (`<ulid>`, `...`, regular expressions), or to stop printing, which breaks "a sample prints its documented result".
- **ADs:** AD-9, D-PROMPT.
- **Proposed rule:** A sample is a run of consecutive `csharp` fences, concatenated in order into one program and closed by one `text` output fence. Prompts use the fence info string `prompt`, never `text`. Samples print only deterministic values: for a generated ID, print a derived check such as `True`. The comparison normalizes only line endings and trailing whitespace.

### H-12 The consumer's package resolution is not fixed

- **Units:** Builds sample tool against Commons, EventStore and every publisher README, with or without `--version` on the install line.
- **How they diverge while complying:** CI-packed packages carry a MinVer prerelease version. `dotnet add package X` without `--prerelease` skips that version and, with nuget.org enabled, restores the last *published stable* package. The test then goes green against old bits, which is exactly the "green tests concealing an unusable README" AD-3 prevents. If the tool instead references every package in the folder, a README that names the wrong package still passes. If a README pins `--version 3.0.1`, each `docs(readme)` release makes that line stale.
- **ADs:** AD-3, AD-9.
- **Proposed rule:** The consumer references exactly the package IDs named by the block's `dotnet add package` lines, at the locally packed version. Package source mapping routes this repository's IDs to the local feed only. README install lines carry no version.

### H-13 Warn-to-fail promotion has no owner, evidence or order

- **Units:**
  - A CiCd agent editing `setup/<Repo>.yml`, against a module migration agent and the Docs ledger.
  - Standalone callers (Docs, CiCd, BmadSkills, `Hexalith/.github`), which pass `--mode` in their own workflows.
- **How they diverge while complying:** AD-2 covers only the pilots, D-ENFORCEMENT says "after review and migration", and the PRD says a CiCd agent makes the switch. A CiCd agent can therefore batch-promote every repository after the pilots. Modules with open findings then go red on `main`, and nightly skips their *product* releases. A module agent cannot promote its own repository, so it may leave the module in warn indefinitely. Standalone callers promote whenever they like, outside CiCd AD-3.
- **ADs:** AD-2, D-ENFORCEMENT.
- **Proposed rule:** A CiCd commit sets `docs: fail` for one module only, citing the ledger record of maintainer acceptance and a hosted warn run with zero error-level findings at that module's current `main`. Standalone callers record their mode in the registry and need the same evidence.

### H-14 Several environment pins have no upstream in the checkout

- **Units:** Dev-container authors in 21 migrations, the Story 1.4 template, Platform's Dapr tooling and the Builds module tool.
- **How they diverge while complying:**
  - **(a) Module tool version.** `hexalith-module` versions are already 4.48.2 (ChatBot), 5.2.1 (EventStore), 6.2.0 (Conversations) and 6.3.0 (Parties, Platform). Repositories without a `.config/dotnet-tools.json` will add whatever is latest, so the "Run it" CLI differs from one repository to the next.
  - **(b) Base image tag.** The exact tag (`3.0.1-11.0-resolute`) exists only in the spine's Stack table, so no offline check can compare it, and the copies drift at the next image release.
  - **(c) Dapr home.** Platform uses `HEXALITH_DAPR_HOME` (about 590 occurrences). Agents will set `DAPR_RUNTIME_PATH` or run `dapr init` themselves.
  - **(d) Which AppHost.** In Tenants and Memories, `aspire.config.json` and the registry's `appHost` point at the *frozen module* AppHost. "The AppHost that runs the block" can therefore be read as that AppHost rather than Platform's `apphost.cs`.
  - **(e) Check timing.** The docs check runs before submodules are initialized (memlog), so D-PREREQUISITES cannot read Platform's AppHost.
- **ADs:** AD-13, AD-10, AD-4.
- **Proposed rule:** Every dev-container pin comes from one catalog entry at the pinned Builds tag: base image tag, features, Aspire CLI install, Dapr CLI and runtime, and a `hexalith-module` version equal to that tag. Dev containers set only Platform's `HEXALITH_DAPR_HOME`. The "Run it" Aspire version is the one in the Platform AppHost at the module's pinned `references/Hexalith.Platform`, and a Builds step that runs after submodule initialization compares it.

### H-15 The ledger is one hand-edited table with more than 21 writers

- **Units:** 21 migration agents ("Record agent run, review and republish evidence per row"), release maintainers, Stories 4.1 and 4.2 trials, the CiCd promotion from H-13, and the maintainer readability checklist (PRD: "[HUMAN] … records the result in the launch ledger").
- **How they diverge while complying:** Edits to adjacent rows in one Markdown table conflict in a three-way merge. The four columns cannot hold the FR-56 and D-EVIDENCE fields (model ID, tool version, prompt, accepted revision, run link), so each agent adds columns or prose sections in its own way. The stranger-test kit emits JSON with different keys. The "Hosted docs check" column duplicates the CiCd setup files and drifts from them.
- **ADs:** AD-5, Evidence convention.
- **Proposed rule:** Evidence lives in one file per registry repository, `_bmad-output/implementation-artifacts/ledger/<Repo>.json`, with a fixed schema that Docs CI validates. Trial records embed the kit's JSON as-is, and only maintainers write acceptance fields. The summary table is generated, and the docs mode is read from the pinned `hexalith-ci.json`, never typed.

### H-16 Migrations consume unpinned inputs that contradict the ADs

- **Units:** 21 migration agents against the Docs templates (1.3) and their own `references/Hexalith.AI.Tools` pins.
- **How they diverge while complying:**
  - The "Run it" prompt in `templates/quickstart-prompts.md` says "Run the README's aspire run command", and no template prompt opens with the fixed line.
  - The baseline tells agents to run `aspire run` before changing code. In Tenants and Memories, that starts the frozen module AppHost through `aspire.config.json`.
  - Module AI.Tools pins differ (`180ca569`, `3a4a78d9`, `7fdf2884`), so agents follow different documentation rules.
  - The migration prompt refers to "the Docs checkout" without a revision while the registry and templates keep changing.
- **ADs:** AD-10, AD-12, AD-8.
- **Proposed rule:** Each migration names the Docs commit and the AI.Tools revision it follows. It first advances its AI.Tools gitlink to the revision Docs pins, and records both revisions. Docs CI tests every template against the conventions: the fixed first line, the AD-10 command, and no `aspire run`.

## Medium

### H-17 Ownership of the organization profile is split

- **Units:** The Docs renderer (AD-14) against the organization maintainer (5.1 About data, 5.2 publishing the Try it link) and `Hexalith/.github`'s own docs check (AD-6 standalone caller).
- **How they diverge while complying:**
  - **Whole file or fragment.** If the renderer emits the whole `profile/README.md`, it overwrites the hand-placed Try it link. If it emits a fragment, the splice point is undefined, and the weekly report flags the hand edit as drift.
  - **Checker shape.** `.github` has no module-shaped root README, so the checker raises D-README, and AD-14 forbids fixing the rendered output by hand.
  - **Fetching.** No AD says how `.github` obtains the renderer without fetching Docs, which would break AD-2.
- **ADs:** AD-14, AD-6, AD-2.
- **Proposed rule:** The renderer writes only between `hexalith-docs` markers in `profile/README.md` and `CONTRIBUTING.md`, and `.github` runs it from a pinned Docs submodule. Standalone callers pass a committed page profile (`module`, `hub` or `org`) that selects which D-rules apply.

### H-18 Offline self-link resolution misses the links READMEs actually use

- **Units:** Builds checker against every migration that follows D-RENDER, which requires absolute image URLs on NuGet-trusted hosts.
- **How they diverge while complying:** Images at `raw.githubusercontent.com/Hexalith/<self>/main/…` and links to `tree/main/…` or `blob/<sha>/…` are self-links that the `blob/main` resolver ignores, so a broken self image passes on every commit. This is the AD-7 Prevents. Migration-time online checks have no shared tool, so 21 agents use curl loops, unpinned lychee or urllib, and private targets return signed-out 404s.
- **ADs:** AD-7, D-LINK.
- **Proposed rule:** The offline resolver treats `github.com/Hexalith/<self>/{blob,tree,raw}/main/` and `raw.githubusercontent.com/Hexalith/<self>/{main,refs/heads/main}/` as self-links, and flags a self-link to any other ref. Migrations run the weekly report's script in single-repository mode as their only online check.

### H-19 Badge workflow names and Sonar keys break on delivery

- **Units:** The Platform migration (3.17), whose registry row has `badges.workflow: "tuple-ci.yml"` and `ciOwnerTarget: "CiCd"`, against CiCd onboarding. The Tenants and Parties migrations act on D-BADGE's Sonar requirement while 19 rows have `sonarKey: null`.
- **How they diverge while complying:** CiCd's `whole-dir` rendering of `.github/workflows/` deletes `tuple-ci.yml`, so D-BADGE goes red in Platform on the delivery commit itself. The Tenants agent invents the key `Hexalith_Hexalith.Tenants` by copying the pilot pattern, which yields a 404 badge or a Docs CI mismatch. The Parties agent omits the badge. Sonar analysis is a CiCd workflow concern that neither agent can add.
- **ADs:** AD-6, AD-2, D-BADGE.
- **Proposed rule:** A managed module's CI badge names only the CiCd-rendered `ci.yml`, and the registry derives that from `ciOwnerTarget`. A README shows Sonar badges only when its registry `sonarKey` is non-null, which the Docs maintainer sets after CiCd delivers analysis.

### H-20 Enabling the sample hook spans two repositories

- **Units:** A publisher's migration agent, which writes `.github/actions/after-unit-tests`, against CiCd's `hooks` knob. CiCd AD-3 requires the action to exist on the module's live `main` before the knob is set.
- **How they diverge while complying:** The migration passes AD-9 locally, but the hook stays disabled, so the sample never runs in hosted CI. In a module that already has an `after-unit-tests` action (one per hook point), the agent may replace the existing action rather than add a step.
- **ADs:** AD-9, CiCd AD-3, CiCd AD-14.
- **Proposed rule:** A publisher reaches Level 1 only after a hosted run in which the sample tool executed. The migration lands the hook first, and the CiCd setup change that enables it cites that commit. An existing hook action gains the tool as one step and is never replaced.

### H-21 Legacy CLI and MCP package READMEs face contradictory rules

- **Units:** The Memories migration (3.15) receives two conflicting instructions. The registry assigns README files to `Hexalith.Memories.Cli` (`dotnet tool install --global Hexalith.Memories.Cli`) and `Hexalith.Memories.Mcp` (an MCP server), and D-PACKAGE says to respect package READMEs. Platform AD-11 says "No README documents a legacy module CLI or MCP host". EventStore's admin CLI tool raises the same question.
- **How they diverge while complying:** One agent keeps the usage blocks to satisfy D-PACKAGE. Another strips them to satisfy AD-11. Either way, the packages keep publishing, and their nuget.org pages differ in kind.
- **ADs:** Platform AD-11, AD-3, D-PACKAGE.
- **Proposed rule:** A package whose surface is a legacy module CLI or MCP host keeps a package README that states only its status, its retirement condition and the McpCli replacement, with no install or usage block. The registry marks the package `legacy`.

### H-22 The package inventory has three sources, and the verifier binds to the wrong revision

- **Units:** Registry `ids`/`count` (Docs), the module's `release-packages.json` (`inventorySource`) and the Builds release, which publishes every `IsPackable` project, against `verify_published_readmes.py`.
- **How they diverge while complying:**
  - **Inventory sources.** Builds' `inventorySource` is an HTTPS release-asset URL for v6.3.1, which needs the network and is stale. Commons, PolymorphicSerializations and ChatBot point at directories. A project that becomes packable during a migration is published without a registry row, so the ledger's "N of M" figure is wrong. AD-1's Prevents names the "package count", yet only descriptions and categories carry a status.
  - **Verifier revision.** The verifier compares nuget.org with `references/<Repo>` at Docs' pin, not with the release commit.
- **ADs:** AD-1, AD-3, AD-6.
- **Proposed rule:** The expected package IDs are the release's `hexalith-release-packages` trailer at the verified tag, and `inventorySource` is a repository-relative file checked offline. The verifier compares nuget.org READMEs with the blobs at the `v<version>` tag commit.

## Low

### H-23 The output form of the weekly report is open

- **Units:** The Docs weekly job (AD-7) against agents' Docs PRs.
- **How they diverge while complying:** "Publishes one report in Docs" can mean a bot commit that races open PRs and needs its own commit type and commit-lint pass, a rolling issue, or a workflow artifact.
- **ADs:** AD-7.
- **Proposed rule:** The weekly report is a workflow artifact plus one rolling issue in Docs, and it never commits.

## Rules that can be satisfied while their Prevents still happens

| AD | How the Rule holds while the Prevents occurs | Hole |
| --- | --- | --- |
| AD-1 | Statuses are distinguished, but an agent writes `confirmed`. The package count carries no status and is published anyway. | H-01, H-22 |
| AD-3 | The consumer restores the last stable package from nuget.org instead of the local prerelease. | H-12 |
| AD-5 | No owner starts a release by hand, and nightly dispatch releases each merged `docs(readme)` commit. | H-04 |
| AD-6 | Docs CI "owns" D-BADGE sources while the checker judges D-BADGE targets: two implementations of one rule. | H-08 |
| AD-7 | `raw.githubusercontent.com` self-images escape the offline resolver. | H-18 |
| AD-8 | The grace lasts one Builds minor, about one night. Scope widening gets no grace. A new ID ships before the table has it. A SHA-reason suppression silences all planning content. | H-07, H-10, H-09 |
| AD-9 | The hook picks which READMEs to run, and the hook is never enabled in CiCd. | H-05, H-20 |
| AD-10 | The README is correct, but the baseline and template still make the agent run `aspire run`, which starts the frozen module AppHost. | H-16 |
| AD-11 | The scope ban is enforced by CiCd commit lint, but its delivery is deferred (OQ-11) while all 21 migrations commit. | — (timing; sequence the 3.x migrations after delivery) |
| AD-12 | The exemption sits in the baseline, which a fresh clone lacks. The halting sentence sits in the entry point. | H-03 |
| AD-13 | SDK, Aspire and Dapr have upstreams, but the module tool version, the image tag and the Dapr home do not. | H-14 |
| AD-14 | The Try it link is added to the profile by hand and flagged as drift, or overwritten by the renderer. | H-17 |

## Evidence pointers

- Checker scope heuristic: Builds `Github/lib/docs_check.py` at `2c33b2d7`, function `readmes` (root README plus `src/libraries/**/README.md` beside a `.csproj`).
- Registry rows with package READMEs outside `src/libraries`: Memories (10), Conversations (1) and FrontComposer (2), in `docs/module-registry.json`.
- Halting sentence location: present in the `AGENTS.md`/`CLAUDE.md` entry points across `references/*` and absent from `references/Hexalith.AI.Tools/hexalith-llm-instructions.md`.
- `hexalith-module` versions: `.config/dotnet-tools.json` in ChatBot (4.48.2), EventStore (5.2.1), Conversations (6.2.0), Parties and Platform (6.3.0).
- Frozen AppHost default: `aspire.config.json` in Tenants and Memories points at `src/Hexalith.<Module>.AppHost`.
- Nightly release dispatch: CiCd spine AD-18 `dispatch`. Release halts on a red `main`: PRD glossary, "Warn mode / fail mode".
- SHA-only suppression intent: PRD addendum §B.2, "Candidate planning-content patterns".
- Template contradictions: `templates/quickstart-prompts.md` ("Run it" uses `aspire run`; no prompt opens with the fixed line).
