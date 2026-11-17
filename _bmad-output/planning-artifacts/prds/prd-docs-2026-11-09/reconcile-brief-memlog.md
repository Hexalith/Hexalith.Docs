---
title: "Reconciliation: brief memlog vs PRD draft"
created: 2026-11-10
source: _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/.memlog.md
target: prd.md, addendum.md (this folder), checked against .memlog.md (this folder)
---

# Reconciliation: brief memlog vs PRD draft

Every entry in the brief's `.memlog.md` (lines 6 to 61, 56 entries) was checked against `prd.md` and `addendum.md`. Entries the PRD memlog records as a deliberate decision or assumption are not reported as gaps.

**Coverage:** 56 entries. 12 are n/a-process (working mode, change and polish notes, or entries superseded by a later one). Of the 44 entries that bear on requirements, 33 are fully carried and 11 are partly carried. No entry is dropped entirely and none is contradicted outright. Partly carried means one part was dropped, weakened, or altered: the named tester, Kubernetes "at launch", stars scope, the planning-folder rule for `Hexalith/.github`, community files in the gate, Hexalith.Docs as a module, "routine" agent tests, and four low items. Overrides were checked: the PRD uses the final value every time (Coverity dropped, contributors added, the BmadSkills check moved into scope, three quickstart blocks rather than four kinds, Docker plus a Kubernetes how-to rather than "local-only", 1,000 stars).

## Entry-by-entry table

| Line | Type | Memlog entry (short) | PRD status |
|---|---|---|---|
| 6 | event | Initial brief: standardize docs across modules per GitHub OSS practice. Written for people, concise top level with details in sub-docs, self-sufficient README. README links NuGet and quality indicators (Coverity, SonarQube, others). | Covered: NFR-1, FR-9, FR-10, FR-22, FR-38. The Coverity part was overridden by line 29, and the PRD uses the final value. |
| 7 | event | 21 module repos plus xppmodel. READMEs run from 0 to 1,275 lines. | Context: Glossary (current repository), §2.2, §6 (xppmodel). |
| 8 | event | About 5 of 20 READMEs presentable. READMEs serve 3 conflicting roles. | Context, addressed by FR-9 and FR-14. |
| 9 | event | Package.props packs the root README into every package, so the README is the NuGet page. | Covered: FR-12, FR-15, §4.2 description. |
| 10 | event | BMAD planning content leaks. Docs are mostly agent-written. aitools has no README rules. | Covered: FR-13, FR-47 to FR-49. |
| 11 | event | No `.github` repo, no SECURITY/SUPPORT/templates, badges with no CI behind them, broken links. | Covered: FR-33 to FR-35, FR-38, FR-39, FR-45. |
| 12 | event | Builds is the de facto enforcement layer. eventstore has unused lint configs. | Covered: FR-41, addendum §B "Existing configs". |
| 13 | event | Side finding: 106 `.claude.json` files in bmadskills, out of brief scope. | Covered with the final value: FR-32 and §7.3 item 6 put it in scope, per lines 57 and 58. |
| 14 | event | A `.github` repo gives org defaults but not LICENSE. Templates copy once with no sync. | Partly covered: FR-33, NFR-5, R-9. No FR requires a LICENSE file in each repository (see Gap 9). |
| 15 | event | nuget.org rendering limits. One README for GitHub and NuGet is a real design decision. | Covered: FR-12, addendum §B NuGet-safe rules. |
| 16 | event | SonarQube Cloud free for OSS. Coverity fragile. Scorecard and Best Practices free. | Covered: FR-40, §6 (Coverity, Scorecard). |
| 17 | event | Org rulesets need a paid plan. Reusable workflows, markdownlint, Vale, and lychee are the realistic path. | Covered: FR-41, FR-42, §6 (Vale, rulesets), addendum §B Enforcement. |
| 18 | decision | User: docs are messy and not harmonized. Goal: simple, crystal-clear documentation. | Covered: §1, NFR-1. |
| 19 | decision | Audience: developers and people who want to use the application, visitors arriving on GitHub. Contributors an open question. | Covered: §2.1. The open question was resolved by line 24. |
| 20 | decision | Core outcome: easy adoption through simple quickstarts, in minutes, with a simple prompt to deploy. Time-to-first-success framing. | Covered: §1, FR-17 to FR-23, FR-51. |
| 21 | assumption | Open points: prompt meaning, deploy target, per-module vs front door, contributor home, stakes. | n/a-process: superseded by lines 22, 23, 28, 35, and 44. |
| 22 | decision | Quickstart offers both an AI prompt and a single command (user: "both"). | Partly covered: FR-6, FR-22, FR-23 ("either the command or the AI prompt"). Only the prompt path is verified (see Gap 8). |
| 23 | decision | Quickstarts both per module and through one front door (user: "both"). Test them against libraries and tooling. | Covered: FR-17, FR-19, FR-21, FR-23, FR-25. |
| 24 | decision | Scope adds contributor docs and policies. | Covered: FR-33 to FR-37. The gate omission is under line 28. |
| 25 | decision | Working mode: coaching. | n/a-process. |
| 26 | event | 11 AppHosts plus platform. Prerequisites make "minutes" impossible. No images. One devcontainer. The mcpcli prompt is about 20 lines. | Covered: FR-5, FR-20, FR-6, §6 (prebuilt images), R-3. |
| 27 | event | Options analysis on 7 proposals. Recommendations pending. | n/a-process: superseded by line 28. |
| 28 | decision | All 7 accepted: devcontainer plus `aspire run`, local-only, AI prompt of 10 lines or fewer; one skeleton; org profile plus docs repo as front door; one NuGet-safe README; NuGet, CI, License, and Sonar badges only; org `.github` defaults plus `docs/development.md`; agent rules plus docs check (warn, then required). | Covered: FR-5, FR-6, FR-8, FR-9, FR-12, FR-17, FR-25, FR-33, FR-36, FR-38, FR-41, FR-42, FR-47. "Local-only" was refined by line 44, and the PRD uses the refined value. Partly weakened: §7.3 doesn't require the org defaults (FR-33) to exist (see Gap 4). |
| 29 | decision | Coverity dropped (user: "2 no"). Codacy dropped with it. | Covered: FR-38, §6. |
| 30 | decision | User: memories, cicd, docs, mcpcli, and others are technical modules. The docs repo is itself a module and follows the standard. | Partly covered: Hexalith.Docs is in scope (Glossary, FR-2, FR-17, FR-43, FR-57), and addendum §A marks the four as confirmed. The Glossary still defines "Module" only for current repositories, and OQ3 doesn't record the confirmed labels (see Gap 6). |
| 31 | assumption | Category plus per-repo quickstart block. Pending. | n/a-process: superseded by line 33. |
| 32 | change | Drafted "The solution". | n/a-process. |
| 33 | decision | Category shown in the catalog. Quickstart blocks chosen per repo, more than one allowed. | Covered: FR-2, FR-17 ("at least one"), FR-25. |
| 34 | decision | "Try it" on the org page points to platform, which deploys the infrastructure the chatbot needs. | Covered: FR-23, FR-25, FR-26. |
| 35 | decision | Stakes: nobody outside the team has tried Hexalith, docs hold back the public launch. Launch-grade rigor. | Covered: §1 "Why now", PRD memlog (stakes: launch). |
| 36 | event | platform README says "empty Aspire AppHost scaffold". The chatbot has M365 mailbox intake. "Try it" prerequisites unverified. | Covered: OQ1, FR-23 note, R-7. |
| 37 | change | Cost of status quo, Try it pointing to platform, AI agents as secondary reader (pending). | n/a-process: content confirmed at line 54. |
| 38 | decision | Platform is in progress. When finished it deploys the chatbot and all services. "Try it" ends in a usable chatbot. Platform completion is a launch dependency. | Covered: FR-23, §6, §10, R-1. |
| 39 | event | platform pulls 17 repos, so a dependency-based launch set covers almost everything. | Covered as context: R-3, rollout option A (FR-57 for all repos). |
| 40 | event | 67 repos, 60 public, 20 current. The other 40 are forks, `_OLD` repos, templates, and stale modules. | Covered: Glossary, FR-25, FR-29, OQ2. |
| 41 | event | Hexalith.Docs is private and must become public. | Covered: FR-31, §7.3 item 5. |
| 42 | event | Round-2 options analysis. Pending. | n/a-process: superseded by line 43. |
| 43 | decision | Round 2 accepted: don't announce until "Try it" works; docs work starts now; demo optional; Level 1 for all 20, Level 2 with Platform first, plus org cleanup; targets 5, 15, and 20 minutes calibrated on a baseline; human test as the launch gate plus a routine agent test. | Covered: FR-26, FR-27, FR-29 to FR-32, FR-51 to FR-58, §7.3, §7.4. "20" became 21, which is deliberate (PRD memlog). "Routine" weakened to event triggers (see Gap 7). |
| 44 | decision | User: "Docker or Kubernetes now; Azure, AWS and Scaleway in future." Interpretation: Docker "Try it" with a time target, a Kubernetes how-to at launch, clouds in the vision. | Partly covered: FR-23, FR-24, §2.2, §6. The Kubernetes how-to isn't in the launch gate or the rollout (see Gap 2). Clouds missing from the Vision (see Gap 10). |
| 45 | decision | Launch targeted for the end of 2026. | Covered: §1, §7.4. |
| 46 | assumption | Docs folders cleaned, not reorganized. xppmodel out. Pending. | Confirmed at line 51. Covered: FR-8, §6. |
| 47 | change | Drafted scope, success criteria, and timeline. | n/a-process. |
| 48 | decision | Platform on track for mid-December. "Try it works" is the fixed condition, end of year the target. | Covered: §1, R-1, §7.4. |
| 49 | decision | Launch-gate tester: Phuong Duong (GitHub `tinouit`). Single-use, so the human test runs once Platform is done. Baseline and iterations use the agent test. | Partly covered: FR-55, R-2, FR-52 to FR-54. The tester's name is dropped (see Gap 1). |
| 50 | decision | Post-launch adoption signal: GitHub stars. Baseline 0 across current public repos, 1 on the legacy repo. | Covered: SM-8. |
| 51 | decision | Confirmed: docs folders cleaned, not reorganized. xppmodel out. | Covered: FR-8, FR-57, §2.2, §6. |
| 52 | change | Updated success criteria and timeline. | n/a-process. |
| 53 | decision | User: 1,000 stars "across the organization within a year of launch, i.e. by end of 2027". Outreach caveat. | Partly covered: SM-8, SM-C5, §6 (outreach). The scope narrowed to "current repositories", and "within a year of launch" was dropped (see Gap 5). |
| 54 | decision | Executive summary, differentiators, and Vision approved. AI agents stay secondary. Docker, Kubernetes how-to, and clouds later stands. | Partly covered: §1, §2.1, FR-23, FR-24, §2.2. The PRD Vision leaves out parts of the approved vision (see Gap 10). |
| 55 | decision | Planning folders stay public in all repos, including Hexalith.Docs and this brief, never linked from READMEs or docs (user chose a). | Partly covered: §0, FR-13, FR-31, FR-56, R-10. Not applied to `Hexalith/.github` (see Gap 3). The FR-31 wording needs a check (see Deliberate changes, item 5). |
| 56 | change | Brief trimmed. Stars, outreach, and the planning-folder rule added. | n/a-process: content covered under lines 53 and 55. |
| 57 | change | Open questions: "Try it" prerequisites, archive list, BmadSkills `.claude.json`. | Covered: OQ1, OQ2, FR-32. |
| 58 | change | Structure polish. Implementation details (`aspire run`, 10 lines or fewer, planning-folder rule) left to the addendum. | n/a-process: the details are carried in FR-6, FR-20, and FR-13. |
| 59 | change | Addendum polish: three quickstart blocks rather than four; four kinds rejected in favor of category plus quickstart blocks; final values (Docker, Kubernetes, clouds later; Coverity dropped). | Covered: Glossary (quickstart block, "Try it" isn't a fourth block), FR-17, FR-2. |
| 60 | change | Prose polish: two named tests; "shared community files" as the one term; SonarQube Cloud bridge; "Run it" published once on target; agent test uses the Platform README. | Partly covered: Glossary, FR-17, FR-53, FR-38. The term drifted to "Community files" (see Gap 11). |
| 61 | event | Finalize, memlog audit. | n/a-process. |

## Gaps

### Gap 1. Named launch-gate tester dropped (medium)

- **Memlog, line 49:** "(decision) Launch-gate stranger tester: Phuong Duong (GitHub tinouit). A stranger test is single-use per person, so the human test runs once Platform is done…"
- **PRD:** FR-55, §7.4 (December row), and §10 ("An outside tester who is available once Platform deploys the chatbot") never name the tester. The PRD memlog has no entry dropping the name. Without it, the dependency reads as unfilled.
- **Fix:** In §10 Dependencies, name the outside tester: Phuong Duong (GitHub `tinouit`), available once Platform deploys the chatbot. Mention the tester in the §7.4 December row as well. If the name was left out on purpose (for example for privacy, because this folder becomes public), log that as a decision instead.

### Gap 2. Kubernetes how-to "at launch" isn't gated or scheduled (medium)

- **Memlog, line 44:** user: "Deploy targets: Docker or Kubernetes now… Kubernetes = deployment how-to guide at launch (no time target)". Line 54 confirms this "stands".
- **PRD:** FR-24 is in §7.1 (in scope), and FR-58 lists the how-to as part of Level 2. But §7.3 says "Try it" is "the only Level 2 item in the launch gate", and no §7.4 row schedules the how-to. As written, the how-to can slip past launch. That weakens the user's "now".
- **Fix:** Add "Platform's Kubernetes how-to exists and passes its FR-24 check" to §7.3. Schedule it in §7.4, for example in the mid-December row once Platform deploys the chatbot. If it's meant to be best effort, log that as a decision.

### Gap 3. Planning-folder and planning-content rules don't reach `Hexalith/.github` (medium)

- **Memlog, line 55:** "Planning folders (_bmad-output/) stay public in all repos… but are never linked from READMEs or docs". Line 10 notes that planning content leaks into READMEs and CONTRIBUTING files.
- **PRD:** FR-13 and the docs check (FR-41, FR-43) cover only the 21 in-scope repositories. The PRD memlog excludes `Hexalith/.github` from the skeleton, but not from these rules. As a result, nothing requires or checks that the front door (`profile/README.md`, the most visible page) and the organization CONTRIBUTING, SECURITY, SUPPORT, and templates are free of internal planning content and `_bmad-output/` links.
- **Fix:** Add a consequence to FR-25 and FR-33 that these files contain no internal planning content (FR-13). Either run the docs check on `Hexalith/.github` in a profile that has the planning-content, link, and badge rules but no skeleton rules, or make this an explicit review item.

### Gap 4. Community files missing from the launch gate (medium)

- **Memlog, lines 24 and 28:** "Scope adds contributor documentation and policies (CONTRIBUTING, CoC, SECURITY, etc.)" and "org .github defaults + per-repo docs/development.md" were accepted. The brief's success criterion 7 says every current repository has the shared community files.
- **PRD:** FR-57 (Level 1) includes FR-34, which deletes local community files, but not FR-33, which creates the organization defaults. §7.3 doesn't list FR-33 either. SM-7 is only a secondary metric. So launch could pass with local files deleted and no organization defaults in place.
- **Fix:** Add FR-33 (with FR-35) to §7.3, for example as part of item 5: "`Hexalith/.github` is public and contains the community files (FR-33)". Or add FR-33 to FR-57's list.

### Gap 5. Stars target: scope narrowed and date anchor dropped (medium)

- **Memlog, line 53:** "Stars target: 1,000 GitHub stars across the organization within a year of launch, i.e. by end of 2027 (user)". Line 50 gives the baseline: "0 stars across all current public repos (1 on the legacy Hexalith repo)".
- **PRD:** SM-8 says "1,000 GitHub stars across current repositories by the end of 2027". "Current repositories" is a defined term (20 repositories), so it excludes Hexalith.Docs, `Hexalith/.github`, and legacy repositories. That silently changes the user's measurement base. "Within a year of launch" is also gone, although the PRD lets the launch date move (§1). No PRD memlog entry covers either change. The extract (item 18) flagged this conflict, but it was resolved without a log entry. The framing (outside the initiative's control, outreach a non-goal, SM-C5) matches the brief.
- **Fix:** Change SM-8 to "across the Hexalith organization". Either keep "within a year of launch (end of 2027 if launch is on time)" or log a decision that end of 2027 is fixed. State how stars are counted, for example the sum of stargazers over the organization's public, non-archived repositories, checked quarterly.

### Gap 6. Hexalith.Docs isn't a "module" under the PRD glossary (low)

- **Memlog, line 30:** "User classifies memories, cicd, docs, mcpcli etc. as 'technical modules'… The docs repo is itself a module and follows the standard."
- **PRD:** The Glossary defines "Module" as "the capability one current repository delivers", and "current repository" excludes Hexalith.Docs. Yet FR-2 and FR-25 give every in-scope row, Docs included, a category. §0 says FRs use Glossary terms exactly, so an agent could conclude that Docs needs no category. Two smaller points: OQ3 asks for every category without recording the four the user confirmed (only addendum §A does), and the Glossary examples (EventStore, Builds, Parties, Timesheets) are unconfirmed guesses.
- **Fix:** Define Module as "the capability one in-scope repository delivers". Have OQ3 note that Memories, CiCd, Docs, and McpCli are confirmed technical modules. Use confirmed examples for technical modules in the Glossary.

### Gap 7. "Routine" agent stranger test weakened to event triggers (low)

- **Memlog, line 43:** "measured by human stranger test as launch gate plus routine agent stranger test". The brief addendum's decision 10 revisits a CI smoke test "if quickstarts keep breaking after launch".
- **PRD:** FR-54 runs the test only on events: the baseline, before publishing, after changes to a quickstart's command or prerequisites, and before launch. Breakage caused by dependency drift, such as a Platform submodule or toolchain bump, wouldn't trigger a run. Then nothing detects the §7.2 revisit trigger.
- **Fix:** Add a recurring run to FR-54, for example monthly after launch on "Try it" and every published "Run it" block, or a run after a Platform release. Tie §7.2's trigger to those results.

### Gap 8. "Both" paths: only the AI-prompt path is verified (low)

- **Memlog, line 22:** "Deploy quickstart offers both an AI-agent prompt and a single command (user: 'both')."
- **PRD:** FR-23 allows "either the command or the AI prompt". The agent stranger test (FR-53) exercises the prompt. FR-55 doesn't say which path the human tester takes, so no gate verifies the command-only path for a human.
- **Fix:** State in FR-55 which path the outside tester uses, for example the command, since the agent test already covers the prompt. Or require both paths to be exercised before launch.

### Gap 9. No explicit LICENSE-file requirement, and Hexalith.Docs has none (low)

- **Memlog, line 14:** "a public Hexalith/.github repo can supply org-wide defaults… but not LICENSE". Line 30 says Docs follows the standard.
- **PRD:** FR-9 (License section, MIT) and FR-39 (the License badge reads the LICENSE file) imply the file, but no FR requires it. Hexalith.Docs has no LICENSE file at its root today (checked: `ls LICENSE*` finds nothing).
- **Fix:** Add a consequence to FR-57 or FR-9: "The repository root contains an MIT LICENSE file". Note that Hexalith.Docs needs one before FR-31.

### Gap 10. Approved Vision only partly carried (low)

- **Memlog, lines 44 and 54:** "cloud providers out of launch scope, listed in vision" and "Executive summary, differentiators and Vision approved as drafted". The approved brief Vision also says a website, hosted demo, and prebuilt images come later, "each one only when demand justifies the effort".
- **PRD:** §1 Vision mentions only Docker. Clouds appear as non-users in §2.2 and as non-goals in §6, not as the stated direction. The demand-justified "later" items appear only as non-goals.
- **Fix:** Add one sentence to §1: "Later, Hexalith deploys to Kubernetes and to Azure, AWS, and Scaleway. A documentation website, hosted demo, and prebuilt images follow when demand justifies them."

### Gap 11. Term drift: "shared community files" (low)

- **Memlog, line 60:** "'shared community files' as the one term".
- **PRD:** §1 uses "Shared community files", but the Glossary defines "Community files", and FR-33 and FR-34 say "organization community files".
- **Fix:** Pick one term (the brief chose "shared community files") and use it in the Glossary and in §4.5.

## Deliberate changes to confirm

These come from PRD memlog decisions and assumptions. Most agree with the brief memlog. The ones below deserve a quick confirmation.

1. **"Try it" link goes live after the agent stranger test, before the human test** (PRD memlog line 25, FR-26). Brief memlog line 43 says "don't announce until Try it works", and the brief addendum's decision 8 says the front door "never promises something the product doesn't do". Showing the link publicly once 2 of 3 agent runs pass is effectively a soft launch, and a real visitor may fail where an agent did. The human test does need the live link, which makes the choice reasonable, but confirm it. An alternative is to have the human tester start from a branch or preview.
2. **Operator runbooks go to a new `docs/operations.md`** (PRD memlog line 23, FR-37). Brief memlog line 28 accepted "per-repo docs/development.md" as the home for runbook content, and the brief addendum says "Runbooks move to docs/development.md". The PRD adds a second per-repository page that the user didn't decide. Probably right, but confirm.
3. **21 in-scope repositories instead of 20** (PRD memlog line 13). This agrees with brief memlog line 30 (Docs follows the standard). No action beyond Gap 6.
4. **"Use the tool" target of 5 minutes** (FR-21, FR-51, OQ7). Brief memlog line 43 set only three targets (5, 15, 20). Flagged as an assumption and an open question, which is acceptable.
5. **FR-31 confirmation before Hexalith.Docs goes public.** This isn't in the PRD memlog. Brief memlog line 55 says planning folders "stay public… including Hexalith.Docs and this brief". FR-31 has a maintainer confirm that `_bmad-output/` "can be published", which could be read as allowing planning content to be removed. Clarify that the check is for sensitive data such as credentials or personal data, not for removing planning artifacts.
