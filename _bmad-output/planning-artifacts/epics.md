---
updated: 2026-11-21
inputDocuments:
  - prds/prd-docs-2026-11-09/prd.md
  - prds/prd-docs-2026-11-09/addendum.md
  - architecture/architecture-docs-2026-11-11/ARCHITECTURE-SPINE.md
  - sprint-change-proposal-2026-11-20.md
---

# Hexalith Docs epics and stories

The approved November 20 backlog covers the documentation standard, migration of 21 repositories, the newcomer’s first operation and the launch decision. The November 21 revision makes the architecture’s acceptance criteria explicit. The sprint tracker records delivery status. The launch ledger records reviewed revisions, trial results, releases and maintainer decisions. [Sprint status](../implementation-artifacts/sprint-status.yaml) · [Launch ledger](../implementation-artifacts/launch-ledger.md)

The PRD defines the reader outcomes and ten launch conditions. Its addendum supplies trial and package-verification details. The architecture assigns the checks to their owners and identifies upstream decisions that still need agreement. Epic 6 carries the three workspace corrections approved in the sprint change proposal. [Final PRD](prds/prd-docs-2026-11-09/prd.md) · [PRD addendum](prds/prd-docs-2026-11-09/addendum.md) · [Architecture](architecture/architecture-docs-2026-11-11/ARCHITECTURE-SPINE.md) · [Approved change proposal](sprint-change-proposal-2026-11-20.md)

**Delivery sequence.** Begin the exposure review and Platform dependency assessment immediately. The standard, released checker and package verification enable the two pilots. Begin subsequent migrations after pilot review as capacity allows. The organization profile can publish early. Its Try it link depends on both Platform agent qualifications. The outside trial follows the live link, and the launch maintainer decides against all ten conditions. Platform and ChatBot feature delivery stays with their respective product owners.

## Epic 1 Establish a guide hub that maintainers can publish

Maintainers can publish a guide whose module descriptions, package inventory and quickstarts readers can verify.

### Story 1.1 Reconcile exposure

As a maintainer opening Docs to the public, I need to know which revision was reviewed and who owns the disposition.

**Owner** Security maintainer

**Acceptance criteria**

- Start with already-public planning content. At BmadSkills revision `c0b2171aa205`, reconcile the 53 original state files and 53 backups. Review `_bmad/` and `_bmad-output/` across the 21 repositories, recording the revision and count for each. Account for files added or changed before closing the review.
- Verify secret scanning and push protection for the 21 repositories and `Hexalith/.github`. Keep item-level findings, remediation and credential-owner follow-up private. Record reviewed revisions, counts, reviewer role, controls and status in the ledger. Docs visibility requires the security maintainer’s disposition for the revision proposed for publication.

**Traceability** FR-32, FR-65, AD-5.

### Story 1.2 Publish the standard and inventory

As a reader choosing a module, I need the guide hub, profile and package information to agree about what each repository offers.

**Owner** Docs and module maintainers

**Acceptance criteria**

- Provide a root “Start here” page, one Markdown standard with one entry per rule ID, and a JSON registry readable with the Python standard library. Validate all 21 rows, their required fields, source paths and package-to-README mappings. Before linking a public hub, complete Story 1.1 and check the overview, standard and inventory signed out.
- Test three inventory cases in the validator, ledger and forecast. An owner-confirmed empty list at a specific revision qualifies for a package exemption. An empty legacy row without confirmation remains pending. A changed package set requires renewed confirmation. An unresolved inventory keeps the migration and forecast open.
- Use the Docs tree, the 19 direct gitlinks at the Docs acceptance commit and an owner-approved external BmadSkills SHA. Only a maintainer confirms descriptions, categories and inventories. Public catalog text uses confirmed values.

**Traceability** FR-1, FR-2, FR-31, AD-1, AD-6, AD-16.

### Story 1.3 Supply authoring materials

As a documentation author, I want to fill in a template and see whether a newcomer can use the resulting page.

**Owner** Docs

**Acceptance criteria**

- Fill the nine-section README skeleton and the development and operations templates with examples and pass the fail-mode check. The overview explains how business and technical modules run together under Platform. Apply the readability checklist to rendered output, including heading order, meaningful links, alt text and text equivalents for images or video.
- Exercise each quickstart prompt variant. Its first line is `You are running a Hexalith quickstart.` It fits in ten lines, wraps the printed setup command, lists prerequisites, and checks the documented result. Use the module tool for eligible module workspaces and `aspire run` for Platform. Track the PRD’s older module-level `aspire run` wording in FR-5, FR-6 and FR-20 for owner reconciliation. Check the Python 3.12 minimum in the authoring guidance against the architecture.
- Run the migration prompt against a pilot. It identifies the owning repository and pinned inputs, supplies file-and-line findings and distinguishes contributor, operator, release and planning material. It lists content without a new home and escalates if a proposed deletion exceeds the PRD’s 20-line threshold and respects CiCd’s file ownership.

**Traceability** FR-3, FR-4, FR-6, FR-7, FR-8, FR-62, AD-1, AD-10, AD-12, AD-15.

### Story 1.4 Define the clean environment

As a first-time contributor, I want the dev container to provide the versions and permissions the quickstart promises.

**Owner** Platform and Docs maintainers

**Acceptance criteria**

- Open the pinned template in VS Code Dev Containers and Codespaces. Test how each supported agent reaches the container from a clean host. Record prerequisite acquisition, privileged Docker or other host changes, and a working first call. Only a maintainer changes the container and agent entry points.
- Check the image’s .NET major against `global.json`. Restore the pinned module tool, source Aspire from the candidate AppHost and Dapr CLI and runtime from Platform’s pinned Builds catalog. Verify install and run share one `HEXALITH_DAPR_HOME`. Test every listed extra runtime, including the documented ASP.NET Core 10 prerequisite while it applies.
- Record the candidate Platform and effective Builds SHAs, module-tool version and declared and observed SDK, Aspire and Dapr versions. A different sibling catalog or installed version disqualifies a timing. Initialize only directly declared submodules and verify a fresh-clone quickstart completes.
- For example, the November 21 Platform checkout `0aacf132` pins module tool `6.5.1`, Builds `055d7df5` and McpCli `e79b7f8b`. For a trial on that candidate, record those pins and the identity of the loaded McpCli artifact. Resolve the pins again when the candidate changes.

**Traceability** FR-5, FR-18, FR-63, AD-4, AD-10, AD-12, AD-13.

## Epic 2 Keep documentation accurate through CI and release

A maintainer can reproduce a CI finding locally and verify that the README a consumer receives belongs to the released package.

### Story 2.1 Run the same rules locally and in CI

As a maintainer fixing a documentation finding, I want a local run to reproduce the hosted result at the same source revision.

**Owner** Builds, CiCd and Docs

**Acceptance criteria**

- Run the released Builds checker locally and in hosted CI at the same SHA, committed mode and page profile. Exercise the prepare step after the stage-1 guard and before restore. Cover the 17 managed repositories through CiCd, Builds and CiCd in their own CI, and Docs, BmadSkills and `Hexalith/.github` through their callers. A missing checker in the pinned release blocks qualification.
- Test passing and failing fixtures for each rule. For checked pages emit `file`, `line`, `rule`, `level` and a fix `hint`. Docs registry findings also name the repository. Verify warning mode reports failures and fail mode blocks applicable unsuppressed fail-level findings. The job summary lists findings and suppression counts. Only a reasoned exact match for a pinned action or submodule SHA under `D-PLANNING` can suppress a planning finding. Badge findings always remain visible.
- Keep module checks local to their checkout. In the paired Docs check, resolve cross-repository file links and fragments against the immutable source inputs from Story 1.2, including an explicit organization-repository SHA where used. A missing target blocks the affected migration. Run the live-link check for each migration and weekly across repositories, deduplicate URLs, report bad destinations in the Docs issue and keep network failures out of module CI.
- Before the first promotion, calibrate planning-content patterns in warning mode on all 21 source revisions. Record checker and rule revisions, source SHAs, coverage and finding dispositions. Recalibrate changed patterns. Introduce new or widened rules at report level until the weekly report shows zero findings in fail-mode repositories. Compare EventStore CI runs and verify at most two minutes of added time.
- After a repository’s hosted warning run and maintainer review, its configuration owner enables fail mode. Require a passing hosted run and the separate pinned Docs check for Level 1. The architecture assigns checkout-only checks to Builds, registry rules to Docs, and managed suppressions to CiCd setup. Preserve the PRD owner’s outstanding FR-41, FR-45 and FR-46 reconciliations, including FR-45’s requirement to check internal links on every run.

**Traceability** FR-13, FR-41, FR-42, FR-43, FR-44, FR-45, FR-46, FR-64, AD-2, AD-6, AD-7, AD-8, AD-15.

### Story 2.2 Verify package examples and republishing

As a package consumer, I want the sample on the package page to work with the version I install.

**Owner** Builds, CiCd and package owners

**Acceptance criteria**

- Pack the same revision into a temporary feed at a unique version. In a fresh consumer with only that feed enabled, compile the displayed C# blocks and compare actual output line by line with the documented output. A broken sample or incorrect nuspec README selection fails the check even when library tests pass. Retain the pilot hooks until the shared stage-3 sample step is released and delivered. After delivery, run the shared step after unit tests and before the module hook, and remove the duplicate sample execution.
- For an eligible module, prove ordinary documentation changes do not select a release and the delivered README selector authorizes a patch. After candidate review and before final Level 1 acceptance, the module owner approves the release start, including any accompanying product changes. Verify the actual eligible nightly result.
- For every expected package ID in the confirmed inventory, compare the latest listed stable version, nuspec-selected README bytes and mapped source at the release tag. Inspect the rendered page and links. Record release version, verified/expected count and evidence per ID. A missing package leaves acceptance open. Builds and McpCli use the specific routes in Stories 3.5 and 3.14.

**Traceability** FR-12, FR-15, FR-16, FR-19, AD-3, AD-9, AD-11, AD-18.

### Story 2.3 Establish trustworthy signals and agent rules

As a reader, I want badges that report real results and agent guidance that follows the same documentation standard.

**Owner** AI.Tools, CiCd and maintainers

**Acceptance criteria**

- Check the five-badge limit and trace each displayed badge to its registered package, license, delivered CI workflow or current Sonar analysis. Show Sonar badges only after CiCd delivers an admitted analysis path and Docs confirms the registry key. Leave FR-40 open for the configuration owner while that delivery or scope decision is pending.
- Follow `AGENTS.md`, `CLAUDE.md` and `.github/copilot-instructions.md` to the same documentation rules at the pinned AI.Tools revision. The rules fit within 100 lines and cite catalog IDs. Check normalized entry-point text and the permitted CiCd marker block. Verify that a fresh-clone quickstart reaches its first result and that repository work still uses the contributor baseline.
- Review the terms “business module” and “technical module” across public pages and agent guidance. Document how “business module” maps to the architecture term “domain module.”

**Traceability** FR-38, FR-39, FR-40, FR-47, FR-48, FR-49, FR-50, FR-63, AD-8, AD-12, AD-17.

## Epic 3 Migrate the two package pilots, then the remaining repositories

Each repository gives its intended reader a verified first action. Commons and PolymorphicSerializations establish the evidence and review effort for the remaining 19 migrations.

### Common Level 1 criteria

Stories 3.1–3.21 use these criteria. Begin the remaining migrations after pilot review, in CiCd adoption order for managed modules. Each module owner supplies evidence for its own row in the launch ledger.

1. **Identify the candidate.** Record the owning repository SHA, Docs template and registry revision, AI.Tools revision and released Builds checker SHA. Verify managed adoption where applicable, a hosted warning run, merged documentation rules and any registered Sonar analysis. Use the source identities in the Docs acceptance commit even when a developer has newer checkouts.
2. **Review the pages a reader sees.** Check the nine-section README order, 150-line maximum, five-line audience description and 30-line quickstart limit. Record any PRD-permitted time/length exception. Match the confirmed description, quickstarts and package list to the registry. Verify NuGet-safe absolute links and images, live badges, the repository’s own root MIT license, inherited community files, agent entry points, readable GitHub rendering and accessibility. Move release history, contributor steps, operator runbooks and planning material to their designated locations. Follow checked guide links and run the documented commands.
3. **Prove each first action.** Before publishing a package or tool block, one fresh, unaided agent session reaches the documented result on the immutable candidate. This package or tool trial is untimed. Hosted CI must also run each displayed package sample at that revision. A repository can reach Level 1 with its planned Run it block still unpublished. Link to the development guide until the applicable timed qualification passes. A module running in its own workspace needs a v2 manifest, a direct Platform gitlink and the matching pinned module tool. EventStore, Memories and McpCli use Platform’s workspace. Platform alone starts its AppHost with `aspire run`. For flagged frozen CLI or MCP packages, publish an obsolescence notice pointing to McpCli, omit quickstarts and keep every ID in the release count.
4. **Close the checks.** Link the 21-repository calibration from Story 2.1. After warning review, the configuration owner promotes the candidate. Record the hosted fail-mode run URL, the passing Docs registry and pinned-link check at the same module revision, and live-link results when the migration lands. Record a disposition for each mandatory rule, including affirmative manual or report-only review. An unresolved mandatory finding keeps the row open.
5. **Close the release and review.** The maintainer records the readability review and date. For publishers, Story 2.2 supplies a verified public page and matching archive for every confirmed package ID. Record source-built results separately from public results. Only an owner-confirmed empty inventory at the accepted source revision qualifies for a package exemption.

**Common requirements** FR-9, FR-10, FR-11, FR-12, FR-13, FR-14, FR-15, FR-16, FR-17, FR-18, FR-19, FR-21, FR-22, FR-28, FR-34, FR-36, FR-37, FR-38, FR-39, FR-48, FR-56, FR-57, FR-60, FR-62, FR-63.

### Story 3.1 Pilot Commons

As a new Commons consumer, I want to install the core package and run the example exactly as displayed.

**Owner** Commons maintainer

**Acceptance criteria**

- Run the root and core-package examples from the candidate README against the same-source package. Compare their output and inspect all mapped READMEs, including project-specific files. A type or namespace error fails the pilot.
- Use the common migration criteria above. The November 20 baseline counted 12 packages, six length findings and two matching public READMEs. Reconcile the candidate inventory, resolve the findings or record an allowed exception for each and verify every public package at the intended release before recording pilot acceptance.

**Traceability** FR-15, FR-16, FR-19, FR-57, [Common Level 1 criteria](#common-level-1-criteria), AD-3, AD-9.

### Story 3.2 Pilot PolymorphicSerializations

As a consumer registering a polymorphic model, I want to see the documented type and value survive a round trip.

**Owner** PolymorphicSerializations maintainer

**Acceptance criteria**

- Run both displayed fences in a clean consumer and compare the output with the documented Volvo (Electric) result. Check live badge destinations and the README selected by each archive.
- Apply the common migration criteria to the candidate inventory. The November 20 baseline counted two source-built packages, one length finding and zero matching public READMEs. Require both hosted fail-mode and public release evidence for pilot acceptance.

**Traceability** FR-15, FR-19, FR-57, [Common Level 1 criteria](#common-level-1-criteria), AD-3, AD-9.

### Story 3.3 Migrate Docs

As a reader choosing a module, I want “Start here” to take me to the overview and an accurate registry.

**Owner** Hexalith.Docs maintainer

**Acceptance criteria**

- After the security disposition and maintainer visibility decision, follow the overview, standard and inventory links signed out. Run the hub-profile check and registry check on the Docs commit. Record its SHA in subsequent evidence so the evidence commit can identify its predecessor.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-6, AD-15.

### Story 3.4 Migrate AI.Tools

As an agent user, I want the same rules to be discoverable from all three supported entry points.

**Owner** Hexalith.AI.Tools maintainer

**Acceptance criteria**

- In a fresh clone, follow each entry point to the topical rule file and confirm the catalog IDs resolve. Have the maintainer confirm the proposed tool quickstart, then demonstrate its first command if selected. Compare the canonical text against the revision used by Docs.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-12.

### Story 3.5 Migrate Builds

As a tool user, I want the first command in the README to work with the released tool.

**Owner** Hexalith.Builds maintainer

**Acceptance criteria**

- Run the confirmed tool quickstart. Verify the Evidence CLI and Module CLI READMEs against `Hexalith.Builds.Evidence.Cli` and `Hexalith.Builds.Module.Cli` in the next qualifying Builds release. Builds’ selector excludes docs, test and style changes. Record any forecast miss against FR-15 for owner disposition.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-11.

### Story 3.6 Migrate CiCd

As a module maintainer, I want a working path from the CI guide to an adopted module’s configuration.

**Owner** Hexalith.CiCd maintainer

**Acceptance criteria**

- Follow “Start here” to the managed setup and delivery instructions, identify where a docs-mode change belongs, and verify its rendered value at a candidate revision. Check that CiCd runs the common checker in its own CI.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.7 Migrate BmadSkills

As a workflow user, I want the installation instructions to match the distribution the owner supports.

**Owner** Hexalith.BmadSkills maintainer

**Acceptance criteria**

- Obtain the owner-approved external checkout and immutable revision. Confirm the proposed first tool command, test it in a fresh session, and complete the privacy review before linking. Keep the repository and its inventory pending if the owner has yet to confirm the source or package list. Other migrations can proceed.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-1, AD-16.

### Story 3.8 Migrate Agents

As a developer evaluating Agents, I want to make the documented first call with its primary package.

**Owner** Hexalith.Agents maintainer

**Acceptance criteria**

- Have the maintainer confirm the category, description and primary package. Run the example against the same-revision package and compare the result with the README. Match the approved description across the repository, registry and public surfaces.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.9 Migrate ChatBot

As a developer evaluating ChatBot, I want a working package example and an accurate description of its availability.

**Owner** Hexalith.ChatBot maintainer

**Acceptance criteria**

- Run the confirmed package example in a fresh consumer. Check that its module guide identifies the supported Platform route. Keep the post-launch chat claim tied to the independent evidence in Story 4.3.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.10 Migrate Conversations

As a contributor, I want a working package example and a checkout with resolvable direct dependencies.

**Owner** Hexalith.Conversations maintainer

**Acceptance criteria**

- Run the confirmed package example. At the migration SHA compare direct gitlinks with their declarations and trace the Docs checkout to the repair in Story 6.3. A missing declaration leaves the onboarding check open.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.11 Migrate EventStore

As a developer evaluating EventStore, I want a working package example and a reproducible runtime route.

**Owner** Hexalith.EventStore maintainer

**Acceptance criteria**

- Run the primary-package sample from the candidate and measure documentation-check overhead against the two-minute CI budget. Exercise the Platform-workspace route before publishing Run it. Verify that the organization’s code of conduct is inherited.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.12 Migrate Folders

As a developer integrating Folders, I want the documented package path to work from a clean environment.

**Owner** Hexalith.Folders maintainer

**Acceptance criteria**

- Install the confirmed primary package in a fresh consumer, run its first example and compare the documented result. Compare the advertised runtime prerequisites with the eligible manifest, Platform gitlink and tool version before qualifying Run it.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.13 Migrate FrontComposer

As a developer trying FrontComposer, I want the public package and dev container to agree on the supported starting point.

**Owner** Hexalith.FrontComposer maintainer

**Acceptance criteria**

- Exercise the confirmed consuming package and verify its rendered README. Open the supported dev container, compare its SDK to the repository pin, and record the first call from the qualified Platform composition before publishing Run it.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.14 Migrate McpCli

As an operator, I want to install the supported CLI and recognize a successful first command.

**Owner** Hexalith.McpCli maintainer

**Acceptance criteria**

- Run the documented first command from a clean environment, using private credential input when needed. Move operator procedures to the linked operations page. Before a documentation-triggered paired release, Platform and McpCli owners must reconcile Platform’s ownership of the stable tool and McpCli’s ownership of Abstractions with the workflow that publishes both. Record one authorized publisher and one receipt per stable ID. A missing receipt keeps acceptance open.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-10, AD-11, AD-18.

### Story 3.15 Migrate Memories

As a consumer of Memories, I want to find the supported package and reproduce its local example.

**Owner** Hexalith.Memories maintainer

**Acceptance criteria**

- Run the confirmed primary-package example. For Run it, use the target manifest from the Platform workspace and the McpCli build bound to that run. Record the result before publishing the block. Retain notices and republish coverage for any confirmed frozen package IDs.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-10, AD-18.

### Story 3.16 Migrate Parties

As a developer integrating Parties, I want its README to explain the public use case and show the first successful call.

**Owner** Hexalith.Parties maintainer

**Acceptance criteria**

- Confirm the public description with its owner, run the package example and verify that the run guide points to its Platform-owned composition. Match the call’s documented output on the candidate before promoting Run it.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.17 Migrate Platform

As a newcomer, I want the organization’s Try it link to open the same Platform instructions that passed the timed trials.

**Owner** Hexalith.Platform maintainer

**Acceptance criteria**

- Use the Platform dev container, `aspire run`, and the run-scoped McpCli build. The default-branch quickstart links to the development guide until both Story 4.2 candidate qualifications pass. For Level 1, verify the guide link and the other common checks. For publication of Run it and Try it, compare the instructions proposed for promotion with the tested candidate.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria), AD-4, AD-10, AD-13.

### Story 3.18 Migrate Projects

As a developer trying Projects, I want the package example to identify the host that serves the operation.

**Owner** Hexalith.Projects maintainer

**Acceptance criteria**

- Run the first registered package operation, compare its output and follow the link to the Platform-owned topology. Supply the Projects owner’s evidence for the separate Try it dependency check in Story 4.2, where the newly created project must appear in the same tenant’s list.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.19 Migrate Tenants

As a developer trying Tenants, I want the example to show the tenant context for the first successful operation.

**Owner** Hexalith.Tenants maintainer

**Acceptance criteria**

- Run the same-source package sample, check that the documented call uses the intended tenant and record the expected result. Qualify any published Run it block against the manifest and toolchain selected by the candidate.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.20 Migrate Timesheets

As a developer trying Timesheets, I want to know which package and host its example uses.

**Owner** Hexalith.Timesheets maintainer

**Acceptance criteria**

- Verify the owner-confirmed package against the release inventory and run its displayed example. Follow the prerequisites to the supported host. Keep the Run it block linked through the development guide until its first call passes timed qualification.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

### Story 3.21 Migrate Works

As a consumer of Works, I want a working public package sample and a clear route to operator instructions.

**Owner** Hexalith.Works maintainer

**Acceptance criteria**

- Run the registered package example and compare its result. Confirm the description across public surfaces. Follow the link from the README to the operations page and verify it contains the module’s release procedure.

**Traceability** [Common Level 1 criteria](#common-level-1-criteria).

## Epic 4 Prove that a newcomer can use Hexalith

A newcomer can follow the public instructions from a clean machine and observe the documented result within the promised time.

### Story 4.1 Measure the first run

As a trial observer, I want a reproducible record of where the clock starts, what the newcomer did and what counted as success.

**Owner** Docs and Platform

**Acceptance criteria**

- Provide a clean-host preflight, fresh-session instructions, no-help rule, friction log and one record per trial. Capture the role, entry URL, exact printed prompt, candidate SHA, predeclared tool/version/model, actual toolchain, timestamps, first result, friction severity and issue links. Fail a run that solicits a secret in chat. Store only role-level information and link records from the ledger.
- At baseline, measure every existing quickstart and Platform’s cold prerequisite acquisition, container start and full build. Keep the 10.60-second seven-project restore labeled as a partial measurement. Include prerequisite time in every qualifying trial. Package and tool targets are five minutes, Run it is 15 and Try it is fixed at 20. A maintainer records calibration and any cold-build or prerequisite bottleneck decision.

**Traceability** FR-20, FR-23, FR-51, FR-52, FR-56, FR-61, AD-4, AD-13, AD-16.

### Story 4.2 Verify first success

As a newcomer starting from the organization page, I want to create a project and see it in my tenant within 20 minutes.

**Owner** Platform, launch maintainer and outside tester

**Acceptance criteria**

- After Platform stories 3.2–3.8 supply the seven-module topology, rehearse **two separate sets** on one immutable candidate Platform README. Predeclare the agent tool, version and model for each route and use its exact prompt in three independent clean sessions. At least two of three must finish each route unaided. Run it ends at the documented first call within 15 minutes. Try it ends within 20 minutes, with all seven modules healthy and McpCli listing the project just created in the same run-scoped tenant. Demonstrate the result via both the documented command and the prompt.
- Compare the candidate and publication versions of the prompt, commands, prerequisites and path. Changes require requalification of the affected route. A different agent configuration starts a new set of three. After both routes pass, publish Platform’s block and the organization’s link. The maintainer confirms an eligible outside tester and backup, and predeclares the route. The tester starts at the live organization page on their own clean machine and reaches the same result unaided in 20 minutes, including prerequisites.
- File issues for red agent friction and every human friction item. After a failed outside trial, fix the issues, requalify the agent route and run the backup tester. For the separate Kubernetes gate, one fresh independent agent follows only the local-cluster how-to, loads the locally built images and obtains the documented McpCli result unaided in an untimed run.
- Qualify every published block against its FR-51 target by launch. After launch, repeat Try it and each published Run it at least monthly per the PRD assumption. Two failed periodic runs in a quarter trigger the smoke-test decision.

**Traceability** FR-20, FR-23, FR-24, FR-26, FR-51, FR-53, FR-54, FR-55, FR-58, AD-4, AD-5, AD-10, AD-13.

### Story 4.3 Qualify chat after launch

As a newcomer trying chat after launch, I want the advertised path to end at a real reply.

**Owner** ChatBot and Platform

**Acceptance criteria**

- Once Platform’s one-command composition includes ChatBot, run the upgraded Try it through the first message and its reply. Record a qualifying agent set followed by a new outside tester’s unaided clean-host run within the fixed 20-minute target. Publish the chat promise only after that evidence is recorded.

**Traceability** FR-66, AD-4.

## Epic 5 Publish the organization entry point

A visitor can find a current module and try the qualified route from the organization page. The maintainer can trace the launch decision to its evidence.

### Story 5.1 Publish community and organization pages

As a visitor or contributor, I want the organization page to lead to current modules, shared contribution instructions and a working private reporting channel.

**Owner** Organization maintainer

**Acceptance criteria**

- From a signed-out session, verify the public community repository, profile, confirmed module descriptions and categories, guide links and chosen pins. Generate the profile catalog and contributing-guide list from a pinned Docs registry inside their marked sections. CI detects drift. The maintainer sets About descriptions and topics, chooses up to six in-scope pins with Platform first under the PRD assumption, and records and applies one disposition per archive candidate.
- Check the common CONTRIBUTING, code of conduct, SECURITY, SUPPORT, issue and pull request templates. Check inheritance from a participating repository and private vulnerability reporting on every public repository in the organization. The organization caller applies the organization page profile. The architecture specifies Contributor Covenant 3.0 and flags the PRD’s 2.1 assumption for reconciliation before acceptance. Link to Docs only after the exposure review and visibility decision. The front door may go live before Try it qualifies.

**Traceability** FR-25, FR-28, FR-29, FR-30, FR-31, FR-33, FR-34, FR-35, FR-59, AD-5, AD-7, AD-14.

### Story 5.2 Decide launch

As the maintainer deciding launch, I need evidence for each condition and enough reviewer and release capacity to finish the outstanding work.

**Owner** Launch maintainer

**Acceptance criteria**

- For the proposed 1 December decision, record both pilot acceptances, the Platform/Projects/McpCli dependency assessment and two forecast finish dates. Use remaining migrations, confirmed inventories, releases, per-ID verification, measured pilot rates and available owner days. Compare publisher completion with the assumed 10 December stabilization deadline and all 21 Level 1 acceptances with planned launch. An unknown inventory leaves the forecast incomplete.
- For the proposed 15 December decision, record the timed Try it qualification. Apply the January 2027 fallback under PRD §8.4 when the corresponding conditions fail. Publish the Try it link only after both agent qualifications in Story 4.2. The outside trial starts from that live link.
- At launch, record a disposition and evidence for each of the ten PRD §8.3 conditions, including the independent Kubernetes run, all package pages and the outside trial. Link the PRD gate checklist to individual receipts in the ledger. Only the launch maintainer records acceptance. An optional current demo is at most 30 seconds and has a text alternative.

**Traceability** FR-26, FR-27, FR-55, FR-56, FR-57, FR-58, AD-4, AD-5, AD-11, AD-16.

## Epic 6 Keep the documentation workspace reliable

Contributors can rely on the planning log, installed workflow metadata and direct repository references identified in the November 20 audit.

### Story 6.1 Preserve acknowledged planning writes

As a planning contributor, I want to find every acknowledged entry when concurrent writers finish.

**Owner** Authoring tools owner

**Acceptance criteria**

- Overlap initialization, append and metadata updates to the same log. Reopen it and compare acknowledged entries and stored entries one for one. Exercise malformed input and sequential updates to older logs. A failed transaction preserves the last valid contents.

### Story 6.2 Reconcile marketplace metadata

As a workflow installer, I want each supported IDE to discover the distribution under its documented name.

**Owner** Authoring tools owner

**Acceptance criteria**

- At the installed upstream version, compare the distribution naming contract with the generated marketplace and plugin metadata. Run the fixture against both installed IDE copies. Verify each generated name and plugin reference resolves to the expected distribution.

### Story 6.3 Repair the Conversations workspace pin

As a contributor opening the workspace, I want Git to resolve every direct dependency from its recorded revision.

**Owner** Docs owner

**Acceptance criteria**

- Verify the selected Conversations revision contains the reviewed repair for the orphaned CiCd gitlink. At that revision match each direct gitlink to a `.gitmodules` declaration. Repeat the declaration check for every direct Docs reference and confirm the inventory succeeds with zero initialized nested submodules.

## Requirements coverage

Use the story references below to locate the acceptance criteria. “Epic 3” applies the common Level 1 criteria to both pilots and each of the 19 subsequent migrations. The PRD retains the full testable consequences for each requirement.

| PRD requirement | Acceptance criteria |
| --- | --- |
| FR-1 · Standard on one page | 1.2 |
| FR-2 · Module registry | 1.2 |
| FR-3 · README skeleton template | 1.3 |
| FR-4 · Development guide and operations page templates | 1.3 |
| FR-5 · Dev container template | 1.4 |
| FR-6 · AI prompt pattern | 1.3 |
| FR-7 · Migration prompt | 1.3 |
| FR-8 · Cross-module guides | 1.3 |
| FR-9 · README skeleton sections | Epic 3 |
| FR-10 · README size limits | Epic 3 |
| FR-11 · One-sentence description everywhere | Epic 3 |
| FR-12 · NuGet-safe README | 2.2, Epic 3 |
| FR-13 · No internal planning content | 2.1, Epic 3 |
| FR-14 · Release history and runbooks leave the README | Epic 3 |
| FR-15 · Package pages republished | 2.2, Epic 3 |
| FR-16 · Per-package READMEs | 2.2, Epic 3 |
| FR-17 · Quickstart block choice | Epic 3 |
| FR-18 · Prerequisites up front | 1.4, Epic 3 |
| FR-19 · "Use the package" block | 2.2, Epic 3 |
| FR-20 · "Run it" block | 4.1, 4.2 |
| FR-21 · "Use the tool" block | Epic 3 |
| FR-22 · AI prompt in every block | Epic 3 |
| FR-23 · "Try it" | 4.1, 4.2 |
| FR-24 · Kubernetes how-to | 4.2 |
| FR-25 · Front door | 5.1 |
| FR-26 · Honest "Try it" link | 4.2, 5.2 |
| FR-27 · Optional demo | 5.2 |
| FR-28 · About description and topics | 5.1, Epic 3 |
| FR-29 · Non-current repositories removed from view | 5.1 |
| FR-30 · Pinned repositories | 5.1 |
| FR-31 · Public guide hub | 1.2, 5.1 |
| FR-32 · Hexalith.BmadSkills sensitive-data check, now | 1.1 |
| FR-33 · Community files | 5.1 |
| FR-34 · No local overrides | 5.1, Epic 3 |
| FR-35 · Private vulnerability reporting | 5.1 |
| FR-36 · Development guide | Epic 3 |
| FR-37 · Operations page | Epic 3 |
| FR-38 · Allowed badges | 2.3, Epic 3 |
| FR-39 · A live source behind every badge | 2.3, Epic 3 |
| FR-40 · SonarQube Cloud in the shared CI | 2.3 |
| FR-41 · Docs check job | 2.1 |
| FR-42 · Warn mode and fail mode | 2.1 |
| FR-43 · Docs check everywhere | 2.1 |
| FR-44 · Actionable findings | 2.1 |
| FR-45 · Link checking | 2.1 |
| FR-46 · Visible exceptions | 2.1 |
| FR-47 · Documentation rules in Hexalith.AI.Tools | 2.3 |
| FR-48 · Rules reachable from every in-scope repository | 2.3, Epic 3 |
| FR-49 · Short, enforceable rules | 2.3 |
| FR-50 · One vocabulary | 2.3 |
| FR-51 · Time targets | 4.1, 4.2 |
| FR-52 · Baseline and calibration | 4.1 |
| FR-53 · Agent stranger test | 4.2 |
| FR-54 · When the agent stranger test runs | 4.2 |
| FR-55 · Human stranger test | 4.2, 5.2 |
| FR-56 · Launch ledger | 4.1, 5.2, Epic 3 |
| FR-57 · Level 1 "Clean" done | 5.2, Epic 3 |
| FR-58 · Level 2 "Try-able" done | 4.2, 5.2 |
| FR-59 · Organization `.github` repository | 5.1 |
| FR-60 · LICENSE file | Epic 3 |
| FR-61 · Stranger-test kit | 4.1 |
| FR-62 · Readability checklist | 1.3, Epic 3 |
| FR-63 · Agent entry points never block a quickstart | 1.4, 2.3, Epic 3 |
| FR-64 · Local docs check | 2.1 |
| FR-65 · Planning-folder exposure review | 1.1 |
| FR-66 · "Try it" upgrades to chat | 4.3 |

### Non-functional requirements

| PRD requirement | Stories | Acceptance evidence |
| --- | --- | --- |
| NFR-1 · Writing for people | 1.3, 3.1–3.21 | The reviewer completes the readability checklist on the rendered page. Record unclear steps from the trial friction log. |
| NFR-2 · Rendering parity | 2.2, 3.1–3.21 | Review GitHub rendering for each migration and the actual NuGet page for each confirmed package ID. |
| NFR-3 · Honest claims | 2.3, 4.2, 5.2 | Trace each badge, public capability and time claim to a live source or eligible trial. |
| NFR-4 · Commands run as printed | 1.3, 3.1–3.21, 4.2 | A fresh user reaches the documented output using only the listed prerequisites and inputs. |
| NFR-5 · One source per rule | 1.2, 2.1, 2.3 | Resolve every checker and AI.Tools rule ID against the standard’s single rule table. |
| NFR-6 · Accessibility | 1.3, 3.1–3.21, 5.2 | Check meaningful link text and alt text. The optional demo and any informational image have a text equivalent. |
| NFR-7 · CI time budget | 2.1, 3.11 | Measure the added documentation-check time on EventStore. The PRD budget is two minutes or less. |
| NFR-8 · Secret handling | 1.3, 4.1, 4.2 | Use ignored local input or a hidden prompt for credentials. A request for a secret in chat fails the trial. |
| NFR-9 · Contained agent actions | 1.3, 1.4, 2.3 | Check that prompts confine changes to the clone or container, prerequisites name host changes, and maintainers control container and entry-point changes. |
