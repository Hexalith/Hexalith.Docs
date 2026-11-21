# Hexalith documentation architecture

**Validation verdict — revise before using the spine to accept migrations or publish “Try it.”** The five architecture decisions pass structural lint. Across repositories, teams can still follow them and disagree about which registry revision governs a check, who can enable enforcement, and what evidence qualifies a release or a first run.

21 November 2026 · Initiative architecture · Docs `bbdfc01` · Six high and two medium findings

## High-priority findings

### A single registry still permits different inputs for the same build

**AD-1 and AD-2.** Docs can migrate a README using one approved registry revision while the module’s checker uses another. Either revision can be immutable and still give a different result for the same description or package list. The checker’s current pilot rules cover readability, length and same-repository workflow badge paths. Registry-dependent rules make this choice consequential as coverage expands. [Spine, lines 23–33][spine1] · [Registry requirements][registryreq] · [Checker implementation][checker]

**Decision for Docs, Builds and CiCd.** Bind each module revision to one retrievable Docs registry and rule-set revision. Local checks, hosted checks and migration evidence should identify the same input. Accept the handoff when rerunning an older module commit after a registry change produces its original findings.

### CI enrollment and promotion need a rule for each owner

**AD-2.** “Enroll modules through CiCd” covers 17 managed modules. Builds and CiCd use their own CI. Docs and BmadSkills use caller workflows, as does the organization’s separate `.github` repository. A pilot owner could also promote after reviewing only that pilot’s warnings. FR-13 requires tuning the planning-content patterns across all 21 repositories first. [Spine, lines 29–33][spine2] · [CI ownership and accepted-revision evidence][ciowners] · [All-repository tuning][tuning]

**Decision for Builds, CiCd and the Docs maintainer.** Name who sets the mode for each route. Define whether a central warning run against 21 recorded revisions satisfies calibration or whether hosted runs are required. Require the pilot’s own successful hosted fail-mode run at the migration revision before recording acceptance.

### Checks on links between Hexalith repositories have conflicting schedules

**AD-2.** The PRD requires checking links within the organization on every run. The standard sends other Hexalith targets to migration checks. After a target file moves, one checker can pass a README that another rejects. Looking up a moving default branch on each run also breaks reproducibility. [FR-45][linkreq] · [D-LINK in the standard][linkstandard]

**Decision for Docs and Builds.** Reconcile the two schedules. Define how a PR check resolves its own files and sibling-repository targets at known revisions, and which live destinations the central weekly job checks. Use a cross-repository link whose target changes as the acceptance fixture.

### Builds has two packages and no documented README-only release route

**AD-3.** The module release selector awards a patch for `docs(readme)`. The selector for Builds itself excludes documentation changes. Builds publishes two registered CLI packages. If their migration changes only README files, the ordinary Builds release selector can decline a version increment, leaving both pages awaiting the release required by FR-15. [Spine, lines 35–39][spine3] · [Release selector][selector] · [Builds package inventory][buildsids] · [Republish criteria][republish]

**Decision for the Builds release maintainer.** Record an approved route for those two IDs, such as including their docs in a qualifying Builds release before the deadline. Require the intended stable version, assigned README and rendered-page review for each ID.

### The public “Try it” link can advance after only one qualification

**AD-4 and the delivery table.** A first call at minute 16 and successful project creation and listing at minute 18 can satisfy the 20-minute “Try it” test while failing the separate 15-minute “Run it” test. The spine names only the 20-minute gate. The PRD requires both on the same candidate before publishing the link. Independent trials also need a consistent tool, version, model and prompt. [Spine delivery table][delivery] · [Agent trial identity][trials] · [Publication sequence][sequence]

**Decision for Platform and the launch maintainer.** Link both qualification records to the candidate revision, on clean environments, with at least two of three unaided passes for each route. For “Try it,” require all seven modules ready and creation and retrieval of the same project in the same tenant through McpCli. Publish the link after both agent gates. Run the outside test from the public front door before launch. Requalify when the tested path changes.

### Public repositories need immediate exposure review

**AD-5.** A team waiting for a visibility change can miss a repository that is already public. Bind review to the current public revision, reconcile intervening changes before closure, and keep item-level evidence with the security maintainer. The exposure record still lists owner review as pending. [FR-32 and FR-65][exposurereq] · [Recorded review scope][exposure]

## Medium-priority findings

- **AD-1 · Unknown inventory can look like a confirmed zero.** BmadSkills has an external checkout and a recorded package count of zero, and its ledger row marks republishing inapplicable. AD-1 explicitly leaves the inventory pending. Give consumers a way to distinguish a verified nonpublisher from an inventory awaiting owner review before excluding packages from the rollout count. [Registry row][externalrow] · [Ledger row][ledgerrow] · [Source-check scope][sourcecheck]
- **AD-4 · A common Dapr home can contain different runtimes.** Platform at `abb62da8` selects .NET SDK 11.0.100 and Aspire 17.0.0. Its pinned Builds catalog selects Dapr runtime 1.19.1. The refreshed sibling catalog selects runtime 1.19.2, and Platform’s build configuration prefers that sibling when available. Record the effective Builds SHA, CLI and runtime with every trial and qualify the dependency set readers receive. [Platform lookup order][lookup] · [Pinned catalog][pincatalog] · [Sibling catalog][sibcatalog] · [Trial setup][trialsetup]

## What the refreshed checkout demonstrates

| Check | Result on 21 November |
| --- | --- |
| Spine lint | Zero findings across five decisions. |
| Module registry | Offline and source validation passed for 21 rows covering 101 package IDs. The population is Docs, 19 direct submodules and external BmadSkills. The source check skips external rows. |
| Docs test suite | All 12 tests passed. |
| Pilot README checker, warning mode | Six length findings for Commons and one for PolymorphicSerializations. Both pilot workflows reference Builds v6.4.4. The shared checker exists on Builds main and is absent from that tag. These local runs establish the warning baseline. |
| Public package archives | Commons 3.0.2 matched 12 of 12 mapped READMEs. PolymorphicSerializations 2.0.1 matched 2 of 2. The 20 November ledger reported 2 of 12 and 0 of 2 on the prior versions. Rendered gallery pages, their links and maintainer acceptance are separate evidence. |
| Platform and McpCli | The approved Projects inventory contains four queries. The create operation required for the timed journey is still outstanding. The ledger records a 10.60-second restore and no qualifying end-to-end measurement. |
| Publication | The ledger records zero Level 1 acceptances. The private exposure disposition and the outside-tester run remain with their owners. |

[Docs CI][docsci] · [Public archive verifier][verifier] · [Commons CI pin][commonspin] · [Serialization CI pin][serialpin] · [Approved Projects operations][ops] · [Recorded pilot and first-run evidence][ledgerevidence]

## Reproduce the checks

Run these commands from the Hexalith.Docs root with the direct submodules at the reviewed revisions.

```sh
uv run .agents/skills/bmad-architecture/scripts/lint_spine.py --workspace _bmad-output/planning-artifacts/architecture/architecture-docs-2026-11-11
python3 scripts/validate_registry.py
python3 scripts/validate_registry.py --check-sources
python3 -m unittest discover -s scripts/tests
python3 references/Hexalith.Builds/Github/lib/docs_check.py --root references/Hexalith.Commons --mode warn
python3 references/Hexalith.Builds/Github/lib/docs_check.py --root references/Hexalith.PolymorphicSerializations --mode warn
python3 scripts/verify_published_readmes.py
```

The final command reads the live NuGet feed. To verify the releases seen here, run the same script separately with `--module Hexalith.Commons --version 3.0.2` and `--module Hexalith.PolymorphicSerializations --version 2.0.1`. A newer stable release will require a new comparison.

## Review scope and revisions

The superproject was already current with `origin/main`. All 19 direct submodules fast-forwarded beyond its recorded pins. Each checkout’s SHA was compared with the default-branch SHA reported by GitHub. The parent’s 19 gitlink changes are unstaged. All 208 nested submodule declarations remain uninitialized. Validation produced this report and reviewer notes. The spine, decision log and launch ledger retain their reviewed contents.

| Repository | Reviewed main commit |
| --- | --- |
| Hexalith.Docs | [`bbdfc010a9d4`](https://github.com/Hexalith/Hexalith.Docs/commit/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21) |
| Hexalith.CiCd | [`62dc50b18888`](https://github.com/Hexalith/Hexalith.CiCd/commit/62dc50b18888be88d9ce27415d22f612c55c50af) |
| Hexalith.AI.Tools | [`87a738ceeba8`](https://github.com/Hexalith/Hexalith.AI.Tools/commit/87a738ceeba8975c0b087bc5ecee7dfbc14bf73c) |
| Hexalith.Agents | [`6865c6e6e4aa`](https://github.com/Hexalith/Hexalith.Agents/commit/6865c6e6e4aad374683a9461eac2ae5c112e471a) |
| Hexalith.Builds | [`e1380b813b23`](https://github.com/Hexalith/Hexalith.Builds/commit/e1380b813b230022db0b8656ac3a0480e57c07e8) |
| Hexalith.ChatBot | [`cdc4e3448821`](https://github.com/Hexalith/Hexalith.ChatBot/commit/cdc4e344882162db556e9f9ca9e71c8762446664) |
| Hexalith.Commons | [`258f9d20e33b`](https://github.com/Hexalith/Hexalith.Commons/commit/258f9d20e33bd0ae411cf8b3836a26a131f5b9ae) |
| Hexalith.Conversations | [`08953f5eed40`](https://github.com/Hexalith/Hexalith.Conversations/commit/08953f5eed404228a2b8bd41c7d2bf5eaaab543a) |
| Hexalith.EventStore | [`7435254cc1a1`](https://github.com/Hexalith/Hexalith.EventStore/commit/7435254cc1a148031224eebe1aafd53a8659b2cd) |
| Hexalith.Folders | [`73ca79b4fbc0`](https://github.com/Hexalith/Hexalith.Folders/commit/73ca79b4fbc09d233cbab5f836507c88894f0420) |
| Hexalith.FrontComposer | [`61dcd07fb412`](https://github.com/Hexalith/Hexalith.FrontComposer/commit/61dcd07fb412acf2feb66d8ee61513c16ef6ec4d) |
| Hexalith.McpCli | [`e79b7f8b6430`](https://github.com/Hexalith/Hexalith.McpCli/commit/e79b7f8b64303397ce9dfd856ed2111b513ade88) |
| Hexalith.Memories | [`e413124b3caf`](https://github.com/Hexalith/Hexalith.Memories/commit/e413124b3cafe437c3e512d4b65114c09b0df0f3) |
| Hexalith.Parties | [`42b27f2e9375`](https://github.com/Hexalith/Hexalith.Parties/commit/42b27f2e9375c6d8db270524029c3e875d830a8e) |
| Hexalith.PolymorphicSerializations | [`c6d0dfce6dc4`](https://github.com/Hexalith/Hexalith.PolymorphicSerializations/commit/c6d0dfce6dc4f9a0699a51f80baf021ba5ef5d60) |
| Hexalith.Projects | [`2c1d7363e23a`](https://github.com/Hexalith/Hexalith.Projects/commit/2c1d7363e23add596d289184d68242bd0f752056) |
| Hexalith.Tenants | [`f15f61706a9d`](https://github.com/Hexalith/Hexalith.Tenants/commit/f15f61706a9ddc3c6fa2b0d63ab4bda6c0e7c299) |
| Hexalith.Timesheets | [`271442d0cad2`](https://github.com/Hexalith/Hexalith.Timesheets/commit/271442d0cad21a66be9aacb7fb0b36e28b670181) |
| Hexalith.Works | [`07020c842239`](https://github.com/Hexalith/Hexalith.Works/commit/07020c84223937d3a3326e3ed45633eaf9ea73db) |
| Hexalith.Platform | [`abb62da83045`](https://github.com/Hexalith/Hexalith.Platform/commit/abb62da83045058903b479f78a6bd6c7bb90f792) |

[Good-spine rubric](reviews/review-rubric.md) · [Technology and implementation review](reviews/review-reality.md) · [Adversarial review](reviews/review-adversarial.md)

[spine1]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/architecture/architecture-docs-2026-11-11/ARCHITECTURE-SPINE.md#L23-L33
[spine2]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/architecture/architecture-docs-2026-11-11/ARCHITECTURE-SPINE.md#L29-L33
[spine3]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/architecture/architecture-docs-2026-11-11/ARCHITECTURE-SPINE.md#L35-L39
[delivery]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/architecture/architecture-docs-2026-11-11/ARCHITECTURE-SPINE.md#L68-L76
[registryreq]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L230-L244
[checker]: https://github.com/Hexalith/Hexalith.Builds/blob/e1380b813b230022db0b8656ac3a0480e57c07e8/Github/lib/docs_check.py#L36-L65
[ciowners]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L793-L813
[tuning]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L412-L421
[linkreq]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L824-L832
[linkstandard]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/docs/documentation-standard.md#L22
[selector]: https://github.com/Hexalith/Hexalith.Builds/blob/e1380b813b230022db0b8656ac3a0480e57c07e8/Github/lib/release_version.py#L29-L49
[buildsids]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/docs/module-registry.json#L96-L113
[republish]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L433-L441
[trials]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L957-L967
[sequence]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L1157-L1163
[externalrow]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/docs/module-registry.json#L68-L83
[ledgerrow]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/implementation-artifacts/launch-ledger.md#L3-L10
[sourcecheck]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/scripts/validate_registry.py#L95-L110
[lookup]: https://github.com/Hexalith/Hexalith.Platform/blob/abb62da83045058903b479f78a6bd6c7bb90f792/Directory.Build.props#L11-L13
[pincatalog]: https://github.com/Hexalith/Hexalith.Builds/blob/fe68718b6c074a6b500a7191e3554a1d39e17688/Props/Directory.Packages.props#L42-L44
[sibcatalog]: https://github.com/Hexalith/Hexalith.Builds/blob/e1380b813b230022db0b8656ac3a0480e57c07e8/Props/Directory.Packages.props#L42-L44
[trialsetup]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/addendum.md#L130-L136
[exposurereq]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/planning-artifacts/prds/prd-docs-2026-11-09/prd.md#L639-L657
[exposure]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/implementation-artifacts/exposure-review.md#L3-L20
[docsci]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/.github/workflows/documentation.yml#L14-L23
[verifier]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/scripts/verify_published_readmes.py#L120-L143
[commonspin]: https://github.com/Hexalith/Hexalith.Commons/blob/258f9d20e33bd0ae411cf8b3836a26a131f5b9ae/.github/workflows/ci.yml#L13-L17
[serialpin]: https://github.com/Hexalith/Hexalith.PolymorphicSerializations/blob/c6d0dfce6dc4f9a0699a51f80baf021ba5ef5d60/.github/workflows/ci.yml#L13-L17
[ops]: https://github.com/Hexalith/Hexalith.McpCli/blob/e79b7f8b64303397ce9dfd856ed2111b513ade88/tools/inventory-coverage/v1/projects-approved.json#L5-L26
[ledgerevidence]: https://github.com/Hexalith/Hexalith.Docs/blob/bbdfc010a9d4c112b6ddf71e88864fa4e6a24e21/_bmad-output/implementation-artifacts/launch-ledger.md#L29-L59
