---
title: "Adversarial review: PRD Hexalith Documentation Standard"
reviewed: prd.md, addendum.md (prd-docs-2026-11-09)
reviewer: adversarial-general
date: 2026-11-10
---

# Adversarial review: Hexalith Documentation Standard PRD

> FR-31 will publish this folder, so this review avoids repeating sensitive details. It points to the source files instead.

## Verdict

The PRD reads well, but it is a plan for a workspace that no longer exists. It was written as if Hexalith.Builds were still the CI lever and Hexalith.CiCd were empty. But CiCd holds a final architecture, dated 2026-11-08, that makes it the only writer of every module's workflows. Its rules block module agents from pushing `.github/workflows/**`, freeze the Builds files the docs check would extend, and cut back the required-status-check rules the PRD asks for. The launch gate rests on three claims nobody checked:

- **"Platform deploys the chatbot by mid-December."** Platform's own MVP leaves the chatbot out, and its local seven-module story is still in backlog.
- **"An outside tester."** The tester named in the brief is the second organization owner, which makes them a maintainer by the PRD's own glossary.
- **"Agents can open the dev container and run one command."** The repositories' own agent entry points tell a fresh clone's agent to stop.

Below that, the FRs contradict one another. Platform and Hexalith.Docs can't reach Level 1 as written. CiCd is required to offer a "Use the tool" quickstart for a tool that doesn't exist. Nearly half of the existing `docs/` pages trip internal-planning patterns that the PRD makes unsuppressible, which invites agents to delete pages in bulk across 21 repositories. One maintainer, who wrote nearly every commit in the workspace, is expected to review all of it, republish about 100 packages, and run the stranger tests in seven weeks that include the holidays.

Under NFR-3, the PRD fails its own honesty rule: "reported on track" is a claim with nothing measured behind it. Fix the critical findings before epics are drafted. Otherwise the stories will send agents to edit files that CiCd will revert within the hour.

Counts: **4 critical, 9 high, 13 medium, 6 low.**

Evidence below comes from the pinned submodule checkouts under `references/` in this workspace. Live `main` may differ. Check before acting.

---

## Critical

### C-1. The PRD collides with Hexalith.CiCd's final architecture and has no CI ownership model

- **Location:** FR-40, FR-41, FR-42, FR-43, FR-15, FR-57, UJ-5, UJ-6, §10, addendum §A (CiCd row) and §B (Mode, Enforcement, Package republish), Open Question 5.
- **Quotes:**
  - "Each repository sets its own mode in the workflow file that calls the docs check, where reviewers can see it."
  - "the docs check is a required status check on each default branch [ASSUMPTION: enforced through branch protection]"
  - "The Hexalith.Builds reusable CI runs the SonarQube Cloud scanner"
  - "Use the tool (it has no content yet)"
- **Why it fails:**
  - `references/Hexalith.CiCd/_bmad-output/planning-artifacts/architecture/architecture-cicd-2026-11-07/ARCHITECTURE-SPINE.md` (status: final) settles these points:
    - CiCd's `deliver.yml` "is the only writer of owned files into modules".
    - The guard fails a PR that changes owned files ("CI/CD is owned by Hexalith.CiCd. Fix the product code, not the pipeline."), and the restore job reverts such changes on push to `main` (AD-4, AD-8).
    - AD-20 freezes every Builds file a module uses today, including `domain-ci.yml`, "until the last module has moved". So the "Hexalith.Builds reusable CI" that FR-40 and FR-41 extend can't change.
  - `SPEC.md` and `enforcement.md` in `_bmad-output/specs/spec-cicd/` add three more constraints:
    - Module agents' tokens have no Workflows write, so GitHub rejects their pushes to `.github/workflows/**` (`enforcement.md:7`). The Level 1 migration agent of UJ-5 can't flip warn mode to fail mode.
    - Rulesets on `main` block only deletion and force-push, and stricter ones are "cut back". Delivery checks that rulesets are "exactly the AD-21 ones" (`enforcement.md:60-61`, spine AD-6). FR-42's required status check would be removed, or would break delivery.
    - The SPEC lists "Enforcement through human review, CODEOWNERS, or required-status-check rulesets" as out of scope and states "Agents push directly to `main`" (`SPEC.md:155`, `:201`). That empties FR-57's "maintainer reviewed the migration pull request" and UJ-5.
  - Semantic-release config "exist[s] only in Builds" (AD-4). Releases run by nightly dispatch, so addendum §B's release rule isn't something a Level 1 story can add.
  - CiCd is the hub of that design, not an empty repository. The registry row and Open Question 5 are false.
  - In UJ-6, an agent "moves the release note to GitHub Releases". In CiCd's model, the App and the release workflow own releases.
- **Fix:** Make Hexalith.CiCd a named dependency and co-owner. Deliver the docs check and Sonar through CiCd's `setup/<Repo>.yml`, the render, and the new `ci.yml`, not the frozen `domain-ci.yml`. Express mode as a `hexalith-ci.json` knob. Replace "required status check" with CiCd's actual enforcement layers: guard, nightly pre-dispatch, and hourly delivery. Run a reconciliation pass against the CiCd spine before epics. Delete "it has no content yet".

### C-2. The launch dependency contradicts Platform's own tracked plan

- **Location:** §1, FR-23, R-1, §7.4, §10, glossary ("Hexalith").
- **Quotes:**
  - "Platform deploys the chatbot (reported on track)."
  - "One command (`aspire run` in the dev container) deploys the chatbot and every service it needs."
- **Why it fails:**
  - Platform's PRD defines a seven-module MVP: EventStore, Tenants, Parties, Folders, Projects, McpCli, and Memories (`references/Hexalith.Platform/_bmad-output/planning-artifacts/prds/prd-platform-2026-09-27/extract-platform-brief.md:30`). ChatBot isn't in it, and `epics.md` never mentions the chatbot.
  - "Run all seven MVP modules together locally" (story 3-6) is in backlog. Epics 6 to 10 are in backlog, and the latest change proposal (2026-11-08) is about containing a sprawling Story 2.8.
  - ChatBot describes itself as a "governed email-to-project orchestration module". Its chat surface is its Epic 10, and its `sprint-status.yaml` shows epics 2 to 13 in backlog. That contradicts its own README, so neither source supports mid-December.
  - ChatBot's AppHost "fails closed if `ChatBot:LiveRecoveryValidation:MailboxClientSecret` is not configured". That is a `dotnet user-secrets` step before the "one command".
  - The PRD carries a verbal report as fact, which violates NFR-3. The November "baseline" of "Try it" (FR-52) will measure a path that doesn't exist.
- **Fix:** Before epics, have the Platform owner write down, in Platform's own planning, which story delivers "chatbot reachable through `aspire run` from Platform" and when. Until then, label R-1 "unverified", not "on track". Add a go/no-go date (for example, 2026-12-01). If no chat surface runs from Platform by that date, re-plan launch to Q1, or redefine "Try it" around what Platform actually ships, such as the seven-module McpCli path.

### C-3. The only identified human tester fails the PRD's own definition of "outside tester"

- **Location:** glossary ("Outside tester", "Maintainer", "Newcomer"), FR-55, R-2, §10.
- **Quotes:**
  - "Outside tester. A newcomer outside the team who runs the human stranger test."
  - "Maintainer. A Hexalith team member with admin rights"
  - "An outside tester who is available once Platform deploys the chatbot."
- **Why it fails:** The PRD's input brief names the launch-gate tester and their GitHub handle. The same handle is recorded as the organization's second owner and as an admin collaborator on CiCd and Builds (`references/Hexalith.CiCd/_bmad-output/specs/spec-cicd/stories/1-maintainer-preconditions-and-remaining-checks.md:52,245`, `references/Hexalith.Platform/eng/repository-controls/README.md:11`). The tester is also a named writer of Platform's operations repositories (Platform architecture `.memlog.md`). By the PRD's glossary, that makes them a maintainer. The launch gate's one human run is void before it starts, and the PRD names no backup, though FR-55 needs one if the first run fails. A hostile reader will ask on launch day whether an org owner was the "stranger".
- **Fix:** Add a testable eligibility rule to FR-55: no organization membership, no commits, no access, and no prior exposure to Hexalith repositories. Record how eligibility was verified. Recruit two eligible testers now, a primary and a reserve, and list them in §10 without publishing their names in `_bmad-output/`.

### C-4. FR-32 treats live credential exposure as a launch checklist item

- **Location:** FR-32, §7.3 item 6, §7.4 (November), Open Question 8.
- **Quotes:**
  - "No sensitive data is exposed in Hexalith.BmadSkills at launch."
  - "Before launch, someone reviews the 106 `.claude.json` files"
- **Why it fails:**
  - Hexalith.BmadSkills is already one of the 20 *public* current repositories. If those eval-run `.claude.json` files hold tokens, OAuth account data, or MCP server credentials, they have been scrapable since they were pushed. "At launch" is the wrong deadline.
  - "Someone" is not an owner.
  - Removing the files at HEAD does nothing for credentials already in history. Open Question 8 (rewrite history?) is the wrong first question: revocation comes first.
  - The brief also announces, in a planning folder that will be published, that these files "may hold sensitive content". That points readers straight at the files.
- **Fix:** Pull this out of the docs plan and do it today. Have a named maintainer review the files. Revoke and rotate anything found, whether or not history is rewritten. Enable secret scanning and push protection on BmadSkills and Hexalith.Docs; CiCd's plan already covers its managed modules (spine, onboarding steps). Then decide on history. In the PRD, keep only "done, with a dated record" as a gate check.

---

## High

### H-1. The repositories' agent entry points will halt the newcomer's AI prompt

- **Location:** FR-48, addendum §B (Agent entry points), FR-6, FR-22, UJ-1, UJ-3, SM-2.
- **Quote:** "Every in-scope repository's agent entry points (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`) lead to the documentation rules."
- **Why it fails:**
  - 16 of the repositories checked out here carry the shared baseline: "If no permitted location exists, stop and report the missing baseline as a blocker." The required file lives in `references/Hexalith.AI.Tools`, a submodule that a plain `git clone` or a Codespace doesn't populate.
  - A newcomer's agent that opens Tenants (UJ-3), or Platform once FR-48 adds the baseline there (Platform has none today), loads CLAUDE.md first and stops by design. The same baseline loads maintainer-grade rules into a newcomer session: commitlint validation, "run the AppHost before changing code", and no dependency updates.
  - The addendum's fix, "verify … that this chain resolves when the repository is cloned on its own", checks the maintainer chain, not what the newcomer experiences.
  - "Wraps exactly one command" also hides real steps: clone, initialize 17 root submodules (Platform), and set user secrets (ChatBot).
- **Fix:**
  - Add an FR: the agent entry points must let a quickstart run in a fresh clone without submodules. For example, the baseline gains a "quickstart/consumer mode" carve-out, or the AI prompt tells the agent which instructions apply.
  - Make the agent stranger test start from `git clone` with no submodules, so it catches the halt.
  - Count clone and submodule initialization inside the "one command", or stop calling it one command.

### H-2. The docs check will fail nearly half of `docs/` with unsuppressible rules, and agents will mass-delete

- **Location:** FR-13, FR-41, FR-46, FR-8, FR-1, addendum §B (candidate patterns), §0.
- **Quotes:**
  - "Rules for internal planning content and badges can't be suppressed [ASSUMPTION]."
  - "Existing `docs/` folders are cleaned, not reorganized."
- **Why it fails:**
  - In the local checkouts, 431 of 973 `docs/**/*.md` files match the addendum's patterns (about 2,800 "Story N", about 2,360 `_bmad-output`, about 390 "Epic N", and about 280 FR, NFR, or SM IDs). Another 180 files contain 40-character hexadecimal SHAs. EventStore alone has 324 docs pages.
  - Some matches are legitimate: pinned commits in a development guide (Platform requires "submodules checked out at exact commits"), or SHA-pinned actions that the addendum itself recommends ("pin the action to a commit SHA"). Under FR-46, those can never pass.
  - The standard (`docs/documentation-standard.md` in Hexalith.Docs, inside `docs/`) has to quote `_bmad-output` and the FR-ID pattern to explain the ban, so it fails its own check.
  - Every repository's BMAD config sets `project_knowledge: "{project-root}/docs"` (`_bmad/bmm/config.yaml`), so BMAD workflows will keep writing planning content back into `docs/` after launch. The PRD never touches that config.
  - An agent told to reach fail mode with no suppression, where "content it proposes to delete" is just a list item, will take the shortest path and delete pages or strip SHAs. That happens across 21 repositories, with one reviewer.
- **Fix:**
  - Scope the hard check to README, CONTRIBUTING, and pages linked from the README. Report the rest of `docs/` in warn mode until it has been triaged.
  - Allow per-line suppressions with a reason, inside fenced code blocks, and in the standard itself. Keep the suppression count visible (FR-46 already does this).
  - Add an FR that moves BMAD's `project_knowledge` out of `docs/`, or excludes BMAD-owned paths.
  - Require the migration prompt to *move* planning-only pages to `_bmad-output/` rather than delete them, and to stop and escalate when deletions exceed N files.

### H-3. Level 1 deadlocks for Platform, Hexalith.Docs, and CiCd, and the front door can't be published

- **Location:** FR-17, FR-25, FR-26, FR-2, FR-57, §7.4, addendum §A.
- **Quotes:**
  - "A "Run it" block is added only once it meets its time target (FR-58). Until then, the README keeps its other blocks."
  - "Hexalith.Docs has no package, service, or tool, so its Quickstart section links to "Try it" and to the standard"
  - "shows the "Try it" link (FR-26)"
- **Why it fails:**
  - **Platform:** Platform has no packages, and its only block is "Run it". It can't publish that block before the agent stranger test passes, which requires the chatbot. So Platform has zero blocks and fails FR-17 and FR-57 until mid-December at the earliest, yet §7.4 finishes Level 1 for "all 21" in "late November to early December".
  - **Hexalith.Docs:** Docs's quickstart contains no block, which contradicts FR-17's first bullet ("at least one quickstart block, named exactly…"). It also links to "Try it" before FR-26 allows that link anywhere.
  - **CiCd:** CiCd must ship a "Use the tool" block, with an install command, expected output, and a 5-minute agent test, for a control-plane repository that no newcomer installs.
  - **Front door:** FR-25 requires the "Try it" link in the first 10 lines, and FR-26 forbids it until the agent test passes. So the front door can't be published in November or early December in any form FR-25 accepts.
- **Fix:**
  - Allow a "Coming soon: Try it" stub, or no quickstart, for Platform until Level 2, and exempt Platform's Level 1 from FR-17.
  - Give Docs and CiCd a defined "no quickstart" variant that the docs check recognizes.
  - Let the front door publish without the link (FR-26 already describes that state) and drop "first 10 lines" from FR-25 until the link exists.

### H-4. "Run it" for business modules rests on AppHosts the architecture rules say must not exist

- **Location:** FR-5, FR-20, FR-58, UJ-3, addendum §A (Parties, Tenants, Projects, Timesheets: "Run it").
- **Quote:** "Each module with an Aspire AppHost publishes a "Run it" block"
- **Why it fails:**
  - `hexalith-llm-instructions.md` states: "A domain module **must not** ship its own `*.AppHost`, `*.Aspire`, or `*.ServiceDefaults` project". It also says "AppHost lives in the platform/host repo".
  - Tenants ships `Hexalith.Tenants.AppHost` and `Hexalith.Tenants.Aspire` today. ChatBot's roadmap retires its standalone Aspire packages, and its README calls the retained AppHost "a local-development umbrella only".
  - Agents read both the PRD's stories and those rules. Some will build dev containers and "Run it" blocks around AppHosts. Others will delete those AppHosts as architecture violations. Sofia's UJ-3 path disappears the day the architecture rule is enforced.
- **Fix:** Decide where "Run it" starts for business modules. One option is a Platform composition scoped to the module, which matches Platform's Epic 1, "develop a module against its minimum environment". Write that decision into FR-20. Remove "Run it" from business-module rows unless the architecture owner grants an explicit exception.

### H-5. FR-15 plus the addendum's release rule is a mass-republish trigger

- **Location:** FR-15, R-11, addendum §B (Package republish), §7.3 item 3.
- **Quotes:**
  - "a maintainer publishes a new version of every package that the repository publishes, before launch."
  - `{ type: "docs", scope: "readme", release: "patch" }`
- **Why it fails:**
  - The local checkouts have about 100 packable `src/` projects. If `docs(readme)` triggers a patch, every README typo fix an agent makes publishes the whole package set of that repository, permanently. NuGet versions can't be deleted, only unlisted.
  - In CI package mode, Platform consumes module packages (Platform PRD addendum). Two weeks of version churn across 18 repositories lands right on Platform's mid-December stabilization.
  - The rule must live in Builds' shared release config, which CiCd owns (C-1). CiCd's SPEC already fixes Builds releases to skip `docs`.
  - "An agent verifies each package page" covers about 100 pages with no stated check method, and nuget.org indexing lags.
- **Fix:** Use a one-time, maintainer-dispatched release per repository after migration, not a standing commit-type rule. State the expected package count per repository. Script the page check against the nuget.org README endpoint. Freeze republishing during Platform's stabilization window.

### H-6. The timeline assumes review capacity that doesn't exist

- **Location:** §7.4, R-4, Open Question 6, FR-54, FR-57.
- **Quotes:**
  - "Late November to early December | Level 1 migration of all 21 in-scope repositories, each switching to fail mode and republishing its packages."
  - "Open Question 6 asks who reviews."
- **Why it fails:**
  - Commit history across the local checkouts: about 18,400 commits by one maintainer, about 400 by one other contributor, and the rest by bots. Open Question 6 already has an answer: one person.
  - That person is also driving the CiCd migration and the Platform work, and this PRD gives them all of the following:
    - 21 migration reviews
    - triage of about 430 `docs/` files
    - accuracy checks on every linked page (FR-57, which is unverifiable without reading)
    - about 100 package republishes
    - agent stranger tests at three runs each, with friction logs, for about 20 blocks before launch (FR-54), on re-imaged clean machines
    - organization admin chores
  - All of that fits in about 7 weeks, including the Christmas week. The PRD sets no slip-decision date, so slippage will be discovered on 2026-12-28.
- **Fix:** Answer Open Question 6 with a number of reviews per week, now, and derive the scope from it. Add explicit milestones with go/no-go dates. Rank repositories (Platform's dependency chain and the packages on the front door first), and allow a "Level 1 lite" for low-traffic repositories such as CiCd, BmadSkills, and AI.Tools.

### H-7. The launch gate's human test has no pass criteria, no machine spec, and a loophole for excluded steps

- **Location:** FR-55, FR-51, FR-53, SM-1, SM-C4, glossary ("Clean machine").
- **Quotes:**
  - "is timed to the chatbot's first reply. The target is 20 minutes or less."
  - "Every excluded step must be listed."
  - "Clean machine. A machine with Docker and VS Code installed and no Hexalith toolchain"
- **Why it fails:**
  - FR-53 requires "without human help" for the agent test, but FR-55 never says that for the human test. A maintainer nudging the tester still produces a pass.
  - The path isn't fixed (command or AI prompt?), so one route goes untested by any human.
  - OS, CPU, RAM, disk, and bandwidth are unspecified. Building 17 repositories inside Docker-in-Docker on a Windows laptop with 8 GB of RAM and a home connection is a different universe from a maintainer's workstation. A tester's own development machine usually isn't "clean" (it has a .NET SDK), so somebody prepares one, and preparing it can quietly warm caches.
  - SM-C4 *permits* excluded steps as long as they're listed, which contradicts FR-51 ("The timer includes everything the reader must obtain").
  - The agent test for "Try it" starts at the Platform README (FR-53, SM-2), while the gate starts at the front door. No agent ever exercises the front-door hop.
- **Fix:**
  - Define a pass: no help, a single path declared in advance, and a clock that runs from opening `github.com/Hexalith`.
  - Publish a reference machine profile: OS, minimum specs, and a bandwidth floor. Ship a script that verifies a machine is clean.
  - Delete the SM-C4 exclusion clause.
  - Start the agent "Try it" test at the front door.

### H-8. "The agent opens the dev container" isn't shown to be possible, and NFR-8 is only checked against prompt text

- **Location:** UJ-1, FR-6 steps 1–5, FR-18, NFR-8, NFR-9.
- **Quotes:**
  - "The agent opens the dev container, runs the one command, waits for services to be healthy, and gives her the URL."
  - "The prompt never asks the reader to paste a secret into the agent conversation (NFR-8)."
- **Why it fails:**
  - A terminal agent on a clean host can't "open" a VS Code dev container without the devcontainer CLI, which needs Node, and Node isn't on the clean machine.
  - An in-editor agent loses its session when VS Code reopens in the container.
  - This is the headline launch feature, and no FR proves the mechanism or names a supported agent and tool set.
  - On secrets, the testable consequence inspects the *prompt*, not the agent's behavior. Faced with an interactive key prompt it can't answer, the agent's path of least resistance is "paste your key here". FR-6 passes while NFR-8 is violated.
- **Fix:** Name the supported agent tools and their versions. Spike the mechanism now: a devcontainer CLI install counted in the timer, or "open the container yourself, then paste the prompt inside it". Add a friction-log check that fails a run if the agent asked for a secret in chat. Ship a secrets step the agent can hand off, for example "edit `.env` yourself, then say done".

### H-9. Public planning folders publish security-relevant detail that only Docs gets reviewed for

- **Location:** FR-13 ("`_bmad-output/` stays in each repository and stays public"), FR-31, FR-56, R-10.
- **Quotes:**
  - "Before Hexalith.Docs goes public, a maintainer confirms that all its contents, including `_bmad-output/`, can be published."
  - "Results are stored in Hexalith.Docs under `_bmad-output/`, public but never linked"
- **Why it fails:**
  - FR-31 reviews only Docs. The other 20 repositories' planning folders are already public, and launch will send traffic to them.
  - Platform's `_bmad-output/` holds plenty for an attacker: internal network addresses of the staging cluster, the identity-provider realm and auth host, the registry's access policy, accepted in-transit and token-exchange risks, and owner identities (for example, `planning-artifacts/architecture/architecture-platform-2026-09-27/.memlog.md`).
  - FR-56 publishes human stranger-test friction logs, and possibly the tester's identity, in a public folder.
  - "Never linked" isn't protection: GitHub search and the file tree expose everything.
- **Fix:** Add an FR: before launch, a named maintainer runs secret scanning plus a manual "attacker-useful" review over every in-scope repository's `_bmad-output/` and `_bmad/`, and moves sensitive operations material to a private repository. Keep human-tester records anonymized, or private. Revisit brief decision 11 for Platform at least.

---

## Medium

### M-1. NFR-5 "one source per rule" is broken by FR-47's self-contained copy

- **Location:** NFR-5, FR-1, FR-47, FR-49.
- **Quote:** "One source per rule. The standard states each rule once." / "The file is self-contained"
- **Why it fails:** The AI.Tools authoring rule forbids linking out, so `hexalith-docs-instructions.md` has to restate every rule. That gives two hand-maintained copies, the standard and the agent file, plus 21 template copies, which is exactly the drift NFR-5 says can't happen.
- **Fix:** Declare one source of truth (the agent file or the standard) and generate the other, or have a docs check rule compare the rule IDs and wording in both.

### M-2. The 40-line Quickstart can't hold what FR-18, FR-19, FR-20, and FR-22 require

- **Location:** FR-10, FR-17, FR-18, FR-19, FR-22.
- **Quote:** "The Quickstart section fits on one screen [ASSUMPTION: 40 lines of Markdown or fewer]."
- **Why it fails:** Count one "Use the package" block: prerequisites, a fenced `dotnet add`, a compiling sample with usings, and a fenced AI prompt of up to 10 lines. That's about 35 lines. Add a "Run it" block (prerequisites, container, `aspire run`, first call, expected result, prompt) and the total passes 70. Every two-block repository in the registry fails by construction, and SM-C1 then forbids the only way to comply. "The first block is the action a reader is most likely to take first" isn't testable.
- **Fix:** Budget per block (for example, 30 lines each, 60 for the section). Allow the AI prompt in a collapsed or linked form only if FR-22 changes. Replace "most likely" with "the registry's first listed block".

### M-3. SonarQube Cloud in shared CI has no token, no fork-PR story, and no "red gate" policy

- **Location:** FR-38, FR-40, UJ-4, §10.
- **Quote:** "Results appear for default-branch builds and for pull requests." / "one organization token"
- **Why it fails:**
  - CiCd's story 1 has just restricted the legacy `SONAR_TOKEN` to old, non-current repositories and forbids `secrets: inherit`.
  - Fork PRs get no secrets, so Tomás's first PR (UJ-4) either goes red or skips analysis, and "results for pull requests" fails. The `pull_request_target` workaround is a known security footgun.
  - On launch day, some READMEs may show a failing quality gate or single-digit coverage. Nothing says whether that's acceptable.
- **Fix:** Route the Sonar design through CiCd. Specify the fork-PR behavior ("skipped, not failed"). Decide whether a failing gate blocks the Level 1 sign-off.

### M-4. FR-39's "badge URLs resolve" can't detect a dishonest badge

- **Location:** FR-39, SM-6.
- **Quote:** "Every badge link resolves to the same repository, and the docs check verifies that badge URLs resolve."
- **Why it fails:** A Shields badge for a wrong or nonexistent package normally comes back as an image ("not found", "invalid"), not as a broken URL, so "resolves" is true for a lying badge. "Resolves to the same repository" is also false by design for the NuGet and Sonar badges, which link to nuget.org and sonarcloud.io.
- **Fix:** Check the badge *parameters* instead: the workflow file exists on the default branch, the Sonar project key matches the repository, and the package ID is one this repository packs. Reword "same repository" to "is about this repository".

### M-5. Fail mode will flag links that are correct

- **Location:** FR-12, FR-45, FR-42, FR-31, NFR-7.
- **Quote:** "Every docs check run checks internal links (within the Hexalith organization) and badge URLs, and in fail mode a broken one fails the job."
- **Why it fails:**
  - The migration PR creates `docs/development.md` and `docs/operations.md` and links them with absolute `…/blob/main/…` URLs, which return 404 until the PR merges. The PR that switches to fail mode fails itself.
  - Every README links to Hexalith.Docs (the standard and guides), which FR-31 keeps private until launch, so those links 404 for lychee.
  - Unauthenticated github.com checks get rate-limited (429) at scale.
- **Fix:** Rewrite `main` URLs to the PR head for internal checks. Make Docs and `.github` public at the *start* of migration, not at launch. Require an authenticated lychee setup and treat 429 as a retry, not a failure.

### M-6. FR-14 sends release history to files full of planning content and then links them

- **Location:** FR-14, FR-13, FR-41 (scan scope).
- **Quote:** "Release history moves to CHANGELOG.md or GitHub Releases, both of which semantic-release already produces." / "The README links to each new location."
- **Why it fails:** Semantic-release generates those files from commit subjects. Tenants' `CHANGELOG.md` has 117 story or epic lines out of 771, and CiCd's latest commit is `ci(story-2-1): …`, which GitHub shows above every file tree. FR-41 doesn't scan CHANGELOG, so the README will link straight to the content FR-13 bans. A hostile reader finds it in one click.
- **Fix:** Add a commitlint rule against story, epic, and FR scopes going forward, owned by CiCd. Either exclude CHANGELOG from the "README links to" requirement or scan it in warn mode.

### M-7. FR-33 and SM-7 test against a checklist that doesn't contain what they claim

- **Location:** FR-33, SM-7, FR-34, §7.3.
- **Quote:** "GitHub's Community Standards page for every in-scope repository shows all six as present." / "GitHub's Community Standards page is complete for all 21."
- **Why it fails:** SUPPORT isn't an item on GitHub's Community Standards checklist, so "all six" can't be observed there. "Complete" also requires content reporting to be enabled, which no FR asks for. FR-33 (the organization files *exist*) isn't in Level 1 or the launch gate, while FR-34 *deletes* local files. The gate can pass with no CONTRIBUTING or SECURITY anywhere.
- **Fix:** Test FR-33 by direct file check in `Hexalith/.github`, plus the checklist items that do exist. Add content reporting or drop "complete". Put FR-33 in §7.3 and order it before any FR-34 deletion.

### M-8. The Kubernetes how-to is real engineering that contradicts the "no prebuilt images" non-goal

- **Location:** FR-24, FR-58, §6, §7.1.
- **Quote:** "An agent stranger test that follows only the how-to reaches a first chat message on a local Kubernetes cluster"
- **Why it fails:** Kubernetes needs images. The non-goal excludes prebuilt images, so the how-to must build and load about 17 service images plus Dapr and Keycloak into kind. That's a deliverable, not a page. Meanwhile, Platform's planning records a registry with anonymous read. Either images already exist, which undercuts R-3's framing and the non-goal, or they don't, and FR-24 is unbuildable. It's also unclear whether FR-24 blocks launch: it sits in §7.1 but not in §7.3.
- **Fix:** Mark FR-24 as post-launch, or state that it reuses Platform's registry images, and amend §6. In either case, say explicitly that it's not in the gate.

### M-9. Calibration happens before the only thing worth calibrating exists

- **Location:** FR-51, FR-52, glossary ("Baseline").
- **Quote:** "In November 2026, the agent stranger test runs on Platform's current "Try it" path" / "Targets can change only through calibration (FR-52)."
- **Why it fails:** There is no current "Try it" path (C-2), so the November baseline measures nothing, and FR-51 freezes the targets before any real measurement. When the mid-December build takes 40 minutes, the PRD leaves two options: never launch, or quietly recalibrate.
- **Fix:** Measure the dev container cold start plus a cold build of Platform's dependency graph *now*. Those parts exist and decide R-3. Allow one dated recalibration once the chatbot path first runs, and record it in the standard.

### M-10. "Move, don't delete" has no destination for planning-only content

- **Location:** FR-7, FR-34, FR-8.
- **Quote:** "Repository-specific content from deleted files moves to the development guide." / "When content has a home (development guide, operations page, CHANGELOG.md or GitHub Releases), the agent moves it rather than deleting it."
- **Why it fails:** Memories' CONTRIBUTING holds sprint rules. FR-34 moves them into `docs/development.md`, where FR-13 bans them, and no regex catches "sprint rules". The backlogs and evidence files under `docs/` have no listed home, so agents will invent locations, which is the "reorganizing" FR-8 forbids, or delete them.
- **Fix:** List `_bmad-output/` as the home for planning-only content. Tell the agent to classify each block (contributor, operator, planning) before moving it.

### M-11. The central link checker needs a cross-repository write credential nobody has designed

- **Location:** FR-45, addendum §B (Scheduled runs).
- **Quote:** "one central scheduled run, which opens or updates an issue in the affected repository"
- **Why it fails:** `GITHUB_TOKEN` can't write issues in 20 other repositories, so this needs a PAT or an App. CiCd's security model enumerates every App permission (spine AD-7), and adds nothing for Issues. The design also produces issue spam when a popular external site goes down.
- **Fix:** Route it through CiCd's nightly run and the App, with explicit Issues permission, or post a single report in Hexalith.Docs. Deduplicate per URL.

### M-12. The AI-prompt model trains newcomers to run whatever the repository tells their agent

- **Location:** FR-6, FR-22, NFR-9, FR-5.
- **Quote:** "AI prompts keep installs and changes inside the dev container or the cloned repository where possible"
- **Why it fails:** The newcomer's agent obeys `AGENTS.md`, `CLAUDE.md`, the devcontainer's lifecycle commands, and 17 submodules, and Docker-in-Docker runs privileged. CiCd's SPEC says agents push directly to `main` with no human review. One bad agent commit to an entry point runs on every newcomer's machine. "Where possible" makes NFR-9 untestable.
- **Fix:** Name the files that newcomer agents execute or read (entry points, `.devcontainer/`, the quickstart scripts) as protected. Changes to them need a maintainer, enforced by CiCd's guard or perimeter. State the host-level privileges up front in the prerequisites.

### M-13. Sample compilation against "the package it uses" checks either the wrong version or the wrong path

- **Location:** FR-19, UJ-2, addendum §B (Compiled samples).
- **Quote:** "CI compiles the sample on every pull request that changes it or the package it uses"
- **Why it fails:** CI references Hexalith libraries "by NuGet package reference only" (`hexalith-llm-instructions.md`). In the PR that changes an API, the sample therefore compiles against the *published* package and passes, and the next release breaks the sample. Compiling against the project reference instead stops testing the `dotnet add package` path. Either way, UJ-2's "CI prevents this" is false for breaking changes.
- **Fix:** Compile the sample against the PR's freshly packed package, from a local feed in CI. State that compiling the sample doesn't verify the "returns the documented result" part.

---

## Low

### L-1. The glossary says only current repositories are modules, but Docs gets a category

- **Location:** §3 ("Module", "Current repository"), FR-2, addendum §A.
- **Quote:** "Each current repository is one module, with exactly one category."
- **Why it fails:** Hexalith.Docs isn't a current repository, yet it has a registry row with category "technical (confirmed)".
- **Fix:** Define "module" over in-scope repositories, or give Docs a category of "none".

### L-2. The agent instructions' ecosystem table still advertises a legacy repository

- **Location:** FR-47, FR-50.
- **Quote:** "The documentation rules say that "business module" names the same repositories the architecture instructions call "domain modules""
- **Why it fails:** `hexalith-llm-instructions.md` lists `Hexalith/Hexalith` as "Core framework and shared components". That repository isn't in scope and is an archive candidate. The table also omits most in-scope repositories, so agents writing docs will link a repository FR-29 may archive.
- **Fix:** Add an FR to replace that table with the module registry.

### L-3. FR-57's review requirement isn't enforced anywhere

- **Location:** FR-57.
- **Quote:** "A maintainer reviewed the migration pull request before it merged."
- **Why it fails:** No ruleset requires reviews, and CiCd rejects review as an enforcement layer (C-1). The item is self-attested.
- **Fix:** Record the reviewer and date in the audit report, or drop the item.

### L-4. The stars metric drifts from the brief, and it will be mocked

- **Location:** SM-8.
- **Quote:** "1,000 GitHub stars across current repositories by the end of 2027"
- **Why it fails:** The brief says "across the organization", but the PRD says current repositories. The target is also published in a public planning folder that a hostile reader will quote next to the launch-day count.
- **Fix:** Align the wording with the brief, and consider keeping vanity targets out of public folders.

### L-5. "Contains code" is undefined

- **Location:** FR-36.
- **Quote:** "Every in-scope repository that contains code"
- **Why it fails:** It's unclear whether BmadSkills (skills), AI.Tools (instructions and scripts), and CiCd (Python tools) count.
- **Fix:** List the repositories that need a development guide in the registry.

### L-6. The organization SECURITY default reaches repositories without the channel it points to

- **Location:** FR-35, FR-29.
- **Quote:** "Private vulnerability reporting is enabled on every in-scope repository and on `Hexalith/.github`."
- **Why it fails:** The organization SECURITY default also applies to every stale repository marked "keep", where private reporting isn't enabled. SECURITY then points reporters to a disabled channel.
- **Fix:** Enable it organization-wide for public repositories, or give SECURITY a fallback contact.
