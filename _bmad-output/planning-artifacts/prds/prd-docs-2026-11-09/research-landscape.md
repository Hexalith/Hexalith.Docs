# Research landscape: Hexalith Documentation Standard (2026-11-09)

This file covers what the brief's digest left out. The digest is in `briefs/brief-docs-2026-11-09/addendum.md`, section "Best-practices research digest", and nothing here repeats it.

Source labels:

- **[primary]**: official documentation, a vendor's own page, or a paper.
- **[secondary]**: a blog, mirror, or summary.
- **[vendor]**: a source that promotes its own product.
- **[unverified]**: a claim not confirmed against a primary source.

## 1. Comparable ecosystems

### Dapr

- **Org profile.** The profile is a short welcome followed by five links in order: website, docs, "Do some quickstarts", videos, and Discord. It has no badges. Six repos are pinned, including `quickstarts` and `community`. [primary] <https://github.com/dapr>
- **Getting started.** It is a five-step ladder: install the CLI, run `dapr init`, try the API, then quickstarts, then tutorials. No step has a time estimate, and there is no Codespaces or dev container option. [primary] <https://docs.dapr.io/getting-started/>
- **Quickstarts repo.** Quickstarts are listed in a table by building block. Each one runs with `make validate`, and a CI badge sits at the top. Releases are tagged to match Dapr runtime versions. [primary] <https://github.com/dapr/quickstarts>
- **Executable docs.** Dapr tests its tutorials with mechanical-markdown. An annotation in the markdown itself, `<!-- STEP name: … expected_stdout_lines: … -->`, runs the code block and checks its output. The tool also has `--dry-run` and `--manual` modes. [primary] <https://github.com/dapr/mechanical-markdown>
- **Worth adopting:** the README doubles as the test, and quickstarts are tagged per release.
- **Failure pattern:** the try-it path crosses three places: the org page, the docs site, and the quickstarts repo.

### Aspire samples and eShop

- **aspire-samples.** It has a catalog table with columns for workload languages, AppHost language, and deploy target (run only, Docker Compose, or Azure). The dev container or Codespaces is the recommended way to run. The README pins the CLI version (13.6.0) and states plainly that the code is "not intended for operational deployment". [primary] <https://github.com/dotnet/aspire-samples>
- **eShop.** Prerequisites are explicit: an SDK matching `global.json`, the Aspire CLI, and a container runtime. Running takes one `aspire run`. The README has no badges, no time estimate, and no mention of a dev container. [primary] <https://github.com/dotnet/eShop>
- **eShop pitfalls:**
  - The container runtime must already be running, and the README's warning about it is easy to miss.
  - The `$env:` lines work only in PowerShell.
  - The optional Azure Foundry step costs money.
  - `aspire destroy` deletes the whole resource group.
- **Worth adopting:** the deploy-target column, and "evaluation only" labels.
- **Failure patterns:** commands that work in only one shell, and optional steps whose costs or destructive effects aren't flagged before you start.

### Orleans

- **README layout.** The README reads like a feature brochure, with 11 feature subsections. "Get started" comes near the bottom and only links out to Hello World. [primary] <https://github.com/dotnet/orleans>
- **Defects:**
  - The page has no H1.
  - A numbered list is broken.
  - The `ThermostatGrain` sample doesn't compile, because it uses types that aren't defined and a field that is never initialized.
- **Failure patterns:** README snippets that are never compiled, and a quickstart buried below the features.

### ABP Framework

- **README layout.** It has 11 badges. Getting started is five links to other pages, with no commands in the README. It also contains a book promotion, a request to star the repo, and a typo in a docs link (`authorizationn`). [primary] <https://github.com/abpframework/abp>
- **What works:** the CLI (`dotnet tool install -g Volo.Abp.Cli`, then `abp new`) gives a one-command start, but it lives in the external docs.
- **Failure patterns:** a wall of badges, and a README that only points elsewhere.

### JasperFx (Marten and Wolverine)

- **Org profile.** It has no README content: just six pinned product cards, a sponsor button, and a support email. There is no try-it path. [primary] <https://github.com/JasperFx>
- **Marten README.** It is a contributor handbook covering the PostgreSQL test harness, the CI matrix, and how the docs are published. It has no install command or first-use example; usage lives on martendb.io. [primary] <https://github.com/JasperFx/marten>
- **Worth adopting:** Marten pulls code samples into its docs from compiled source with MarkdownSnippets.
- **Failure pattern:** user and contributor material mixed on one page.

### MassTransit and Akka.NET

- **Template-first start.** Both start with `dotnet new install <Templates>` followed by a single template command (`dotnet new mtworker`, `dotnet new akka.console`). [primary] <https://masstransit.io/quick-starts/in-memory>, <https://github.com/akkadotnet/akka.net>
- **Zero infrastructure first.** MassTransit tells users to start on the in-memory transport and switch transports once that works. [primary] <https://masstransit.io/quick-starts/in-memory>
- **Akka.NET failure pattern.** Its docs are spread across several hosts and mirrors, and search results get confused with JVM Akka. [secondary] <https://petabridge.com/bootcamp/lessons/unit-1/akka-templates/>

### Kurrent (formerly EventStoreDB)

- **Rename.** EventStoreDB became KurrentDB, and the first KurrentDB release was 25.0. [primary] <https://kurrent.io/blog/kurrent-re-brand-faq>
- **Docker command drift.** Different doc versions give different Docker run commands:
  - `docker.kurrent.io/kurrent-latest/kurrentdb`
  - `kurrentplatform/kurrentdb --dev`
  - `eventstore/eventstore:24.10.1`

  Sources: [primary] <https://docs.kurrent.io/server/v26.0/quick-start/installation.md>, <https://hub.docker.com/r/kurrentplatform/kurrentdb>
- **README and docs.** The GitHub README mostly links out to the docs. The docs site publishes an llms.txt. [primary] <https://docs.kurrent.io/llms.txt>
- **Failure pattern:** after a rename, the try-it command drifts between copies. It needs a single source.

### Across all comparables

- None of them publishes a timed target.
- None enforces a uniform README skeleton across its repos.
- The strongest try-it mechanisms are template packages, a dev container or Codespaces, and executable markdown run in CI.

## 2. Agent-runnable quickstarts and docs for agents

### AGENTS.md and how agents load it

- **Governance and behavior.** AGENTS.md has been stewarded by the Agentic AI Foundation (Linux Foundation) since 2025-12-09. When several files apply, "the closest AGENTS.md to the edited file wins". Agents run the checks the file lists. [primary] <https://agents.md/>, <https://openai.com/blog/agentic-ai-foundation>
- **Claude Code.** Since v2.1.277 (2026-09-18), Claude Code reads AGENTS.md only as a fallback when there is no CLAUDE.md. If both exist, CLAUDE.md wins. An `@AGENTS.md` import inside CLAUDE.md is still the documented bridge. The fallback depends on feature flags and is unavailable on Bedrock, Vertex, and Foundry. [secondary] <https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/>, <https://infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html>
- **Copilot coding agent.** It reads AGENTS.md at the root and in nested folders, plus `.github/copilot-instructions.md`, CLAUDE.md, and GEMINI.md. The fetched page gives an announcement date that differs from the date in its URL. [primary] <https://github.blog/changelog/2026-06-23-copilot-coding-agent-now-supports-agents-md-custom-instructions/>
- **Copilot organization instructions.** These went GA in April 2026 for Copilot Business and Enterprise only. They are set in the settings UI, not in a file. I found no mechanism that makes repos inherit an AGENTS.md from the org `.github` repo. [primary] <https://github.blog/changelog/2026-04-02-copilot-organization-custom-instructions-are-generally-available/>

### Evidence on whether instruction files help

- **ETH Zurich study.** "Evaluating AGENTS.md" (arXiv 2602.11988, v3 from September 2026) found that context files generally don't improve task success and raise inference cost by more than 20%. Repository overviews "are not helpful". Agents do follow the instructions, so the files are useful for practices that aren't standard. [primary] <https://arxiv.org/abs/2602.11988>
- **Same study, split by author.** A secondary summary breaks the result down: LLM-generated files lowered success by about 3%, while developer-written files raised it by about 4%. [secondary] <https://developer.upsun.com/posts/ai/agents-md-less-is-more>
- **What context files contain.** "Agent READMEs" (arXiv 2511.12884) studied 2,303 files. Test procedures appear in 75.9%, implementation details in 70.8%, and architecture in 68.1%. Security appears in only 14.8% and performance in 14.5%. The files change like configuration, through small and frequent additions, and they are hard to read. [primary] <https://arxiv.org/abs/2511.12884>
- **What agents actually read.** Gao and Chen (arXiv 2608.20195) found that instruction files and working notes make up 60.5% of agents' documentation reads. Agents rarely follow links from one document to another, so they favor files that are injected or that sit at conventional paths. [secondary summary] <https://agentpatterns.ai/instructions/documentation-read-counts/>

### Evidence on agents setting up environments

- **SetupBench** (arXiv 2507.09063) evaluated OpenHands starting from a bare Linux sandbox. [primary] <https://arxiv.org/abs/2507.09063>
  - Repository setup succeeded 38.9–57.4% of the time, and local database setup 20–53%.
  - Failures came from incomplete tooling installs, constraints the agent invented, and environment changes that didn't persist.
  - Between 38% and 89% of agent actions were unnecessary.
- **EnvBench.** The best result on its hard subset was 6.69%. [primary] <https://arxiv.org/pdf/2503.14443>

### llms.txt

- **Little use by crawlers.** Adoption is growing, but crawlers rarely fetch the file:
  - Ahrefs found that 97% of llms.txt files were never requested.
  - Otterly found llms.txt in about 0.1% of AI bot visits.
  - Google says it doesn't support the file.

  Sources: [secondary] <https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/>, <https://searchengineland.com/does-llms-txt-matter-467740>
- **Some use by tools.** The Aspire MCP server's documentation search reads `aspire.dev/llms-full.txt`. [primary] <https://aspire.dev/llms.txt>, <https://aspire.dev/get-started/aspire-mcp-server/>
- **Aspire agent setup.** `aspire agent init` (Aspire 13.2 and later) installs Aspire skills and MCP configuration for coding agents. [primary] <https://aspire.dev/reference/cli/commands/aspire-agent-init/>

### The "copy this prompt into your agent" pattern

- **Corti** opens Claude Code, Cursor, or Codex through deeplinks with the prompt pre-filled, and falls back to manual copy if the link doesn't launch. [vendor] <https://docs.corti.ai/quickstart/ai-coding-tools>
- **Databricks** has a "Copy prompt" button. [vendor] <https://developers.databricks.com/templates/onboard-your-coding-agent>
- **NVIDIA NemoClaw** keeps the prompt as a canonical markdown file in the repo, so the copy button always pulls the current text. [vendor] <https://docs.nvidia.com/nemoclaw/user-guide/hermes/resources/agent-skills.md>
- **No convention yet.** There is no single standard for this pattern.

### Writing docs agents can run

Mintlify recommends the following. [vendor] <https://www.mintlify.com/library/how-to-make-your-documentation-agent-friendly>

- State versions and prerequisites before the commands that need them.
- Give complete commands that don't prompt for input, in fenced blocks, each followed by its expected output.
- Document each error where it occurs.
- Mark human handoffs explicitly.
- Test with fresh agent sessions that start from a fixed state and end with a result you can check.
- Rerun those tests after the product or docs change.

## 3. Time to first value and stopping quickstarts from going stale

### Measuring time to first value

- **The metric.** Time to hello world (TTHW), also called time to first call, runs from first contact (landing on the docs) to the first successful result. [vendor] <https://buildwithfern.com/post/reduce-time-to-hello-world-enterprise-partners>
- **Targets vary.** Axway uses under 30 minutes and Zuplo under 15 minutes. [secondary] <https://blog.axway.com/api-management/api-program-time-first-hello-world>, <https://zuplo.com/learning-center/api-analytics-in-developer-experience>
- **What slows people down.** Manual provisioning (credentials, access requests, support tickets) causes the biggest delays. The fix is to remove manual steps, not to write more docs. Same sources as above.
- **Define the milestone.** Choose and write down what counts as "hello world", and measure it with real participants. [secondary] <https://nordicapis.com/sessions/whats-tripping-developers-up-how-to-measure-and-improve-your-time-to-hello-world/>

### Friction logs

The method comes from Google's developer relations practice. [secondary] <https://developerrelations.com/guides/an-introduction-to-friction-logging>

- **Header:** who logged it, the platform, the date, and the product.
- **Scenario:** described in two sentences or fewer.
- **Log:** each step, color-coded: green for delight, yellow for frustration, red for "I would have given up".
- **Triage:** logs go to the owning teams and are linked to existing bugs or new ones.

Resend has every new hire write one. [vendor] <https://resend.com/blog/how-we-use-friction-logs-to-improve-the-product>

### How many testers

The rule that five users find about 85% of problems is disputed. A meta-analysis suggests about nine think-aloud users are needed to find 80%. [primary] <https://cacm.acm.org/research/number-of-people-required-for-usability-evaluation>

### Tools that execute docs

- **mechanical-markdown** (Dapr). [primary] <https://github.com/dapr/mechanical-markdown>
- **Runme**, which offers a GitHub Action. [vendor] <https://stateful.com/blog/readmeops-testing-docs-in-ci>
- **Doc Detective**, which supports inline tests and has a GitHub Action with `create_issue_on_fail`. [vendor] <https://www.mintlify.com/doc-detective/doc-detective/guides/ci-cd>

### Compiled snippets

The .NET docs keep code snippets in compilable projects that articles reference, so CI builds them. [primary] <https://learn.microsoft.com/en-us/contribute/content/dotnet/dotnet-contribute>

### Constraints on scheduled checks and the run paths

- **Scheduled workflows stop silently.** "In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days." [primary] <https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows>
- **Codespaces prebuilds.** Prebuilds cut dev container startup from minutes to seconds, but they use Actions minutes and storage. Whether the open-source grant still exists is [unverified]. [secondary] <https://github.blog/news-insights/product-news/whats-new-with-codespaces-from-github-universe-2022/>, <https://github.com/orgs/community/discussions/179654>
- **Aspire to Docker Compose.** `aspire publish` generates a Compose file with unresolved placeholders such as `${PG_PASSWORD}`, which you supply through `.env` files. Sources conflict on whether `aspire deploy` supports Docker Compose. [primary] <https://aspire.dev/deployment/docker-compose/>, <https://learn.microsoft.com/dotnet/aspire/deployment/docker-integration>

## 4. Docs checks in CI across many repos

### Link checking with lychee

- **Defaults.** In lychee-action v2's `action.yml`, `fail`, `failIfEmpty`, and `jobSummary` all default to `true`, and the pinned lychee version is v0.24.2. [primary] <https://raw.githubusercontent.com/lycheeverse/lychee-action/master/action.yml>
- **Recipes in the README:**
  - A scheduled daily run with `fail: false`, plus `peter-evans/create-issue-from-file` when the exit code isn't zero.
  - A `.lycheecache` kept with `actions/cache`, using `--cache --max-cache-age 1d` to reduce rate limiting.

  [primary] <https://github.com/lycheeverse/lychee-action>
- **Pin to a commit SHA.** Projects pin the action to a full commit SHA because code scanning flags tags that aren't pinned. [primary] <https://cos.googlesource.com/third_party/containerd/+/refs/heads/release-R129/.github/workflows/links.yml>
- **Org-wide switch.** One reusable link-check workflow exposes a `fail_on_errors` boolean input. [secondary] <https://n3b3x.github.io/hf-general-ci-tools/preview/docs/docs-link-check-workflow.html>

### Required sections with markdownlint

- **MD043 (`required-headings`).** It takes a list of headings. A `*` entry matches zero or more headings and `?` matches exactly one, which handles a variable title. Matching ignores case by default, and the rule only detects problems; it doesn't fix them. [primary] <https://github.com/DavidAnson/markdownlint/blob/main/doc/md043.md>
- **markdownlint-cli2-action.** Its README suggests `continue-on-error: true` when introducing rules gradually. A shared base configuration can be passed through the `config` input. [primary] <https://github.com/DavidAnson/markdownlint-cli2-action>

### Banned content with Vale

- **Existence rules.** An `extends: existence` rule flags tokens or regular expressions, such as epic and story ID patterns. Its `level` can be suggestion, warning, or error. [primary] <https://vale.sh/docs/topics/styles>
- **vale-cli/vale-action@v3.**
  - `filter_mode` defaults to `added`, so only new lines are reported.
  - `fail_on_error` defaults to `false`, and when enabled it fails only on error-level alerts.

  [primary] <https://github.com/errata-ai/vale-action>
- **Gradual rollout.** Start rules at warning level and promote them to error later. The `added` filter enforces rules on new content without first cleaning up old files.

### Enforcing across the organization

- **Plan required.** Requiring workflows through rulesets is a GitHub Enterprise Cloud feature. [primary] <https://github.blog/2023-10-11-enforcing-code-reliability-by-requiring-workflows-with-github-repository-rules>
- **Evaluate mode.** It runs a rule without blocking merges and reports what would have failed. Some sources say it needs enterprise billing [unverified]. [primary] <https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/>
- **Merge queues.** Workflows required by an organization ruleset need a `merge_group` trigger if the repo uses a merge queue. [primary] <https://docs.github.com/en/enterprise-server@3.16/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/troubleshooting-rules>

## 5. NuGet README rendering: what's new since the digest

- **No change in behavior.** The Learn page was updated on 2026-07-07, though its `ms.date` still reads 2022-08-31. [primary] <https://learn.microsoft.com/en-us/nuget/nuget-org/package-readme-on-nuget-org>
  - Rendering is still CommonMark through Markdig, and HTML isn't among the listed features.
  - Images with relative paths, and images from domains not on the allow-list, don't render. The warning about them is visible only to package owners.
  - You can preview a README by uploading through the web portal.
- **Allow-list details.** The en-us page lists 38 domains. New details the digest didn't record:
  - devpod.sh, cdn.jsdelivr.net, media.githubusercontent.com, and camo.githubusercontent.com are allowed.
  - The Codespaces badge (`github.com/codespaces/badge.svg`) isn't allowed. Only the `github.com/.../workflows/.../badge.svg` form is, so an "Open in Codespaces" badge won't render on nuget.org.
  - Translated copies of the page show different lists, so use the en-us page. [primary] (same URL)
- **Rewriting relative links when you pack.** These packages haven't been tested here. [primary package pages]
  - `Readme` (MSBuild) rewrites relative links and images to GitHub URLs pinned to the commit. <https://nuget.org/packages/Readme>
  - `NugetRepoReadme` (MSBuild) rewrites them to raw URLs and can remove or replace sections. <https://www.nuget.org/packages/NugetRepoReadme>
  - `RepoReadmeRewriter.CLI` does the same as a .NET tool. <https://www.nuget.org/packages/reporeadmerewriter.cli>
- **Updated .NET guidance.** The .NET blog refreshed "Write a high-quality README for NuGet packages" in July 2026. [primary] <https://devblogs.microsoft.com/dotnet/write-a-high-quality-readme-for-nuget-packages>
  - It recommends a description, highlights, install steps with real examples, the main public types, links, related packages, and feedback or contributing details.
  - It says nothing about AI agents.

## Implications for requirements

1. **Run quickstarts in CI, not only check their links.** *Sharpens the brief.*
   - Every command block in "Use the package", "Run it", and "Try it" carries an annotation stating its expected output, and CI executes it. mechanical-markdown or Runme can do this.
   - These checks run on PRs that touch docs, and on a schedule from one central, active repo. A schedule in a quiet repo stops after 60 days without activity.
   - C# snippets are pulled from compiled source.
2. **Make "Try it" work without manual credentials.** *Challenges the brief.* Manual provisioning is the main cause of slow time to first value. The ≤20-minute "Try it" needs both of these:
   - A default that needs no credentials, such as a local or stub LLM. Otherwise, the API-key step is the only manual step, it is marked as a human handoff, and it is timed separately.
   - A documented start and stop for the clock: from loading the org page to the first chat reply.
3. **Specify the stranger tests as repeatable protocols.** *Sharpens the brief.*
   - The agent test runs inside the dev container with a fixed model and prompt and a deterministic success command. It runs at least three times with a stated pass threshold, because agents in bare environments set up repos successfully only 39–57% of the time.
   - The human test is a smoke test, not a statistical result. It uses a friction-log template, and every red entry becomes an issue.
4. **Keep the shared doc rules short and limited to rules.** *Challenges the brief.* Repository overviews don't help agents and add more than 20% to inference cost.
   - The shared AGENTS.md doc-rules block has a size budget.
   - It holds only rules an agent can't discover: the skeleton, banned content, and link style.
   - Every rule is also enforced by the docs check, so prose isn't the only safeguard.
5. **Copy the rules into each repo, and let CI check they match.** *Sharpens the brief.* No file-based way exists for repos to inherit agent instructions from the org; Copilot's org instructions are paid and set in a UI. Claude Code reads AGENTS.md only when no CLAUDE.md exists.
   - Each repo ships an AGENTS.md and a CLAUDE.md that imports `@AGENTS.md`, synced from one source.
   - CI checks that the shared block is present and matches the source.
6. **Put the command and prompt in the README itself.** *Sharpens the brief.* Agents rarely follow links between documents.
   - The README contains the literal command and prompt, not a link to them.
   - The prompt lives in one canonical file, and CI checks the README copy against it for drift.
7. **Don't require llms.txt.** *Confirms the brief.*
   - No repo needs an llms.txt; at most, a future docs site might publish one.
   - The "Run it" prompt should point agents to Aspire's own agent tooling (`aspire agent init` and the Aspire MCP server).
8. **Roll the docs check out as warn first, then fail, per repo.** *Sharpens the brief.* Ruleset-required workflows are an Enterprise Cloud feature, so plan without them.
   - The reusable workflow takes a `mode: warn|fail` input that defaults to warn.
   - Vale rules start at warning level and use `filter_mode: added`.
   - A rollout table tracks when each repo switches to fail.
   - Internal link checks block merges. External link checks run on a schedule and open issues instead.
   - The lychee wrapper overrides `failIfEmpty`, caches results, and pins the action to a commit SHA.
9. **Enforce the README skeleton without breaking the NuGet page.** *Sharpens the brief.*
   - CI enforces the skeleton with markdownlint MD043 and wildcard entries.
   - Either relative links are rewritten when the package is packed (with `Readme` or `NugetRepoReadme`), or they're banned in the README.
   - The Codespaces badge is kept out of anything shipped to NuGet.
   - Consider adding "Main types" and "Related packages" sections, following the updated .NET guidance.
10. **A uniform skeleton with timed targets would set Hexalith apart, so design out the comparables' failures.** *Confirms the brief.* No comparable has a uniform skeleton or timed targets. The standard should prevent the failures they show:
    - Badge walls (ABP has 11).
    - Contributor material in the user README (Marten).
    - A quickstart buried below the features (Orleans).
    - Snippets that are never compiled (Orleans).
    - Commands that drift after a rename (Kurrent). Keep the "Try it" command in a single source.
