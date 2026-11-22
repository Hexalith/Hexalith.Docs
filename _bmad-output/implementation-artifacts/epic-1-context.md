# Epic 1 Context: Establish a guide hub that maintainers can publish

<!-- Compiled from planning artifacts. Edit freely. Regenerate with compile-epic-context if planning docs change. -->

## Goal

Give a newcomer one place to understand how Hexalith modules work together, find the packages a module supplies and try the documented first operation. A maintainer can trace each public claim to a specific revision, the evidence checked there and the person’s role in accepting it.

## Stories

- Story 1.1: Reconcile exposure
- Story 1.2: Publish the standard and inventory
- Story 1.3: Supply authoring materials
- Story 1.4: Define the clean environment

## Requirements & Constraints

- The security maintainer begins with planning material already visible to the public. Cover both planning trees across 21 repositories and the original and backup state files in BmadSkills. Reconcile changes through the proposed publication revision. Check secret scanning and push protection on each repository and on the organization community repository.
- Keep findings, remediation and credential-owner follow-up in the private review record. The launch ledger records revisions, aggregate counts, control status and reviewer role. The Docs maintainer can change visibility once the security maintainer gives a disposition covering that candidate.
- Maintain one standard with a uniquely identified rule and enforcement method for each requirement. A single registry supplies descriptions, categories and package mappings to the guide hub, organization profile and migration tooling. Public catalog entries require maintainer confirmation.
- An owner-confirmed empty inventory at a specific revision qualifies for a package exemption. A legacy empty list still requires confirmation, and a changed package set needs a new decision. An unresolved inventory keeps the migration and its forecast open.

## Technical Decisions

- Use the Docs acceptance commit, the 19 direct gitlinks it records and an immutable external BmadSkills revision approved by its owner. Check source paths and package-to-README mappings against those inputs. Keep all 21 rows in scope even when an input is pending. Docs tooling uses Python 3.12 or later and the standard library.
- Keep cross-module guides and shared templates in Docs. Contributor and operator instructions belong to the owning module. Preserve material lacking an agreed destination for review. CiCd owns its delivered workflows, configuration and instruction blocks.
- Platform composes the runnable modules. Eligible module workspaces use the pinned module tool. Platform’s own route uses its AppHost with `aspire run`. The documented first operation runs through the McpCli built for the selected Platform revision. Older module-level Aspire wording needs owner reconciliation.
- Match the container image’s .NET major to the repository SDK. Restore the pinned module tool and obtain Aspire from the candidate AppHost and Dapr from Platform’s pinned Builds catalog. Install and run Dapr with the same home. Record declared and observed versions, extra runtimes and host prerequisites when qualifying a clean checkout. Only maintainers change dev container or agent entry-point files.

## UX & Interaction Patterns

The root “Start here” path leads to the system overview, standard and inventory. Explain how business and technical modules run together under Platform. Render sample READMEs and guides to check heading order, link text, image alternatives and text equivalents for video. Match the quickstart to the reader’s task. Its short agent prompt wraps the printed command, checks prerequisites and compares observed output with the documented result.

## Cross-Story Dependencies

Public hub links depend on the Docs exposure disposition and signed-out access to the overview, standard and registry. The standard and templates supply the pilot migrations, which exercise the checker and package examples. The verified container and pinned Platform toolchain supply the later clean-host timing trials.
