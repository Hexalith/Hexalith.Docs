---
title: "PRD: Hexalith Documentation Standard"
status: final
created: 2026-11-09
updated: 2026-11-20
inputs:
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/brief.md
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/addendum.md
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/.memlog.md
---

# PRD: Hexalith Documentation Standard

## 0. Document purpose

This PRD turns the final brief and its addendum (`_bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/`) into testable requirements. Its next reader is the epics-and-stories workflow. AI agents will carry out most of the resulting stories across 21 repositories. So each functional requirement (FR) names one capability, with consequences that can be verified per repository.

How to read it:

- §3 Glossary fixes the vocabulary. FRs, journeys, and metrics use those terms exactly.
- §4 groups FRs by feature. FRs are numbered globally. Numbers stay stable, so FRs added during review (FR-59 to FR-66) sit inside their feature, out of numeric order.
- `[ASSUMPTION]` marks a recommended default applied without explicit confirmation. §13 indexes them.
- `[HUMAN]` marks a step only a maintainer can take, because it needs admin rights or a human decision. Agents prepare these steps but don't take them.
- §5 lists the human-only steps, §8.3 the launch gate, §8.4 the rollout dates and go/no-go decisions, and §12 the open questions.
- `addendum.md`, next to this file, holds the proposed module registry and mechanism notes for architecture. The brief's addendum holds the current-state baseline and rejected alternatives. `research-landscape.md` holds the comparables research.

**How FRs become work.** The epics author should treat FRs by type:

| Type | FRs | Becomes |
| --- | --- | --- |
| One-time deliverable | FR-1 to FR-8, FR-24, FR-25, FR-27, FR-40 to FR-42, FR-45, FR-47, FR-59, FR-61, FR-62, FR-64, FR-66 (after launch) | One story or a small epic each |
| Per-repository rule | FR-9 to FR-14, FR-16 to FR-22, FR-28, FR-34, FR-36 to FR-39, FR-48, FR-60, FR-63 | Acceptance criteria inside each repository's Level 1 work (FR-57), not separate stories per rule |
| Per-repository action | FR-15, FR-43 | One step inside each repository's Level 1 work |
| Organization action | FR-26, FR-29 to FR-33, FR-35, FR-65 | Mostly `[HUMAN]` steps |
| Test and gate | FR-23, FR-51 to FR-58 | Test runs and definitions of done |
| Realized within another FR | FR-44 and FR-46 (within FR-41), FR-49 and FR-50 (within FR-47) | No separate story |

The [Docs backlog](../../epics.md) assigns the work to repository owners. The [20 November course correction](../../sprint-change-proposal-2026-11-20.md) records the pilot changes and their verification gates.

Each repository's Level 1 work (FR-57) splits into three parts: the agent's content change, the maintainer's settings and review, and the republish with its verification.

**Visibility.** This file lives in Hexalith.Docs under `_bmad-output/`. That folder becomes public with the repository and is never linked from docs (FR-13). FR IDs are internal planning content: they must never appear in a README, CONTRIBUTING file, or `docs/` page.

## 1. Vision

Anyone who finds Hexalith can understand what a module does and get it working in minutes, without asking anyone. They might find it on GitHub, on nuget.org, or through their AI coding agent. The front door explains Hexalith on one screen and offers "Try it". One command, or one short prompt to the newcomer's own AI coding agent, deploys Hexalith on Docker on the newcomer's own machine. Within 20 minutes, the newcomer's own AI agent is putting Hexalith to work: it runs a first Hexalith operation through Hexalith.McpCli. The chat interface follows as an upgrade, once ChatBot joins Platform (FR-66).

Every README is simple, clear, and easy to read. It follows one short skeleton and doubles as the NuGet package page. Every badge reads a live source. The community files and a development guide let a contributor open a first pull request without reverse-engineering the build.

AI agents write most of Hexalith's documentation. So the standard lives where agents read their instructions, and a docs check in the shared CI catches what they miss. Together, these keep the standard in place after launch.

**Why now.** Nobody outside the team uses Hexalith yet. The code is public and the packages are on nuget.org, but the documentation stands between the project and a public launch targeted for the end of 2026. If the date and a working "Try it" conflict, the date moves.

**Launch at a glance.** Launch targets the end of 2026. It happens only when all ten launch gate conditions hold (§8.3). Go/no-go decisions fall on 2026-12-01 and 2026-12-15 (§8.4). The one blocking dependency is D-2: Platform stories 3.2 to 3.8, which run all seven MVP modules locally with agent access through Hexalith.McpCli. Five of those stories haven't started (R-1).

**Later.** Hexalith will deploy with one command to Azure, AWS, and Scaleway too. A documentation website, a hosted demo, and prebuilt images each come later, once their revisit triggers in §8.2 are met.

## 2. Target user

### 2.1 Jobs to be done

- **Developer evaluating a module.** When I find a Hexalith module on GitHub or nuget.org, I want to know within a minute what it does and whether it suits me. Then I want it working in minutes, without asking anyone.
- **Newcomer who wants to use the application.** I want a running Hexalith on my own machine, doing real work within 20 minutes. I want to judge the experience, not a description of it.
- **Newcomer who delegates to an agent.** I want to hand my AI coding agent one prompt and have it set Hexalith up and use it, because that's how I already work.
- **Contributor.** I want to build, test, and open a first pull request by following one guide, without reverse-engineering the build.
- **Operator.** I want to deploy and run Hexalith services by following runbooks I can find.
- **AI coding agent (secondary).** It writes docs and runs quickstarts for newcomers. It needs explicit rules about what goes where, and short commands it can run and verify.
- **Maintainer.** I want docs to stay consistent across 21 repositories without re-checking every rule by hand.

### 2.2 Non-users (v1)

- Teams that want to deploy to Azure, AWS, or Scaleway (later).
- Readers looking for a documentation website or a hosted demo.
- Users of xppmodel, which belongs to the Itaneo organization.

### 2.3 Key user journeys

[ASSUMPTION: these journeys are inferred from the brief's audiences and drafted in Fast path. The protagonists are illustrative. Replace any journey with a real session if one exists.]

- **UJ-1. Lena tries Hexalith through the front door.** Lena is an operations lead comparing agent-driven workflow tools. Her own laptop has Docker, VS Code, and the AI coding agent she already uses, and nothing else Hexalith needs.
  1. She opens `github.com/Hexalith`, reads one screen, and selects "Try it".
  2. The Platform README lists every prerequisite up front, including what the dev container will do on her machine. Hexalith needs no LLM provider key, because her agent brings its own model.
  3. She pastes the AI prompt into her coding agent. The agent opens the dev container and runs the setup command.
  4. The agent waits for services to be healthy, then connects to Hexalith's MCP server.
  5. The agent creates a project in Hexalith and lists it back to her.
  6. It's 20 minutes or less since she opened the front door, and nobody helped. The front door tells her the chat interface is coming.

  **Edge case:** Docker isn't running. The prompt's prerequisite check tells her before anything is installed.

- **UJ-2. Karim uses a package from nuget.org.** Karim is a .NET developer searching nuget.org for polymorphic JSON serialization. The package page shows a one-sentence description, a few honest badges, and a "Use the package" block. He runs `dotnet add package`, pastes the code sample, and gets a working call within 5 minutes. **Edge case:** the sample might not compile against the latest version. CI prevents that, because it compiles the sample against the package built from the same commit.
- **UJ-3. Sofia runs a module.** Sofia is evaluating Hexalith.Tenants for a multi-tenant product. She opens the repository in Codespaces, runs `aspire run`, and makes the first call shown in the README. She has a first result within 15 minutes.
- **UJ-4. Tomás opens a first pull request.** Tomás wants to fix a bug in Hexalith.Parties. The README's Contributing section takes him to the organization CONTRIBUTING and to the repository's development guide. He builds and runs the tests green, then opens a pull request using the organization template.
- **UJ-5. An agent migrates a repository to Level 1.** A maintainer gives an AI agent the migration prompt and Hexalith.Works.
  1. The agent works from the Hexalith.Docs workspace. It audits the README against Level 1 and sorts every out-of-place block as contributor content, operator content, planning content, or release history (FR-7).
  2. It moves the release procedure to an operations page and rewrites the README to the skeleton (FR-9, FR-37). It doesn't touch any file that Hexalith.CiCd owns.
  3. It runs the local docs check until it's clean (FR-64). Then it hands the maintainer the migration and a list of the decisions it left open.
  4. The maintainer reviews the migration, applies the GitHub settings, and lands it.
  5. A Hexalith.CiCd agent switches the repository's docs check to fail mode (FR-42).
  6. A one-time release republishes the README to nuget.org, and a script confirms every package page (FR-15).
- **UJ-6. The docs check catches an agent's mistake.** Months after launch, an agent adds a story reference and a release note to a README. The local docs check flags both before the push. Each finding names the file, the line, and the rule, with a one-line fix hint. Had the agent pushed anyway, `main` would turn red and the nightly release would skip the repository until it was fixed. The agent moves the release note to GitHub Releases and removes the reference, without opening the standard.

## 3. Glossary

### Product and repositories

- **Hexalith.** A set of business modules and technical modules for managing enterprise workflows through a chatbot. Platform deploys them together.
- **Module.** The capability one in-scope repository delivers. Each in-scope repository is one module and has exactly one category.
- **Business module.** A module that implements a business domain, such as Parties or Timesheets. It is the same set of repositories the architecture instructions call "domain modules".
- **Technical module.** A module that provides a reusable platform capability, such as EventStore or Builds.
- **Current repository.** One of the 20 public Hexalith repositories under active development, with commits pushed in November 2026. Each name starts with `Hexalith.`: Agents, AI.Tools, BmadSkills, Builds, ChatBot, CiCd, Commons, Conversations, EventStore, Folders, FrontComposer, McpCli, Memories, Parties, Platform, PolymorphicSerializations, Projects, Tenants, Timesheets, and Works.
- **In-scope repository.** A current repository, or Hexalith.Docs: 21 in total. `Hexalith/.github` and xppmodel aren't in-scope repositories.
- **Hexalith.CiCd.** The repository that owns CI/CD for its managed modules. It renders and delivers their workflow files, runs their nightly release, and guards those files. Only agents working in Hexalith.CiCd change CI/CD.
- **Managed module.** An in-scope repository whose CI/CD Hexalith.CiCd manages. That's 17 in total: every current repository except Builds, BmadSkills, and CiCd. Hexalith.Builds hosts the shared CI, and Hexalith.CiCd agents change it.
- **Shared CI.** The reusable CI and release pipelines in Hexalith.Builds. Hexalith.CiCd delivers them to managed modules.

### People

- **Maintainer.** A Hexalith team member who reviews and lands documentation changes and holds the admin rights that `[HUMAN]` steps need.
- **Newcomer.** A person who has never used Hexalith.
- **Operator.** A person who deploys or runs Hexalith services.
- **Outside tester.** A person who has never run Hexalith or worked on its code, whatever their GitHub rights. They run the human stranger test.

### Pages and artifacts

- **Organization page.** Everything `github.com/Hexalith` shows a visitor: the front door, the pinned repositories, and the repository list.
- **Front door.** The organization profile README at `Hexalith/.github/profile/README.md`, shown at the top of the organization page.
- **Package page.** A package's page on nuget.org. It shows the README packed into the package's latest version.
- **Standard.** The documentation standard: one authoritative document in Hexalith.Docs that states every documentation rule.
- **Rule ID.** The stable identifier of one rule in the standard. It is shared by the docs check, the documentation rules, and findings.
- **Module registry.** The machine-readable table in Hexalith.Docs that lists every in-scope repository with the facts the other FRs depend on (FR-2).

### README and quickstarts

- **README skeleton.** The fixed, ordered set of nine README sections that every in-scope repository follows (FR-9).
- **One-sentence description.** A single sentence of 120 characters or fewer that describes a repository. It is identical in the README, the About description, the module registry, and the front door.
- **About description.** The description field of a GitHub repository.
- **Quickstart block.** One of three README blocks, named for what the reader does first: "Use the package", "Run it", or "Use the tool".
- **"Start here" list.** The Quickstart section of a repository the module registry marks as having no quickstart block. It is a short list of links the docs check recognizes.
- **"Try it".** The journey from the front door to a first Hexalith operation run by the newcomer's AI agent through Hexalith.McpCli, by way of the Platform README's "Run it" block. It isn't a fourth quickstart block. It upgrades to end at a first chat message once ChatBot joins Platform (FR-66).
- **Setup command.** The one command an AI prompt wraps: `dotnet add package`, `aspire run`, or the tool's install command.
- **AI prompt.** A prompt of 10 lines or fewer inside a quickstart block. It wraps the setup command so the newcomer's AI coding agent can run the quickstart.
- **Supported agent tool.** An AI coding agent tool that the standard names as supported by the AI prompts and the agent stranger test.
- **Dev container.** A `.devcontainer/` configuration, copied from the template in Hexalith.Docs, that pins the exact toolchain and opens in VS Code or GitHub Codespaces.
- **First success.** The event that stops a quickstart timer:
  - "Use the package": a working sample call.
  - "Run it": a first successful call.
  - "Use the tool": the expected output of a first command.
  - "Try it": the newcomer's AI agent runs the block's first Hexalith operation through Hexalith.McpCli and shows its result. On the command path, one Hexalith.McpCli command returns the same result.

### Timing and testing

- **Clean environment.** The starting state for a timed quickstart, defined per block in the stranger-test kit:
  - "Use the package" and "Use the tool": a machine or container with only the .NET SDK.
  - "Run it": a machine with Docker and VS Code and no Hexalith toolchain, or a browser with Codespaces.
  - "Try it": the newcomer's own machine, with only Docker and VS Code, plus a supported agent tool for the AI prompt path.
- **Time target.** The maximum time from a quickstart's starting page to first success in a clean environment (FR-51).
- **Stranger-test kit.** The environments, scripts, templates, and rules that make stranger tests repeatable (FR-61).
- **Agent stranger test.** A set of timed runs in which fresh sessions of a supported agent tool attempt a quickstart (FR-53). Each session has only the starting page and the quickstart's AI prompt.
- **Human stranger test.** A timed run in which an outside tester attempts "Try it" from the front door, with no help. It is launch gate condition 1 (§8.3, FR-55).
- **Friction log.** The record of every step of a stranger test, with elapsed time and severity:
  - red: blocked, or needed help
  - amber: slowed down or confused
  - green: as documented
- **Baseline.** The first set of measurements, taken in November 2026 and used to calibrate the time targets (FR-52).
- **Launch ledger.** The record of each in-scope repository's Level 1 status, docs check mode, republish status, and stranger test results (FR-56).

### Contributor and operator docs

- **Development guide.** The `docs/development.md` page that explains prerequisites, build, test, and debug.
- **Operations page.** The `docs/operations.md` page that holds operator runbooks and release procedures.
- **Community files.** The organization defaults in `Hexalith/.github`: CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, issue templates, and the pull request template.
- **Agent entry points.** A repository's `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md`.
- **Shared baseline.** The normalized instruction text that every agent entry point shares. It points agents to `hexalith-llm-instructions.md` in Hexalith.AI.Tools.

### Docs check and enforcement

- **Internal planning content.** Any of the following:
  - epic and story references
  - FR and NFR IDs
  - sprint rules and backlogs
  - links to `_bmad-output/`
  - commit SHAs or CI run IDs used as release or evidence logs
- **Checked pages.** The pages the docs check judges in fail mode: the README, per-package READMEs, and the `docs/` pages the README links to. The docs check reports on other `docs/` pages without judging them.
- **NuGet-safe.** Markdown that renders correctly on both GitHub and nuget.org: absolute HTTPS links and images, no raw HTML, and badge images only from hosts nuget.org allows.
- **Badge.** A status image near the top of a README. Every badge reads a live source.
- **Live source.** What a badge reads: a CI workflow on the default branch, a SonarQube Cloud analysis that CI runs, a package the repository packs, or the repository's LICENSE file.
- **Docs check.** The job in the shared CI that checks documentation against the standard (FR-41).
- **Warn mode / fail mode.** The two docs check modes. Warn mode reports findings and never fails. In fail mode, any finding on a checked page fails the CI run. That turns `main` red, and the nightly release skips the repository.
- **Documentation rules.** The standard's rules, restated for agents in the shared agent instructions in Hexalith.AI.Tools (FR-47).

### Levels and launch

- **Migration.** One in-scope repository's change set that brings it to Level 1 "Clean".
- **Migration prompt.** The audit-and-migration prompt in Hexalith.Docs that an agent uses to prepare a migration.
- **Level 1 "Clean".** The done state for one repository's documentation (FR-57).
- **Level 2 "Try-able".** The done state for timed quickstarts: every published block meets its time target, and "Try it" passes the human stranger test (FR-58).
- **Launch.** The public announcement of Hexalith. It happens only after the launch gate passes.
- **Launch gate.** The conditions in §8.3. All of them must hold before launch.

## 4. Features

### 4.1 Standard, registry, and templates in Hexalith.Docs

**Description.** Hexalith.Docs holds the single authoritative source of every rule, the module registry, and every template. Templates are copied once and never synced, so the docs check keeps repositories aligned, not the templates. The migration prompt lets agents carry out Level 1 at scale. Realizes UJ-5.

#### FR-1: Standard on one page

A maintainer or AI agent can read the complete standard in one authoritative document in Hexalith.Docs.

**Consequences (testable):**

- The standard is one Markdown file [ASSUMPTION: `docs/documentation-standard.md`].
- It states each rule exactly once. The rules cover:
  - what a README is for: a self-standing overview, with the details in linked `docs/` pages
  - the README skeleton and quickstart blocks
  - AI prompts and badges
  - NuGet-safe Markdown
  - community files, the development guide, and the operations page
  - internal planning content
  - writing style, the readability checklist (FR-62), and time targets
- A rule table gives every rule a rule ID and says how it is enforced: by the docs check or by review.
- It names the GitHub and README practices it follows, and its deliberate departures, such as no table of contents in a 150-line README.
- It names the supported agent tools.
- It links to every template (FR-3 to FR-7) and to the module registry (FR-2).

#### FR-2: Module registry

The front door, the About descriptions, the docs check, and the migration prompt all read one machine-readable module registry.

**Consequences (testable):**

- The registry has one row per in-scope repository, 21 rows in total. Docs stores it in `docs/module-registry.json` alongside the standard. Tools can read it with the Python standard library.
- Each row records:
  - name, category, and one-sentence description
  - quickstart blocks in display order, or "none"
  - whether it publishes packages, its package count, its primary package, and whether it has per-package READMEs
  - whether it has an Aspire AppHost, a development guide, an operations page, and a dev container
  - CI owner (Hexalith.CiCd, its own CI, or a caller workflow), badge sources, and SonarQube Cloud key
- `[HUMAN]` A maintainer confirms every category and one-sentence description before the front door is published (Open Question 3).
- A docs check rule verifies that the README, the About description, and the front door use the registry's one-sentence description word for word.

#### FR-3: README skeleton template

A maintainer or agent can copy a README template that already follows the README skeleton.

**Consequences (testable):**

- The template contains the nine sections of FR-9, in order, with placeholder text that explains each section.
- It contains all three quickstart blocks and the "Start here" list variant. Whoever copies the template deletes the ones that don't apply.
- Filled with sample values, it passes the docs check in fail mode.
- Templates and prompts live outside the checked pages [ASSUMPTION: `templates/` and `.github/prompts/` in Hexalith.Docs].

#### FR-4: Development guide and operations page templates

A maintainer or agent can copy a template for the development guide and for the operations page.

**Consequences (testable):**

- The development guide template has sections for prerequisites, build, test, and debug, plus running locally where that applies.
- Its prerequisites section names exact versions or points to the dev container.
- The operations page template has sections for deploy, configure, monitor, and release procedure.
- Filled with sample values, both pass the docs check in fail mode.

#### FR-5: Dev container template

A maintainer can add a dev container to a runnable repository by copying the template.

**Consequences (testable):**

- The template pins exact versions of the .NET SDK, Aspire CLI, Dapr CLI and runtime, and Docker-in-Docker.
- It opens in VS Code (Dev Containers) and in GitHub Codespaces.
- After the container starts, `aspire run` succeeds with no further installation in a repository that has an Aspire AppHost.
- A Platform variant also provides what the Platform README needs today: submodules at their pinned commits and an isolated Dapr home with matching versions.
- A docs check rule verifies that each dev container's .NET SDK pin matches the repository's `global.json`.
- Hexalith.FrontComposer's existing dev container is aligned with the template [ASSUMPTION].

#### FR-6: AI prompt pattern

A maintainer or agent can write an AI prompt from a pattern in the standard, with one variant per block type.

**Consequences (testable):**

- Every variant is 10 lines or fewer and wraps exactly one setup command.
- **"Use the package":** add the package, paste and run the sample, and report the result.
- **"Run it":**
  1. Check prerequisites, or open the dev container.
  2. Run `aspire run`.
  3. Wait until services report healthy.
  4. Return the dashboard URL.
  5. Explain the first call.
- **"Try it":**
  1. Check prerequisites, or open the dev container.
  2. Run `aspire run`.
  3. Wait until services report healthy.
  4. Connect to Hexalith's MCP server through Hexalith.McpCli.
  5. Run the block's first Hexalith operation and show its result.
- **"Use the tool":** install the tool, run the first command, and compare its output with the documented output.
- When a secret is needed, the prompt tells the agent to wait while the reader enters it in an environment file that Git excludes and replies "done". The agent never asks for the secret in chat.
- The standard states the rule: "If a prompt needs more than 10 lines, fix the command, not the prompt."
- How a supported agent tool opens the dev container from a clean host is settled by a spike (Open Question 15), and the pattern records it.

#### FR-7: Migration prompt

An AI agent given the migration prompt and an in-scope repository can prepare a migration for maintainer review. Realizes UJ-5.

**Consequences (testable):**

- The prompt is modeled on `Hexalith.Builds/.github/prompts/audit-hexalith-ci-cd.prompt.md`.
- The agent works from the Hexalith.Docs workspace, where every in-scope repository is a root submodule [ASSUMPTION: Hexalith.BmadSkills is added to `.gitmodules`]. It produces one change set per repository.
- It produces an audit with a pass or fail result for each Level 1 requirement, with file and line as evidence.
- It sorts every out-of-place block as contributor content, operator content, planning content, or release history, and moves it:
  - contributor content to the development guide
  - operator content to the operations page
  - planning content to `_bmad-output/`
  - release history to GitHub Releases
- Before it deletes content that has no new home, it lists that content for the reviewer. It stops and escalates when a change would delete more than [ASSUMPTION: 20] lines of such content.
- It doesn't touch files Hexalith.CiCd owns: workflows, `.github/hexalith-ci.json`, the Builds pointer, and the marked CI/CD block in agent entry points.
- It runs the local docs check (FR-64) until no findings remain on checked pages.
- It lists the decisions it leaves for the reviewer: category, quickstart blocks, content destinations, and content proposed for deletion.

#### FR-8: Cross-module guides

A reader can learn from guides in Hexalith.Docs how Hexalith modules fit together.

**Consequences (testable):**

- At launch, Hexalith.Docs has at least an overview guide that covers the concepts, the architecture, business modules and technical modules, and how Platform composes modules into one system [ASSUMPTION: this is the minimum launch set].
- A guide about one module lives in that module's `docs/`, not in Hexalith.Docs.
- Existing `docs/` folders are cleaned on checked pages only, never reorganized.

#### FR-62: Readability checklist

A maintainer can check that a README is written for people.

**Consequences (testable):**

- The standard contains a short readability checklist.
- The checklist confirms that, from the README alone as nuget.org shows it, a newcomer can say:
  - what the module does and who it's for
  - how to start
  - which packages exist
  - where to get help
  - the license
- It confirms that the first five lines state the module's purpose.
- It confirms that every term a newcomer might not know is defined or linked.
- It confirms that the writing follows NFR-1.
- `[HUMAN]` The maintainer reviewing each migration completes the checklist and records the result in the launch ledger (FR-56).

### 4.2 README and package page

**Description.** The README is the first page on GitHub. Hexalith.Builds also packs it into every package, so it is the package page too. Because one file serves both, it must stay short and NuGet-safe, and be written for readers. Realizes UJ-1, UJ-2, UJ-6.

#### FR-9: README skeleton sections

The README of every in-scope repository contains these sections in this order, with nothing after License:

1. Title and one-sentence description
2. Badges
3. What it does and who it's for
4. Quickstart: quickstart blocks, or a "Start here" list
5. Packages, if the repository publishes packages
6. Documentation, with links into `docs/`
7. Part of Hexalith, with a link to the front door
8. Contributing: a link to the organization CONTRIBUTING by absolute URL, and a link to the development guide if the module registry records one
9. License, as an SPDX identifier (MIT)

**Consequences (testable):**

- The docs check fails a README when a required section is missing or out of order, or when content follows License.
- Section headings use fixed text from the standard [ASSUMPTION].
- No table of contents section, because GitHub generates an outline [ASSUMPTION].
- The docs check fails a repository that has a `.github/README.md`, because GitHub would show it instead of the root README.

#### FR-10: README size limits

A reader can take in a README quickly.

**Consequences (testable):**

- The README is 150 lines or fewer.
- "What it does and who it's for" is five lines or fewer.
- Each quickstart block is 30 lines or fewer, including its AI prompt [ASSUMPTION].
- Blocks appear in the module registry's order.
- When a block can't meet both its line limit and its time target, the time target wins, and the reviewer records why.
- The Packages table has one row per package: name, nuget.org link, and a one-line purpose.

#### FR-11: One-sentence description everywhere

The same one-sentence description identifies a repository wherever a reader meets it.

**Consequences (testable):**

- The description is one sentence of 120 characters or fewer.
- It is identical in the README, the About description, the module registry, and the front door.
- The NuGet `Description` of every package that packs the README starts with that sentence and may add one package-specific sentence [ASSUMPTION]. Hexalith.Commons packages with their own README follow the same rule, using the first sentence of their own README.

#### FR-12: NuGet-safe README

The README renders correctly on both GitHub and nuget.org.

**Consequences (testable):**

- Every link and image uses an absolute HTTPS URL, and there is no raw HTML.
- Badge images come only from hosts on nuget.org's published allow list.
- The docs check detects relative links, raw HTML, and image hosts that aren't allowed.
- After the republish (FR-15), the package page shows no broken link, broken image, or raw markup.

#### FR-13: No internal planning content

Checked pages, the front door, and the community files contain no internal planning content.

**Consequences (testable):**

- The docs check finds internal planning content on checked pages, the front door, and the community files. Its patterns are defined in the docs check configuration. They are tuned against all 21 in-scope repositories in warn mode, before any repository switches to fail mode.
- It reports internal planning content on other `docs/` pages without failing. Cleaning those pages is deferred until after launch (§8.2).
- `_bmad-output/` stays in each repository and stays public. No documentation page links to it, and the docs check doesn't scan it [ASSUMPTION].
- The standard itself may quote the patterns, through an exemption recorded in the rule table [ASSUMPTION].

#### FR-14: Release history and runbooks leave the README

Content that isn't for README readers moves to where it belongs.

**Consequences (testable):**

- Release history moves to GitHub Releases, and the README links there [ASSUMPTION: GitHub Releases rather than CHANGELOG.md].
- Build, test, and debug runbooks move to the development guide (FR-36), and operator runbooks and release procedures move to the operations page (FR-37).
- The docs check doesn't scan existing CHANGELOG history. From now on, a commit-lint rule owned by Hexalith.CiCd keeps story, epic, and FR scopes out of new commit subjects, so the history stays clean (Open Question 11).

#### FR-15: Package pages republished

Once a repository's migration lands, every package it publishes gets a new version, before launch.

**Consequences (testable):**

- `[HUMAN]` A maintainer starts one release per repository, through the release path Hexalith.CiCd provides (Open Question 11). The republish happens before Platform's stabilization window starts [ASSUMPTION: the window starts on 2026-12-10].
- A script checks the latest version of every package on nuget.org. It confirms that the version shows the migrated README, with the one-sentence description and the Quickstart section, and that the number of packages matches the module registry.
- The launch ledger records the result for each repository.

#### FR-16: Per-package READMEs

Any repository may keep or add per-package READMEs. Hexalith.Commons already has them.

**Consequences (testable):**

- Each per-package README is NuGet-safe (FR-12), contains no internal planning content (FR-13), and links to the repository README.
- Per-package READMEs don't have to follow the README skeleton.
- The module registry records which repositories have them.

#### FR-60: LICENSE file

Every in-scope repository has its own LICENSE file. The organization can't supply one as a default.

**Consequences (testable):**

- An MIT LICENSE file is at the root of all 21 in-scope repositories.
- The docs check fails a repository without one.

### 4.3 Quickstarts and AI prompts

**Description.** Each README's Quickstart starts with what the reader does first, using one or more of the three quickstart blocks. Every block offers the setup command and an AI prompt. "Try it" is the front-door journey through Platform's "Run it" block. The time to get every prerequisite counts toward the timer. Level 1 requires that blocks work. Level 2 requires that they meet their time targets. Realizes UJ-1, UJ-2, UJ-3.

#### FR-17: Quickstart block choice

A reader sees a first action that matches what they came to do.

**Consequences (testable):**

- Every in-scope repository's README has the quickstart blocks the module registry lists, named exactly "Use the package", "Run it", or "Use the tool", in registry order.
- A repository the registry marks as having no quickstart block has a "Start here" list instead [ASSUMPTION: Hexalith.Docs and Hexalith.CiCd].
- The Hexalith.Docs "Start here" list links to "Try it" only once FR-26 allows it.
- A "Run it" block appears only once it meets its time target (FR-58).
- Until "Try it" passes the agent stranger test, the Platform README's Quickstart section links to its development guide.

#### FR-18: Prerequisites up front

A reader knows everything a quickstart needs before the first step.

**Consequences (testable):**

- Every quickstart block opens with the complete list of prerequisites. That includes any account, key, or mailbox to get, and any host-level change, such as a privileged Docker-in-Docker container.
- No later step needs anything missing from that list, as the stranger tests verify.
- Secrets are typed into an environment file that Git excludes, or into an interactive prompt. They never go into the AI prompt, the chat, or a commit (NFR-8).

#### FR-19: "Use the package" block

A developer can add a package and make a working call. Realizes UJ-2.

**Consequences (testable):**

- The block gives a `dotnet add package` command and a code sample that makes a working call.
- CI compiles the sample against the package built from the same commit. Hexalith.Builds and Hexalith.CiCd choose how, before the first package repository's migration (`addendum.md` §B.4).
- First success: the sample call runs and returns the documented result.
- The time target is 5 minutes, verified at Level 2 (FR-58).

#### FR-20: "Run it" block

A developer can run a module and make a first call. Realizes UJ-3.

**Consequences (testable):**

- The repository ships a dev container copied from the template (FR-5).
- The block says: open the dev container (VS Code or Codespaces), run `aspire run`, and make the first call the block shows.
- The block starts from whatever composition the architecture work chooses for each business module: a module AppHost, or a Platform composition scoped to the module (Open Question 14).
- First success: the first call returns the documented result.
- The time target is 15 minutes. The block appears only once it meets that target (FR-58).

#### FR-21: "Use the tool" block

A developer can install a tool and run a first command.

**Consequences (testable):**

- The block gives an install command, a first command, and that command's expected output.
- First success: the first command produces the expected output.
- The time target is 5 minutes [ASSUMPTION], verified at Level 2 (FR-58).

#### FR-22: AI prompt in every block

A newcomer can hand any quickstart block to their AI coding agent.

**Consequences (testable):**

- Every quickstart block contains an AI prompt in the README itself, using the variant for its block type (FR-6).
- The prompt wraps the same setup command the block shows.

#### FR-23: "Try it"

A newcomer can go from the front door to a first Hexalith operation, run by their own AI agent, on their own machine in 20 minutes or less. They can use the setup command or the AI prompt. Realizes UJ-1.

**Consequences (testable):**

- The front door's "Try it" link opens the Platform README's "Run it" block.
- One setup command (`aspire run` in the Platform dev container) starts all seven MVP modules, with a generated local sign-in realm and a ready-made tenant. This depends on Platform stories 3.2 to 3.8 (§11, D-2).
- The block connects the newcomer's agent to Hexalith's MCP server through Hexalith.McpCli, and names one first operation with its expected result [ASSUMPTION: create a project, then list it] (Open Question 20).
- The block lists every prerequisite (FR-18), including a supported agent tool for the AI prompt path (Open Question 1). Hexalith itself needs no LLM provider key. The time spent getting any prerequisite counts toward the 20 minutes.
- First success: the agent shows the first operation's result. On the command path, one Hexalith.McpCli command returns it.
- "Try it" passes the agent stranger test (FR-53), and then the human stranger test (FR-55).

#### FR-66: "Try it" upgrades to chat

Once ChatBot's chat ships in Platform's one-command composition, "Try it" ends at a first chat message. This is an upgrade after launch, not a launch condition.

**Consequences (testable):**

- When ChatBot's chat runs from Platform's setup command (D-10), the Platform README's "Run it" block adds a first chat message as its final step. First success for "Try it" becomes the chatbot's reply to that message.
- The upgraded "Try it" passes the agent stranger test, and then a human stranger test with a new outside tester, before the front door describes the chat as available.
- Until then, the front door states that the chat interface is coming (FR-25).

#### FR-24: Kubernetes how-to

An operator can deploy Platform to Kubernetes by following a how-to.

**Consequences (testable):**

- Platform's `docs/` contains a how-to for deploying Platform to a local Kubernetes cluster [ASSUMPTION: Docker Desktop Kubernetes or kind]. The service images are built locally and loaded into the cluster, so no published images are needed [ASSUMPTION].
- One agent stranger test run, following only the how-to, reaches the how-to's documented result without help: a first Hexalith operation through Hexalith.McpCli returns its result.
- There is no time target.
- It depends on Platform supporting Kubernetes deployment (§11, D-3).

### 4.4 Front door and organization

**Description.** A first visitor to the organization page sees one screen that explains Hexalith and lists only in-scope repositories. It shows the "Try it" link once FR-26 allows it. Cleanup removes non-current repositories and forks from view, and removes sensitive material from public planning folders. FR-32 and FR-65 start now, well ahead of the front door work. Realizes UJ-1.

#### FR-25: Front door

A first visitor learns what Hexalith is, and where to start, from one screen.

**Consequences (testable):**

- The front door is published at `Hexalith/.github/profile/README.md`.
- It fits on one screen [ASSUMPTION: 60 lines of Markdown or fewer].
- It says what Hexalith is and links to the Hexalith.Docs guides.
- Once FR-26 allows it, it shows the "Try it" link within its first 10 lines. It may be published without the link before then.
- It lists every in-scope repository with its category, one-sentence description, and link, taken from the module registry.
- It lists no repository that isn't in scope.
- It passes the docs check, with the skeleton rules turned off.
- Until FR-66 completes, it states plainly that the chat interface is coming.

#### FR-26: Honest "Try it" link

The front door never promises what the product doesn't do.

**Consequences (testable):**

- The "Try it" link appears only after "Try it" passes the agent stranger test. The link isn't the announcement. The human stranger test needs it in place.
- Hexalith isn't announced until "Try it" passes the human stranger test.
- Until the link appears, no page claims that Hexalith deploys in minutes.

#### FR-27: Optional demo

The front door may show a demo video or GIF of "Try it" in action, 30 seconds or less. It is optional and not part of the launch gate.

**Consequences (testable):**

- If present, it has a text alternative and shows the current UI.
- It is removed when it no longer matches the product.

#### FR-28: About description and topics

A visitor browsing the organization page sees accurate metadata on every in-scope repository.

**Consequences (testable):**

- `[HUMAN]` The About description of each in-scope repository is its one-sentence description.
- `[HUMAN]` Its topics include `hexalith` and one category topic [ASSUMPTION: `hexalith-business-module` or `hexalith-technical-module`].
- The registry consistency rule (FR-2) verifies the About description.

#### FR-29: Non-current repositories removed from view

A visitor sees only current work on the organization page.

**Consequences (testable):**

- `[HUMAN]` A maintainer reviews the archive candidate list in the brief's addendum and records, for each repository, keep, archive, make private, or transfer.
- `[HUMAN]` Each decision is applied before launch. No repository is deleted.
- `[HUMAN]` Packages of archived repositories that have a replacement are marked deprecated on nuget.org, naming the replacement [ASSUMPTION]. For example, the EventStores packages name EventStore as their replacement.

#### FR-30: Pinned repositories

A visitor sees the most important repositories first.

**Consequences (testable):**

- `[HUMAN]` Up to six in-scope repositories are pinned, with Platform first [ASSUMPTION].
- A maintainer chooses the set (Open Question 4).

#### FR-31: Public guide hub

Hexalith.Docs and `Hexalith/.github` are public early enough for links to them to work.

**Consequences (testable):**

- `[HUMAN]` Hexalith.Docs becomes public before the first migration that links to it, once the FR-65 exposure review has covered its contents. The review looks for sensitive data and doesn't remove planning artifacts.
- `[HUMAN]` `Hexalith/.github` is public from its creation (FR-59).

#### FR-32: Hexalith.BmadSkills sensitive-data check, now

The repository is already public, so the check is immediate. It isn't a launch-time task.

**Consequences (testable):**

- `[HUMAN]` Starting immediately, the 106 `.claude.json` files under `skills/reports/` are reviewed for credentials, tokens, personal data, and private paths.
- `[HUMAN]` Sensitive data found is removed, exposed credentials are revoked, and the result is recorded. Whether removal also requires rewriting Git history is a maintainer decision (Open Question 8).

#### FR-65: Planning-folder exposure review

Public planning folders expose no credentials or sensitive operational detail.

**Consequences (testable):**

- `[HUMAN]` Secret scanning, with push protection, is turned on for all 21 in-scope repositories and for `Hexalith/.github`.
- `[HUMAN]` A maintainer reviews every in-scope repository's `_bmad-output/` and `_bmad/`. The review looks for credentials and sensitive operational detail, such as staging addresses, identity-provider configuration, and registry policy. It starts now, because these folders are already public.
- `[HUMAN]` Sensitive material moves to a private repository, and the result is recorded per repository.
- Stranger test records identify testers by role, not by name.

### 4.5 Community files and contributor docs

**Description.** The community files live once, in `Hexalith/.github`, and apply to every in-scope repository. Each repository adds only its own development guide, and an operations page if it has operator content. Realizes UJ-4.

#### FR-59: Organization `.github` repository

The organization has a public `Hexalith/.github` repository.

**Consequences (testable):**

- `[HUMAN]` A maintainer creates `Hexalith/.github` as a public repository.
- It holds the front door (FR-25) and the community files (FR-33).
- It runs the docs check through a caller workflow, with the skeleton rules turned off.

#### FR-33: Community files

A contributor finds the same community files in every in-scope repository.

**Consequences (testable):**

- `Hexalith/.github` contains these files:
  - CONTRIBUTING, which links each in-scope repository's development guide by absolute URL, listed from the module registry
  - CODE_OF_CONDUCT [ASSUMPTION: Contributor Covenant 2.1]
  - SECURITY, which points to private vulnerability reporting
  - SUPPORT, which names the support channel (Open Question 17)
  - issue templates for a bug report and a feature request, plus a `config.yml` whose contact links point to SUPPORT
  - a pull request template, with a checklist covering tests, docs, and the Conventional Commit format
- Every in-scope repository shows these files as provided by the organization.

#### FR-34: No local overrides

The community files apply everywhere, because no in-scope repository overrides them.

**Consequences (testable):**

- In-scope repositories have no local CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, issue templates, or pull request template. Hexalith.EventStore's local code of conduct is removed too. Issue templates are all-or-nothing, so one local template would hide every organization template.
- The docs check fails a repository that has a local CONTRIBUTING.
- Repository-specific content from removed files moves to the development guide.

#### FR-35: Private vulnerability reporting

A security researcher has a real channel for reporting a vulnerability.

**Consequences (testable):**

- `[HUMAN]` Private vulnerability reporting is turned on for every public repository in the organization, so the SECURITY file never points to a channel that's turned off.

#### FR-36: Development guide

A contributor can build and test any in-scope repository that has code by following one page. Realizes UJ-4.

**Consequences (testable):**

- Every repository the module registry marks as having a development guide has one, copied from the template (FR-4).
- An agent following only the development guide builds the repository and runs its tests green, inside the dev container if the repository has one.
- The README's Contributing section links to it.

#### FR-37: Operations page

An operator finds runbooks and release procedures in `docs/`, not in the README.

**Consequences (testable):**

- Operator content lives on the operations page, copied from the template (FR-4). Examples are the Hexalith.McpCli operator runbook and the Hexalith.Works release procedure.
- The README's Documentation section links to it.

### 4.6 Honest quality signals

**Description.** A README shows few badges, and each one is trustworthy. Each badge reads a live source about its own repository. SonarQube Cloud runs once, in the shared CI. Realizes UJ-2.

#### FR-38: Allowed badges

A README shows at most five badges, all from the allowed set.

**Consequences (testable):**

- The allowed badges are:
  - NuGet version, required if the repository publishes packages
  - CI status, required
  - License, required
  - SonarQube Cloud quality gate and SonarQube Cloud coverage (two badges), required where CI builds .NET code [ASSUMPTION]
- No other badge appears.
- The module registry names each repository's badge sources. For a repository outside the managed modules, its own CI or caller workflow is the CI status source.
- The docs check fails a README with more than five badges, or with a badge outside the allowed set.

#### FR-39: A live source behind every badge

Every badge reads a live source about its own repository.

**Consequences (testable):**

- The docs check verifies each badge's parameters against the module registry:
  - the CI workflow exists on the default branch and runs there
  - the SonarQube Cloud key is the repository's own
  - the NuGet package ID is one the repository packs
  - the License badge reads the repository's own LICENSE file
- A badge whose live source reports "not found" counts as broken.

#### FR-40: SonarQube Cloud in the shared CI

Every in-scope repository that has .NET code gets a quality gate and coverage from the shared CI.

**Consequences (testable):**

- The shared CI runs the SonarQube Cloud scanner and reports the quality gate and coverage on `main`.
- There is one SonarQube Cloud project per repository, keyed by a convention (`addendum.md` §B.6), using an organization token. Without a token, as in a fork, the scan is skipped, not failed.
- `[HUMAN]` A maintainer creates the SonarQube Cloud organization and token, and decides whether to reuse or delete the existing legacy projects of Hexalith.Commons and Hexalith.PolymorphicSerializations (Open Question 18).
- A failing quality gate doesn't block Level 1, because the badge shows the failure honestly [ASSUMPTION].

### 4.7 Docs check

**Description.** One docs check, a job in the shared CI, checks documentation against the standard in every in-scope repository. For managed modules, Hexalith.CiCd turns it on and sets its mode. Other repositories call it from their own CI. It starts in warn mode and switches to fail mode at each migration. Every repository is in fail mode by launch. A failing check turns `main` red, and the nightly release then skips the repository, so enforcement uses what Hexalith.CiCd already has. Findings are precise enough for an agent to fix them without reading the standard. Realizes UJ-5, UJ-6.

#### FR-41: Docs check job

The shared CI includes a docs check that judges checked pages against the standard.

**Consequences (testable):**

- The docs check runs markdownlint-cli2, lychee, and a script.
- The script covers:
  - sections, order, and size (FR-9, FR-10)
  - the one-sentence description and registry consistency (FR-2, FR-11)
  - NuGet-safe rules (FR-12)
  - internal planning content (FR-13)
  - local CONTRIBUTING and `.github/README.md` files (FR-9, FR-34)
  - LICENSE (FR-60)
  - badges (FR-38, FR-39)
  - dev container pins (FR-5)
- It runs in every CI run on `main` and in the local docs check (FR-64).
- It judges checked pages and reports on other `docs/` pages.
- Every rule ID has a test fixture with its expected findings.
- Hexalith.CiCd classifies it as a product gate, because the README is the package page.

#### FR-42: Warn mode and fail mode

Each repository's docs check mode can be seen and changed in one place.

**Consequences (testable):**

- For a managed module, the mode is set through Hexalith.CiCd, and only Hexalith.CiCd agents change it (`addendum.md` §B.2). Other repositories set it in their own caller workflow or CI.
- Every in-scope repository runs the docs check in warn mode before its migration starts.
- Each repository switches to fail mode once its migration lands.
- At launch, all 21 in-scope repositories run in fail mode.
- Fail mode works as the Glossary's "Warn mode / fail mode" entry describes.

#### FR-43: Docs check everywhere

The docs check runs in all 21 in-scope repositories and in `Hexalith/.github`.

**Consequences (testable):**

- The 17 managed modules get the docs check once Hexalith.CiCd adopts them. That adoption is a prerequisite for their migration.
- Hexalith.Builds and Hexalith.CiCd run it from their own CI, which Hexalith.CiCd agents change.
- Hexalith.BmadSkills, Hexalith.Docs, and `Hexalith/.github` run it from a caller workflow [ASSUMPTION].

#### FR-44: Actionable findings

An agent can fix a finding without opening the standard. Realizes UJ-6.

**Consequences (testable):**

- Each finding names the file, line, rule ID, and a one-line fix hint.
- The job summary lists every finding.

#### FR-45: Link checking

Links keep working, and a flaky external site doesn't turn `main` red.

**Consequences (testable):**

- Every run checks internal links within the Hexalith organization. Absolute links to the repository's own files are resolved against the commit being checked.
- External links and badge hosts are checked weekly, by one central scheduled run across all in-scope repositories. It deduplicates by URL and reports failures without turning any `main` red [ASSUMPTION: it writes issues through Hexalith.CiCd's GitHub App, or a single report in Hexalith.Docs].
- Each migration verifies every external link on its checked pages once.

#### FR-46: Visible exceptions

Nobody can quietly pass the docs check by suppressing a rule.

**Consequences (testable):**

- Every suppression lives in the repository's docs check configuration, with a reason, and the job summary shows the suppression count.
- The planning-content and badge rules can't be suppressed, with one exception: the commit-SHA pattern may be suppressed with a reason, for pinned actions and submodule commits.

#### FR-64: Local docs check

An agent can run the docs check before pushing.

**Consequences (testable):**

- The local pre-push check from the shared CI includes the docs check, and its result matches CI's on the same commit.

### 4.8 Documentation rules for agents

**Description.** Agents write most Hexalith documentation, so the standard is also written as short agent instructions in Hexalith.AI.Tools. Every in-scope repository's agent entry points reach them. Every rule an agent could break mechanically has a docs check rule behind it. The agent entry points must never stop a newcomer's agent from running a quickstart. Realizes UJ-5, UJ-6.

#### FR-47: Documentation rules in Hexalith.AI.Tools

An AI agent receives the documentation rules with the shared agent instructions.

**Consequences (testable):**

- The documentation rules live in a topical instruction file in Hexalith.AI.Tools, referenced from `hexalith-llm-instructions.md` [ASSUMPTION: `hexalith-docs-instructions.md`].
- The file restates the standard's rules with the same rule IDs, and changes together with the standard (§8.5). The standard is authoritative.
- It is self-contained, as the Hexalith.AI.Tools authoring rule requires.
- It covers:
  - what a README is for
  - the README skeleton
  - where content belongs
  - the ban on internal planning content
  - badge rules and NuGet-safe rules
  - the AI prompt rule
  - writing style
  - "never add content after License"

#### FR-48: Rules reachable from every in-scope repository

An agent that starts work in any in-scope repository reaches the documentation rules.

**Consequences (testable):**

- Every in-scope repository has all three agent entry points. Missing ones are created. For example, Hexalith.PolymorphicSerializations has no `.github/copilot-instructions.md`.
- `[HUMAN]` Updating a repository's `references/Hexalith.AI.Tools` pointer is explicitly authorized, as the shared baseline requires.
- A check script, run during each migration, confirms that the chain from the entry points reaches the documentation rules in a fresh clone with root submodules initialized.
- The documentation rules (FR-47) are merged before the first migration.
- Changes leave the marked CI/CD block that Hexalith.CiCd delivers untouched.

#### FR-49: Short, enforceable rules

The documentation rules stay short enough that agents follow them.

**Consequences (testable):**

- The documentation rules file is 100 lines or fewer [ASSUMPTION].
- It holds only rules an agent can't infer from the repository.
- Each rule names its rule ID.

#### FR-50: One vocabulary

Public docs and agent instructions name module categories the same way.

**Consequences (testable):**

- Public docs say "business module" and "technical module".
- The documentation rules state that "business module" names the same repositories the architecture instructions call "domain modules" [ASSUMPTION].

#### FR-63: Agent entry points never block a quickstart

A newcomer's agent can run a quickstart in a fresh clone.

**Consequences (testable):**

- In a fresh clone without submodules, the agent entry points don't tell a newcomer's agent to stop while it runs a quickstart AI prompt. The shared baseline's "stop and report a missing baseline" rule applies to contributor work, not to running a quickstart (Open Question 13).
- The agent stranger test confirms this for every published block.

### 4.9 Time targets and stranger tests

**Description.** Each quickstart has a time target, measured in a clean environment. The 20-minute "Try it" target is fixed. The others are calibrated against a November baseline. Agent stranger tests are cheap and repeatable, so they cover the baseline and every iteration. Each person can be a newcomer only once, so each outside tester runs the human stranger test once, and a backup tester is ready. It is launch gate condition 1 (§8.3). Realizes UJ-1, UJ-2, UJ-3.

#### FR-51: Time targets

Every quickstart has a time target that stranger tests verify.

**Consequences (testable):**

- "Use the package": 5 minutes or less, from the README to a working sample call.
- "Run it": 15 minutes or less, from the README to a first successful call.
- "Use the tool": 5 minutes or less, from the README to the expected output [ASSUMPTION].
- "Try it": 20 minutes or less, from `github.com/Hexalith` to first success, on the newcomer's own machine. This target is fixed, including after the FR-66 upgrade.
- Each target is measured in its block's clean environment. No step is left out of the timer.
- Only the "Use the package", "Run it", and "Use the tool" targets can change, and only through calibration (FR-52).

#### FR-52: Baseline and calibration

The time targets are checked against real measurements before Level 2 work starts.

**Consequences (testable):**

- In November 2026, the agent stranger test runs on every existing quickstart.
- In November 2026, Platform's dev container cold start and cold build of its full dependency graph are measured, ahead of the R-3 decision.
- Each run records the minutes, the outcome, and a friction log.
- `[HUMAN]` Before Level 2 work starts, a maintainer records whether each calibratable target stays or changes. Any change goes into the standard.
- `[HUMAN]` If the cold build, or getting the prerequisites alone, would break the 20 minutes, a maintainer makes a scope decision by the R-3 deadline (§10): prebuilt images, or a "Try it" that needs no key.

#### FR-61: Stranger-test kit

A maintainer or agent can run a stranger test the same way every time.

**Consequences (testable):**

- Hexalith.Docs contains:
  - a definition of each clean environment, with a script that checks that a machine or container is clean
  - instructions for starting a fresh session of each supported agent tool
  - the friction log template
  - the result record format
  - the "no help" rule
- A run fails if the agent asks for a secret in chat.

#### FR-53: Agent stranger test

A maintainer can run a repeatable agent stranger test on any quickstart.

**Consequences (testable):**

- A fresh session of a supported agent tool gets only the starting page and its AI prompt, in the block's clean environment, using the kit (FR-61).
- For "Try it", the starting page is the Platform README until the link is live, and the front door after that.
- The model, the agent tool and its version, and the prompt are recorded.
- Each test is three runs. It passes when at least two reach first success within the time target without help [ASSUMPTION].
- Every red friction item becomes an issue.

#### FR-54: When the agent stranger test runs

The agent stranger test runs whenever a quickstart might have changed.

**Consequences (testable):**

- It runs at the baseline, before any block or the "Try it" link is published, after any change to a published quickstart's command or prerequisites, and before launch.
- The docs check reports changes to Quickstart sections, so the test can be triggered.
- After launch, it runs at least monthly for "Try it" and for every published "Run it" block [ASSUMPTION].
- Two failed periodic runs in one quarter count as "quickstarts keep breaking", which triggers a decision on adding the automated CI smoke test (the brief's addendum, decision 10, option C; §8.2).

#### FR-55: Human stranger test

An outside tester confirms "Try it" before launch.

**Consequences (testable):**

- The test runs after "Try it" passes the agent stranger test.
- The outside tester uses their own machine, checked clean with the kit's script. They start at `github.com/Hexalith` and are timed to first success, with no help. The target is 20 minutes or less.
- The outside tester's path (the setup command or the AI prompt) is declared before the test [ASSUMPTION: the setup command].
- The test produces a friction log, and every friction item becomes an issue.
- `[HUMAN]` A maintainer confirms the outside tester qualifies and names a backup outside tester before the first run (Open Question 12).
- If the test fails, the issues are fixed, "Try it" passes the agent stranger test again, and the backup tester runs the human stranger test.

#### FR-56: Launch ledger

Maintainers and agents can see each in-scope repository's progress and evidence in one place.

**Consequences (testable):**

- For each in-scope repository, the launch ledger records:
  - Level 1 date and reviewer
  - readability checklist result (FR-62)
  - docs check mode
  - republish status, with the package count
- It records every stranger test result: date, quickstart, duration, outcome, friction log, and, for agent stranger tests, the model and tool.
- It lives in Hexalith.Docs under `_bmad-output/`. It is public, never linked, and identifies testers by role [ASSUMPTION].

### 4.10 Rollout levels

**Description.** Each level is a definition of done. Agents can do most Level 1 writing. A maintainer reviews it and applies the GitHub settings. Level 2 adds the time targets and "Try it". Realizes UJ-5.

#### FR-57: Level 1 "Clean" done

An in-scope repository reaches Level 1 "Clean" when every item below holds.

**Consequences (testable):**

- **Prerequisites:**
  - Hexalith.CiCd has adopted the repository, if it is a managed module.
  - The docs check is running in warn mode.
  - The documentation rules (FR-47) are merged.
  - SonarQube Cloud (FR-40) is in place, where the module registry lists it.
- **Rules that hold:** FR-9 to FR-14, FR-16, FR-17, FR-18, FR-22, FR-28, FR-34, FR-36 to FR-39, FR-48, FR-60, and FR-63.
- **Quickstart blocks work but aren't timed:**
  - Every "Use the package" sample compiles in CI.
  - One agent run completes each published block.
  - For Platform, the Quickstart section links to its development guide until "Try it" passes the agent stranger test.
- **Accuracy:** every checked `docs/` page is accurate: its commands run as written, and every path, package, and type it names exists on the default branch.
- **Checks:** every external link on checked pages works when the migration lands. The docs check passes in fail mode.
- **Review and release:**
  - `[HUMAN]` A maintainer has reviewed the migration and completed the readability checklist (FR-62).
  - The packages are republished and verified (FR-15).

#### FR-58: Level 2 "Try-able" done

Every timed quickstart meets its time target, and "Try it" works.

**Consequences (testable):**

- Every published "Use the package" and "Use the tool" block passes the agent stranger test within its time target.
- Each repository listed with "Run it" in the module registry publishes the block once it passes the agent stranger test within 15 minutes. This can happen before or after launch.
- Platform's "Try it" passes the agent stranger test and then the human stranger test (FR-23, FR-55).
- Platform's Kubernetes how-to passes its agent stranger test (FR-24).

## 5. Human-only steps

Agents prepare these steps but don't take them. Each needs admin rights or a human decision.

- **Create and configure repositories:**
  - create `Hexalith/.github` (FR-59)
  - change repository visibility (FR-31)
  - set About descriptions and topics (FR-28)
  - archive repositories, make them private, or transfer them (FR-29)
  - deprecate packages (FR-29)
  - pin repositories (FR-30)
- **Turn on security features:** private vulnerability reporting, secret scanning, and push protection (FR-35, FR-65).
- **SonarQube Cloud:** create the organization and token, and decide on the legacy projects (FR-40).
- **Confirm the module registry's categories and one-sentence descriptions** (FR-2).
- **Review and land each migration, and complete the readability checklist** (FR-57, FR-62).
- **Start each republish release** (FR-15).
- **Authorize the `references/Hexalith.AI.Tools` pointer update** (FR-48).
- **Sensitive-data reviews and credential revocation** (FR-32, FR-65).
- **Calibration, and scope decisions on prebuilt images or a "Try it" that needs no key** (FR-52).
- **Recruit and confirm the outside tester and a backup** (FR-55).
- **Go or no-go decisions** (§8.4).

## 6. Cross-cutting non-functional requirements

- **NFR-1. Written for people.** Docs are simple, clear, and easy to read. They put the most important point first and use second person, active voice, sentence-case headings, and numbered steps. They are short and written for a global audience. Vale is out of scope, so the readability checklist (FR-62), the documentation rules, and stranger test friction logs enforce this.
- **NFR-2. Rendering parity.** Every README renders on both GitHub and nuget.org without a broken link, a broken image, or raw markup.
- **NFR-3. Honest claims.** No document claims a capability, a time, or a quality level that isn't measured or backed by a live source.
- **NFR-4. Commands run as written.** Readers copy and paste quickstart commands. The only values they supply are ones the prerequisites list.
- **NFR-5. One source per rule.** The standard is authoritative and states each rule once. The documentation rules restate it, using its rule IDs. The docs check keeps copies aligned. Nothing depends on templates staying in sync.
- **NFR-6. Accessibility.** Images have alt text, link text describes its target, and no information appears only in an image or a video.
- **NFR-7. Docs check speed.** The docs check adds 2 minutes or less to a CI run of Hexalith.EventStore, the reference repository [ASSUMPTION].
- **NFR-8. Secret handling.** No quickstart asks for a secret in an AI prompt or in chat, and none asks the reader to commit one. The stranger-test kit fails any run that breaks this.
- **NFR-9. Contained agent actions.** AI prompts keep installs and changes inside the dev container or the cloned repository, and list every host-level change in the prerequisites. Dev container files and agent entry points take effect on a newcomer's machine, so only a maintainer may change them (Open Question 19).

## 7. Non-goals

- This initiative doesn't build Platform or the chatbot. It depends on them (§11).
- Changing CI/CD outside Hexalith.CiCd.
- Vale, organization-wide rulesets or required workflows, Coverity, Codacy, and Codecov.
- Reorganizing `docs/` folders.
- A per-repository `llms.txt`.
- Package types other than NuGet.
- xppmodel.
- Outreach.

Deferred items, each with its revisit trigger, are in §8.2.

## 8. Launch scope and rollout

### 8.1 In scope

- Foundations in Hexalith.Docs: the standard, the module registry, the templates, the prompts, the overview guide, the readability checklist, and the stranger-test kit (FR-1 to FR-8, FR-61, FR-62).
- Level 1 "Clean" for all 21 in-scope repositories, as FR-57 defines it, including the republish (FR-15).
- Level 2 "Try-able": every published block on target, "Try it", and the Kubernetes how-to (FR-23, FR-24, FR-51 to FR-56, FR-58).
- The front door, community files, organization cleanup, and exposure reviews (FR-25 to FR-27, FR-29 to FR-33, FR-35, FR-59, FR-65).
- SonarQube Cloud and the docs check in the shared CI (FR-40 to FR-46, FR-64).
- Documentation rules in Hexalith.AI.Tools (FR-47 to FR-50).

### 8.2 Out of scope for launch, with revisit triggers

| Item | Revisit trigger |
| --- | --- |
| Prebuilt images, for "Try it" only | The baseline or an iteration shows "Try it" can't meet 20 minutes while building from source (R-3) |
| Automated CI smoke test (the brief's addendum, decision 10, option C), for "Try it" first | Two failed periodic agent stranger test runs in one quarter after launch (FR-54) |
| Published container images, beyond prebuilt images for "Try it" | Demand justifies them. The Kubernetes how-to builds its images locally |
| Documentation website | There are enough docs to justify one |
| Hosted demo | Demand justifies one |
| Package READMEs generated at pack time | A single README would mislead users of a repository's packages |
| OpenSSF Scorecard | Later, when wanted. It renders on nuget.org only through Shields |
| Azure, AWS, and Scaleway deployment | After launch |
| Cleaning unlinked `docs/` pages | After launch, working from the docs check report |
| "Try it" ending at a first chat message (FR-66) | ChatBot's chat runs from Platform's setup command (D-10) |

### 8.3 Launch gate

Launch happens only when all of these hold:

1. "Try it" passes the human stranger test (FR-55). That requires Platform stories 3.2 to 3.8 (D-2).
2. All 21 in-scope repositories reach Level 1 "Clean", with the docs check in fail mode (FR-57).
3. Every published quickstart block meets its time target in its latest agent stranger test (FR-58).
4. Every package has a republished version that shows its migrated README (FR-15).
5. The front door is published with the "Try it" link, lists only in-scope repositories, and the pinned set is chosen (FR-25, FR-26, FR-30).
6. The community files are live in the public `Hexalith/.github`, and private vulnerability reporting is on (FR-33 to FR-35, FR-59).
7. The documentation rules are published in Hexalith.AI.Tools and reachable from every in-scope repository (FR-47, FR-48).
8. Hexalith.Docs is public with the overview guide (FR-8, FR-31).
9. The Kubernetes how-to passes its agent stranger test (FR-24).
10. The exposure reviews are complete (FR-32, FR-65), and the archive decisions are applied (FR-29).

### 8.4 Rollout sequence and decision points

[ASSUMPTION: the dates are proposed and depend on Open Question 6, review capacity. The holiday weeks are treated as low-capacity.]

| When | Work |
| --- | --- |
| Now | The Hexalith.BmadSkills check and the planning-folder exposure review start (FR-32, FR-65). |
| By 2026-11-20 | Foundations (FR-1 to FR-8, FR-61, FR-62). Documentation rules merged (FR-47). The docs check is in the shared CI in warn mode, with its patterns tuned (FR-41, FR-42). The baseline is taken, including Platform's cold build (FR-52). The dev container spike is done (Open Question 15). Platform confirms that stories 3.2 to 3.8 are on track for mid-December (D-2 target). Hexalith.Docs and `Hexalith/.github` are public (FR-31, FR-59). |
| By 2026-11-27 | Pilot migrations of Hexalith.Commons and Hexalith.PolymorphicSerializations, the first repositories Hexalith.CiCd adopts. Their packages are republished. |
| **2026-12-01: go/no-go 1** | `[HUMAN]` Are the pilots done? Is the review rate measured (Open Question 6)? Are Platform stories 3.2 to 3.8 on track for mid-December (D-2)? If any answer is no, the launch moves to January 2027, with the same "Try it". |
| December | Level 1 waves, following Hexalith.CiCd's adoption order. Each repository switches to fail mode and republishes. |
| Mid-December | Platform runs all seven MVP modules locally, with agent access through Hexalith.McpCli (D-2). Agent stranger test iterations run on "Try it". |
| **2026-12-15: go/no-go 2** | `[HUMAN]` Does "Try it" pass the agent stranger test? If not, launch moves to January 2027. |
| Late December | The "Try it" link goes live, the human stranger test runs, and launch follows once the gate passes. |

**"Try it" sequence.**

1. The Platform README's Quickstart section links to its development guide (FR-17).
2. "Try it" passes the agent stranger test, starting from the Platform README (FR-53).
3. The Platform README shows its "Run it" block, the front door's "Try it" link goes live, and later agent stranger tests start from the front door (FR-17, FR-26, FR-53).
4. The human stranger test runs (FR-55). If it fails, the issues are fixed, "Try it" passes the agent stranger test again, and the backup tester runs the test.
5. Launch follows once every launch gate condition holds (§8.3).

### 8.5 After launch

- The Hexalith.Docs maintainer owns the standard and the module registry [ASSUMPTION].
- **Rule changes:** a rule change updates the standard (FR-1) and the documentation rules (FR-47) together, under the same rule ID. The new rule first reports findings without failing any repository, then starts failing in a later release of the shared CI.
- **New repositories:** a new repository gets a registry row (FR-2) and a front door entry (FR-25). It reaches Level 1 before it is announced.
- **Testing:** agent stranger tests run monthly (FR-54). SM-9 is measured 90 days after launch.

## 9. Success metrics

### Primary

- **SM-1. "Try it" time.** The human stranger test reaches first success in 20 minutes or less from `github.com/Hexalith`, on the tester's own machine, with no help. This is launch gate condition 1 (§8.3). Validates FR-23, FR-55.
- **SM-2. Agent "Try it".** At least two of three agent stranger test runs complete "Try it" within 20 minutes. Validates FR-22, FR-23, FR-53.
- **SM-3. Docs check coverage.** All 21 in-scope repositories run the docs check in fail mode, and `main` is green. Validates FR-41 to FR-43, FR-57.

### Secondary

- **SM-4. Quickstarts on target.** Every published quickstart block passes its latest agent stranger test within its time target. Validates FR-19 to FR-21, FR-51, FR-58.
- **SM-5. Package pages.** The latest version of every package shows the one-sentence description and the Quickstart section on nuget.org. Validates FR-15.
- **SM-6. Badge honesty.** Every badge reads a live source about its own repository. Validates FR-38 to FR-40.
- **SM-7. A clean organization page.** The front door and the pinned set show only in-scope repositories. Every other public repository has been archived, made private, or transferred. Every in-scope repository shows the community files. Validates FR-25, FR-29, FR-30, FR-33 to FR-35.
- **SM-10. "Run it" coverage.** This counts, without a target, how many registry rows listed with "Run it" have a published block at launch. It is informational. Validates FR-58.

### After launch

- **SM-9. The standard holds.** Ninety days after launch:
  - all 21 in-scope repositories are still in fail mode
  - checked pages have zero planning-content findings
  - at least 80% of docs check failures were fixed without a human edit [ASSUMPTION]

  Validates FR-41, FR-47.
- **SM-8. Stars.** 1,000 GitHub stars across the organization within a year of launch, which is the end of 2027 if launch holds. The baseline is 0 on 2026-11-09. This depends on outreach, which is outside this initiative's control, and no FR drives it.

### Counter-metrics (do not optimize)

- **SM-C1. README brevity.** Don't cut a README to meet its line limit by removing what a newcomer needs to understand the module or start the quickstart. A README that passes the docs check but fails the readability checklist or a stranger test is a failure. Counterbalances SM-3.
- **SM-C2. Suppressions.** Don't pass the docs check by adding suppressions. Track the suppression count across in-scope repositories. Counterbalances SM-3, SM-9.
- **SM-C3. AI prompt length.** Don't let the prompt absorb a complex setup. If a prompt grows, fix the command. Counterbalances SM-2.
- **SM-C4. Timer integrity.** Don't meet a time target by pre-provisioning keys or accounts, warming caches, or leaving steps out of the timer. Counterbalances SM-1, SM-2, SM-4.
- **SM-C5. Star chasing.** Don't add marketing copy to READMEs to attract stars. Counterbalances SM-8.

## 10. Risks and mitigations

| ID | Risk | Mitigation |
| --- | --- | --- |
| R-1 | **Platform's agent-access stories may not land by mid-December.** Platform's Epic 2 is still open after about six weeks. In Epic 3, only story 3.1 is done, stories 3.2 and 3.3 are in progress, and stories 3.4 to 3.8 haven't started (GitHub `main`, 2026-11-11). The chat ending is further away: ChatBot isn't in Platform's MVP, its chat interface is its Epic 13, and only its Epic 1 is in progress. | D-2, with its target and hard deadline. If D-2 slips, the launch moves to January 2027 with the same "Try it". The chat ending is a later upgrade (FR-66), not a launch condition. |
| R-2 | **Only one human stranger test, and its tester's eligibility is uncertain.** Each person can be a newcomer only once, and the tester the brief names is an organization owner. | Define the outside tester by never having run Hexalith, not by their GitHub rights. Confirm eligibility and name a backup before the first run (FR-55). Use agent stranger tests for every iteration. |
| R-3 | **Build time.** Building Platform from source pulls in 17 repositories and may exceed 20 minutes. | Measure the cold build and dev container start in November (FR-52). `[HUMAN]` Make the prebuilt-images decision by 2026-11-30 if needed [ASSUMPTION]. That work isn't in this plan. |
| R-4 | **Review capacity.** One maintainer reviews 21 migrations and republishes about 100 packages in about 7 weeks that include the holidays. | Run pilots first and measure the review rate. Use go/no-go dates (§8.4). The docs check removes mechanical review, and the migration prompt lists the decisions it leaves open. |
| R-5 | **The docs check turns `main` red for the wrong reasons.** | Tune the patterns in warn mode first, keep a fixture per rule, never let external links turn `main` red, and allow the commit-SHA suppression. |
| R-6 | **Agent results vary.** In one benchmark, agents set up a repository from a bare environment only 39–57% of the time. | Three runs with a 2-of-3 threshold, the stranger-test kit, a recorded model, and prompts of 10 lines or fewer. |
| R-7 | **Getting prerequisites takes too long.** The AI prompt path needs a supported agent tool. A newcomer who doesn't have one may run out of time. | The command path needs no agent tool, and Hexalith needs no LLM provider key. Prerequisite time counts toward the timer by decision. `[HUMAN]` If it alone breaks the target, make a scope decision (FR-52). |
| R-8 | **Opening the dev container from a terminal agent may not work on a clean host.** The devcontainer CLI needs Node, and an agent inside the editor loses its session when VS Code reopens in the container. | A spike by 2026-11-20 settles the mechanism and the supported agent tools (Open Question 15). |
| R-9 | **Copies drift from templates.** | The docs check enforces the standard, including dev container pins (NFR-5, FR-5). |
| R-10 | **Public planning folders expose sensitive detail.** These folders are already public in 20 repositories. | Start the exposure review now (FR-65), with secret scanning and push protection. |
| R-11 | **The republish creates package versions** that consumers notice. | One patch release per repository, outside Platform's stabilization window (FR-15). |
| R-12 | **Hexalith.CiCd's adoption pace limits Level 1.** A managed module can't run the docs check until Hexalith.CiCd adopts it. Platform and Timesheets are adopted last. | Follow Hexalith.CiCd's adoption order. Confirm its timeline at go/no-go 1 (D-1). |
| R-13 | **`docs/` folders hold far more planning content than the plan assumed.** About 430 of 970 pages match the patterns, and Platform has about 2,600 evidence files. | Judge checked pages only, and report on the rest. Cleanup happens after launch. The migration prompt moves content and never deletes it in bulk. |
| R-14 | **Agent entry points stop a newcomer's agent.** In 16 repositories, the agent entry points tell an agent to stop when the `references/Hexalith.AI.Tools` submodule is missing, as it is in a fresh clone. | FR-63, and Open Question 13. |

## 11. Dependencies

- **D-1. Hexalith.CiCd.** It adopts all 17 managed modules before launch. It also:
  - delivers the docs check job and sets its modes
  - provides the republish release path and the commit-lint rule for scopes
  - keeps its CI/CD block in the agent entry points
  - may guard dev container files
- **D-2. Platform stories 3.2 to 3.8.** One command starts all seven MVP modules locally, with a generated local realm, a ready-made tenant, and agent access through Hexalith.McpCli. This is the blocking dependency for "Try it" (R-1).
  - **Target:** Platform confirms by 2026-11-20 that the stories are on track for mid-December.
  - **Hard deadline:** go/no-go 1, on 2026-12-01. If they aren't on track by then, the launch moves to January 2027.
- **D-3. Platform Kubernetes support** for the how-to (FR-24).
- **D-4. Hexalith.Builds.** It hosts the shared CI and release pipelines, the docs check, the SonarQube Cloud scanner, README packing, and the local pre-push check.
- **D-5. Hexalith.AI.Tools.** It hosts the documentation rules and the shared baseline that FR-63 needs changed.
- **D-6. SonarQube Cloud.** An organization on the free OSS plan, one project per repository, and an organization token.
- **D-7. GitHub organization admin rights** for every `[HUMAN]` step.
- **D-8. nuget.org publishing** for every package.
- **D-9. An outside tester and a backup,** available once "Try it" passes the agent stranger test.
- **D-10. ChatBot's chat in Platform's composition.** This is needed only for the FR-66 upgrade, not for launch.

## 12. Open questions

| # | Question | Owner | Blocks | Needed by |
| --- | --- | --- | --- | --- |
| 1 | Does "Try it" need anything besides Docker, VS Code, and, for the AI prompt path, a supported agent tool? | Platform maintainer | FR-18, FR-23, FR-51 | Mid-December |
| 2 | Which archive candidates are archived, made private, or transferred? This includes the three template repositories. | Maintainer | FR-29 | 2026-11-30 |
| 3 | What is each repository's category and one-sentence description? Memories, CiCd, Docs, and McpCli are confirmed as technical modules. | Maintainer | FR-2, FR-25, FR-28 | Before the first migration |
| 4 | Which repositories are pinned? | Maintainer | FR-30 | Before launch |
| 5 | Which quickstart blocks do Hexalith.Builds, Hexalith.AI.Tools, and Hexalith.BmadSkills use? | Maintainer | Those three Level 1 migrations | During their migrations |
| 6 | How many migrations can be reviewed per week? | Maintainer | §8.4 dates | Go/no-go 1 |
| 7 | Is 5 minutes right for "Use the tool"? | Maintainer | FR-21, FR-51 | Calibration |
| 8 | Does the Hexalith.BmadSkills cleanup require rewriting Git history? | Maintainer | FR-32 | When its review ends |
| 9 | When does ChatBot's chat join Platform's plan? | Platform and ChatBot maintainer | FR-66 | After launch |
| 10 | Where does the docs check sit in the shared CI pipeline? Hexalith.CiCd has accepted it as a product gate (2026-11-11). | Hexalith.CiCd maintainer, in architecture | FR-41 to FR-43 | Before the docs check is built |
| 11 | The pilot release design gives module `docs(readme)` changes a patch version. When will the compatible Builds release reach each pilot, and will commit lint ban story, epic, and FR scopes? | Hexalith.CiCd maintainer | FR-14, FR-15 | Before the pilots |
| 12 | Does the named tester qualify as an outside tester, and who is the backup? | Maintainer | FR-55 | Before mid-December |
| 13 | How do agent entry points let a newcomer's agent run a quickstart in a fresh clone? | Hexalith.AI.Tools maintainer | FR-63 | Before the first block is published |
| 14 | Where does "Run it" start for business modules, given the rule that domain modules ship no AppHost? | Architecture | FR-20, FR-58 | Before the first "Run it" block |
| 15 | How does a supported agent tool open the dev container from a clean host, and which tools are supported? | Maintainer (spike) | FR-6, FR-23, FR-53 | 2026-11-20 |
| 16 | Should BMAD's `project_knowledge` setting stop pointing at `docs/`, so planning content isn't written back there? | Maintainer | FR-13 durability | Before the waves |
| 17 | What is the support channel (GitHub Discussions, issues, other)? | Maintainer | FR-33 | Before `Hexalith/.github` is published |
| 18 | Are the legacy SonarQube Cloud projects reused or deleted? | Maintainer | FR-40 | Before the pilots |
| 19 | Can Hexalith.CiCd's guard protect dev container files and agent entry points from unreviewed changes? | Hexalith.CiCd maintainer | NFR-9 | Before the first block is published |
| 20 | Which first operation does "Try it" run, on which module? | Platform maintainer | FR-23 | Before the "Try it" block is written |

## 13. Assumptions index

- §2.3: the user journeys are inferred from the brief's audiences, with illustrative protagonists.
- FR-1: the standard's file name, `docs/documentation-standard.md`.
- FR-2 format decision (20 November 2026). The registry is JSON next to the standard. Category and description confirmation remains a maintainer step.
- FR-3: templates and prompts live in `templates/` and `.github/prompts/`.
- FR-5: Hexalith.FrontComposer's dev container is aligned with the template.
- FR-7:
  - Hexalith.BmadSkills is added to `.gitmodules`.
  - Deleting more than 20 lines without a new home triggers escalation.
- FR-8: the minimum launch guide set.
- FR-9: fixed heading text, and no table of contents section.
- FR-10: quickstart blocks are 30 lines or fewer.
- FR-11: package `Description` values start with the one-sentence description.
- FR-13:
  - The docs check doesn't scan `_bmad-output/`.
  - The standard has an exemption for quoting the patterns.
- FR-14: release history goes to GitHub Releases.
- FR-15: republishing happens before 2026-12-10.
- FR-17: Hexalith.Docs and Hexalith.CiCd have no quickstart block.
- FR-21, FR-51: the "Use the tool" target is 5 minutes.
- FR-23: the first "Try it" operation is creating a project, then listing it.
- FR-24: the Kubernetes how-to uses a local cluster and locally built images.
- FR-25: the front door is 60 lines or fewer.
- FR-28: the category topic names.
- FR-29: deprecating replaced packages.
- FR-30: up to six pins, with Platform first.
- FR-33: Contributor Covenant 2.1.
- FR-38: the SonarQube Cloud badges are required where CI builds .NET code.
- FR-40: a failing quality gate doesn't block Level 1.
- FR-43: Hexalith.BmadSkills, Hexalith.Docs, and `Hexalith/.github` use a caller workflow.
- FR-45: how the central link run reports.
- FR-47: the documentation rules file is named `hexalith-docs-instructions.md`.
- FR-49: the documentation rules file has a 100-line budget.
- FR-50: "business module" means "domain module".
- FR-53: a 2-of-3 pass threshold.
- FR-54: monthly agent stranger tests after launch.
- FR-55: the outside tester's declared path is the setup command.
- FR-56: the launch ledger lives under `_bmad-output/` and identifies testers by role.
- NFR-7: a 2-minute budget on Hexalith.EventStore.
- §8.4: the rollout dates.
- §8.5: the owner of the standard.
- R-3: the prebuilt-images decision deadline of 2026-11-30.
- SM-9: the 80% threshold.

**Recorded decisions (not assumptions).** These are logged as decisions in this folder's `.memlog.md`:

- the 21 in-scope repositories
- prerequisite time counts toward the timer
- the republish
- compiled samples
- the plan rebuilt on Hexalith.CiCd's ownership of CI/CD
- "Try it" ends with the newcomer's agent running a first Hexalith operation through Hexalith.McpCli, and the chat comes as a later upgrade (FR-66)
- the outside tester definition
- the immediate Hexalith.BmadSkills check
- Level 1 without timing
- the scope of checked pages
- the fixed "Try it" target
