# Documentation launch ledger

Baseline on 20 November 2026. Public documentation must not link to this planning record. The module registry owns the expected package inventory. Record a release version and verified count when a maintainer republishes. An empty acceptance date means the gate is open. No repository has been accepted for Level 1 by this course correction.

| Repository | Level 1 date / reviewer role | Readability | Hosted docs check | Verified republish count |
| --- | --- | --- | --- | --- |
| Hexalith.AI.Tools | Pending | Pending | Unverified | Not applicable |
| Hexalith.Agents | Pending | Pending | Unverified | 0 of 6 verified |
| Hexalith.BmadSkills | Pending | Pending | Unverified | Not applicable |
| Hexalith.Builds | Pending | Pending | Unverified | 0 of 2 verified |
| Hexalith.ChatBot | Pending | Pending | Unverified | 0 of 3 verified |
| Hexalith.CiCd | Pending | Pending | Unverified | Not applicable |
| Hexalith.Commons | Pending | Pending | Unverified | 0 of 12 verified |
| Hexalith.Conversations | Pending | Pending | Unverified | 0 of 5 verified |
| Hexalith.Docs | Pending | Pending | Unverified | Not applicable |
| Hexalith.EventStore | Pending | Pending | Unverified | 0 of 14 verified |
| Hexalith.Folders | Pending | Pending | Unverified | 0 of 5 verified |
| Hexalith.FrontComposer | Pending | Pending | Unverified | 0 of 8 verified |
| Hexalith.McpCli | Pending | Pending | Unverified | 0 of 2 verified |
| Hexalith.Memories | Pending | Pending | Unverified | 0 of 10 verified |
| Hexalith.Parties | Pending | Pending | Unverified | 0 of 11 verified |
| Hexalith.Platform | Pending | Pending | Unverified | Not applicable |
| Hexalith.PolymorphicSerializations | Pending | Pending | Unverified | 0 of 2 verified |
| Hexalith.Projects | Pending | Pending | Unverified | 0 of 5 verified |
| Hexalith.Tenants | Pending | Pending | Unverified | 0 of 5 verified |
| Hexalith.Timesheets | Pending | Pending | Unverified | 0 of 6 verified |
| Hexalith.Works | Pending | Pending | Unverified | 0 of 5 verified |

## Pilot evidence on 20 November 2026

The following results are for local candidate changes and the current public feed. The hosted mode and completed-release columns above require a delivered version and maintainer acceptance.

| Pilot | Local Release build, package and example | Docs warning baseline | Latest stable NuGet content |
| --- | --- | --- | --- |
| Commons | 357 tests passed in eight projects. All 12 archives contain the selected README. The repository and core-package examples run against the source-built core package. | Six README length findings. Both pilots’ corrected workflow badges return HTTP 200. | Version 3.0.1 matches 2 of 12 expected READMEs. Six packages have no usable README declaration and four have different text. |
| PolymorphicSerializations | 15 tests passed. Both archives contain the intended README. The two displayed fences produce the expected Volvo (Electric) result in a new consumer. | One README length finding. | Version 2.0.0 matches 0 of 2 expected READMEs. |

Recheck published content with `python3 scripts/verify_published_readmes.py`. Pass `--module` and `--version` after a republish to bind the check to the intended release. The gallery rendering still requires review. The candidate shared checker and docs-only release selector must be published and delivered through CiCd before either pilot can claim hosted acceptance.

## First-run results

| Date | Path | Role and environment | Result | Duration and evidence |
| --- | --- | --- | --- | --- |
| 2026-11-20 | Platform Try it preflight | Engineering audit host, existing checkout | Ineligible. VS Code unavailable and SDK/cache warm. | Timing did not start. Docker responded. Recheck with the clean-host kit. |

The 20-minute target is unmeasured. Record the revision, role, fresh environment, agent/model/version, public prompt, per-step elapsed time, outcome and issue references for each actual run. Promote the Try it link only in the PRD sequence.

An engineering run on 20 November restored seven projects in **10.60 seconds** of wall time. It used `dotnet restore apphost.cs`, SDK 11.0.100, a fresh Platform `b0159ad` checkout with its pinned sibling dependencies, and empty NuGet package and HTTP caches. The measurement ended at restore. Full build, service readiness and the first create/list operation still need timing on a qualifying host.

## Publication and release decisions

| Gate | Evidence required | Owner | State |
| --- | --- | --- | --- |
| Exposure review | All reviewed revisions, original and backup inventory reconciled, protection settings checked | Security maintainer | Private disposition pending |
| Registry and public hub | Confirmed module descriptions and categories, signed-out link check | Docs maintainer | Local work under review |
| Hosted pilot checks | Compatible Builds release delivered by CiCd with pilot warning settings, then accepted fail-mode run | CiCd maintainer | Pending release and delivery |
| Public packages | Approved mapping and release version, archive content and rendered page checked for each ID | Pilot release maintainers | Awaiting republish |
| First go/no-go, 1 December | Both pilots, measured review rate, Platform dependency assessment | Launch maintainer | Pending |
| Second go/no-go, 15 December | Qualified agent Try it runs and subsequent outside test in launch sequence | Launch maintainer | Pending |
