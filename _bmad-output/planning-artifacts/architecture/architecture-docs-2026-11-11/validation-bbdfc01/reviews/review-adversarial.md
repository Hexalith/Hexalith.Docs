# Independent adversarial review

**Verdict.** Revise the cross-repository checking contract and the qualification handoff before teams use this draft to accept migrations or publish the organization link. The examples below are counterexamples to the written decisions. None asserts that a release or a trial passed.

Reviewed on 21 November 2026 against Docs `bbdfc01`, Builds `e1380b81` and the refreshed direct submodules. Line numbers refer to those checkouts. “PRD” refers to `_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md`.

## High · The module check and migration can select different registry revisions

A module owner takes the newly confirmed description from Docs revision B when migrating its README. A Builds author ships identity checking against the same authoritative JSON captured at revision A with a checker release. Both can run locally and in hosted CI against immutable files. The module then fails for using the newly approved wording. The opposite mismatch is possible if a migration retains the older wording. AD-1 specifies one authority and AD-2 pins the checker. Neither identifies which Docs revision both consume for this migration, how it reaches the checkout or which record selects it.

**Evidence.** The PRD requires the registry to feed the migration and the docs check, and requires verbatim agreement across the README, About and front door. The pilot checker currently takes the root, repository and mode and checks README readability, length and badge paths. It supplies no precedent for selecting the registry input. Schema version 1 identifies the JSON format and survives ordinary changes to a description. Spine lines 25–33. PRD lines 232–244 and 395–399. `docs/module-registry.json` line 2. `references/Hexalith.Builds/Github/lib/docs_check.py` lines 36–65 and 85–103.

**Discuss with Docs, Builds and CiCd.** Bind a module migration and its local and hosted checks to the same immutable Docs registry revision or content digest. Record the selection with the accepted module revision and define who advances it. Build and storage layout can remain with the owners.

## High · Cross-repository Hexalith links have conflicting check schedules

The Builds team treats a link from Commons to a Docs guide as external to the checkout and leaves it for migration and the weekly check. A module owner implementing FR-45 expects that same link to be checked on every run because both repositories belong to Hexalith. After a target moves, one process can go green while the other expects a finding. Fetching a mutable default branch during CI would also undermine AD-2’s reproducibility promise. The current texts agree on same-repository files and public third-party hosts. They give different instructions for a sibling repository.

**Evidence.** FR-45 explicitly requires an every-run check for links inside the organization. D-LINK places other Hexalith destinations in migration checking. Story 2.1 distinguishes repository-local checks from scheduled external checks. The present pilot checker looks up same-repository badge workflow files. Spine lines 29–33. PRD lines 824–832. `docs/documentation-standard.md` line 22. `_bmad-output/planning-artifacts/epics.md` line 45. `references/Hexalith.Builds/Github/lib/docs_check.py` lines 36–41 and 63–65.

**Discuss with the requirements and checker owners.** Reconcile the cadence, evidence and failure behavior for same-organization cross-repository links. To retain FR-45 and commit reproducibility together, define the immutable sibling reference or versioned target inventory available on every run. Keep the live external report and migration-time network verification separately identifiable.

## High · The organization can publish “Try it” before Platform qualifies “Run it”

Suppose two of three independent Platform rehearsals finish the full create/list journey in 18 minutes, with the first call at minute 16. A profile owner reading AD-4 and the delivery table can release the link after the 20-minute set. The Platform README owner applying FR-58 must withhold the 15-minute “Run it” block. The link can point to a README whose qualifying block is still unpublished. The PRD already settles this sequence, so resolving it requires no new performance target.

**Evidence.** The spine binds the kit, Platform and the Try it link, then records only the 20-minute qualification and outside test in the delivery table. The PRD separates the gate for publishing the link from the gate for announcing launch. It requires two separate candidate qualifications before the link and the outside trial afterwards. The observer already defines distinct journeys and milestones. Spine lines 41–45 and 70–76. PRD lines 582–590, 963–966 and 1157–1163. `tools/stranger-test.py` lines 14–27. `docs/stranger-test.md` lines 5–10.

**Autofix in an approved update.** Make AD-4 refer to the PRD §8.4 promotion sequence. Require separate passing 15-minute and 20-minute sets at the same candidate, each using the designated tool, version, model and prompt for that journey. Name the public-link handoff before the human trial and the human gate before announcement.

## Medium · Unknown package inventory can count as a verified nonpublisher

The registry producer includes the external BmadSkills row and uses an empty ID list while ownership and inventory review are pending. A ledger consumer treats that exact representation as zero expected packages and marks republication inapplicable. Both follow the 21-row inventory convention. An automated capacity or release rollup cannot distinguish this case from an owner-confirmed nonpublisher. The authority for an unreviewed inventory matters even if the eventual confirmed count is zero.

**Evidence.** The BmadSkills row contains zero IDs and a null source. The validator requires the count to equal the number of IDs, requires a null source for an empty list and skips external checkout evidence. The ledger already records the package cell as “Not applicable” while the migration remains pending. The PRD directs the team to retain the pending migration until the owner supplies the external revision. Spine lines 25–27. PRD line 313 and lines 1029–1031. `docs/module-registry.json` lines 68–83. `scripts/validate_registry.py` lines 65–74 and 98–102. `_bmad-output/implementation-artifacts/launch-ledger.md` lines 3–10.

**Discuss with the registry and ledger owners.** Define how a consumer distinguishes inventory awaiting evidence from confirmed zero. Require an owner-approved revision or equivalent source before a pending external row can be counted as exempt from package verification.

## Boundaries that held

The spine assigns Docs, module, Builds, CiCd, Platform and McpCli responsibilities. Its package table requires per-ID rendered-page review and AD-5 assigns release and exposure decisions to human owners. Those existing rules exclude substituting a passing unit suite for a published package review or publishing item-level security findings in the ledger.
