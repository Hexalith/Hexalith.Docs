# Technology and implementation review

**21 November 2026.** Reviewed the edited 18-decision spine against the CiCd and Platform parent decisions and the direct module revisions in Docs. One release-owner conflict needs explicit disposition.

| Priority | Finding | Required disposition |
| --- | --- | --- |
| High | AD-11 names Platform as publisher of the stable McpCli tool and McpCli as publisher of Abstractions, then calls the process a paired release. At McpCli `e79b7f8b`, the operational workflow stages and pushes both stable packages under one approval. A second publisher could attempt the same tool ID and version. | Preserve the inherited owner split, record the deployed workflow conflict and hold the documentation republish until the two owners reconcile publication for each ID. Require a single authorized publishing path and its receipt per ID. A missing result keeps acceptance open. |
| Medium | The Stack row labels the run-scoped tool 3.0.0. Platform locks the Abstractions package at that version. Platform builds the local tool from mapped source and binds its loaded content identity to the run. | Identify the locked package and the run-scoped tool separately. Record the candidate McpCli source revision and loaded artifact identity for a qualifying trial. |

**Source evidence.** Platform `abb62da8`, inherited architecture AD-4 and AD-11, lines 109–114, 123 and 190, and `eng/owner-packages.lock.json:44–47`. The Platform gitlinks select McpCli `e79b7f8b` and Builds `fe68718b`. McpCli `README.md:160–168` describes the current paired workflow and its handling of partial publication.

**Remaining scoped checks.** AD-11 reflects the Builds selector that excludes docs, test and style for Builds itself and the two registered CLI IDs. AD-13 distinguishes the candidate Dapr runtime 1.19.1 from the sibling's 1.19.2 and ties trial evidence to the effective catalog revision. The Platform SDK 11.0.100, Aspire 17.0.0 and module tool 6.4.4 match the Platform checkout. The published 6.4.4 CLI and three bundled host runtime configurations target .NET 11. The extra ASP.NET Core 10 prerequisite still appears in the Platform README, and the spine leaves cold-host verification with Platform. CI references v6.4.4 while the checker and README release selector require a later compatible delivery. Planned coverage and the FR-45 reconciliation remain explicit implementation and owner dependencies.

## Final disposition

**Passed on recheck.** AD-11 and the upstream-conflicts table now record the current paired publisher and hold a documentation-triggered republish until the Platform and McpCli owners agree on one publisher and receipt for each ID. That owner action remains open. The Stack now identifies the locked Abstractions package as 3.0.0 and identifies the trial tool by its candidate source and loaded content. Both review findings are closed in the architecture.
