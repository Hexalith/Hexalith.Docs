# PRD review follow-up — 20 November 2026

The previous validation recorded five high, four medium and two low findings at Docs commit `b2f7018`. This review checked each acceptance rule in the revised PRD against its neighboring requirements, the addendum and the registry. [Original validation](validation-report.md) · [Revised PRD](prd.md) · [Addendum](addendum.md)

## Disposition of the original findings

| Original severity | Finding and source | Disposition and evidence |
| --- | --- | --- |
| High | 1. Capacity to meet both deadlines, §8.4, R-4, OQ-6 | Resolved. The maintainer forecasts verified publisher releases before stabilization and all 21 Level 1 acceptances by launch from outstanding counts, observed pilot rates and owner availability. Missing evidence or a missed deadline moves launch to January. |
| High | 2. Organization cleanup count, SM-7, FR-29, FR-59 | Resolved. The denominator is the reviewed candidate inventory. An approved keep counts as a disposition, and the public community repository sits outside that count. |
| High | 3. Readability evidence for nonpublishers, FR-62, FR-57, NFR-2 | Resolved in the acceptance rules. GitHub rendering applies to every repository. Only the 16 publishers have NuGet rendering and release checks. The five other registry rows record those fields as inapplicable. |
| High | 4. Level 1 and Level 2 publication tests, FR-53, FR-54, FR-57, FR-58 | Resolved. Level 1 package and tool blocks require one successful, unaided, untimed candidate run. Every published block requires timed qualification by launch. A “Run it” block requires a 15-minute qualification before initial publication. |
| High | 5. First Platform rehearsal, FR-17, FR-53, §8.4, addendum §C | Resolved. An immutable candidate README supplies the entry URL and prompt. The observer records the revision and repeats qualification if the commands, prompt, prerequisites or path to first success change. The 15-minute first call and 20-minute project create/list have separate timed tests. Both precede the public front-door link. |
| Medium | 6. First-call result, FR-6, FR-20 | Resolved. The “Run it” prompt executes the documented first call and compares its result with the expected value. |
| Medium | 7. Kubernetes gate, FR-24, FR-58, §8.3 item 9 | Resolved. One independent agent in a fresh environment follows the how-to unaided and records a successful McpCli result. No time threshold applies. |
| Medium | 8. Migration checkout, FR-7, §13 | Resolved. Docs owns the parent checkout and declares 19 direct submodules. BmadSkills remains in scope and its migration awaits an external checkout and revision approved by its owner. |
| Medium | 9. Designated agent configuration, FR-53, SM-2, OQ-15, addendum §C | Resolved. Before a timed qualification, a maintainer records the tool, version and model. Two of three independent runs on that configuration must pass. A changed configuration starts a new set. |
| Low | 10. Existing agent instruction files, FR-48 | Resolved. Check all three entry points at the migration revision, preserve existing guidance and create a file only when absent. |
| Low | 11. Ledger facts in the assumptions index, FR-56, FR-65, §13 | Resolved. The ledger location and role-only tester identification appear in recorded decisions. |

All 11 original document findings are resolved. A final cross-check confirms that FR-63 uses the check appropriate to the block’s level, FR-17 withholds an unqualified “Run it” block, §1 recognizes package-specific READMEs, and OQ-2 includes the approved keep option.

**Rubric judgment.** Decision-readiness is strong for the December decision because the maintainers must compare two forecast completion dates with their deadlines. Substance and strategic coherence are strong because the first-result, rendering and cleanup measures each identify the population and evidence they cover. Done-ness clarity and downstream usability are strong for the revised qualifications because each has a trigger, test count, observable result and record. Scope honesty and shape fit are strong for this update because the registry defines the complete repository population and the addendum carries the trial mechanics.

## Delivery evidence still open

The ledger records zero Level 1 acceptances. The capacity forecast needs measured review, release and verification rates. The public pilot archives match 2 of 12 expected Commons READMEs and 0 of 2 expected serialization READMEs. Hosted fail-mode checks, republishing and gallery verification remain with their owners. [Launch ledger](../../../implementation-artifacts/launch-ledger.md)

The Platform engineering observation covers only a 10.60-second restore. The documented project write, seven-module readiness, separate first-call and create/list tests, and eligible outside-tester run still require evidence. No completed clean-host qualification appears in the ledger. The PRD retains 66 distinct functional requirement identifiers and ten launch conditions. [Qualification protocol](../../../../docs/stranger-test.md) · [Launch ledger](../../../implementation-artifacts/launch-ledger.md)
