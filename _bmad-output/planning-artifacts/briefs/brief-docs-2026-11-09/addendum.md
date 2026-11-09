---
title: "Addendum: Hexalith Documentation Standard"
created: 2026-11-09
updated: 2026-11-09
---

# Addendum: Hexalith Documentation Standard

This addendum holds the detail behind the brief:

- the decisions, with the alternatives that were rejected
- the launch checklists
- the evidence: a survey of the current state and a research digest

Downstream documents (PRD, architecture, rollout plan) build on it. Repositories are listed by short name. For example, builds is Hexalith.Builds.

## Decisions at a glance (accepted 2026-11-09)

| # | Topic | Accepted option |
|---|---|---|
| 1 | Deploy in minutes | Run one command (`aspire run`) inside a dev container. The "Try it" quickstart runs on Docker, Platform gets a Kubernetes how-to, and Azure, AWS and Scaleway come later. An AI prompt of 10 lines or fewer wraps the command. |
| 2 | README skeleton and quickstarts | Use one skeleton for every repository. Each module is labeled business or technical, and each repository picks one or more of three quickstart blocks. |
| 3 | Front door | Use the organization profile README, with cross-module guides in Hexalith.Docs. No website for now. |
| 4 | GitHub README and NuGet page | Write one NuGet-safe README per repository. |
| 5 | Quality indicators | Show NuGet version, CI status, license, and SonarQube Cloud. Drop Coverity and Codacy. |
| 6 | Contributor docs and policies | Put organization defaults in `Hexalith/.github`, and add `docs/development.md` to each repository. |
| 7 | Keeping docs consistent | Add agent rules to aitools and a docs check to the builds CI. The check warns first, then becomes required. |
| 8 | "Try it" while Platform is in progress | Do the docs now, and announce only when "Try it" works. A demo video is optional. |
| 9 | Rollout | Bring all 20 repositories to Level 1, "Clean." For Level 2, "Try-able," start with Platform. Clean up the organization. |
| 10 | Time targets and how to measure them | Targets are 5, 15, and 20 minutes or less. A human stranger test is the launch gate, and an agent test runs routinely. |
| 11 | Planning folders | Keep `_bmad-output/` public in every repository, but never link it from READMEs or docs. This was decided in conversation, without an options analysis. |

## Launch scope detail

### Foundations in Hexalith.Docs

- The standard, on one page
- The README skeleton, with three quickstart blocks: "Use the package," "Run it," and "Use the tool"
- A `docs/development.md` template
- A dev container template
- The AI-prompt pattern: 10 lines or fewer, wrapping exactly one command
- An audit-and-migration prompt, modeled on `builds/.github/prompts/audit-hexalith-ci-cd.prompt.md`
- Cross-module guides

The README skeleton is 150 lines or fewer and has these sections:

1. Title and a one-sentence description of 120 characters or fewer. The description matches the GitHub About text and the NuGet description.
2. Up to five badges.
3. What the module does and who it's for, in five lines or fewer.
4. Quickstart: one or more quickstart blocks that fit on one screen.
5. A packages table, if the repository publishes packages.
6. Documentation links into `docs/`.
7. A "Part of Hexalith" link to the front door.
8. A link to contributing guidance.
9. License.

### `Hexalith/.github` (public)

- The organization profile (`profile/README.md`)
- CONTRIBUTING, with a link to each repository's `docs/development.md`
- CODE_OF_CONDUCT
- SECURITY, with GitHub private vulnerability reporting turned on
- SUPPORT
- Issue and PR templates

### Shared CI in Hexalith.Builds

- The SonarQube Cloud scanner, with the quality gate and coverage.
- A docs-check job that runs markdownlint-cli2, lychee, and a script that checks for required sections, length, and forbidden content. It starts as a warning and becomes required for each repository once that repository is migrated.

### Hexalith.AI.Tools

- Documentation rules in the shared agent instructions

### Level 1 "Clean" checklist (all 20 current repositories)

- The README follows the skeleton and meets its target of 150 lines or fewer.
- The README is NuGet-safe: it uses absolute links, avoids raw HTML, and only shows badges from hosts that nuget.org allows.
- The one-sentence description matches the GitHub About text and the NuGet description, and topics are set.
- The README, CONTRIBUTING, and `docs/` contain no internal planning content: no epics, stories, FR/NFR IDs, or links to `_bmad-output`.
- `_bmad-output/` stays public but is never linked from docs.
- Repository-level CONTRIBUTING files are removed, so the organization defaults apply.
- Runbooks move to `docs/development.md`.
- Release history moves to CHANGELOG.md or GitHub Releases.
- All links and badges work.
- Every `docs/` page linked from the README is accurate. `docs/` folders are cleaned, not reorganized.

### Level 2 "Try-able"

- The Platform "Try it" quickstart on Docker is the launch gate. It ends with a first chat message.
- Each module's "Run it" quickstart is added as soon as it meets its time target.
- Platform gets a Kubernetes deployment how-to, with no time target.

### Organization cleanup

- After review, archive the repositories listed under [Archive candidates](#archive-candidates-awaiting-review). Archiving can be undone.
- Before launch, check Hexalith.BmadSkills for sensitive data. It contains 106 `.claude.json` files under `skills/reports/` that were copied from eval runs.
- Make Hexalith.Docs and `Hexalith/.github` public.
- Pin the key repositories.

**After launch:** Stars will probably concentrate on Platform, the repository behind "Try it."

## Current-state baseline (2026-11-09)

This baseline comes from a read-only survey of the local clones and from GitHub organization data.

### Repositories

Every repository is MIT-licensed. "CQL+DR" means CodeQL plus dependency review, run through the shared workflows in Hexalith.Builds.

| Repo | README lines | Role the README plays today | Badges | NuGet | Quality CI |
|---|---|---|---|---|---|
| agents | 6 | stub | – | yes | CQL+DR |
| aitools | 61 | agent instructions | – | no | none |
| bmadskills | none | – | – | no | none |
| builds | 1275 | build runbook (about 935 lines on local tools) | version tag | yes | CQL+DR |
| chatbot | 175 | epic changelog + local setup | – | yes | none |
| cicd | 2 | stub | – | no | none |
| commons | 557 | product intro, per-package READMEs | License, Discord, Build, NuGet, Coverity, Codacy, Sonar×4 | yes | CQL+DR |
| conversations | 157 | contract/evidence log | – | yes | CQL+DR |
| eventstore | 203 | product intro (best example) | stars, NuGet, Build, Docs, License | yes | CQL+DR, coverage |
| folders | 54 | submodule setup | – | yes | CQL+DR, coverage gate |
| frontcomposer | 26 | dependency pinning | – | yes | CQL+DR, Stryker |
| mcpcli | 631 | operator runbook | – | yes | none |
| memories | 138 | quick start + operations | – | yes | CQL+DR, coverage |
| parties | 341 | product intro + appended content | – | yes | CQL+DR, coverage |
| platform | 608 | release/evidence log (SHAs, run IDs) | – | no (source releases) | none |
| polymorphicserializations | 182 | product intro | License, Discord, Build, NuGet, Coverity, Codacy, Sonar×11 | yes | CQL+DR |
| projects | 1 | title only | – | yes | CQL+DR, coverage |
| tenants | 175 | product intro (good example) | CI, NuGet, License | yes | CQL+DR, coverage gate |
| timesheets | 149 | agent hooks + build | – | yes | CQL+DR, coverage |
| works | 131 | release procedure | – | yes | CQL+DR |
| xppmodel (Itaneo) | 2 | stub | – | no (Python) | none |

### Findings that shape the standard

- **The README is the NuGet package page.** `builds/Hexalith.Package.props` packs the root README into every package. The projects README is only a title, so the nuget.org page for `Hexalith.Projects.Contracts` 1.2.3 shows only a title. Only commons ships separate per-package READMEs (`commons/src/libraries/*/README.md`).
- **READMEs have no shared purpose.** Depending on the repository, the README acts as a product introduction, a contributor runbook, or a release and evidence log.
- **Internal planning content leaks into public docs.** Examples include:
  - epic and story references
  - FR/NFR IDs
  - links to `_bmad-output`
  - backlogs and evidence files under `docs/`
  - sprint rules in `memories/CONTRIBUTING.md`
- **AI agents write most of the docs.** Nearly every repository has agent files. The shared agent instructions in `aitools/hexalith-*-instructions.md` contain no README rules, and agents tend to add content after the License section.
- **Quality badges don't match the tooling.** Two repositories display Coverity, Codacy, and SonarCloud badges, but no workflow runs those scans. The Sonar analyzer is only a compile-time package (`builds/Hexalith.Build.props:40`).
- **Some links are broken.** Badges point to deleted workflows (commons, eventstore), a license badge points to the wrong repository, and one link points to a sample path that doesn't exist.
- **Community health files are missing.** There's no `Hexalith/.github` repository. No repository has SECURITY.md, SUPPORT.md, issue templates, or a PR template. Only eventstore has a code of conduct.
- **GitHub About metadata is thin.** No repository has topics or a homepage. Some descriptions are missing, and several contain typos.

### Runtime and deploy

- **A common start command.** Eleven repositories plus platform have an Aspire AppHost: chatbot, conversations, eventstore, folders, frontcomposer, memories, parties, projects, tenants, timesheets, builds, and `platform/apphost.cs`. That makes `aspire run` the start command they already share.
- **Prerequisites.** The platform README requires:
  - .NET SDK 10.0.403 or later
  - Aspire CLI 13.6.4 exactly
  - Docker
  - an isolated Dapr home with CLI 1.18.2 and runtime 1.18.7 (a machine-wide `dapr init` doesn't qualify)
  - submodules checked out at exact commits

  The README's own commands then export `HEXALITH_DAPR_HOME` with a version in the path (1.18.2) that differs from the one the setup script creates (1.18.7).
- **An AI-prompt quickstart already exists.** The mcpcli README has a "Quick start: Claude Code sets it up for you" section. The prompt is about 20 lines and needs a handoff folder, a gateway URL, and a token from an "environment owner." It shows that the idea works, and also how a prompt grows when the command under it is complex.
- **No container images and one dev container.** No CI workflow publishes container images, and frontcomposer is the only repository with a `.devcontainer/`.
- **Dependencies.** Platform's submodules cover 17 repositories, and chatbot's cover 16. So nearly every current repository is something the chatbot needs.

### Organization

- **Size.** The organization has 67 non-archived repositories, and 60 of them are public. Only 20 public repositories are current modules, with commits pushed in November 2026.
- **This repository is private.** Hexalith.Docs must become public before it can serve as the guide hub.

### Archive candidates (awaiting review)

The 40 public repositories that aren't current modules:

- 5 apparent forks of third-party projects: semantic-kernel, ollama, open-webui, qdrant, and kernel-memory.
- 2 `_OLD` repositories: Documents_OLD and Security_OLD.
- 3 templates: Templates, MyNewModule, and MyNewPackage. These haven't been inspected yet, so decide whether to keep them.
- About 30 older modules. Some sit next to their replacements, such as EventStores beside EventStore and FrontShell beside FrontComposer.

### Existing levers

- **Hexalith.Builds is the de facto enforcement layer.** Sixteen repositories use its reusable workflows (`domain-ci.yml`, `codeql.yml`, `commitlint.yml`, and others). It also holds:
  - `ci-cd-standards.md`, which has no documentation rules yet
  - the audit prompt `audit-hexalith-ci-cd.prompt.md`
  - `Hexalith.Package.props`
  - the module templates
- **cicd** was set up to harmonize workflows but contains none.
- **eventstore** has `docs/page-template.md` plus markdownlint-cli2 and lychee configs, but no workflow runs them yet.
- **frontcomposer** has a docfx site.

## Best-practices research digest (2026-11-09)

Claims were checked against primary sources where possible. Items marked [unverified] couldn't be confirmed.

### GitHub

- **README handling.** GitHub looks for the README in `.github/`, then the root, then `docs/`, and truncates it past 500 KiB. It builds an Outline table of contents from the headings and resolves relative links against the current branch. ([About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes))
- **Organization-wide defaults.** A public `.github` repository can provide:
  - CODE_OF_CONDUCT
  - CONTRIBUTING
  - SECURITY
  - SUPPORT
  - ACCESSIBILITY
  - FUNDING
  - issue, PR, and discussion templates

  There are three caveats:
  - LICENSE can't be a default.
  - The defaults don't appear in clones or packages.
  - Issue templates are all-or-nothing for each repository.

  ([Creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file))
- **Community Standards checklist.** The checklist covers: description, README, code of conduct, contributing, license, security policy, issue templates, PR template, and content reports.

### README conventions

- **[Standard Readme](https://github.com/RichardLitt/standard-readme/blob/main/spec.md) order:**
  1. Title
  2. Badges
  3. Short description (120 characters or fewer, matching the GitHub and package descriptions)
  4. Long description
  5. Table of contents (required above 100 lines)
  6. Security
  7. Background
  8. Install
  9. Usage
  10. Extra sections
  11. API
  12. Maintainers
  13. Thanks
  14. Contributing
  15. License (last, as an SPDX identifier)
- **Other guides:**
  - [Make a README](https://www.makeareadme.com/) adds Support, Roadmap, and Project status sections.
  - [Google's docguide](https://google.github.io/styleguide/docguide/READMEs.html) describes a README as a short summary that links to the full docs.
- **Organizing sub-documents.** [Diátaxis](https://diataxis.fr/) defines four types of documentation: tutorials, how-to guides, reference, and explanation.

### NuGet package README

- **Setup.** `PackageReadmeFile` must point to a Markdown file, and you have to pack that file explicitly.
- **Rendering.** nuget.org renders CommonMark through Markdig, with these limits:
  - Raw HTML isn't allowed.
  - Relative links and images don't render ([issue #8876](https://github.com/NuGet/NuGetGallery/issues/8876), open since 2021).
  - Images must come from an allow-list. The list includes img.shields.io, sonarcloud.io, codecov.io, coveralls.io, GitHub workflow badges, and raw.githubusercontent.com. It excludes scan.coverity.com, api.scorecard.dev, and bestpractices.dev. Coverity and Scorecard badges can be routed through Shields. Whether that works for bestpractices.dev is [unverified].

  ([Package README on nuget.org](https://learn.microsoft.com/nuget/nuget-org/package-readme-on-nuget-org))
- **Fixing a broken page** means publishing a new package version.
- **Separate package READMEs** are common practice, but Microsoft doesn't explicitly recommend them. ([Package authoring best practices](https://learn.microsoft.com/nuget/create-packages/package-authoring-best-practices))

### Quality and artifact badges

| Service | Status (Nov 2026) | Badge renders on nuget.org? |
|---|---|---|
| NuGet version and downloads (Shields) | Free | Yes |
| GitHub Actions workflow status | Free for public repositories | Yes |
| SonarQube Cloud (renamed from SonarCloud on 2024-10-29, same domain) | Free OSS plan since 2026-01-27 | Yes |
| Codecov | Free for OSS; uploads to protected branches need a token | Yes |
| Coverity Scan (Black Duck Software) | Still listed as free for OSS, including C#, with builds capped per week. It has a history of outages and an unclear "EOL" release note, so treat it as fragile [unverified status] | Only through Shields |
| OpenSSF Scorecard | Free (scorecard-action v2) | Only through Shields |
| OpenSSF Best Practices | Free self-certification, now with a Baseline series (baseline-1 to baseline-3) | No (routing through Shields is [unverified]) |
| CodeQL | No dedicated badge; use the workflow badge with advanced setup | Yes (workflow badge) |

Shields caches badges and retires them when the underlying service changes. The fewer badges a README carries, the fewer can go stale. ([Shields changelog](https://github.com/badges/shields/blob/master/CHANGELOG.md))

### Enforcement tooling

- [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) checks Markdown structure and style.
- [Vale](https://docs.vale.sh/) checks prose. vale-action v3 can flag only added lines, which allows a gradual rollout.
- [lychee-action v2](https://github.com/lycheeverse/lychee-action) checks links. The gaurav-nelson markdown-link-check action was archived on 2026-04-20.
- **Reusable workflows** run through `workflow_call`. Hexalith already uses them through Hexalith.Builds.
- **Organization-level enforcement.** Organization rulesets and required workflows need GitHub Team or Enterprise. Hexalith's GitHub plan is unknown.

### Writing style

These principles come from the [Microsoft style guide](https://learn.microsoft.com/style-guide/top-10-tips-style-voice) and the [Google style guide](https://developers.google.com/style/highlights):

- Put the most important point first.
- Write in the second person and the active voice.
- Keep it short.
- Use sentence-case headings and numbered steps.
- Write descriptive link text and alt text.
- Write for a global audience.

## Decisions (accepted 2026-11-09)

Each decision lists the options considered and explains why the accepted option won. The facts behind the decisions are in the [current-state baseline](#current-state-baseline-2026-11-09).

### 1. Deploy in minutes: one command with an AI prompt on top

| Option | How it works | Pros | Cons |
|---|---|---|---|
| A. Better docs for today's path | List the prerequisites clearly, then run `aspire run` | No engineering | 30–60+ minutes of installs; the "deploy in minutes" promise stays false |
| B. Dev container + `aspire run` | `.devcontainer/` pins .NET, the Aspire CLI, Dapr, and Docker-in-Docker. Open it in VS Code, or in Codespaces with one click, then run `aspire run` | One template removes the prerequisite pain; reuses the existing AppHosts; also onboards contributors | Builds from source, so the first run takes a few minutes; Codespaces has a limited free quota; Docker-in-Docker is heavy |
| C. Prebuilt images + `docker compose up` | Release CI pushes images to ghcr.io and ships a compose file (Aspire can generate one) | Needs only Docker; fastest run | A new image pipeline for each service; Dapr sidecars in compose; a version matrix to maintain |
| D. Azure (`azd up`) | Provision to Azure Container Apps | Production-like | Needs a subscription and costs money; provisioning takes 10–20 minutes |

**AI prompt layer.** Each quickstart gets a prompt of 10 lines or fewer. It checks prerequisites (or opens the dev container), runs the command, waits for the services to be healthy, returns the dashboard URL, and explains the first call.

- **Pros:** It copes with differences between machines and suits a chatbot product.
- **Cons:** Results vary by agent, the agent runs commands on the user's machine, and the prompt needs testing.

**Accepted: B.**

- The command is `aspire run` everywhere.
- The prompt wraps only that command. If a prompt needs more than about 10 lines, fix the command, not the prompt.
- Deployment targets, as refined with the user:
  - The "Try it" quickstart runs on Docker, on the user's own machine, and the time target applies to it.
  - Platform gets a Kubernetes how-to, with no time target.
  - Azure, AWS, and Scaleway come after launch.
- Consider C later for the "Try it" path only, if B misses the 20-minute target (see decision 10).

### 2. README skeleton and quickstart blocks

| Option | Pros | Cons |
|---|---|---|
| A. One template with the same sections for every repository | Simple | Forces "deploy" onto libraries and tooling, so sections fill up with filler |
| B. A separate template for each kind of repository | Each one fits | Several files to keep in sync |
| C. One skeleton where only the quickstart varies | Same look everywhere; the quickstart fits the repository | Each repository needs its quickstart assigned |

**Accepted: C.** The skeleton is listed under [Foundations](#foundations-in-hexalithdocs).

The quickstart blocks are chosen for each repository, and a repository can use more than one. For example, eventstore uses "Use the package" for its SDK and "Run it" for its server.

| Quickstart block | What the reader does | Examples |
|---|---|---|
| Use the package | Adds the NuGet package and pastes a short code sample | commons, polymorphicserializations |
| Run it | Runs `aspire run` in the dev container, then makes a first call | memories, eventstore, tenants, parties |
| Use the tool | Installs the tool and runs a first command | mcpcli, builds, cicd, aitools |

**The first proposal was rejected.** It used four kinds: Library, Module, Application, and Tooling. The user groups repositories as business or technical modules instead. That category labels the module list on the organization page, while the quickstart blocks follow what the reader does first.

### 3. Front door

| Option | Pros | Cons |
|---|---|---|
| A. Organization profile README (`Hexalith/.github/profile/README.md`), shown at github.com/Hexalith | The literal entry point; no hosting | Short format; appears only on the organization page |
| B. Hexalith.Docs as the hub for cross-module guides | Room for depth | Visitors rarely land on a "docs" repository |
| C. Docs website (GitHub Pages with docfx or MkDocs) | Polished and searchable | Build, hosting, and upkeep; over-engineering for now |
| D. Platform README | It's where everything comes together | Today it's a release log, and the repository is aimed at maintainers |

**Accepted: A + B.**

- The profile fits on one screen. It says what Hexalith is, links "Try it" to the Platform quickstart, and lists every module with its category (business or technical), a one-line description, and a link.
- Cross-module guides (concepts, architecture, how modules fit together) live in Hexalith.Docs.
- Every repository gets an About description and topics.
- Revisit a website once there are enough docs to justify one.

### 4. GitHub README and NuGet package page

| Option | Pros | Cons |
|---|---|---|
| A. One README per repository, written to NuGet's limits (Hexalith.Builds already packs it) | No build change; one file | Absolute URLs only; no HTML; every package in the repository shows the same page |
| B. A hand-written README for each package (as commons does) | Best page for each package | More files that drift apart |
| C. Generate the package README at pack time | Best of both | Build tooling to write and maintain |

**Accepted: A.**

- Use absolute HTTPS links and images, avoid raw HTML, and use badges only from hosts that nuget.org allows. Linting enforces these rules.
- commons keeps its per-package READMEs. Other repositories don't have to adopt them.
- Revisit C only if a single page would mislead users of a repository's packages.

### 5. Quality indicators

The rule is **no badge without a pipeline that produces it.**

| Badge | Setup | Verdict |
|---|---|---|
| NuGet version | Shields, no setup | Required when the repository publishes packages |
| CI build status | GitHub Actions workflow badge | Required |
| License | Shields | Required |
| SonarQube Cloud quality gate and coverage | Add the scanner once to the Hexalith.Builds reusable CI; one Sonar project per repository; an organization token | Accepted: free OSS plan, renders on NuGet, one service covers quality and coverage |
| OpenSSF Scorecard | scorecard-action workflow | Later: a cheap security signal that renders on NuGet only through Shields |
| Coverity Scan | Separate build upload, capped per week | Dropped: fragile service, overlaps with Sonar for C#, badge renders on NuGet only through Shields, and no customer or certification needs it |
| Codacy, Codecov | Separate services | Dropped: they overlap with Sonar |

**Accepted:** the three required badges plus SonarQube Cloud.

### 6. Contributor docs and policies

| Option | Pros | Cons |
|---|---|---|
| A. Organization defaults in `Hexalith/.github` (CONTRIBUTING, code of conduct, SECURITY, SUPPORT, and issue and PR templates) | Written once; consistent | The `.github` repository must be public; the files don't appear in clones; issue templates are all-or-nothing; no room for repository-specific steps |
| B. Copy the files into each repository | Visible in clones | 20 times the edits; the copies drift apart |
| C. Hybrid: A for shared policies, plus `docs/development.md` in each repository for build, test, and debug steps | Shared rules written once; repository details live where they belong | Contributors look in two places (the shared CONTRIBUTING links to each repository's development guide) |

**Accepted: C.**

- Delete each repository's own CONTRIBUTING file, so the organization default applies.
- Move the runbooks that are now in READMEs into `docs/development.md`.
- Enable GitHub private vulnerability reporting so that SECURITY.md points to a real channel.
- Move release history to CHANGELOG.md or GitHub Releases.

### 7. Keeping docs consistent

| Option | Pros | Cons |
|---|---|---|
| A. A written standard only | Cheapest | People and agents won't read it, so drift returns |
| B. Documentation rules in the aitools shared agent instructions | Reaches the actual authors while they write; cheap | Compliance isn't guaranteed |
| C. A docs-check job in the Hexalith.Builds reusable CI. It runs markdownlint-cli2, lychee, and a small script for required sections, length, and forbidden content (`_bmad-output`, epic and story IDs, FR/NFR IDs) | Enforced automatically; catches regressions | Needs tuning; can block PRs |
| D. Vale prose linting | Enforces tone | Noisy and takes effort to configure; skip for v1 |
| E. Organization rulesets with required workflows | Hard enforcement | Needs a paid GitHub plan |

**Accepted: B + C.**

- The check starts as a warning and becomes required in each repository after migration.
- An agent migrates each repository with the audit-and-migration prompt.

### 8. "Try it" while Platform is in progress

| Option | How it works | Pros | Cons |
|---|---|---|---|
| A. Wait to announce | Docs work starts now; the public announcement waits until the Platform quickstart meets its time target | The front door never promises something the product doesn't do | The launch date depends on Platform |
| B. Interim "Try it" on a single module | Point "Try it" at a module that runs today, for example Tenants | Something runs now | It isn't the chatbot experience, and a business module on its own makes a poor first impression |
| C. Hosted demo instance | Visitors chat with a Hexalith instance that's already running | True "minutes," or even seconds, for application users | Hosting and LLM costs, abuse, tenant isolation, ongoing operations; over-engineering for v1 |
| D. Short demo video or GIF on the organization page | Shows the chatbot in 30 seconds | Cheap; shows the value before anyone installs anything | Goes stale as the UI changes |

**Accepted: A, with D optional.**

- Don't hold back the docs. The repositories and packages are already public, so people already see today's docs.
- Don't announce until "Try it" works.

### 9. Rollout

| Option | Pros | Cons |
|---|---|---|
| A. Every current repository reaches the full standard before launch | One consistent result | Working quickstarts depend on engineering (the dev container, Platform), which blocks everything |
| B. A launch set limited to the chatbot's dependencies | Looks smaller | Doesn't shrink the scope in practice (17 repositories) |
| C. Waves by kind of repository | Predictable order | The order seems arbitrary to a visitor |
| D. Opportunistic: each repository is updated the next time someone works on it | No planning | Never finishes; inconsistent at launch |

**Accepted: A, split into two levels of "done" plus cleanup.**

- **Level 1, "Clean,"** is writing work that agents can do with the audit prompt and the templates. Human review is the bottleneck.
- **Level 2, "Try-able,"** starts with the Platform "Try it" path, which is the launch gate.
- **Cleanup** includes archiving, which can be undone.

The checklists are in the [Launch scope detail](#launch-scope-detail).

### 10. Time targets and how to measure them

The targets apply to a first run on a clean machine. The machine starts with Docker and VS Code installed, or with only a browser if you use Codespaces. The timer starts on the README and stops at the first success.

| Journey | Target [ASSUMPTION: calibrate against a measured baseline] |
|---|---|
| Use the package (working sample call) | 5 minutes or less |
| Run a module (first successful call) | 15 minutes or less |
| "Try it" on Platform (first chat message) | 20 minutes or less |

Four ways to measure these targets were considered:

| How to measure | Pros | Cons |
|---|---|---|
| A. No number | Nothing to do | Untestable; nobody can say when it's done |
| B. Stranger test: someone who has never used Hexalith follows the quickstart on a clean machine, with a timer | Cheap; catches unclear writing | Manual; needs people from outside the team |
| C. An automated CI smoke test that runs the quickstart and checks health | Catches quickstarts that stop working | Docker-in-Docker with Dapr and Keycloak in CI is heavy and flaky |
| D. Agent stranger test: a fresh AI agent gets only the README and the AI prompt in a clean dev container | Cheap and repeatable; tests the AI-prompt path, which is a launch feature | Doesn't replace a human; agents and people get stuck in different places |

**Accepted: B as the launch gate, plus D routinely.**

- Phuong Duong (GitHub: `tinouit`) runs the human stranger test once Platform is finished. Each person can be a stranger only once, so the baseline and all iterations use the agent test (D).
- Measure a baseline now to calibrate the targets.
- Add C (the automated smoke test) only for the "Try it" path, and only if quickstarts keep breaking after launch.
- If "Try it" can't meet its 20-minute target while building from source, switch to prebuilt images (option C of decision 1).
