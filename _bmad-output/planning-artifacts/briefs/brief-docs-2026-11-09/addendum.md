---
title: "Addendum: Hexalith Documentation Standard"
created: 2026-11-09
updated: 2026-11-09
---

# Addendum: Hexalith Documentation Standard

Supporting detail that informs the brief but belongs in downstream documents (PRD, architecture, rollout plan).

## Current-state baseline (survey of local clones, 2026-11-09)

Read-only survey of the 20 module repos. Every repo is MIT-licensed. "CQL+DR" means CodeQL plus dependency review via Builds' shared workflows.

| Repo | README lines | Role the README plays today | Badges | NuGet | Quality CI |
|---|---|---|---|---|---|
| agents | 6 | stub | – | yes | CQL+DR |
| aitools | 61 | agent instructions | – | no | none |
| bmadskills | none | – | – | no | none |
| builds | 1275 | build runbook (~935 lines on local tools) | version tag | yes | CQL+DR |
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
| platform | 608 | release/evidence log (SHAs, run IDs) | – | no (source) | none |
| polymorphicserializations | 182 | product intro | License, Discord, Build, NuGet, Coverity, Codacy, Sonar×11 | yes | CQL+DR |
| projects | 1 | title only | – | yes | CQL+DR, coverage |
| tenants | 175 | product intro (good example) | CI, NuGet, License | yes | CQL+DR, coverage gate |
| timesheets | 149 | agent hooks + build | – | yes | CQL+DR, coverage |
| works | 131 | release procedure | – | yes | CQL+DR |
| xppmodel (Itaneo) | 2 | stub | – | no (Python) | none |

### Findings that shape the standard

- **The README is the NuGet package page.** `builds/Hexalith.Package.props` packs the root README into every package. On nuget.org, `Hexalith.Projects.Contracts` 1.2.3 shows only a title. Only commons ships separate per-package READMEs (`commons/src/libraries/*/README.md`).
- **There is no shared purpose.** READMEs act as a product introduction, a contributor runbook, or a release and evidence log, depending on the repo.
- **Internal planning content leaks into public docs.** Examples include epic and story references, FR/NFR IDs, links to `_bmad-output`, backlogs and evidence files under `docs/`, and sprint rules in `memories/CONTRIBUTING.md`.
- **Most docs are written by AI agents.** Agent files are in nearly every repo. The shared agent instructions in `aitools/hexalith-*-instructions.md` contain no README rules, and agents tend to add content after the License section.
- **Quality badges don't match the tooling.** Two repos display Coverity, Codacy and SonarCloud badges, but no workflow runs those scans. The Sonar analyzer is only a compile-time package (`builds/Hexalith.Build.props:40`).
- **Some links are broken.** These include badges pointing to deleted workflows (commons, eventstore), a license badge pointing to the wrong repo, and a missing sample path.
- **Community health files are missing.** There is no `Hexalith/.github` org repo, and no repo has SECURITY.md, SUPPORT.md, issue templates or a PR template. Only eventstore has a CODE_OF_CONDUCT.
- **GitHub "About" metadata is thin.** No repo has topics or a homepage, some descriptions are missing, and several contain typos.

### Existing levers

- **builds is the de facto enforcement layer.** Sixteen repos use its reusable workflows (`domain-ci.yml`, `codeql.yml`, `commitlint.yml`, …). It also holds `ci-cd-standards.md` (no documentation rules yet), the audit prompt `audit-hexalith-ci-cd.prompt.md`, `Hexalith.Package.props` and the module templates.
- **cicd** was set up to harmonize workflows but contains none.
- **eventstore** has `docs/page-template.md` plus markdownlint-cli2 and lychee configs, though no workflow runs them yet.
- **frontcomposer** has a docfx site.
- **Not yet inspected:** the `Hexalith.Templates`, `Hexalith.MyNewModule` and `Hexalith.MyNewPackage` repos on GitHub.

## Best-practices research digest (2026-11-09)

Checked against primary sources where possible. Items marked [unverified] could not be confirmed.

### GitHub

- **README handling.** GitHub looks for the README in `.github/`, then the root, then `docs/`, and truncates it past 500 KiB. It builds an "Outline" TOC from the headings and resolves relative links against the current branch. ([about READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes))
- **Org-wide defaults.** A public `.github` repo can provide CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, SUPPORT, ACCESSIBILITY, FUNDING, issue and PR templates, and discussion templates. Three caveats:
  - LICENSE cannot be a default.
  - The defaults don't appear in clones or packages.
  - Issue templates are all-or-nothing per repo.

  ([default community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file))
- **Community Standards checklist.** The items are: description, README, CoC, contributing, license, security policy, issue templates, PR template, and content reports.

### README conventions

- **[Standard Readme](https://github.com/RichardLitt/standard-readme/blob/main/spec.md) order:** Title, Badges, Short description (≤120 characters, matching the GitHub and package descriptions), Long description, TOC (required above 100 lines), Security, Background, Install, Usage, Extra, API, Maintainers, Thanks, Contributing, License (last, as an SPDX identifier).
- **Other guides:**
  - [Make a README](https://www.makeareadme.com/) adds Support, Roadmap and Project status sections.
  - [Google's docguide](https://google.github.io/styleguide/docguide/READMEs.html) describes a README as a short summary that links to the full docs.
- **Organizing sub-documents.** [Diátaxis](https://diataxis.fr/) offers four types: tutorials, how-to guides, reference and explanation.

### NuGet package README

- **Setup.** `PackageReadmeFile` must be a Markdown file, and you have to pack it explicitly.
- **Rendering.** nuget.org renders CommonMark through Markdig:
  - Raw HTML isn't allowed.
  - Relative links and images don't render ([issue #8876](https://github.com/NuGet/NuGetGallery/issues/8876), open since 2021).
  - Images must come from an allow-list. It includes img.shields.io, sonarcloud.io, codecov.io, coveralls.io, GitHub workflow badges and raw.githubusercontent.com. It excludes scan.coverity.com, api.scorecard.dev and bestpractices.dev, which you can route through Shields instead.

  ([package README on nuget.org](https://learn.microsoft.com/nuget/nuget-org/package-readme-on-nuget-org))
- **Fixing a broken page** requires publishing a new package version.
- **Separate package README.** This is common practice, but Microsoft doesn't explicitly recommend it ([authoring best practices](https://learn.microsoft.com/nuget/create-packages/package-authoring-best-practices)).

### Quality and artifact badges

| Service | Status (Nov 2026) | Badge renders on nuget.org? |
|---|---|---|
| NuGet version and downloads (Shields) | Free | Yes |
| GitHub Actions workflow status | Free, public repos | Yes |
| SonarQube Cloud (renamed from SonarCloud 2024-10-29; same domain) | Free OSS plan since 2026-01-27 | Yes |
| Codecov | Free for OSS; token needed for protected-branch uploads | Yes |
| Coverity Scan (Black Duck Software) | Still listed as free for OSS, including C#. It caps builds per week, has a history of outages and has an unclear "EOL" release note, so treat it as fragile [unverified status] | Only through Shields |
| OpenSSF Scorecard | Free (scorecard-action v2) | Only through Shields |
| OpenSSF Best Practices | Free self-certification, now with a Baseline series (baseline-1 to baseline-3) | No [unverified via Shields] |
| CodeQL | No dedicated badge; use the workflow badge with advanced setup | Yes (workflow badge) |

Shields caches badges and retires them when the underlying service changes. The fewer badges a README carries, the fewer can go stale. ([Shields changelog](https://github.com/badges/shields/blob/master/CHANGELOG.md))

### Enforcement tooling

- [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) checks Markdown structure and style.
- [Vale](https://docs.vale.sh/) checks prose. vale-action v3 can flag only added lines, which allows a gradual rollout.
- [lychee-action v2](https://github.com/lycheeverse/lychee-action) checks links. The gaurav-nelson markdown-link-check action was archived on 2026-04-20.
- **Reusable workflows** run through `workflow_call`, which Hexalith already uses via builds.
- **Org-level enforcement.** Org rulesets and required workflows need GitHub Team or Enterprise. The Hexalith plan is unknown.

### Writing for people

These principles come from the [Microsoft style guide](https://learn.microsoft.com/style-guide/top-10-tips-style-voice) and the [Google style guide](https://developers.google.com/style/highlights):

- Put the most important point first.
- Write in the second person and the active voice.
- Keep it short.
- Use sentence-case headings and numbered steps.
- Write descriptive link text and alt text.
- Write for a global audience.
