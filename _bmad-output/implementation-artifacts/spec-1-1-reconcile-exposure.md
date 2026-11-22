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

- Updated the exposure review and launch ledger against Docs `f2061a2585601bebcd92dd5e69d5000c46717f01`, its 19 direct references and the specified BmadSkills SHA. The inventory includes endpoint changes and paths touched only in intermediate commits.
- Checked the repository metadata and code-security configuration endpoints for all 22 targets. The dated Platform snapshot provides historical settings for Platform and Memories. The current settings and private review still require security-maintainer evidence.
- The final publication SHA must include reconciliation of this story’s working-tree changes. The story and the publication decision remain pending.

## Review Triage Log

- Medium, corrected. FR-65 requires both settings enabled on all 22 targets. A verified disabled setting keeps the gate open.
- Medium, corrected. The private closure procedure now covers removal or relocation of sensitive material and credential-owner revocation where applicable.
- Medium, corrected. The ledger records a live check across all 20 public repositories and separately reconciles three branches that advanced beyond their Docs pins.
- Medium, corrected. The private review retains each commit, parent and affected blob identity so a path changed several times receives version-level review.
- Medium, corrected. The security maintainer binds the disposition to the final SHA outside the candidate commit. The Docs maintainer compares that SHA immediately before changing visibility.
- Low, corrected. The ledger identifies the automated engineering inventory and its date separately from the security maintainer’s pending disposition.
