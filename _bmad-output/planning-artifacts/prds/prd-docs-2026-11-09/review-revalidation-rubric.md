# PRD quality review — Hexalith Documentation Standard

Full review of the working PRD and addendum on 20 November 2026.

## Overall verdict

The PRD gives each of the 21 repositories an applicable review path and gives the launch maintainer measurable December decision criteria. The eleven findings from the earlier validation are resolved in the working text. The remaining clarifications concern evidence for pilot promotion, calibrated targets, the order of metadata updates and the calculation of one postlaunch metric.

## Decision-readiness — adequate

Section 8.4 requires two completion forecasts based on observed pilot throughput and actual owner availability. Missing capacity evidence has a stated consequence. For the first pilot’s transition to fail mode, the owner still has to interpret one prerequisite.

- **[medium] Evidence for cross-repository rule tuning is unspecified** (FR-13, FR-42, FR-43, §8.4, addendum §B.2) — FR-13 requires planning-content patterns to be tuned “against all 21 in-scope repositories in warn mode, before any repository switches to fail mode.” FR-43 rolls hosted checks out as CiCd adopts each module, and §8.4 schedules pilot acceptance ahead of later waves. One reviewer could accept a warning-mode checker run over 21 recorded source revisions while another could require a hosted run from every repository before either pilot advances. *Fix:* Specify which evidence satisfies the all-21 tuning prerequisite, who records it, and where the pilot reviewer can find it alongside that pilot’s own hosted checks.

## Substance over theater — strong

FR-19 ties package acceptance to the code shown to readers and the artifact built at that revision. FR-15 checks the actual stable archive and the rendered package page. Section 8.4 identifies the 10.60-second measurement as a restore and gives the full clean-host journey its own qualification. Each evidence type answers a different question.

## Strategic coherence — strong

The primary metrics follow the newcomer to a verified result and the maintainer to sustained documentation checks. Fixed launch criteria, the separate chat upgrade and explicit counter-metrics support that strategy. The 90-day improvement metric needs a scoring convention.

- **[low] The 90-day automation metric lacks a counting rule** (§9, SM-9) — “80% of docs check failures were fixed without a human edit” leaves retries, multiple findings in one failed run, human-reviewed agent fixes and the zero-failure case open to different counts. *Fix:* Define one unit of failure and its resolution evidence, count repeated observations consistently, distinguish human review from human edits, and report the numerator and denominator with an explicit zero-denominator convention.

## Done-ness clarity — adequate

The body differentiates the untimed first package or tool run, the timed two-of-three checks, the separate Platform journeys and the single untimed Kubernetes execution. The designated tool, version, model, prompt and candidate are fixed for a timed set. An ambiguity remains if the maintainer exercises the existing calibration authority.

- **[medium] A calibrated “Run it” target can conflict with its publication gate** (FR-20, FR-51, FR-52, FR-57, FR-58, §8.4) — FR-51 permits calibration of the 15-minute “Run it” target, and FR-52 records a change in the standard. FR-57 and FR-58 still require publication “within 15 minutes.” If the approved target changes to 12 minutes, a 14-minute result would pass one instruction and fail the other. *Fix:* Mark 15 minutes as the initial value and have the publication gate use the approved target for the recorded revision. If Platform has a fixed exception, state it explicitly. Preserve the fixed 20-minute “Try it” requirement.

## Scope honesty — strong

FR-7 distinguishes the parent Docs checkout, 19 direct submodules and the externally approved BmadSkills source. FR-62 applies a GitHub review to all 21 and package-page review to the 16 publishers. D-2 assigns the missing authorized write and end-to-end demonstration to the product owners. The PRD keeps the launch decision pending until the corresponding evidence exists.

## Downstream usability — adequate

Stable requirements and the addendum support extraction by repository and owner. A migration agent can now identify the exact candidate to rehearse and determine what changes invalidate the results. The migration handoff still needs a workable order when a maintainer changes a public description.

- **[medium] The agent’s clean-check handoff can depend on a later human action** (UJ-5 steps 3–4, FR-2, FR-7, FR-11, FR-28, FR-64) — The local check must be clean before the agent hands over the migration. The check compares the candidate description with the live About field and front door, while the next step assigns GitHub settings to the maintainer. When a new description differs from the live one, the agent cannot complete the stated handoff in that order. *Fix:* Identify how a candidate with pending metadata differences is handed to the maintainer, when the authorized owner applies the public changes, and when exact equality is verified before acceptance.

## Shape fit — strong

The document suits a program involving multiple repositories, publishers, end users and human owners. The PRD carries the outcomes, owners and decision points. The addendum carries CI placement, package verification mechanics, runtime pins and trial-record details. The historical registry proposal points readers to the working inventory.

## Mechanical notes

The PRD defines FR-1 through FR-66, UJ-1 through UJ-6 and SM-1 through SM-10 once each. All ten launch conditions are present. The PRD and addendum’s relative Markdown file links resolve in the checkout. Section 13 records the trial threshold and the ledger’s role-only identity convention as decisions. Zero Level 1 acceptances, outstanding public republishing and pending clean-host qualification remain delivery evidence in the ledger.
