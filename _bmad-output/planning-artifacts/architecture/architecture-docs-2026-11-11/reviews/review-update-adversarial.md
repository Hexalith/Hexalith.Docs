# Adversarial review of the architecture update

**Verdict.** Resolve the Platform eligibility rule and distinguish a successful hosted run from acceptance of every mandatory rule. The revised decisions specify who owns the registry check, how the first promotion is calibrated, when public material is reviewed and which catalog is admissible for a trial.

The line references below identify the candidate reviewed on 21 November 2026, before triage.

## High · Platform's candidate can be ineligible to take its own qualification test

The trial team can render a candidate Platform README at an immutable commit and run the two AD-4 qualifications. A README reviewer applying AD-10 literally must withhold that same candidate. AD-10 makes a direct Platform gitlink a prerequisite for a “Run it” block and says a README shows only qualified blocks. Platform has no self gitlink. Each team can apply its reading consistently and reach the opposite answer about the same candidate. The PRD already authorizes access to the candidate before publication.

**Disposition.** Limit the module manifest and direct Platform gitlink requirements to the module-workspace route. State the prerequisites for Platform's own AppHost separately. Permit an immutable candidate README to contain the block for rehearsal. Apply the qualification restriction to the publicly promoted default-branch README. [Spine AD-4 lines 81–84 and AD-10 lines 140–145](../ARCHITECTURE-SPINE.md) · [Platform submodule declarations](../../../../../references/Hexalith.Platform/.gitmodules) · [FR-53 and rollout sequence, lines 963–966 and 1157–1163](../../../prds/prd-docs-2026-11-09/prd.md)

## High · A mandatory content violation can coexist with a green hosted fail-mode run

Consider a newly delivered D-PLANNING rule at report level which correctly finds an internal story reference on a pilot’s root README. The findings have been calibrated over 21 revisions and reviewed. Builds can return a successful check in fail mode because this rule is still at report level. A migration owner can cite that successful hosted run and the calibration, while a human reviewer applying FR-13 and FR-57 rejects the same page. The handling of newly introduced rules protects shared CI. It does not certify cleanup of an actual violation for Level 1.

**Disposition.** Require a clean result or recorded review demonstrating that each applicable Level 1 rule holds at the accepted revision, including mandatory rules still at report level or awaiting automation. Keep the existing phased rollout and hosted evidence requirements. The standard already instructs reviewers to cover the remaining requirements. [Spine AD-8 lines 118–124 and delivery table lines 346–353](../ARCHITECTURE-SPINE.md) · [Standard line 7](../../../../../docs/documentation-standard.md) · [FR-13 and FR-57, lines 414–421 and 1018–1031](../../../prds/prd-docs-2026-11-09/prd.md)

## Medium · The maintainer's role in trial selection and the human time limit need to follow the record

AD-4 requires a predeclared tool, version and model. A team could predeclare an unsupported model on its own, obtain two successful trials, then ask the maintainer to accept that configuration retrospectively. A second owner follows FR-53 and accepts only a maintainer-designated, supported configuration recorded beforehand. The delivery table identifies the acceptance owners. The PRD also sets the outside trial’s unaided 20-minute limit and requires the path to be declared in advance.

**Disposition.** Name the maintainer who records the supported configuration before the first run. Compare the instructions to be published with the qualified candidate before promotion. Reference FR-55 for the independently timed human attempt from the public link, including the 20-minute target, no-help rule and advance path selection. [Spine AD-4 lines 81–84 and delivery table lines 352–353](../ARCHITECTURE-SPINE.md) · [FR-53 and FR-55, lines 963–966 and 985–992](../../../prds/prd-docs-2026-11-09/prd.md)

## Disposition of the eight earlier findings

| Earlier finding | Result of the counterexample |
| --- | --- |
| Registry and checker revision | AD-6/15 fix the registry and source identities and require local and hosted module checks at the same Builds commit. A subsequent record can cite the self-checked Docs commit. |
| Enrollment and promotion | AD-2/8 separate the three configuration ownership routes and distinguish shared calibration from per-candidate hosted evidence. The rule-coverage case above still affects acceptance. |
| Cross-repository links | AD-7 distinguishes offline checks on pinned sibling files from live migration and weekly checks. The literal FR-45 cadence for every module run remains a stated PRD-owner decision. |
| Builds package release | AD-11 assigns both registered Builds IDs, allows a qualifying non-docs release, requires per-ID public evidence, and defines what to record if the date slips. |
| Independent timed qualifications | AD-4 now requires two distinct successful sets on the same candidate. AD-10 eligibility and trial authorization need the clarifications above. |
| Exposure of already-public repositories | AD-5 requires immediate private review at the reviewed revision and reconciliation through closure. |
| Unknown package inventory | AD-16 prevents an unverified empty list from becoming an exemption and specifies legacy-row handling. |
| Effective Dapr runtime | AD-13 requires the effective catalog SHA and both installed version identities. A sibling override or an installed-version mismatch disqualifies the trial. |

## Final disposition after triage

**Pass for this adversarial review.** All three counterexamples are closed in the revised architecture.

| Finding | Result on recheck |
| --- | --- |
| Platform candidate eligibility | AD-10 lines 141–145 apply the Platform gitlink requirement to a module running from its own workspace. Platform rehearses its own AppHost route on an immutable candidate. The default branch retains the development-guide link until both AD-4 qualifications pass. |
| Passing CI with a mandatory report-only violation | AD-8 line 124 requires affirmative evidence for manual and report-only rules. An unresolved mandatory finding holds Level 1 open even after a successful hosted fail-mode run. |
| Trial authorization and human evidence | AD-4 lines 81–84 require the maintainer to select a supported tool, version and model before each set and to compare the candidate with the proposed instructions before promotion. The outside tester follows a predeclared route from the public link, unaided, on a clean machine, and has 20 minutes including prerequisites. |

FR-45's literal every-module-run cadence remains explicitly assigned to the PRD owner. The operational trial, release and exposure gates remain with their named owners. [Updated architecture](../ARCHITECTURE-SPINE.md)
