# Publication exposure review

The security maintainer owns the private review. The Docs maintainer may change visibility after reviewing the resulting disposition. Only aggregate inventory and review status belong here. The audit did not inspect credential contents, revoke credentials or establish admin settings.

## BmadSkills state files

At commit `c0b2171aa205ba2743413a7e61732a16762d4b8b`, the complete Git tree includes **53 originals and 53 backups** under `skills/reports/`. Enumerating only the exact basename misses the backups. Each of the 106 private review rows needs a path, blob identifier, reviewer role and disposition. State-file remediation and history decisions belong to the security maintainer. Status on 20 November 2026 is **awaiting owner review**.

Rebuild the inventory in a private review workspace with the repository already available.

```sh
git ls-tree -r --full-tree c0b2171aa205ba2743413a7e61732a16762d4b8b -- skills/reports |
  awk -F '\t' '$2 ~ /(^|\/)\.claude\.json(\.backup[^\/]*)?$/'
```

Match the 106 entries against private dispositions. For secret scanning and push protection, record an admin-visible check for each repository and the organization community repository. A missing field in the API response leaves the status unknown. Check file content and history through the owner's approved private process.

## Planning folders

The inventory below counts tracked entries beneath `_bmad/` and `_bmad-output/` at each source revision. Counts describe review scope. Reconcile intervening changes, including the Docs changes under review, before any public visibility change. For a fixed revision, enumerate entries privately with `git ls-tree -r --full-tree REVISION -- _bmad _bmad-output`.

| Repository | Revision | Planning entries | Owner review |
| --- | --- | ---: | --- |
| Hexalith.AI.Tools | `2a1784bec7d2` | 0 | Pending |
| Hexalith.Agents | `887ae0f4e854` | 11288 | Pending |
| Hexalith.BmadSkills | `c0b2171aa205` | 28 | Pending |
| Hexalith.Builds | `6b6eb4eec1b9` | 574 | Pending |
| Hexalith.ChatBot | `ddd385ec6b37` | 609 | Pending |
| Hexalith.CiCd | `d868b8270003` | 4656 | Pending |
| Hexalith.Commons | `cb53158b7770` | 0 | Pending |
| Hexalith.Conversations | `58b8aa365efe` | 935 | Pending |
| Hexalith.Docs | `820c821e2d67` | 45 | Pending |
| Hexalith.EventStore | `c426b454a44a` | 818 | Pending |
| Hexalith.Folders | `97e04cafb4c2` | 11439 | Pending |
| Hexalith.FrontComposer | `93171f26494a` | 693 | Pending |
| Hexalith.McpCli | `ac34ea908d28` | 17930 | Pending |
| Hexalith.Memories | `4aa7f59bea22` | 1059 | Pending |
| Hexalith.Parties | `39ecdc0fafe3` | 10004 | Pending |
| Hexalith.Platform | `b0159ad4cd96` | 23102 | Pending |
| Hexalith.PolymorphicSerializations | `df1a0e5c21ac` | 0 | Pending |
| Hexalith.Projects | `b22f615eed36` | 21528 | Pending |
| Hexalith.Tenants | `929bac5a9881` | 3797 | Pending |
| Hexalith.Timesheets | `91bac81ca05f` | 5293 | Pending |
| Hexalith.Works | `e4511b19482e` | 9436 | Pending |
