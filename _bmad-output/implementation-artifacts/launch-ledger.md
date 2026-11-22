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

## Exposure review on 22 November 2026

**Docs publication awaits security sign-off.** An automated engineering inventory on 22 November recorded the following committed trees. The security maintainer owns the private review and sign-off. The 19 direct references come from Docs `f2061a2585601bebcd92dd5e69d5000c46717f01`. External BmadSkills was checked at its FR-32 revision, which matched its public `main`. Its separate state-file inventory contains 53 originals and 53 backups. The two planning folders contain **123,676 entries** across the 21 revisions. The security maintainer’s private content disposition is pending for every row. [Baseline, changes and private review procedure](exposure-review.md)

GitHub reported 20 public project repositories and private Docs. On each of the 21, the repository API omitted both protection fields and the code-security configuration request returned HTTP 403. Both requests for `Hexalith/.github` returned HTTP 404 for this integration. The table records the current status on 22 November. A security maintainer with access must verify both effective settings for each target. Reproduce the metadata checks with `gh api repos/Hexalith/REPOSITORY` and `gh api repos/Hexalith/REPOSITORY/code-security-configuration`.

The GitHub repository settings snapshot in Hexalith.Platform at `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` recorded **both controls disabled** for **Hexalith.Platform and Hexalith.Memories** at **2026-11-05 22:26 UTC**. The source record is `parent-platform-and-memories-actual-merge-method-discovery-20261105-2220.json`. The snapshot supplies historical control evidence. The Platform review found no security-maintainer disposition for this Docs revision. FR-65 remains open until both controls are verified enabled for every target.

| Repository | Inventoried revision | Planning entries | Secret scanning | Push protection |
| --- | --- | ---: | --- | --- |
| Hexalith.AI.Tools | `87a738ceeba8975c0b087bc5ecee7dfbc14bf73c` | 0 | Unknown | Unknown |
| Hexalith.Agents | `412528ed47dfa9bd33453784e70aaedc6dc2214d` | 11318 | Unknown | Unknown |
| Hexalith.BmadSkills | `c0b2171aa205ba2743413a7e61732a16762d4b8b` | 28 | Unknown | Unknown |
| Hexalith.Builds | `27fe4d62ca1f3cce07a9f19e1e30b02cbaa51357` | 574 | Unknown | Unknown |
| Hexalith.ChatBot | `cbff0bba2d9736f1a68b999c045a86b04013f30c` | 610 | Unknown | Unknown |
| Hexalith.CiCd | `b7102103ebbe2d3644f9c080834306d890ccbc3d` | 4757 | Unknown | Unknown |
| Hexalith.Commons | `258f9d20e33bd0ae411cf8b3836a26a131f5b9ae` | 0 | Unknown | Unknown |
| Hexalith.Conversations | `a252b7f6cc7f758a7d10bdc745caade0c77cabe1` | 944 | Unknown | Unknown |
| Hexalith.EventStore | `ad93eae92d9468245914fe90168310e0b650d9e1` | 847 | Unknown | Unknown |
| Hexalith.Folders | `73ca79b4fbc09d233cbab5f836507c88894f0420` | 11448 | Unknown | Unknown |
| Hexalith.FrontComposer | `a9e755da2c060f4bf49e0cc2df094bd8a4940df6` | 729 | Unknown | Unknown |
| Hexalith.McpCli | `fac167e6cf1703badf17d2f66780ffa0677d91f9` | 17955 | Unknown | Unknown |
| Hexalith.Memories | `0eb509e87958f2bd27791351a4d262c604677076` | 1084 | Unknown | Unknown |
| Hexalith.Parties | `1783bb2360b08c53276780987b1467c72fb6ba07` | 10028 | Unknown | Unknown |
| Hexalith.Platform | `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` | 23165 | Unknown | Unknown |
| Hexalith.PolymorphicSerializations | `c6d0dfce6dc4f9a0699a51f80baf021ba5ef5d60` | 0 | Unknown | Unknown |
| Hexalith.Projects | `60747ce2183d5bf4e8df3f76b6a7ac8d179369eb` | 21536 | Unknown | Unknown |
| Hexalith.Tenants | `4cf66b848b4627aabfcd74035c84fe08b7e39728` | 3831 | Unknown | Unknown |
| Hexalith.Timesheets | `151fd37308eb08f942040c283209e7886ad954a6` | 5303 | Unknown | Unknown |
| Hexalith.Works | `cd617eb1edc6c51a1459eaa8967e8a5acde4745a` | 9444 | Unknown | Unknown |
| Hexalith.Docs | `f2061a2585601bebcd92dd5e69d5000c46717f01` | 75 | Unknown | Unknown |
| Hexalith/.github | Controls only | — | Unknown | Unknown |

### Public branches beyond the Docs pins

On 22 November the engineering inventory checked all 20 public `main` references against the revisions above. Seventeen matched, including BmadSkills. Three advanced during the inventory. The counts below compare each Docs pin with the observed public tip and cover intervening commits. The private review includes both sets of revisions.

| Repository | Observed public main | `_bmad/` | `_bmad-output/` | Added | Changed | Removed | History only |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Hexalith.EventStore | `2ca76828bf1b9e666b1ed309da4a96f7252290b2` | 43 | 804 | 0 | 0 | 0 | 0 |
| Hexalith.Folders | `d58d5d7a54f63f7223b972f22f11c58510a94119` | 40 | 11410 | 2 | 6 | 0 | 0 |
| Hexalith.FrontComposer | `f73a8f25d5e7b6ddd5f2cfd9f76f08ef0b75d290` | 41 | 689 | 1 | 11 | 0 | 0 |

The Docs count of 75 covers the committed input. This story adds two planning files and edits two others. The security maintainer must reconcile all four and any later changes at the final publication SHA. The Docs maintainer awaits the security maintainer’s disposition for that exact revision.

## Publication and release decisions

| Gate | Evidence required | Owner | State |
| --- | --- | --- | --- |
| Exposure review | [Revision inventory and control checks](#exposure-review-on-22-november-2026) | Security maintainer | Private disposition and effective settings pending. Docs publication awaits disposition for its exact candidate. |
| Registry and public hub | Confirmed module descriptions and categories, signed-out link check | Docs maintainer | Local work under review |
| Hosted pilot checks | Compatible Builds release delivered by CiCd with pilot warning settings, then accepted fail-mode run | CiCd maintainer | Pending release and delivery |
| Public packages | Approved mapping and release version, archive content and rendered page checked for each ID | Pilot release maintainers | Awaiting republish |
| First go/no-go, 1 December | Both pilots, measured review rate, Platform dependency assessment | Launch maintainer | Pending |
| Second go/no-go, 15 December | Qualified agent Try it runs and subsequent outside test in launch sequence | Launch maintainer | Pending |
