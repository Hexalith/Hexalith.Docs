# Good-spine review of the architecture update

**Verdict.** The update represents all eight findings in the architecture. Two existing eligibility rules still conflict with the updated handoffs. Clarify those rules before treating the document as a build contract. FR-45 retains one explicitly identified product-owner decision.

| Prior finding | Rubric assessment |
| --- | --- |
| Registry and rules revision | AD-6 and AD-15 identify the module revision, immutable Docs acceptance revision, checker identity and matching local/hosted results. Docs supplies its own tree and records the approved external BmadSkills revision. |
| CI ownership and promotion | AD-2 covers 17 managed repositories, two self-managed repositories and the committed caller workflows. AD-8 requires initial planning-pattern calibration across 21 revisions and accepted-revision hosted evidence for each migration. |
| Cross-repository links | AD-7 resolves source-file targets at immutable revisions on every Docs check. Weekly live checks handle moving destinations. The PRD owner must still ratify the split because FR-45 says every run checks every internal link. |
| Builds release | AD-11 identifies both Builds CLI packages, a genuinely qualifying release, owner escalation if the release window is missed and per-ID public verification. AD-9 still needs the applicability correction below. |
| Qualification and public link | AD-4 now requires independent 15- and 20-minute sets on the same revision, the complete same-tenant operation, and subsequent human and Kubernetes evidence. AD-10 still imposes an impossible self-reference. |
| Public exposure | AD-5 requires immediate review of already-public material, reconciliation at closure, private item-level dispositions and a human owner. FR-32 supplies the BmadSkills evidence baseline. |
| Unknown inventory | AD-1 and AD-16 retain BmadSkills in the rollout population and require owner-confirmed inventory before a zero can excuse a republish. |
| Effective catalog | AD-13 ties observed CLI and runtime versions to the Platform candidate’s Builds gitlink. The stack separates the pinned and sibling catalogs. |

## High · Platform cannot meet the generic Run it entry criteria

AD-4 requires Platform’s Run it block before the public link. AD-10 says a block is eligible only with both a module manifest and a direct Platform gitlink. The Platform repository has neither a module manifest at that path nor a gitlink to itself. Its own AppHost is the designated composition owner. A reviewer applying AD-10 literally can refuse a genuinely qualified Platform candidate. Limit the manifest/gitlink criteria to applicable module-workspace routes and state the eligibility criteria for the Platform AppHost route. Preserve the Platform-hosted entry paths for EventStore, Memories and McpCli. The outside tester’s approved path should carry the same 20-minute, same-project success metric, with both manual command and prompt paths demonstrating the operation as FR-23 requires.

Evidence at review: AD-4 lines 77–84, AD-10 lines 136–145, PRD FR-23 lines 534–541, FR-55 lines 985–992 and §8.4 lines 1157–1163. Platform `.gitmodules` and the tracked file inventory confirm the missing self-link and manifest.

## Medium · Sample-step eligibility exceeds the tool publishers’ contract

AD-9 requires every publisher to run its C# sample step before Level 1. The registry gives Builds and McpCli only a Use the tool block. FR-57 requires a successful unaided first tool command for that block and same-revision CI when a package sample is displayed. A C# sample-step requirement for repositories with no such sample can block their migrations or let an empty sample check stand in for the real command. Apply the sample check to an actual displayed package sample, keep the independent tool evidence, and keep AD-11’s complete republish evidence for every package ID.

Evidence at review: AD-9 lines 126–134, AD-11 lines 147–156, PRD FR-57 lines 1023–1031, and the Builds and McpCli rows in `docs/module-registry.json`.

## Product-owner disposition

Track the recorded FR-45 discrepancy until the owner approves the Docs-plus-module checks or specifies a per-module trigger. Operational launch evidence remains with the owners identified in the PRD. An architecture review supplies no hosted fail-mode run, proof of public exposure review, release approval or qualifying stranger test.

## Final disposition after recheck

**Both review findings are closed.** AD-10 now assigns self-hosted modules, Platform-hosted modules and Platform’s own AppHost their applicable entry paths. AD-4 explicitly requires the unaided outside tester to reach the same-tenant create/list result from the public entry page within 20 minutes including prerequisites. The maintainer declares the route and confirms a backup. Both documented command and prompt paths must demonstrate the result.

AD-9 now requires hosted execution for each displayed package sample and the unaided first-command check for a tool-only publisher. AD-11 retains verification of every expected package ID. These rules satisfy the reviewed FR-23, FR-55 and FR-57 handoffs. The previously recorded FR-45 decision remains with the PRD owner.
