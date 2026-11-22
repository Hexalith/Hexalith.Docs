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

- Reconciled both planning folders at Docs `6e184b5ef360dfebb242ecb66e4fd36d62897261`, its 19 gitlinks and external BmadSkills. The exposure review records the 123,683 pinned entries and changes since baseline. The launch ledger records the 123,709 entries on the 21 fetched public branches and the changes since the signed-off revision. Recounted 53 BmadSkills originals, each paired with one backup at the FR-32 revision.
- The project owner signed off as security maintainer on published Docs `98f268b5dc331766a39ac25e8c980c45a858a23a`. The owner subsequently approved continued public visibility for the 106 BmadSkills files and the planning changes inventoried in Docs `6bf073afae5fb321414922a435bc5d57c852d303`.
- The 22 November request to enable secret scanning and push protection returned HTTP 403 on all 21 project repositories and HTTP 404 on `Hexalith/.github`. The subsequent reads left both settings unknown. FR-65 and story 1.1 remain in progress pending verification that both protections are enabled on all 22 targets.

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

- Medium, corrected. The ledger identifies the separate private disposition still required for the external BmadSkills inventory (FR-32).
- Low, corrected. The public-tip check and the GitHub settings check each have a UTC time.
- Low, corrected. The latest public changes show both planning-folder counts for each advancing repository.
- Medium, corrected. The exposure procedure explains how to bind the post-publication disposition to a commit and record the result.
- Medium, corrected. The ledger identifies its own pending changes as outside the inventory until committed and reconciled.
