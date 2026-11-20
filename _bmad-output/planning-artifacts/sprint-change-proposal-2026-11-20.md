# Sprint change proposal for 20 November 2026

**Approved by the maintainer on 20 November 2026.** The approval covers the initial Docs backlog, the audit corrections and the owner handoffs below.

## Issue and decision

The audit of Docs at 820c821 found that 202 passing Commons core tests coexisted with a first README example that failed with CS0234. Both pilot packages shipped a badge that returned 404. The guide hub had a final PRD, a blank architecture template, and no registry or ledger. The Platform instructions selected two different Dapr directories. The 20-minute newcomer journey has no qualifying run.

The maintainer selected creation of the initial backlog from the final PRD and application of the audit recommendations. The [initial backlog](epics.md) covers all 66 functional requirements. The scope is moderate. The product owner coordinates the backlog and developer owners implement and test the corrections. The public launch decision remains with the maintainer.

## Impact and selected approach

Directly adjust the new stories. The product goals and ten launch conditions in PRD §8.3 already describe the required behavior. Rolling back the product libraries would discard passing behavior and leave the broken examples in place. Reducing the MVP would hide the unproven Platform journey. Time-box the clean-host measurement and use the existing December decision points. A new UI specification is unnecessary. The reader interacts with Markdown, package pages, and the Platform command line.

## Changes to the baseline

| Story and artifact | Before | Accepted change and reason |
|---|---|---|
| 1.1, publication review | PRD records 106 state files. | Track 53 originals plus 53 backups at an exact revision. Preserve the private disposition and require owner review before visibility changes. |
| 1.2, architecture and registry | Placeholder decisions and an unconfirmed Markdown inventory. | Record source of truth, owners, local validation, republishing and measurement boundaries. Validate all 21 rows, with confirmation status visible. |
| 2.1–3.2, pilot CI and packaging | Product tests and existing badges are the available signals. | Run displayed code, resolve the workflow badge, compare packed README contents and test docs-only version selection. Switch a pilot to fail mode only after review. |
| 4.1–4.2, newcomer setup | Two Dapr paths and an unmeasured target. | Use one documented path. Record cold prerequisites and timing, then require first create/list and the specified independent trials. |
| 3.10 and 6.3, workspace checkout | The Conversations pin contains an orphaned gitlink. | Adopt its existing reviewed repair and validate direct declarations without initializing nested modules. |
| 6.1 and 6.2, authoring support | An acknowledged log entry can disappear. Generator and test disagree on distribution names. | Protect the whole log transaction and test concurrent acknowledgements. Reconcile the naming contract against distribution guidance and verify both IDE copies. |

## Handoff and acceptance

- Docs product owner and developers own the registry, guide, architecture, ledger and acceptance evidence. Allow 2–4 person-days for foundations.
- Commons and serialization owners own executable samples and package-specific README selection. Builds and CiCd owners own the shared check, release rules and delivery. Allow 3–6 person-days for pilot integration and verification.
- Platform owns the Dapr correction and prerequisite evidence. Allow 2–4 person-days for clean-host measurement after its runtime dependencies are available.
- The security maintainer alone records private review results. Release, visibility, and outside-tester gates require their named human owners. The ledger must distinguish local verification from published evidence.
- Tooling owners reconcile upstream authoring behavior. Verify successful concurrent appends and the marketplace fixture. The Docs owner can advance the Conversations pin independently.

## Execution record

The scope was accepted in the request to create the missing backlog and apply the audit. The product owner established 6 epics and 36 stories, including a migration for each of the 21 repositories. The backlog maps all 66 functional requirements. The architecture linter returned zero findings and the sprint-status validator accepted the generated state.

| Handoff | Local result | Remaining acceptance |
| --- | --- | --- |
| Docs | Guide, standard, registry and templates available. Registry and source checks pass for all 21 entries. | Confirm registry values, license and public access. |
| Builds and CiCd | Warn/fail checker, same-source package hooks and scoped release selector implemented and tested. | Release Builds, deliver pilot config, record hosted results and review length findings. |
| Package maintainers | Package payloads and displayed examples verified for all 14 source-built pilot packages. | Trigger releases and verify the published versions and rendered pages. |
| Platform | Dapr setup uses one isolated path. Clean-host preflight and observer kit available. An isolated empty-cache restore of seven projects took 10.60 seconds. | Finish seven-module operation and collect genuine timed trials. |
| Security maintainer | Metadata inventory covers 53 originals and 53 backups, plus planning entries for all 21 repositories. | Conduct private review and verify admin settings. |
| Workspace and authoring owners | Conversations points to upstream repair `58b8aa36`. Nested inventory completed with zero initialized. The concurrent log and marketplace suites pass locally. | Review for landing. Upstream vendor refresh must preserve or incorporate the authoring fixes. |

The [launch ledger](../implementation-artifacts/launch-ledger.md) records the measured results. The [exposure review](../implementation-artifacts/exposure-review.md) records only aggregate scope and the pending human gate.
