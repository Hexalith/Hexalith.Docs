# Hexalith documentation standard

A README answers a reader's first question and helps them reach a first result. Put detailed instructions on the page the reader needs next. The module registry records the package IDs, proposed wording, quickstart order and available guide paths for each repository. Maintainers confirm descriptions and categories before those values appear in the organization profile. [Module registry](module-registry.json)

## Author and review a page

“Pilot check” identifies rules with initial automated coverage. Reviewers verify the remaining requirements until a shared check covers them. A green pilot result covers only the rules that ran. The same rule IDs can appear in a local finding, a review comment or the CI summary.

| Rule | Requirement | Verification |
|---|---|---|
| D-README | Keep one readable root README. In order, give the title and one-sentence description, live badges, “What it does and who it's for”, “Quickstart”, “Packages” when the module publishes packages, “Documentation”, “Part of Hexalith”, “Contributing”, and “License”. End at License. Use GitHub's outline for navigation. Omit a replacement README under .github. | Pilot check for the root file, review for structure |
| D-LENGTH | Keep the README within 150 lines, the audience section within five lines and each quickstart block within 30 lines including its prompt. Record a reviewed exception if the time target requires a longer block. | Pilot check for README length, review for section limits |
| D-IDENTITY | Use the confirmed registry description verbatim in the README, GitHub About and organization profile. Keep it to one sentence of at most 120 characters. Begin the package description with the corresponding README sentence. Use the terms “business module” and “technical module”. | Registry validation and maintainer review |
| D-BADGE | Use up to five live badges. Show CI and license, NuGet version for package publishers, and Sonar quality gate and coverage where CI builds .NET. Each source belongs to this repository. The CI badge targets a workflow that runs on its default branch. Verify the badge image and destination. | Pilot check for local workflow targets, live checks at migration |
| D-PACKAGE | Give one table row per package with its purpose and NuGet link. Respect package-specific READMEs, link each one to the repository, compare the packed README with its selected source, and verify the latest NuGet page after republishing. | Archive check and public verification |
| D-RENDER | Use absolute HTTPS links and images in READMEs, descriptive link text, meaningful alt text and Markdown that renders on NuGet. Use NuGet's trusted image hosts. Put all essential information in text. | Render on GitHub and NuGet |
| D-LOCATION | Keep release history in GitHub Releases. Put build, test and debug instructions in docs/development.md, operator procedures in docs/operations.md, and cross-module guides in Docs. Keep planning identifiers, run evidence and links to internal planning folders out of reader-facing pages. | Link and content review |
| D-QUICKSTART | Use the registry's block order. “Use the package” installs the package and runs the displayed code against an artifact built from the same source. “Use the tool” installs the tool and shows expected output. “Run it” opens the qualified environment, starts Aspire and makes the first call. Use “Start here” for a module with no blocks. Publish “Run it” after it meets its target. | Consumer test and clean-environment run |
| D-PREREQUISITES | List tool versions, accounts, host changes, Docker privileges and other prerequisites before the first command. Pin the dev container to the repository SDK and record the Aspire CLI, Dapr CLI/runtime and Docker-in-Docker versions. Keep changes within the documented environment. | Pin comparison and clean-host run |
| D-PROMPT | Include a prompt of ten lines or fewer alongside each quickstart. Use the same single setup command and first-success check as the manual instructions. A reader enters secrets privately in the documented prompt or an ignored environment file. Wait for their confirmation without reading the value. | Prompt review and agent trial |
| D-COMMUNITY | Link to the organization community files once published. GitHub inherits those defaults. Keep repository-specific contributor instructions in the development guide and supply a repository-local MIT license for each module after confirming rights. | Maintainer checks signed-out access, ownership and local files |
| D-LINK | Resolve links to this repository against the source under review. Check other Hexalith targets and all external destinations during migration. Schedule a deduplicated external link and badge-host report weekly. | Local check and scheduled report |
| D-EVIDENCE | Measure from a clean environment through a first verified result, including prerequisite acquisition. Targets are five minutes for package and tool, 15 for a module run and 20 for the complete Platform journey. Record agent tool, version, model, prompt, times, result and friction. At least two of three unaided agent runs must pass. An outside tester confirms the Platform journey before launch. | Recorded trial and maintainer review |
| D-ENFORCEMENT | Start in warning mode. Switch to failure mode after review and migration. Judge the README, package READMEs and linked docs pages. Report findings on other docs pages. Record each suppression and reason. Badge and planning-content rules remain mandatory apart from reviewed references to pinned actions or submodules. | Local and CI result comparison |
| D-PUBLIC | Publish a “Try it” link after qualifying the agent journey and announce after the human trial. Record exposure reviews privately before making repositories public. Keep evidence of public access, per-package publication and live badge sources separate from local run results. | Maintainer gate |

Use GitHub's repository and organization defaults, its heading outline and NuGet's package README rendering. The shared guide links readers to one authoritative page per task. [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) · [NuGet package README guidance](https://learn.microsoft.com/en-us/nuget/nuget-org/package-readme-on-nuget-org)

## Readability checklist

At migration review, read the rendered page as a first-time package user.

- Can you identify the purpose and audience from the first five lines?
- Can you run the first command, see its outcome, and name the packages you need?
- Can you find help, prerequisites and the license without searching the source tree?
- Does each unfamiliar term have a definition or a descriptive link?
- Do active sentences, short steps and text alternatives make the instructions usable without images?

## Templates and agent use

Copy the template into the owning repository and fill it with that repository's verified details. [README skeleton](../templates/readme.md) · [Development guide](../templates/development.md) · [Operations page](../templates/operations.md) · [Quickstart prompts](../templates/quickstart-prompts.md) · [Migration prompt](../templates/migrate-documentation.md)

Codex and Claude Code have authoring entry points in this workspace. The clean-host launch matrix for quickstart prompts is pending qualification. Record the exact tool and version that completed each trial before claiming support for that route. A maintainer qualifies the pinned development container separately for the target repository. [Clean-host trial instructions](stranger-test.md)
