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

The engineering inventory earlier that day recorded the following committed trees. The security maintainer owns the private review and sign-off. The 19 direct references come from Docs `e56c1a9e082d8b97f715811f655d50c420fa2795`. External BmadSkills was checked at its FR-32 revision, which matched its public `main`. Its separate state-file inventory contains 53 originals and 53 backups. The two planning folders contain **123,681 entries** across the 21 revisions. The inventory predates the owner’s sign-off on the published Docs revision. [Baseline, changes and private review procedure](exposure-review.md)

GitHub reported 20 public project repositories and private Docs. The engineering recheck completed at 08:53 UTC on 22 November and found no effective value for either protection in the metadata of any of the 21 repositories. Each code-security configuration request returned HTTP 403. Both requests for `Hexalith/.github` returned HTTP 404 for this integration. The table records the API observations at 08:53 UTC. A later API check after publication again returned unknown effective settings for all 22 targets. Reproduce the metadata checks with `gh api repos/Hexalith/REPOSITORY` and `gh api repos/Hexalith/REPOSITORY/code-security-configuration`.

The GitHub repository settings snapshot in Hexalith.Platform at `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` recorded **both controls disabled** for **Hexalith.Platform and Hexalith.Memories** at **2026-11-05 22:26 UTC**. The source record is `parent-platform-and-memories-actual-merge-method-discovery-20261105-2220.json`. The snapshot supplies historical control evidence. That snapshot predates the Docs publication decision. FR-65 remains open until both controls are verified enabled for every target.

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
| Hexalith.EventStore | `2ca76828bf1b9e666b1ed309da4a96f7252290b2` | 847 | Unknown | Unknown |
| Hexalith.Folders | `d58d5d7a54f63f7223b972f22f11c58510a94119` | 11450 | Unknown | Unknown |
| Hexalith.FrontComposer | `f73a8f25d5e7b6ddd5f2cfd9f76f08ef0b75d290` | 730 | Unknown | Unknown |
| Hexalith.McpCli | `fac167e6cf1703badf17d2f66780ffa0677d91f9` | 17955 | Unknown | Unknown |
| Hexalith.Memories | `0eb509e87958f2bd27791351a4d262c604677076` | 1084 | Unknown | Unknown |
| Hexalith.Parties | `1783bb2360b08c53276780987b1467c72fb6ba07` | 10028 | Unknown | Unknown |
| Hexalith.Platform | `0f6468edbb8efd4e47fb272286cb1bfd5baa3255` | 23165 | Unknown | Unknown |
| Hexalith.PolymorphicSerializations | `c6d0dfce6dc4f9a0699a51f80baf021ba5ef5d60` | 0 | Unknown | Unknown |
| Hexalith.Projects | `60747ce2183d5bf4e8df3f76b6a7ac8d179369eb` | 21536 | Unknown | Unknown |
| Hexalith.Tenants | `4cf66b848b4627aabfcd74035c84fe08b7e39728` | 3831 | Unknown | Unknown |
| Hexalith.Timesheets | `151fd37308eb08f942040c283209e7886ad954a6` | 5303 | Unknown | Unknown |
| Hexalith.Works | `cd617eb1edc6c51a1459eaa8967e8a5acde4745a` | 9444 | Unknown | Unknown |
| Hexalith.Docs | `e56c1a9e082d8b97f715811f655d50c420fa2795` | 77 | Unknown | Unknown |
| Hexalith/.github | Controls only | — | Unknown | Unknown |

### Public branches beyond the Docs pins

At 08:59 UTC on 22 November, 16 of the 20 public `main` revisions matched the inventory above, including BmadSkills. The other four tips together added two planning paths and modified 20. The security maintainer must review those public changes and their intermediate versions immediately. Across the observed public tips and private Docs, the two trees contain 123,683 entries.

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

## Publication and release decisions

| Gate | Evidence required | Owner | State |
| --- | --- | --- | --- |
| Exposure review | [Revision inventory and control checks](#exposure-review-on-22-november-2026) | Security maintainer | Project owner signed off on the published Docs revision on 22 November. Verification of the two effective settings is pending. |
| Registry and public hub | Confirmed module descriptions and categories, signed-out link check | Docs maintainer | Overview, standard and registry verified signed out. Maintainer confirmation of registry content remains pending. |
| Hosted pilot checks | Compatible Builds release delivered by CiCd with pilot warning settings, then accepted fail-mode run | CiCd maintainer | Pending release and delivery |
| Public packages | Approved mapping and release version, archive content and rendered page checked for each ID | Pilot release maintainers | Awaiting republish |
| First go/no-go, 1 December | Both pilots, measured review rate, Platform dependency assessment | Launch maintainer | Pending |
| Second go/no-go, 15 December | Qualified agent Try it runs and subsequent outside test in launch sequence | Launch maintainer | Pending |
