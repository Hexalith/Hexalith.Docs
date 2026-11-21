# Good-spine review

21 November 2026 · Hexalith.Docs `bbdfc01` · initiative-level draft · 19 refreshed direct dependencies.

**Verdict.** Revise the CI input and ownership contracts, the Builds publishing exception and the first-run handoff before independent teams use the spine for rollout. The five decisions identify the responsible systems. Four handoffs can still produce different results under their current wording.

## High · A module revision does not identify its registry inputs

AD-1 makes Docs authoritative and AD-2 promises repeatable checks at a module revision. Neither identifies the Docs registry revision or the copy of the module’s facts delivered with that revision. A new package ID or a confirmed description can consequently produce different findings for the same module commit if one caller reads the latest Docs registry while another uses a cached copy. The PRD requires the checker to consume registry facts. The existing pilot checker only needs repository-local inputs, so its success cannot settle this interface.

**Disposition — discuss.** Agree how the module commit selects an immutable Docs registry snapshot or a materialized row and source revision. Bind both local and hosted callers to it. Specify who delivers a new snapshot and how a CI run identifies the revision it used. Preserve CiCd’s ownership of managed inputs and its restriction on hard-coding module lists in Builds.

**Evidence.** Spine lines 25–33. PRD FR-2 lines 232–244 and addendum §B.2 line 90. CiCd architecture `architecture-cicd-2026-11-07/ARCHITECTURE-SPINE.md` lines 96–121. At Builds `e1380b81`, `Github/lib/docs_check.py` lines 36–65 and 85–103.

## High · CI enrollment omits standalone and self-managed repositories

AD-2 gives a single route through CiCd and specifies promotion for the pilots. The registry has 17 managed rows, two self-managed rows (Builds and CiCd) and two caller rows (Docs and BmadSkills). The organization’s `.github` is an additional caller outside the 21-row inventory. A standalone maintainer can wait for CiCd to deliver a configuration it does not own, or change local and hosted modes separately. The PRD settles that ownership and requires fail-mode hosted evidence at the accepted revision for all 21.

**Disposition — carry forward the settled rule.** Use the registry ownership class to select who sets the mode and how the common contract is invoked. Include the organization caller explicitly. Carry warning review and hosted fail-mode evidence through every migration. Keep the organization caller outside the 21-row launch denominator.

**Evidence.** Spine lines 19, 29–33 and 74. PRD FR-42/43 lines 799–813. Epic 2 story 2.1 line 45. Docs’ own `.github/workflows/documentation.yml` lines 16–24 currently checks its registry and runs its unit tests.

## High · Builds has two packages but the README-only release selector excludes it

AD-3 describes the README release rule for module documentation migrations. It does not give the handoff for Builds’ own migration. Builds is a registered publisher of two packages. Its own release workflow explicitly selects the Builds rule set. That set excludes documentation changes, while the module rule set grants a patch for the README scope. A maintainer can complete the Builds README migration and dispatch a release with only that change in range and get no new version for either package. That blocks the FR-15 republish evidence.

**Disposition — discuss with the Builds release owner.** Record a supported route for the two Builds packages, such as including the approved README in the next genuine release-qualifying Builds change. If that cannot meet the republish window, escalate the release-policy or schedule decision to the owner. Apply per-package public verification to this publisher as well.

**Evidence.** Spine lines 35–39 and 75. PRD FR-15 lines 435–441. Epic 3 story 3.5 lines 93–95. `docs/module-registry.json` lines 96–119. Builds `.github/workflows/builds-release.yml` lines 19–21 and `Github/lib/release_version.py` lines 35–46. CiCd architecture AD-10 lines 289–291.

## High · The organization can promote a route that Platform has not qualified

AD-4 and the first-operation delivery row mention a 20-minute run, the prescribed entry page and outside-tester evidence. They omit the separate 15-minute Run it result required before linking the front door, the identity of the tested candidate, and the public-entry transition. Two agents could meet the 20-minute target on different prompt versions, or the organization could publish after a 19-minute Try it pass even though the 15-minute block failed. The PRD resolves both cases and puts the outside trial after publication of the qualified link.

**Disposition — carry forward the settled rule.** Bind Run it and Try it to the same immutable candidate. Apply each target to its own first result, group three clean trials by candidate, tool, version, model and prompt, and use the PRD’s candidate-to-front-door sequence. Repeat the affected qualification if the route changes. Reference the separate untimed Kubernetes gate when AD-5 hands the final launch decision to the maintainer.

**Evidence.** Spine lines 41–45 and 76. PRD FR-23 lines 534–541, FR-53 lines 963–967, FR-55 lines 987–992, §8.3 lines 1117–1130 and §8.4 lines 1157–1163. `docs/stranger-test.md` lines 7–15 and 22–33 describe the two journeys and observer evidence.

## Rubric coverage

| Decision | What is grounded | Remaining assessment |
| --- | --- | --- |
| AD-1 | A single JSON registry represents the 21 repositories and exposes review state. | Its cross-repository use needs the immutable input above. Refer to FR-47 and §8.5 for same-ID synchronization with AI.Tools. |
| AD-2 | Builds supplies a common checker and CiCd owns managed delivery. | The immutable registry input and the three enrollment routes qualify this decision. |
| AD-3 | The consumer runs the displayed code, the intended README is selected per package and the rendered page is a release gate. | Record the self-publishing Builds exception. Keep archive comparison and human rendering review separate. |
| AD-4 | Platform owns the composition, McpCli owns the operation and the trial uses a cold host. | The two timed routes and promotion boundary need an explicit handoff. |
| AD-5 | Private item-level exposure evidence, public aggregate counts and human authority agree with FR-56 and the ledger. | Refer to PRD §8.3 as the ten-condition launch decision and to FR-24 for untimed local Kubernetes qualification. |

No parent Docs initiative spine is declared. The CiCd and Platform architecture documents supply external constraints. CI delivery stays within the owning repositories, Platform owns local composition, and private disposition stays with the maintainer. The PRD handles the operational scope beyond the local trial, including untimed Kubernetes qualification, weekly external checks and deferred cloud deployment. Service-provider or hosting choices for the documentation standard do not need a new architecture decision. The spine binds no numeric external tool version. Selecting SDK and Aspire pins from Platform’s checked-in configuration remains appropriate.

The ledger’s 20 November baseline records zero Level 1 acceptances. That historical evidence and pending owner sign-offs do not add architecture defects. Mechanical validation and registry checks establish structural consistency only. They do not qualify a trial, publish a package or establish launch readiness.
