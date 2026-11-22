# Publication exposure review

**22 November 2026 · Awaiting security maintainer disposition.** The inventory starts with the 20 public repositories and then covers private Docs. The security maintainer must review the already-public content and its history immediately, then review the private Docs candidate before publication. Each disposition, remediation decision and credential-owner follow-up belongs in the private review record. The launch ledger identifies the revision inventoried for each repository, both GitHub protection checks and the publication gate. [Launch ledger](launch-ledger.md#exposure-review-on-22-november-2026)

## BmadSkills state files

At `c0b2171aa205ba2743413a7e61732a16762d4b8b`, the complete Git tree under `skills/reports/` contains **53 originals and 53 backups**. Each of the 53 original-file directories also contains one backup in its subtree. All 106 entries require private dispositions. The public `main` ref still pointed to that revision on 22 November. The two planning folders in the table below are a separate inventory.

In the approved private review workspace, enumerate the tree with `git ls-tree -rz --full-tree REVISION -- skills/reports`. Select blobs whose basename is exactly `.claude.json` or starts with `.claude.json.backup`. Match each path and blob identifier to its private disposition and reviewer role. If the branch advances, account for intervening versions, additions and removals before closing FR-32. The security maintainer decides remediation and any history action, and confirms credential-owner follow-up privately.

## Planning folders

The table reconciles the 20 November baseline against the candidate SHAs in the launch ledger. It counts tracked leaf entries recursively at each revision. A zero means the tree was enumerated and contained no entries for that folder. The two folder columns describe the candidate.

“Added”, “changed” and “removed” compare paths and Git object IDs or modes at the two endpoints. A rename counts as a removal and an addition. “History only” counts distinct additional paths touched between those revisions that appear identical or absent at both endpoints. A path can have several intermediate versions. The security maintainer must review intermediate versions even when the path also appears in an endpoint column. The ledger records the public commits that followed four of the current Docs pins. [Public branch check](launch-ledger.md#public-branches-beyond-the-docs-pins)

| Repository | Baseline revision | Baseline entries | `_bmad/` | `_bmad-output/` | Added | Changed | Removed | History only |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Hexalith.AI.Tools | `2a1784bec7d249d815cbd166e01b29fd9ad1f451` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hexalith.Agents | `887ae0f4e85415b9e4bb2db4dc23bd80797b84df` | 11288 | 28 | 11290 | 30 | 13 | 0 | 0 |
| Hexalith.BmadSkills | `c0b2171aa205ba2743413a7e61732a16762d4b8b` | 28 | 24 | 4 | 0 | 0 | 0 | 0 |
| Hexalith.Builds | `6b6eb4eec1b9c718e4d3581fdcbe77f8b09907f1` | 574 | 0 | 574 | 0 | 0 | 0 | 0 |
| Hexalith.ChatBot | `ddd385ec6b37a7bb6362cdc66cb3a1a0def935d3` | 609 | 37 | 573 | 2 | 16 | 1 | 0 |
| Hexalith.CiCd | `d868b8270003db4bd443da59b0d8a260508c6182` | 4656 | 28 | 4729 | 118 | 22 | 17 | 0 |
| Hexalith.Commons | `cb53158b77707794560d4589844fd18189d5b8b4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hexalith.Conversations | `58b8aa365efef02deb53b941f901a6f4c83cb1ed` | 935 | 252 | 692 | 9 | 10 | 0 | 0 |
| Hexalith.EventStore | `c426b454a44a0167d400693997b7cda36028dfbb` | 818 | 43 | 804 | 29 | 13 | 0 | 0 |
| Hexalith.Folders | `97e04cafb4c2e11bbe4cfbd6d50856b940cd7376` | 11439 | 40 | 11410 | 11 | 11 | 0 | 0 |
| Hexalith.FrontComposer | `93171f26494a69b57572e76cbd866cdd5ef51447` | 693 | 41 | 689 | 37 | 26 | 0 | 0 |
| Hexalith.McpCli | `ac34ea908d2817738a174d4b47c6fbdcac898efa` | 17930 | 27 | 17928 | 25 | 11 | 0 | 0 |
| Hexalith.Memories | `4aa7f59bea22281672a916c6043e10e61eaa69f2` | 1059 | 52 | 1032 | 25 | 8 | 0 | 0 |
| Hexalith.Parties | `39ecdc0fafe3797503333a3657284aeabedd0821` | 10004 | 44 | 9984 | 24 | 12 | 0 | 0 |
| Hexalith.Platform | `b0159ad4cd9635b000379e83526f0910225e2a26` | 23102 | 26 | 23139 | 63 | 20 | 0 | 2606 |
| Hexalith.PolymorphicSerializations | `df1a0e5c21ac97d3519fd5acd3059aa3f63f656a` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hexalith.Projects | `b22f615eed36ccc1a1d8414bc335ae7f99d5ba27` | 21528 | 42 | 21494 | 8 | 16 | 0 | 0 |
| Hexalith.Tenants | `929bac5a9881213b05ddeefc0e2ebd5b0327d819` | 3797 | 44 | 3787 | 34 | 8 | 0 | 0 |
| Hexalith.Timesheets | `91bac81ca05fbb328f6d8a5563152f1377e468ca` | 5293 | 31 | 5272 | 10 | 8 | 0 | 0 |
| Hexalith.Works | `e4511b19482e0be618b0a41fc0a3aa1f1b67ba4a` | 9436 | 28 | 9416 | 8 | 13 | 0 | 0 |
| Hexalith.Docs | `820c821e2d67ea84c7b18f820100b068722662e6` | 45 | 29 | 48 | 32 | 6 | 0 | 0 |
| **Total** | | **123234** | **816** | **122865** | **465** | **213** | **18** | **2606** |

### Recheck and close

1. In each owning repository, resolve the ledger and baseline SHAs. Use `git ls-tree -rz --full-tree REVISION -- _bmad _bmad-output` at each endpoint. Compare the two trees with `git diff --no-renames --name-status -z BASELINE CANDIDATE -- _bmad _bmad-output`.
2. In the private workspace, enumerate `git rev-list BASELINE..CANDIDATE` and feed it to `git diff-tree --stdin --root -m -r --no-commit-id --name-only --no-renames -z -- _bmad _bmad-output`. Deduplicate the NUL-delimited paths across all commits and parents. Subtract the set of added, changed and removed endpoint paths from step 1. The number of remaining distinct paths is “History only.” For private dispositions, retain the commit and each parent from `git rev-list --parents BASELINE..CANDIDATE` and compare each parent to its commit with `git diff-tree -r --raw --no-abbrev --no-renames -z PARENT COMMIT -- _bmad _bmad-output`. For a root commit, compare against the empty tree with `git diff-tree --root`. Retain each affected path, old/new blob IDs and disposition privately, including versions later removed. Verify that the baseline is an ancestor. If history diverges, review both histories from the common ancestor. Recheck every public tip and the proposed Docs revision at closure.
3. For each of the 22 targets, verify **secret scanning** and **push protection** independently in admin-visible GitHub settings. Record the date and effective status of each control. An omitted field, denied request or inaccessible repository leaves that control unknown.
4. Freeze the exact Docs commit proposed for publication. Resolve its 19 gitlinks with `git ls-tree -r --full-tree CANDIDATE -- references`. Reconcile each changed pin and the story’s committed planning changes against the ledger using steps 1 and 2. The security maintainer confirms privately that sensitive planning material has moved to a private repository, any confirmed sensitive state data has been removed, and credential owners have revoked any exposed credentials, as applicable. All 22 repositories must have both protections confirmed enabled.
5. Record the security maintainer’s dated disposition and exact Docs SHA in the private review record outside the candidate commit. Immediately before changing visibility, the Docs maintainer compares the proposed commit to that signed-off SHA. A different SHA requires a new reconciliation and disposition. The ledger can reference the accepted revision afterward.
