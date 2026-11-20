# Hexalith Docs epics and stories

Baseline approved for creation on 20 November 2026. The [final PRD](prds/prd-docs-2026-11-09/prd.md) supplies the acceptance criteria. The PRD's proposed dates are decision points. Only a maintainer can record launch acceptance. The [sprint status](../implementation-artifacts/sprint-status.yaml) tracks delivery.

## Epic 1 Establish a guide hub that maintainers can publish

### Story 1.1 Reconcile exposure

**Owner** Security maintainer

**Acceptance** Review BmadSkills originals and backups and all in-scope planning folders. Record revision, count, reviewer, controls and disposition privately. Publish only the review status.

**Requirements** FR-32, FR-65

### Story 1.2 Publish the standard and inventory

**Owner** Docs and module maintainers

**Acceptance** Supply a root Start here page, one rule table, and a machine-readable inventory of all 21 repositories. Record unknown facts explicitly. Confirm descriptions, categories and the BmadSkills workspace decision before public publication.

**Requirements** FR-1, FR-2, FR-31

### Story 1.3 Supply authoring materials

**Owner** Docs

**Acceptance** Provide a README skeleton, development and operations templates, a constrained AI quickstart pattern, migration prompt, cross-module guide and readability checklist. Test a filled example.

**Requirements** FR-3, FR-4, FR-6, FR-7, FR-8, FR-62

### Story 1.4 Define the clean environment

**Owner** Platform and Docs maintainers

**Acceptance** Spike supported agent access to a pinned dev container. Record prerequisites, host changes and the supported clean-machine route before distributing the template.

**Requirements** FR-5, FR-18, FR-63

## Epic 2 Keep documentation accurate through CI and release

### Story 2.1 Run the same rules locally and in CI

**Owner** Builds and CiCd

**Acceptance** Report a stable rule ID, file, line and fix. Add positive and negative fixtures. Run warning mode before migration and fail mode after acceptance. Check repo-local links offline and external destinations on the scheduled pass. Cover managed and standalone callers.

**Requirements** FR-41, FR-42, FR-43, FR-44, FR-45, FR-46, FR-64

### Story 2.2 Verify package examples and republishing

**Owner** Builds, CiCd and package owners

**Acceptance** Compile and execute the displayed sample against the same-source package. Exercise docs-only release selection, inspect every resulting archive and verify the approved README on NuGet.

**Requirements** FR-12, FR-15, FR-16, FR-19

### Story 2.3 Establish trustworthy signals and agent rules

**Owner** AI.Tools, CiCd and maintainers

**Acceptance** Confirm badge sources and Sonar configuration. Install short rule-ID guidance, verify reachability and quickstart behavior from a clean clone, and check public terminology.

**Requirements** FR-38, FR-39, FR-40, FR-47, FR-48, FR-49, FR-50, FR-63

## Epic 3 Migrate the two package pilots, then the remaining repositories

### Story 3.1 Pilot Commons

**Owner** Commons

**Acceptance** A new consumer can install the core package and run its first displayed sample. Verify every package-specific README, migration review, docs mode and republish in the ledger.

**Requirements** FR-15, FR-16, FR-19, FR-57

### Story 3.2 Pilot PolymorphicSerializations

**Owner** Serialization

**Acceptance** Run the displayed model registration and round-trip example. Verify live badges, packed README, CI mode, release and review with the same gates as Commons.

**Requirements** FR-15, FR-19, FR-57

**Acceptance for every subsequent migration.** After pilot review, allocate a separate migration per remaining registry row. For each, verify skeleton, length, wording, rendering, planning-content cleanup, quickstart choice, community defaults, development and operations pages, license, badges and preview. Record agent run, review and republish evidence per row. Requirements cover FR-9, FR-10, FR-11, FR-12, FR-13, FR-14, FR-16, FR-17, FR-18, FR-21, FR-22, FR-28, FR-34, FR-36, FR-37, FR-38, FR-39, FR-48, FR-57, FR-60, FR-63. Each repository has its own review and release record.

### Story 3.3 Migrate Docs

Hexalith.Docs maintainer. Verify the standard and inventory are readable from a public session after the exposure gate. Apply the common Level 1 acceptance criteria above.

### Story 3.4 Migrate AI.Tools

Hexalith.AI.Tools maintainer. Make the short documentation rules reachable from the three agent entry points. Apply the common Level 1 acceptance criteria above.

### Story 3.5 Migrate Builds

Hexalith.Builds maintainer. Document a working first tool command and the shared CI contract. Apply the common Level 1 acceptance criteria above.

### Story 3.6 Migrate CiCd

Hexalith.CiCd maintainer. Verify the guide for configuring and delivering a managed module. Apply the common Level 1 acceptance criteria above.

### Story 3.7 Migrate BmadSkills

Hexalith.BmadSkills maintainer. Confirm the tool entry point, privacy review and repository inclusion before linking. Apply the common Level 1 acceptance criteria above.

### Story 3.8 Migrate Agents

Hexalith.Agents maintainer. Confirm its category, main package and expected first call. Apply the common Level 1 acceptance criteria above.

### Story 3.9 Migrate ChatBot

Hexalith.ChatBot maintainer. Describe the module on its own merits until the Platform chat journey qualifies. Apply the common Level 1 acceptance criteria above.

### Story 3.10 Migrate Conversations

Hexalith.Conversations maintainer. Check the standalone dependency inventory during onboarding. Apply the common Level 1 acceptance criteria above.

### Story 3.11 Migrate EventStore

Hexalith.EventStore maintainer. Verify the consumer sample and measured docs-check cost. Apply the common Level 1 acceptance criteria above.

### Story 3.12 Migrate Folders

Hexalith.Folders maintainer. Verify its published package path and the supported run prerequisites. Apply the common Level 1 acceptance criteria above.

### Story 3.13 Migrate FrontComposer

Hexalith.FrontComposer maintainer. Confirm the intended consuming package and the supported dev-container target. Apply the common Level 1 acceptance criteria above.

### Story 3.14 Migrate McpCli

Hexalith.McpCli maintainer. Exercise the first CLI command with a scoped, privately supplied credential when required. Apply the common Level 1 acceptance criteria above.

### Story 3.15 Migrate Memories

Hexalith.Memories maintainer. Check the intended package entry point and local module run route. Apply the common Level 1 acceptance criteria above.

### Story 3.16 Migrate Parties

Hexalith.Parties maintainer. Confirm the public use case and run guide against its deployed host. Apply the common Level 1 acceptance criteria above.

### Story 3.17 Migrate Platform

Hexalith.Platform maintainer. Keep the quickstart linked to the development guide until the first-operation gate passes. Apply the common Level 1 acceptance criteria above.

### Story 3.18 Migrate Projects

Hexalith.Projects maintainer. Verify the first package operation and identify the host that owns the runnable topology. Apply the common Level 1 acceptance criteria above.

### Story 3.19 Migrate Tenants

Hexalith.Tenants maintainer. Check a tenant-scoped sample and record its first successful call. Apply the common Level 1 acceptance criteria above.

### Story 3.20 Migrate Timesheets

Hexalith.Timesheets maintainer. Confirm the supported host and package before publishing a run block. Apply the common Level 1 acceptance criteria above.

### Story 3.21 Migrate Works

Hexalith.Works maintainer. Exercise the public package sample and confirm the module description. Apply the common Level 1 acceptance criteria above.

## Epic 4 Prove that a newcomer can use Hexalith

### Story 4.1 Measure the first run

**Owner** Docs and Platform

**Acceptance** Supply the stranger-test kit and ledger. Measure cold setup, health, first operation and elapsed time across supported paths. Record prerequisites, friction and clean-host evidence.

**Requirements** FR-20, FR-23, FR-51, FR-52, FR-56, FR-61

### Story 4.2 Verify first success

**Owner** Platform and outside tester

**Acceptance** After Platform stories 3.2–3.8, create and list through McpCli on the run-scoped tenant. Require two of three unaided agent runs within 20 minutes and an eligible outside tester. Rerun after prerequisite or command changes. Qualify Kubernetes and each published block.

**Requirements** FR-23, FR-24, FR-26, FR-53, FR-54, FR-55, FR-58

### Story 4.3 Qualify chat after launch

**Owner** ChatBot and Platform

**Acceptance** Once Platform deploys chat, repeat the timed tests to a first chat message before changing the public promise.

**Requirements** FR-66

## Epic 5 Publish the organization entry point

### Story 5.1 Publish community and organization pages

**Owner** Organization maintainer

**Acceptance** After exposure review, verify public access, default community files, vulnerability reporting and pins signed out. Reconcile About data with the registry. Record each archive decision.

**Requirements** FR-25, FR-28, FR-29, FR-30, FR-31, FR-33, FR-34, FR-35, FR-59

### Story 5.2 Decide launch

**Owner** Maintainer

**Acceptance** Apply all ten conditions in PRD §8.3. Publish Try it in the required sequence, add the optional demo only if verified, and record the decision.

**Requirements** FR-26, FR-27, FR-55, FR-56, FR-57, FR-58

Start 1.1 and the Platform dependency check immediately. Stories 1.2, 2.1 and 2.2 enable the pilot migrations. Expansion depends on reviewer capacity and pilot evidence. Platform and ChatBot feature delivery belong to their existing product backlogs.

## Epic 6 Keep the documentation workspace reliable

### Story 6.1 Preserve acknowledged planning writes

Authoring tools owner. Exercise initialization, append and metadata updates with overlapping writers, malformed inputs, and sequential backward compatibility. Re-read the saved log and confirm every acknowledged entry survives exactly once.

### Story 6.2 Reconcile marketplace metadata

Authoring tools owner. Check the distribution name in the upstream source at the installed version. Verify the generated marketplace and plugin names against that contract in each installed IDE copy.

### Story 6.3 Repair the Conversations workspace pin

Docs owner. Adopt the first available upstream revision that removes the unmapped CiCd gitlink. Check that all direct references list their dependencies successfully. Nested checkouts stay uninitialized.
