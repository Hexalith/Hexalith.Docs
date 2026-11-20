# PRD quality review — Hexalith Documentation Standard

Full-document validation, 20 November 2026. Reviewed the PRD and addendum against the approved backlog, module registry and stranger-test protocol.

## Overall verdict

The PRD gives the team a clear launch outcome, 66 identifiable requirements and a dated account of what each pilot has proved. Before using it to accept all 21 migrations, maintainers need a workable readability check for five nonpublishers, a single rule for when timed tests become mandatory, and a capacity test that can actually trigger postponement. The missing McpCli write and the unmeasured cold journey are documented delivery dependencies.

## Decision-readiness — adequate

The two December decisions name an owner, a date and a consequence. The first still allows a positive answer when the observed throughput would miss the release window.

- **[high] Any measured review rate can pass** (§8.4, OQ-6, R-4) — “Is the review rate measured?” can be answered yes even when one accepted migration per week would leave most repositories unfinished. The 1 December decision also precedes the proposed 10 December republish cutoff. *Fix:* At the decision, use the outstanding repository and package-publisher counts, measured review and release capacity, and available working days to forecast both deadlines. Specify the maintainer’s response when the forecast misses either date.

## Substance over theater — strong

The timed journeys correspond to distinct user tasks. FR-19 tests what a developer copies from the README. Section 8.4 distinguishes a successful hosted example from a published archive match and records that the 10.60-second measurement ended at restore. These distinctions would change a real acceptance decision.

## Strategic coherence — adequate

The primary measures track completed newcomer tasks and enforced documentation quality. Counter-metrics protect complete instructions and cold-start timing from superficial improvements. Keeping chat after launch preserves a useful first outcome while making the dependency on an approved Projects write visible.

- **[high] The cleanup metric counts a required public repository as a failure** (§3, FR-29, FR-59, SM-7) — The glossary explicitly excludes the organization’s community repository from the 21. SM-7 requires every other public repository to be archived, made private or transferred, while gate 6 requires that same community repository to be public and live. FR-29 also permits the maintainer to record “keep.” *Fix:* Define SM-7 against the reviewed archive-candidate inventory. Exclude the required organization repository explicitly and specify how approved keep decisions count.

## Done-ness clarity — thin

The create/list identity match and per-package README verification have observable completion conditions. Several other acceptance instructions produce different verdicts for the same evidence.

- **[high] Five repositories have no NuGet page for their required review** (FR-62, FR-57, NFR-2) — Every migration requires the readability checklist “from the README alone as nuget.org shows it.” The registry lists zero packages for AI.Tools, BmadSkills, CiCd, Docs and Platform. No reviewer can inspect those repositories on NuGet. *Fix:* Designate the rendered GitHub README as acceptance evidence for nonpublishers, mark package-only checks inapplicable, and retain the NuGet rendering check for each publisher.
- **[high] Two different test counts govern initial block publication** (FR-53, FR-54, FR-57, FR-58) — FR-54 requires the timed stranger test “before any block … is published.” FR-57 says Level 1 blocks “work but aren’t timed” and requires one completed agent run. A new package block passing one untimed run can therefore satisfy the Level 1 checklist yet fail its publication rule. *Fix:* Specify where the one-run Level 1 check suffices and where the timed two-of-three Level 2 test is required before publication. Retain the explicit Platform and launch gates.
- **[medium] The standard “Run it” prompt ends before first success** (FR-6, FR-20, FR-51) — An agent following the five prescribed steps can return the dashboard and “Explain the first call” without ever receiving its documented result. That prompt can complete while the 15-minute timer still runs. *Fix:* Require execution of the first call and comparison of the returned result with the expected value.
- **[medium] Gate 9 has two possible Kubernetes pass rules** (FR-24, FR-53, §8.3) — FR-24 requires “one agent stranger test run” and gives no time target. FR-53 defines each test as three runs and a pass as two successes within target. Two reviewers can demand different evidence for the same Kubernetes guide. *Fix:* Define the Kubernetes qualification as one untimed, independent execution if that is the intended exception, and reference it in gate 9.

## Scope honesty — adequate

The addendum labels the registry proposal historical and directs readers to the working JSON. The 20 open questions name owners and decision points. FR-7 still makes an impossible checkout assumption about the scope.

- **[medium] Migration instructions omit the parent checkout and exceptional module** (FR-7, §3, §13) — “Every in-scope repository is a root submodule” includes the Docs workspace itself. Docs is the parent, 19 other repositories are declared as direct submodules, and BmadSkills has no gitlink. Adding BmadSkills alone would still leave the statement false. *Fix:* Identify the Docs checkout, its declared direct submodules, and the owner-approved source location for BmadSkills. Keep its inclusion in the registry independent of a checkout decision.

## Downstream usability — adequate

Stable identifiers support story extraction. The module and release owners can trace decisions through the backlog and ledger. The first public test still lacks an unambiguous source revision.

- **[high] The first agent rehearsal has no defined candidate page** (FR-17, FR-22, FR-53, FR-54, §8.4) — The test starts at the Platform README and consumes its prompt. Until qualification, the README links to a development guide and the block containing the prompt is withheld. The protocol does not say how observers supply the exact proposed README and prompt before publication. *Fix:* Define a pinned candidate page or preview and its entry link for the first trials, record the revision and prompt, and identify which changes require retesting before promotion.
- **[low] A named missing file already exists** (FR-48) — The example says PolymorphicSerializations has no Copilot entry point. Its refreshed main at `c6d0dfce` tracks `.github/copilot-instructions.md`. A migration agent could replace a file that carries existing instructions. *Fix:* Remove the stale example and direct the agent to verify reachability in the checked revision before proposing changes.

## Shape fit — strong

A repository-by-repository capability specification suits a program spanning public Markdown, package releases, shared CI and human administration. The user journeys explain why a green code build alone cannot establish a working first run. The addendum holds source-specific setup details.

## Mechanical notes

The PRD contains FR-1 through FR-66, UJ-1 through UJ-6 and SM-1 through SM-10 exactly once as definitions. All ten launch conditions are enumerated. The relative Markdown links in the PRD resolve in the checkout. Four newcomer or contributor journeys name illustrative people. The two operational journeys identify their actors by role.

- **[low] The assumptions index still includes a settled ledger rule** (§13, FR-56) — Section 13 lists the ledger’s location and role-only identity as assumptions while FR-56 states both directly and FR-65 requires role-only identification. *Fix:* Move confirmed ledger facts into the decisions list or retain an assumption only on the specific point still awaiting confirmation.
