---
title: 'Story 1.1 — Reconcile exposure'
type: 'chore'
created: '2026-11-22'
status: 'in-progress'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

Give the security maintainer a revision-bound inventory of already-public planning material and of the Docs candidate before publication. Reconcile BmadSkills originals and backups at the specified revision, count both planning folders in each of the 21 repositories and account for intervening changes. Verify secret scanning and push protection separately on all 21 and the organization community repository.

Record aggregate scope, observed control states, role and review status in the exposure record and launch ledger. The security maintainer owns the private content review, dispositions and credential-owner follow-up. The Docs maintainer can change visibility after the security disposition covers the exact publication revision.

</frozen-after-approval>

## Implementation Notes

- Reconciled the 21 committed inventories at Docs `e56c1a9e082d8b97f715811f655d50c420fa2795`, its 19 gitlinks and the FR-32 BmadSkills revision. The two planning trees contain 123,681 entries. The BmadSkills state-file inventory has 53 originals, each paired with a backup.
- Compared all 20 public main branches. Agents, CiCd, FrontComposer and Tenants advanced beyond the current Docs pins. Their public changes add two planning paths and modify 20. The exposure review and launch ledger record the pinned and public revisions and the changes since baseline.
- The project owner signed off as security maintainer on 22 November for published Docs commit `98f268b5dc331766a39ac25e8c980c45a858a23a`. The ledger records the 11:35 UTC public revisions. The GitHub integration returned unknown effective settings for both protections on all 22 targets.

## Review Triage Log

- Medium, corrected. FR-65 requires both settings enabled on all 22 targets. A verified disabled setting keeps the gate open.
- Medium, corrected. The private closure procedure now covers removal or relocation of sensitive material and credential-owner revocation where applicable.
- Medium, corrected. The ledger records a live check across all 20 public repositories and separately reconciles the branches that advanced beyond their Docs pins.
- Medium, corrected. The private review retains each commit, parent and affected blob identity so a path changed several times receives version-level review.
- Medium, corrected. The security maintainer binds the disposition to the final SHA outside the candidate commit. The Docs maintainer compares that SHA immediately before changing visibility.
- Low, corrected. The ledger identifies the automated engineering inventory and its date separately from the security maintainer’s pending disposition.

- Medium, corrected. The history-only calculation now removes endpoint paths after deduplicating paths across commits and merge parents.
- Low, corrected. The ledger restores the preceding Docs SHA so maintainers can reproduce the two additions and two modifications.
- Medium, corrected. The review and ledger identify immediate review of public content and intermediate versions as outstanding maintainer work.
- Medium, corrected. The closure procedure now resolves all 19 gitlinks from the final Docs commit and reconciles any changed pins against the inventory.
