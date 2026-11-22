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

**Docs is public.** On 22 November the project owner, acting as security maintainer, signed off on published Docs commit `98f268b5dc331766a39ac25e8c980c45a858a23a`. Its tree matches the head of PR #1, including all 19 gitlinks and 77 Docs planning entries. The overview, documentation standard and registry were accessible signed out. [Published revision](https://github.com/Hexalith/Hexalith.Docs/commit/98f268b5dc331766a39ac25e8c980c45a858a23a)

Engineering verified the public tips during the **12:08–12:09 UTC** check on 22 November. The inventory uses Docs at `6e184b5ef360dfebb242ecb66e4fd36d62897261`, all 19 gitlinks in that commit and the external FR-32 BmadSkills revision. These 21 trees contain **123,683 planning entries**. The fetched public `main` revisions contain **123,709**. At the BmadSkills revision, 53 original state files each have one backup. Those 106 files are counted separately. On 22 November the project owner approved the 106 BmadSkills files and the inventoried planning changes to remain public. The private disposition covers the BmadSkills revision in the table and the planning revisions recorded in Docs `6bf073afae5fb321414922a435bc5d57c852d303`. [Folder counts, changes since baseline and review procedure](exposure-review.md)

At 11:56 UTC on 22 November, GitHub returned public metadata for all 21 project repositories. The metadata omitted both effective settings and every code-security configuration request returned HTTP 403. Both requests for `Hexalith/.github` returned HTTP 404. At 12:18–12:19 UTC, engineering requested both protections be enabled through the repository settings API. GitHub denied all 21 project updates with HTTP 403 and identified `administration=write` as the required permission. The community repository update returned HTTP 404. A separate read after each request left both effective settings unknown on all 22 targets. The two control columns record that readback. Repeat with `gh api repos/Hexalith/REPOSITORY` and `gh api repos/Hexalith/REPOSITORY/code-security-configuration`.

The GitHub repository settings snapshot in Hexalith.Platform at `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` recorded **both controls disabled** for **Hexalith.Platform and Hexalith.Memories** at **2026-11-05 22:26 UTC**. The source record is `parent-platform-and-memories-actual-merge-method-discovery-20261105-2220.json`. The snapshot supplies historical control evidence. That snapshot predates the Docs publication decision. FR-65 remains open until both controls are verified enabled for every target.

| Repository | Docs inventory revision | Planning entries | Fetched public `main` | Planning entries on `main` | Secret scanning | Push protection |
| --- | --- | ---: | --- | ---: | --- | --- |
| Hexalith.AI.Tools | `87a738ceeba8975c0b087bc5ecee7dfbc14bf73c` | 0 | `06e486be2ced925b4494760254ac05af76cbb1f2` | 0 | Unknown | Unknown |
| Hexalith.Agents | `0d98305f91899a088ddad0b0a23a596453913274` | 11320 | `c586d2d43ed981797b249a73581fd97294073d74` | 11320 | Unknown | Unknown |
| Hexalith.BmadSkills | `c0b2171aa205ba2743413a7e61732a16762d4b8b` | 28 | Same revision | 28 | Unknown | Unknown |
| Hexalith.Builds | `27fe4d62ca1f3cce07a9f19e1e30b02cbaa51357` | 574 | Same revision | 574 | Unknown | Unknown |
| Hexalith.ChatBot | `cbff0bba2d9736f1a68b999c045a86b04013f30c` | 610 | `555183e984db2adca2175aa214f43d8cab53692e` | 610 | Unknown | Unknown |
| Hexalith.CiCd | `e3a5af309b5006ad30621e3a713ecb2d0033ea20` | 4757 | `9f7a56fd1e0de05f6b8a8789fba983c072ce3db6` | 4758 | Unknown | Unknown |
| Hexalith.Commons | `258f9d20e33bd0ae411cf8b3836a26a131f5b9ae` | 0 | `5f646d4e49279cca0d31ab577e91719c3ed7e434` | 0 | Unknown | Unknown |
| Hexalith.Conversations | `a252b7f6cc7f758a7d10bdc745caade0c77cabe1` | 944 | `6f446d536d621c45d13f0057a65e5f8ad6dea471` | 944 | Unknown | Unknown |
| Hexalith.EventStore | `2ca76828bf1b9e666b1ed309da4a96f7252290b2` | 847 | `8319318850530d756db5b8b7555d0b9f804361e9` | 850 | Unknown | Unknown |
| Hexalith.Folders | `d58d5d7a54f63f7223b972f22f11c58510a94119` | 11450 | `1c8da626f05b25b36dbc5813d68bc44da09a27f4` | 11450 | Unknown | Unknown |
| Hexalith.FrontComposer | `4cecae4e44a98ccd379c0327f258217c010046da` | 730 | `8199bcf7def7d9ddb39b1704429ba611d59fc08e` | 730 | Unknown | Unknown |
| Hexalith.McpCli | `fac167e6cf1703badf17d2f66780ffa0677d91f9` | 17955 | `91abf6df53a9f415e0c8be06e17aaf7c42ec55ac` | 17966 | Unknown | Unknown |
| Hexalith.Memories | `0eb509e87958f2bd27791351a4d262c604677076` | 1084 | `7f8da6e31fa23d1302972ea98f5c283eb3edc9c0` | 1085 | Unknown | Unknown |
| Hexalith.Parties | `1783bb2360b08c53276780987b1467c72fb6ba07` | 10028 | `cc691319b8ee622198f7d8d93a87f85a86b9fd8a` | 10029 | Unknown | Unknown |
| Hexalith.Platform | `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` | 23165 | `b0124db4976acf354e164148859b59e9d6863e3c` | 23165 | Unknown | Unknown |
| Hexalith.PolymorphicSerializations | `c6d0dfce6dc4f9a0699a51f80baf021ba5ef5d60` | 0 | `99c2344f08d3e3560a891f79ab63f8722fa14e60` | 0 | Unknown | Unknown |
| Hexalith.Projects | `60747ce2183d5bf4e8df3f76b6a7ac8d179369eb` | 21536 | `8d6b11b12e60762f9bf2c1e7acd8d2d997a94e6d` | 21539 | Unknown | Unknown |
| Hexalith.Tenants | `1e6d2aa2be64771a96b0dbe84289e0bf88611311` | 3831 | `1161d9f356f62c9f7044d4c536a4653a37898212` | 3831 | Unknown | Unknown |
| Hexalith.Timesheets | `151fd37308eb08f942040c283209e7886ad954a6` | 5303 | Same revision | 5303 | Unknown | Unknown |
| Hexalith.Works | `cd617eb1edc6c51a1459eaa8967e8a5acde4745a` | 9444 | `f72c7832bafd5b8d502eafb140248b557a4e6714` | 9450 | Unknown | Unknown |
| Hexalith.Docs | `6e184b5ef360dfebb242ecb66e4fd36d62897261` | 77 | Same revision | 77 | Unknown | Unknown |
| Hexalith/.github | Controls only | — | — | — | Unknown | Unknown |

### Public branches beyond the Docs pins

At 08:59 UTC on 22 November, 16 of the 20 public `main` revisions matched the inventory at Docs `e56c1a9e082d8b97f715811f655d50c420fa2795`, including BmadSkills. The other four tips together added two planning paths and modified 20. At that check, those public changes and their intermediate versions awaited the security maintainer’s disposition. Across the observed public tips and private Docs, the two trees contain 123,683 entries.

| Repository | Observed public main | `_bmad/` | `_bmad-output/` | Added | Changed | Removed | History only |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Hexalith.Agents | `0d98305f91899a088ddad0b0a23a596453913274` | 28 | 11292 | 2 | 8 | 0 | 0 |
| Hexalith.CiCd | `e3a5af309b5006ad30621e3a713ecb2d0033ea20` | 28 | 4729 | 0 | 3 | 0 | 0 |
| Hexalith.FrontComposer | `4cecae4e44a98ccd379c0327f258217c010046da` | 41 | 689 | 0 | 4 | 0 | 0 |
| Hexalith.Tenants | `1e6d2aa2be64771a96b0dbe84289e0bf88611311` | 44 | 3787 | 0 | 5 | 0 | 0 |

The 08:59 UTC inventory incorporated the EventStore, Folders and FrontComposer tips from the preceding inventory. At that point Docs contained 77 planning entries. Since Docs `f2061a2585601bebcd92dd5e69d5000c46717f01`, two planning files had been added and two modified. PR #1 then modified the exposure review, launch ledger and story record. The published merge retained all 77 paths and all 19 pins.

### Public revisions at the owner’s sign-off

At 11:35 UTC on 22 November, the published Docs tree and its 19 gitlinks matched the PR head. The BmadSkills revision also matched its earlier observation. Fourteen of the other public repositories advanced beyond the 08:59 UTC check. Across those fourteen, nine planning paths were added and 17 were modified. The comparison found zero removals and zero additional paths touched only in intermediate commits. The 21 public trees then contained 123,692 planning entries. The table compares each new public tip with its previous observation. The owner’s Docs sign-off covers the published Docs SHA and the pins it records.

| Repository | Public revision at 11:35 UTC | `_bmad/` | `_bmad-output/` | Added | Changed |
| --- | --- | ---: | ---: | ---: | ---: |
| Hexalith.AI.Tools | `06e486be2ced925b4494760254ac05af76cbb1f2` | 0 | 0 | 0 | 0 |
| Hexalith.Agents | `c586d2d43ed981797b249a73581fd97294073d74` | 28 | 11292 | 0 | 2 |
| Hexalith.ChatBot | `523dae0f44fded0738d68f019cc5ddedfb8f0456` | 37 | 573 | 0 | 0 |
| Hexalith.CiCd | `9f7a56fd1e0de05f6b8a8789fba983c072ce3db6` | 28 | 4730 | 1 | 0 |
| Hexalith.Commons | `5f646d4e49279cca0d31ab577e91719c3ed7e434` | 0 | 0 | 0 | 0 |
| Hexalith.Conversations | `6f446d536d621c45d13f0057a65e5f8ad6dea471` | 252 | 692 | 0 | 0 |
| Hexalith.EventStore | `10c716a4fa885a0c2a30574373e44944788560c8` | 43 | 806 | 2 | 1 |
| Hexalith.FrontComposer | `a79cc810fafbebcb392a413d24b99ffa70326d58` | 41 | 689 | 0 | 0 |
| Hexalith.McpCli | `4863f413803b8b789e360900f9fcfa6aca9fb024` | 27 | 17932 | 4 | 9 |
| Hexalith.Memories | `719820dbca5fb95e2f16f796b8a1124b2194d210` | 52 | 1033 | 1 | 4 |
| Hexalith.Parties | `382407df93d1b7da40cd624f9fe6c46e53f7ec06` | 44 | 9985 | 1 | 1 |
| Hexalith.PolymorphicSerializations | `99c2344f08d3e3560a891f79ab63f8722fa14e60` | 0 | 0 | 0 | 0 |
| Hexalith.Projects | `baf6fa066d973eb50bfbb2d53168146da01968d6` | 42 | 21494 | 0 | 0 |
| Hexalith.Works | `c7008797038c0967fde81fe3c190a25e9d712241` | 28 | 9416 | 0 | 0 |

### Post-publication reconciliation

Since the signed-off Docs revision, Docs changed three planning files and advanced the Agents, CiCd, FrontComposer and Tenants pins to the four revisions in the 08:59 UTC table. Across those four pin ranges, two planning entries were added and 20 changed. The five ranges had zero removals and zero history-only paths. The security maintainer’s recorded sign-off applies to `98f268b5dc331766a39ac25e8c980c45a858a23a`. The owner’s subsequent approval covers the changes inventoried in `6bf073afae5fb321414922a435bc5d57c852d303`. That commit changed three Docs planning records, retained the same 77 entries and preserved all 19 gitlinks.

At the fetched public tips, 17 repositories were ahead of the current Docs pins. Across those ranges, 26 planning entries were added and 89 changed, with zero removals and zero history-only paths. The following public tips advanced since the 11:35 UTC observation. Their new revisions and counts appear in the inventory above.

| Repository | Public revision in the preceding observation | `_bmad/` on main | `_bmad-output/` on main | Added | Changed | Removed | History only |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Hexalith.ChatBot | `523dae0f44fded0738d68f019cc5ddedfb8f0456` | 37 | 573 | 0 | 4 | 0 | 0 |
| Hexalith.Docs | `98f268b5dc331766a39ac25e8c980c45a858a23a` | 29 | 48 | 0 | 3 | 0 | 0 |
| Hexalith.EventStore | `10c716a4fa885a0c2a30574373e44944788560c8` | 43 | 807 | 1 | 5 | 0 | 0 |
| Hexalith.Folders | `d58d5d7a54f63f7223b972f22f11c58510a94119` | 40 | 11410 | 0 | 2 | 0 | 0 |
| Hexalith.FrontComposer | `a79cc810fafbebcb392a413d24b99ffa70326d58` | 41 | 689 | 0 | 4 | 0 | 0 |
| Hexalith.McpCli | `4863f413803b8b789e360900f9fcfa6aca9fb024` | 27 | 17939 | 7 | 45 | 0 | 0 |
| Hexalith.Memories | `719820dbca5fb95e2f16f796b8a1124b2194d210` | 52 | 1033 | 0 | 4 | 0 | 0 |
| Hexalith.Parties | `382407df93d1b7da40cd624f9fe6c46e53f7ec06` | 44 | 9985 | 0 | 0 | 0 | 0 |
| Hexalith.Platform | `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` | 26 | 23139 | 0 | 2 | 0 | 0 |
| Hexalith.Projects | `baf6fa066d973eb50bfbb2d53168146da01968d6` | 42 | 21497 | 3 | 4 | 0 | 0 |
| Hexalith.Tenants | `1e6d2aa2be64771a96b0dbe84289e0bf88611311` | 44 | 3787 | 0 | 1 | 0 | 0 |
| Hexalith.Works | `c7008797038c0967fde81fe3c190a25e9d712241` | 28 | 9422 | 6 | 6 | 0 | 0 |

## Publication and release decisions

| Gate | Evidence required | Owner | State |
| --- | --- | --- | --- |
| Exposure review | [Revision inventory and control checks](#exposure-review-on-22-november-2026) | Security maintainer | Project owner signed off on the published Docs revision on 22 November. The owner approved continued public visibility for the inventoried follow-up revisions and external BmadSkills files. Verification of both GitHub protections across all 22 targets remains pending. |
| Registry and public hub | Confirmed module descriptions and categories, signed-out link check | Docs maintainer | Overview, standard and registry verified signed out. Maintainer confirmation of registry content remains pending. |
| Hosted pilot checks | Compatible Builds release delivered by CiCd with pilot warning settings, then accepted fail-mode run | CiCd maintainer | Pending release and delivery |
| Public packages | Approved mapping and release version, archive content and rendered page checked for each ID | Pilot release maintainers | Awaiting republish |
| First go/no-go, 1 December | Both pilots, measured review rate, Platform dependency assessment | Launch maintainer | Pending |
| Second go/no-go, 15 December | Qualified agent Try it runs and subsequent outside test in launch sequence | Launch maintainer | Pending |
