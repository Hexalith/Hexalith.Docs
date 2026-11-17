# PRD Quality Review — Hexalith Documentation Standard (prd-docs-2026-11-09)

## Overall verdict

This is a disciplined launch PRD. It has a real thesis: documentation, not code, stands between the public repositories and a launch, and because agents write the docs, the rules live where agents read them and CI catches the rest. The gate is honest ("the date moves"), each counter-metric defends a specific SM, and the glossary, IDs, and assumptions are clean. The risk is in execution. The enforcement design (per-repository workflow callers, a required status check, PR-based review) collides with the already-running Hexalith.CiCd initiative, which owns every module workflow and removes required status checks. The quickstart and stranger-test FRs that the launch gate rests on also contain a contradiction ("exactly one command"), an undefined test rig, a hidden launch gate, and an unsized `docs/` cleanup that the non-goals forbid. Resolve the CiCd ownership question and the seven high findings before handing this to epics-and-stories.

## Decision-readiness — adequate

What holds up: §1's "If the date and a working 'Try it' conflict, the date moves" is a real decision with a named loser. §12 separates "Decided in this run" from assumptions, and §6 non-goals carry revisit triggers (§7.2). Both `[NOTE FOR PM]` callouts sit at real tensions: accounts or mailboxes against the 20-minute target (FR-23), and a Git history rewrite (FR-32). Trade-offs name what was given up. Vale is dropped "so agent rules and review enforce style" (NFR-1). Templates are "copied once and never synced" (§4.1, R-9). Republishing creates version noise for consumers (R-11).

What's weak: the most consequential unknown has no decision path, and the schedule's binding constraint isn't sized.

### Findings

- **[high]** The only window to change time targets closes before the data arrives (FR-51, FR-52, OQ1, R-7, §7.4) — FR-51 says "Targets can change only through calibration (FR-52)", and FR-52 calibrates "In November 2026 ... before Level 2 work starts". But Platform doesn't deploy the chatbot until mid-December (R-1, §7.4), so the November "Try it" baseline can't reach first success. OQ1 (what "Try it" needs besides Docker) is revisited only "when Platform deploys the chatbot". The PRD's own NOTE FOR PM says a sign-in account or mailbox "is unlikely to fit in 20 minutes", and R-7 says only that the time "counts toward the timer by decision. Platform owns reducing it." So if getting an LLM key or account alone costs 10 minutes or more, the launch gate can't be reached, and the PRD forbids revisiting the target. *Fix:* add a second calibration point for "Try it" after Platform deploys and before the human stranger test. State the decision rule for when prerequisites alone exceed the budget: a separate allowance for getting prerequisites, a pre-provisioned trial key (which SM-C4 would then have to permit explicitly), or the date moves.
- **[medium]** Review capacity is the named bottleneck but isn't sized (R-4, OQ6, FR-57, §7.4) — §7.4 schedules 21 Level 1 migrations for "Late November to early December", and FR-57 requires that "A maintainer reviewed the migration pull request before it merged". The concurrent Hexalith.CiCd spec says the project is "built by one maintainer" and "there is one human" (`references/Hexalith.CiCd/_bmad-output/specs/spec-cicd/SPEC.md:21`). That means one reviewer for 21 PRs in about three weeks, and several PRs touch hundreds of `docs/` pages (see Scope honesty). *Fix:* answer OQ6 in the PRD (who reviews, how many PRs per week), derive the migration window from that answer, and order the migrations, starting with pilot repositories the way CiCd does with Commons and PolymorphicSerializations.
- **[medium]** FR-32 treats an existing exposure as a launch task (FR-32, OQ8) — FR-32 says "No sensitive data is exposed in Hexalith.BmadSkills at launch". But the glossary defines every current repository as public, and the brief's addendum says "The repositories and packages are already public". If any of the 106 `.claude.json` files holds a credential, it is exposed now, and rewriting history (OQ8) won't un-expose it to anyone who already cloned or forked the repository. *Fix:* make FR-32 an immediate task, not a launch condition: review now, revoke credentials first, then treat a history rewrite as hygiene. Reword OQ8 to match.

## Substance over theater — strong

The Vision is specific to this product: a front door, one command or one prompt, Docker, and a chatbot reply within 20 minutes. It wouldn't fit any other PRD. No differentiation section was invented to fill a template. The six UJ protagonists are illustrative (§2.3 tags them `[ASSUMPTION]`), but each maps to one quickstart path and is cited by a feature ("Realizes UJ-…"), so they carry weight. SM-8 (stars) is honestly labeled "no FR drives it". Most NFRs carry bounds, such as NFR-7's 2 minutes and NFR-4's "only values ... the prerequisites list names".

### Findings

- **[low]** Secret handling and rendering parity are each stated in several places (FR-6, FR-18, NFR-8; FR-12, NFR-2) — this is harmless now, but the PRD breaks its own NFR-5, "One source per rule", and story writers will produce duplicate acceptance criteria. *Fix:* keep each rule in its NFR and have the FRs reference it, or the reverse.

## Strategic coherence — adequate

The thesis is explicit (§1): documentation is what stands between the public code and a launch. Agents write most of the docs, so the standard lives in agent instructions, and a shared CI check catches what agents miss. Prioritization follows from it. "Try it" is the only Level 2 item in the gate (FR-58), "Run it" blocks ship as they become ready, and the SMs test the bet: SM-1 and SM-2 on "Try it", SM-3 on enforcement. The counter-metrics (SM-C1 to SM-C5) are the strongest part of the PRD. Each one names the SM it protects and the specific way to game it, such as SM-C4's "pre-provisioning keys ... warming caches". The arc weakens on the second half of the thesis: enforcement and durability.

### Findings

- **[high]** The docs check doesn't cover what the thesis says it catches (§4.8 description, FR-41, FR-49) — §4.8 promises "Every rule an agent can break mechanically also has a docs check rule", but FR-41's script checks only FR-9, FR-10, FR-11 (length only), FR-12, FR-13, and FR-38/FR-39. These rules can be checked mechanically and are left out:
  - quickstart block names and presence (FR-17)
  - AI prompt presence and the 10-line limit (FR-6, FR-22)
  - the prerequisites list at the top of each block (FR-18)
  - no local community files (FR-34), which is exactly what an agent would add back
  - the description matching the About text and the registry (FR-11)
  - missing required badges (FR-38 fails only on "more than five" or "outside the allowed set")
  - the Contributing links (FR-9 item 8)
  - the front door itself, which lives in `Hexalith/.github`, an out-of-scope repository that runs no docs check

  UJ-6 only works for rules on that list. *Fix:* either extend FR-41's list to every rule that can be checked mechanically, each with a rule ID, or weaken §4.8's claim and name the rules that rely on review.
- **[medium]** No metric tests the durability half of the thesis (§1 "keep the standard in place after launch", SM-3) — SM-3 is a launch-day snapshot. Nothing measures whether agent-written docs stay compliant after launch, which is the thesis's distinctive bet (UJ-6). *Fix:* add a post-launch SM, for example: 90 days after launch, all 21 repositories still run in fail mode, default branches have zero internal-planning-content findings, and N% of docs check failures on agent PRs are fixed without human edits. Use SM-C2 as its counterweight.

## Done-ness clarity — thin

Many FRs are genuinely testable: FR-9's order and "nothing after License", FR-10's line budgets, FR-38's allowed set, FR-44's "file, the line, the rule ID, and a one-line fix hint", and FR-29's keep-or-archive record. The weaknesses are concentrated on the launch path, the quickstarts and stranger tests. Story creation will lean hardest on those FRs, and an agent can't resolve a contradiction there by itself.

### Findings

- **[high]** No block as specified can wrap "exactly one command" (FR-6, FR-22 vs FR-19, FR-20, FR-21) — FR-6 says the prompt "wraps exactly one command", and FR-22 says it "wraps the same single command the block shows". But FR-19 gives "a `dotnet add package` command and a code sample", which also needs a project to add the package to and a step that runs it. FR-20 says "open the dev container ..., run `aspire run`, and make the first call". FR-21 gives "an install command, a first command". An agent writing or checking a block can't satisfy both rules. *Fix:* define "the command" for each block type (for example, `aspire run` for "Run it", and one script or a `dotnet new` + `add` + `run` sequence counted as one step for "Use the package"). Alternatively, change the rule to "one setup command plus the first-success step".
- **[high]** The stranger-test environment is undefined for most blocks, and so is the agent tool (FR-51, FR-53, glossary "Clean machine", R-8) — FR-51 measures every target "on a clean machine". The glossary's clean machine has no .NET SDK, and "The timer includes everything the reader must obtain", so a 5-minute "Use the package" would include installing the SDK. FR-53 instead runs that test "in a clean dev container", but only runnable repositories get one (FR-5, FR-20), and today only FrontComposer has a `.devcontainer/`. Separately, FR-53 records "the model, agent tool, and prompt" but never says which agent tools must pass. So the "Try it" gate (FR-26, the precondition in FR-55, SM-2) can be passed with whichever tool happens to work. The clean-machine definition also leaves out the coding agent itself, and how an agent running on the host "opens the dev container" (FR-6 step 1, UJ-1) without installing anything on the host (NFR-9). *Fix:* define a start environment for each block type (for example, a pinned stock .NET SDK container for "Use the package"). Name the supported agent tools for SM-2, and either require 2 of 3 runs per tool or name one reference tool. Add the agent and the way it enters the dev container to the clean-machine definition and to FR-18's prerequisites.
- **[high]** Level 1 quietly requires timed stranger tests on every "Use the package" and "Use the tool" block (FR-19, FR-21, FR-57, FR-54, SM-4, §4.10) — FR-19 and FR-21 each require the block to meet its time target. FR-57 makes FR-19 and FR-21 Level 1 conditions, and Level 1 for all 21 repositories is launch-gate item 2. That means three fresh-agent runs per block across the 17 repositories that publish packages. Yet §4.10 says "Try it" is "the only Level 2 item in the launch gate", SM-4 is "secondary", FR-54 doesn't list "before a 'Use the package' block is published", and nothing gives a fallback like FR-17's rule for "Run it". *Fix:* choose one explicitly. (a) A "Use the package" block passes Level 1 on CI compilation (FR-19) plus one agent run, and timed tests happen after launch. (b) Keep the gate, add these runs to FR-54 and to the November–December plan, and define a fallback for a block that misses its target.
- **[high]** The absolute-URL rule plus fail-mode link checking breaks the migration PR itself (FR-12, FR-45, FR-7, FR-42) — FR-12 requires absolute HTTPS URLs even for a repository's own pages, and FR-45 fails the job on a broken internal link. A Level 1 migration PR that creates `docs/development.md` and links it as `https://github.com/Hexalith/<repo>/blob/main/docs/development.md` points at a page that doesn't exist on `main` yet. That PR can never "pass the docs check in fail mode" (FR-7). The same mechanism lets a page rename in repository B fail the next unrelated PR in repository A, and R-5's mitigation covers only external links. *Fix:* require the docs check to remap the repository's own absolute URLs to the PR's working tree (lychee supports `remap`). Treat links into other Hexalith repositories like external links (scheduled and non-blocking), or state a different rule.
- **[medium]** Judgment words where stories need conditions (FR-57, FR-17, FR-49, FR-28, NFR-1, NFR-7, NFR-9) — FR-57's "Every `docs/` page linked from the README is accurate" is a launch-gate condition with no test. The same problem appears in FR-17's "the action a reader is most likely to take first", FR-49's "only rules an agent can't infer from the repository itself", FR-28's "checked ... for typos", NFR-1's "short and written for a global audience", NFR-7's "a typical pull request", and NFR-9's "where possible". *Fix:* define "accurate", for example: every command on the page runs as written, and every path, package, and type it references exists on the default branch. Take block order from the registry. Give NFR-7 a reference repository, such as EventStore with its 324 `docs/` pages.
- **[medium]** The 40-line Quickstart budget likely can't hold two blocks (FR-10 `[ASSUMPTION]`, FR-18, FR-22, addendum §A) — 11 of the 21 registry rows propose "Use the package, Run it". Each block needs a prerequisites list, a command, a fenced AI prompt of up to 10 lines, and a sample or first call with its result. Two blocks plausibly exceed 40 lines before counting headings. SM-C1 warns against cutting what the quickstart needs but doesn't say which rule wins. *Fix:* budget per block (for example, 25 lines each) or exclude the AI prompt fence from the count. State that the time target outranks the line budget.
- **[medium]** SonarQube results can't appear on fork PRs as written (FR-40, UJ-4) — FR-40 says "Results appear ... for pull requests". But GitHub doesn't pass secrets, including the organization token, to `pull_request` workflows triggered from forks, and a fork PR is how Tomás contributes in UJ-4. *Fix:* limit the consequence to PRs from the same repository, or require a safe design for fork PRs (such as analysis through `workflow_run`) in architecture.
- **[medium]** Rules that can't be suppressed collide with the standard itself (FR-46, FR-13, FR-1, addendum §B) — FR-46 makes the internal-planning-content rules unsuppressible, and FR-41 scans `docs/**/*.md` in Hexalith.Docs. The standard (FR-1) has to explain the ban there, and the migration prompt (FR-7) has to recognize banned content, so both will contain strings like "Story 1.2" or "FR-12". Ordinary prose also matches patterns like `\bStory\s+\d+`, and a false positive then has no escape. *Fix:* add an exemption that isn't a suppression, such as fenced code or one allow-listed file in Hexalith.Docs. Require the pattern set to be tuned against all 21 repositories before fail mode.
- **[medium]** "Lead to the documentation rules" isn't a test (FR-48) — the chain runs through `references/Hexalith.AI.Tools`, a submodule that's absent from a clone made without submodules, and the addendum says only that the migration "should verify" it resolves. CiCd also delivers a guarded block into the same three files (see Scope honesty). *Fix:* state the condition: "In a fresh clone with root submodules initialized, each entry point references `hexalith-docs-instructions.md` through a path that resolves. Without submodules, the entry point says how to fetch it."
- **[medium]** The launch gate's own pass condition is underspecified (FR-55, FR-23, SM-1, R-8) — FR-23 allows "either the command or the AI prompt", but FR-55 doesn't say:
  - which path the outside tester uses
  - whether any help invalidates the run (FR-53 says "without human help", FR-55 doesn't)
  - whether the clean machine may be Codespaces (the glossary allows it, but R-8 says the gate "is measured on a local clean machine")

  *Fix:* add to FR-55 the path, a local machine, no assistance, and what happens when the tester goes past 20 minutes because of provider sign-up.
- **[low]** FR-9 and FR-36 disagree on the development guide — FR-9 item 8 requires every README to link "the repository's development guide", but FR-36 requires a guide only where a repository "contains code". That leaves Hexalith.Docs, Hexalith.CiCd (which has "no content yet"), and possibly AI.Tools and BmadSkills without a link target. *Fix:* make the link conditional in item 8, or require a development guide everywhere.
- **[low]** FR-33's test uses a GitHub page that doesn't track all six files (FR-33, SM-7) — GitHub's Community Standards checklist doesn't include SUPPORT. SM-7's "complete" would also need items that no FR covers, such as the repository description and content reporting. *Fix:* check for SUPPORT through the API or the file itself, and align SM-7 with FR-33.
- **[low]** FR-24's agent stranger test has no pass rule (FR-24, FR-53) — FR-53's rule (2 of 3 runs within the target) needs a target, and FR-24 says "The how-to has no time target". *Fix:* state a pass rule (for example, 1 of 1 run reaches a first chat message without human help). Add Platform's ability to deploy to Kubernetes to §10.

## Scope honesty — thin

The explicit parts are good. The §6 non-goals are specific, and the prebuilt-images and smoke-test items carry revisit triggers (§7.2). "This initiative doesn't build Platform" is stated plainly. Every inline `[ASSUMPTION]` is indexed, and the open questions have owners. Open-items density is high for launch stakes: 30 inline assumptions, 2 `[NOTE FOR PM]` callouts, and 8 open questions. That's expected in Fast path, and most of the assumptions are cheap defaults such as file names and budgets. The problem is two large omissions that the reader is left to infer away.

### Findings

- **[critical]** A concurrent initiative already owns, and forbids, the enforcement mechanism (FR-41 to FR-43, FR-57, FR-15, FR-48, UJ-5, UJ-6, §10) — Hexalith.CiCd's spec (`references/Hexalith.CiCd/_bmad-output/specs/spec-cicd/`) is already executing; story 1 closed on 2026-11-09. It makes CiCd "the only place CI/CD changes" (SPEC.md:21) and makes the following rules:
  - Each module's `.github/workflows/` "holds only rendered files" (SPEC.md:35).
  - A module PR that changes an owned file fails the guard.
  - The block CiCd delivers into every module's AGENTS.md, CLAUDE.md, and copilot-instructions.md tells agents "Don't edit workflows, CI config, or the Builds pointer" (enforcement.md:98).
  - It lists "Rulesets with required status checks" under "Not used" and cuts existing ones back (enforcement.md:60; SPEC.md:155, 201).
  - It states "Agents push directly to `main`" (SPEC.md:155).

  This PRD depends on the opposite. FR-42 says "Each repository sets its own mode in the workflow file that calls the docs check" and makes the check "a required status check ... enforced through branch protection". FR-43 wires repositories into the check, although CiCd already plans to migrate AI.Tools, ChatBot, McpCli, and Platform. UJ-5 and UJ-6 assume PR-based review, which CiCd says isn't an enforcement layer. FR-15's docs-only release rule belongs in the Builds release config, which only CiCd agents change (SPEC.md:139), and CiCd releases "only a commit whose CI passed" (SPEC.md:97). §10 doesn't name Hexalith.CiCd. Stories generated from the PRD as written will have agents editing files that the guard rejects. *Fix:*
  - Add Hexalith.CiCd to §10 as the owner of docs check delivery and mode.
  - Rewrite FR-42 and FR-43 so the mode lives in CiCd's per-module setup file and "fail mode" means the CI stage fails, not a required check.
  - Reconcile FR-57's review requirement and UJ-6 with direct pushes to `main`.
  - Route FR-15's release rule and FR-48's entry-point edits through CiCd's ownership, including its marked block.
- **[high]** The `docs/` cleanup is far larger than the plan admits, and the non-goals forbid the obvious fix (FR-13, FR-8, §6, FR-41, FR-7, §7.4) — a read-only scan of the local clones with the addendum's §B candidate patterns matches about 430 of about 970 Markdown pages under `docs/`. Conversations has 72 of 86, Folders 76 of 84, EventStore 62 of 324, Platform 55 of 127, and Memories 42 of 54. The matches include user-facing pages: EventStore's `docs/getting-started` and `docs/concepts` cite "Story 2.13" and "Story 3.17". Whole folders are planning evidence, such as Platform's `docs/implementation/` (about 2,600 non-Markdown evidence files) and Conversations' `docs/release-evidence/`. The PRD contradicts itself on this content:
  - FR-13 bans it from `docs/`, but §6 says existing `docs/` folders are "cleaned only", not reorganized.
  - FR-7's list of homes (development guide, operations page, CHANGELOG or Releases) has no place for story evidence.
  - FR-41 scans only `docs/**/*.md`, so the JSON evidence escapes the check that FR-13 relies on.

  *Fix:* define "cleaned". Allow moving planning and evidence folders from `docs/` to `_bmad-output/`, and say that this isn't the reorganization §6 forbids. Extend FR-13's check to all files under `docs/`. Size each repository's Level 1 work from this scan and reflect it in §7.4.
- **[medium]** Level 1 depends on CI health, which the PRD never mentions (FR-36, FR-39, FR-15, §10) — FR-36 needs tests "green", FR-39 needs a CI badge on a workflow that "runs on the default branch", and FR-15 needs a release. CiCd reports that the main CI workflow "fails on 60–100% of runs in 9 of the 15 repositories that have one" (SPEC.md:21), and it releases only commits whose CI passed. A documentation story can't fix that. *Fix:* add CI health (through CiCd) to §10 and the risk table. Say what Level 1 means for a repository whose CI is red: for example, an honest red badge is allowed and the republish waits.
- **[medium]** Old packages stay on nuget.org with old READMEs (FR-15, FR-29, UJ-2) — FR-15 republishes only packages from in-scope repositories, while FR-29 archives "about 30 older modules" (brief addendum), some of which sit next to their replacements (EventStores beside EventStore, FrontShell beside FrontComposer). Karim's journey starts with a nuget.org search, where those packages remain listed. *Fix:* add an FR to deprecate packages from archived repositories (naming the replacement package) or unlist them, or declare it a non-goal.
- **[medium]** Nobody owns changes and drift after launch (§4.1, FR-41, FR-5, FR-25, §6) — the PRD doesn't say:
  - how a rule change reaches repositories (callers pin Builds by SHA today, for example McpCli's `domain-ci.yml@567604b…`, and CiCd moves "one exact Builds release tag" for all modules, SPEC.md:59)
  - how a new repository enters the registry and the front door
  - what keeps copied dev containers aligned with each repository's own `global.json` (FR-5 pins exact SDK versions, and FR-54 doesn't retest after an SDK bump)

  FrontComposer's existing docfx site is also left unaddressed against the "documentation website" non-goal. *Fix:* add a short "After launch" section covering:
  - the owner of the standard
  - the rule-change process (warn first, then fail, through CiCd's version bump)
  - a checklist for new repositories
  - a docs check rule that compares the `.devcontainer` SDK version to `global.json`
- **[medium]** The launch gate omits prerequisites it depends on (§7.3, FR-33, FR-34, FR-47, FR-24) — gate item 2 enforces FR-34 (delete every local community file) through FR-57, but FR-33 (create the organization files) isn't gated. The gate can therefore pass with no community files anywhere. FR-47 (the rules file) isn't gated either, although FR-48 is. §7.1 puts the Kubernetes how-to in scope for launch, and §7.3 doesn't gate it. That's probably intended, but it's never said. *Fix:* add FR-33 and FR-47 to §7.3, and mark the Kubernetes how-to "in scope, not gating" in §7.1.
- **[low]** The open questions don't say what they block (§11) — only OQ1 lists "Affects". OQ3 blocks FR-2, FR-25, and FR-28; OQ5 blocks four repositories' migrations; OQ6 blocks the §7.4 schedule. *Fix:* add "Blocks" and "Needed by" to each open question so epics can be sequenced around them.

## Downstream usability — adequate

The foundations for source extraction are strong:
- a glossary of about 40 terms, used consistently
- FR-1 to FR-58, contiguous with stable IDs
- features that cite the UJs they realize, and SMs that cite the FRs they validate
- the §0 visibility rule that keeps FR IDs out of public docs

Most FRs stand on their own. The gap is specific to this downstream consumer: stories fan out per repository, and many FRs apply through conditions that the PRD never resolves for each repository.

### Findings

- **[medium]** No per-repository applicability matrix (FR-36, FR-37, FR-38, FR-58, FR-20, FR-43, addendum §A) — FRs apply where a repository "contains code", has "operator content", has CI that "builds .NET code", or has "an Aspire AppHost". The registry records only category, quickstart blocks, and packages. A local scan finds AppHost projects in 13 repositories, counting Platform's file-based `apphost.cs` (some may be samples or test fixtures). These include Builds and McpCli, which are proposed as "Use the tool". Only FrontComposer has a dev container. *Fix:* add registry columns for AppHost, contains code, operator content, dev container present, and CI owner, so the epics workflow can generate per-repository stories without judgment calls.

## Shape fit — strong

The shape matches the product. It's a capability spec for a standard that spans many repositories, with UJs only where there's real user experience: four newcomer and contributor paths, plus two agent journeys that motivate FR-7 and FR-44. Fifty-eight FRs is proportionate to launch stakes and 21 repositories. The brownfield references mostly check out against the local clones:
- `Hexalith.Builds/.github/prompts/audit-hexalith-ci-cd.prompt.md` exists.
- EventStore has `.markdownlint-cli2.jsonc`, `.lycheeignore`, and `docs/page-template.md`.
- Every repository's LICENSE is MIT, which matches FR-9.
- Platform's AppHost is file-based (`apphost.cs`), which works with `aspire run`.

### Findings

- **[low]** FR-43's list is partly stale (FR-43) — FR-43 says Hexalith.McpCli doesn't use the Hexalith.Builds reusable workflows today. But McpCli's `.github/workflows/ci.yml` calls `Hexalith/Hexalith.Builds/.github/workflows/domain-ci.yml`, pinned to a SHA and last changed on 2026-11-06. *Fix:* re-derive the list from CiCd's module inventory, or drop the list and say "every in-scope repository, whatever its current CI".

## Mechanical notes

- **Assumptions Index roundtrip: clean.** All 30 inline `[ASSUMPTION]` tags (three in FR-9, two in FR-42) appear in §12, and every §12 entry has an inline tag. Splitting §12 into "Decided in this run" and "Resolved conflicts" helps.
- **IDs: clean.** FR-1 to FR-58, NFR-1 to NFR-9, SM-1 to SM-8, SM-C1 to SM-C5, R-1 to R-11, UJ-1 to UJ-6, and OQ 1 to 8 are contiguous and unique. All FR, NFR, R, and OQ cross-references resolve.
- **§7.1's ranges don't match FR-57.** §7.1 puts "FR-9 to FR-22 ... FR-33 to FR-39" under Level 1, which includes FR-20 ("Run it", which FR-57 excludes) and FR-33 (an organization-level FR). FR-48 is part of FR-57 but appears in §7.1 on the AI.Tools line.
- **FR-12 overstates the addendum.** It says "`addendum.md` §B lists" the allowed hosts, but §B lists 7 of the 38 ("These include …"). Link to nuget.org's list or copy it.
- **FR-13 and FR-41 contradict FR-34.** They check "any CONTRIBUTING file", while FR-34 bans local CONTRIBUTING files. Say instead that the check fails when one is present.
- **Friction-log severity isn't in the glossary.** FR-53's "red friction item" relies on a scale defined only in addendum §C, and FR-55 turns "every friction item" into an issue. If that difference is intentional, say so, and add red, amber, and green to the glossary.
- **Term drift.**
  - §4.4 says the front door "lists only current modules", but FR-25 lists in-scope repositories, which include Hexalith.Docs, not a current module.
  - The glossary defines a "Module" as one current repository, yet the registry gives Hexalith.Docs a category.
  - "Operator" (FR-24, FR-37) appears in neither the glossary nor §2.1.
- **UJ protagonists.** UJ-5 and UJ-6 have no named protagonist ("An agent", "a maintainer"). That's acceptable for agent journeys, but naming the maintainer role consistently would help story extraction.
- **Required sections.** Everything required for launch stakes is present.
