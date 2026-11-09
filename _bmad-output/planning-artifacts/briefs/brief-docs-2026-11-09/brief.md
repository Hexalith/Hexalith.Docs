---
title: "Product Brief: Hexalith Documentation Standard"
status: final
created: 2026-11-09
updated: 2026-11-09
---

# Product Brief: Hexalith Documentation Standard

## Executive summary

Hexalith is a set of technical and business modules for managing enterprise workflows through a chatbot. The code is public on GitHub and the packages are on NuGet, but the documentation isn't ready for anyone outside the team:

- READMEs range from a bare title to 1,275 lines.
- Internal planning notes appear in public files.
- Quality badges don't reflect real scans.
- A newcomer has no quick way to try Hexalith.

Nobody outside the team uses Hexalith yet. The documentation is what stands between the project and a public launch.

This initiative gives every Hexalith repository one documentation standard: simple, clear, and written for people. The organization page explains Hexalith and offers "Try it". One command, or one prompt to an AI coding agent, deploys Hexalith on Docker, so a newcomer is chatting with it within 20 minutes. Every README follows the same short skeleton and doubles as the NuGet package page.

Launch is targeted for the end of 2026, but "Try it" must work first. If the two conflict, the date moves.

AI agents write most of Hexalith's documentation. So the standard lives in their shared instructions, and a check in the shared CI enforces it. Together, these keep the standard in place after launch.

## The problem

Someone who wants to build with Hexalith or use the application can open any of its 20 current repositories. They still won't quickly learn what each module does, whether it suits them, or how to get it running.

- **There is no front door.** A first visitor finds no organization page, and the 20 current repositories sit among 40 stale or forked ones.
- **READMEs don't share a purpose.** Some introduce the product, some are build runbooks, and some are release logs full of commit SHAs and CI run IDs.
- **NuGet package pages inherit the README's gaps.** The README doubles as the package page, so on nuget.org, `Hexalith.Projects.Contracts` shows only a title.
- **Nothing gets a newcomer started fast.** Five repositories have a quickstart, and nobody has timed any of them.
- **Quality claims can't be trusted.** The Coverity and SonarCloud (now SonarQube Cloud) badges have no scans behind them, and some badges point to deleted workflows.
- **Contributors get no consistent guidance.** Five repositories have a CONTRIBUTING file, ranging from 23 to 680 lines. One has a code of conduct. None has a security policy, issue templates, or pull request (PR) templates.
- **Internal planning content leaks into public docs.** Epics, stories, and requirement IDs appear because agents write most of the docs and nothing tells them what a README is for.

## The solution

- **A front door.** The organization page (`github.com/Hexalith`) explains Hexalith on one screen. It lists every business and technical module and links "Try it" to the Platform quickstart, which deploys the chatbot and the services it needs. Guides that span several modules live in Hexalith.Docs.
- **One README skeleton everywhere.** Each README targets 150 lines or fewer and covers:
  - what the module does and who it's for
  - a quickstart
  - its packages
  - links to the detailed docs in `docs/`
  - how to contribute
  - the license

  The same file must render correctly on both GitHub and nuget.org.
- **Quickstarts that work in minutes.** Each quickstart opens with what the reader does first: use the package, run the module, or use the tool. For a module that runs, the "Run it" quickstart starts with one command inside a dev container, and the dev container installs the exact toolchain. A short AI prompt lets a newcomer's coding agent do the setup.
- **Honest quality signals.** Each README shows at most five badges: NuGet version, CI status, license, and the SonarQube Cloud quality gate with coverage. A running pipeline produces each one.
- **Shared community files.** A CONTRIBUTING guide, a code of conduct, a security policy, a support page, and issue and PR templates apply to every repository. Each repository adds its own development guide.
- **Automatic enforcement.** The shared agent instructions carry the documentation rules. A docs check in the shared CI flags missing sections, broken links, and internal planning content.

## What makes this approach different

None of this is technically hard to copy. The value comes from applying it consistently across 20 repositories. Three choices set it apart:

- **Built for documentation written by agents.** The rules sit where agents read them, and CI catches what agents miss.
- **Command plus prompt.** Newcomers can let their own agent do the setup, which suits a product people use through a chatbot.
- **Honesty is a rule.** No badge appears without a pipeline behind it. "Try it" isn't announced until it passes a timed stranger test, run by someone who has never used Hexalith.

## Who this serves

- **Developers evaluating or building with Hexalith.** They find a module on GitHub or nuget.org and want something working in minutes, without asking anyone.
- **People who want to use the application.** They start at "Try it" and want a running Hexalith to chat with within minutes.
- **Contributors.** They need the shared community files and a development guide, so they can open a first pull request without reverse-engineering the build.
- **AI coding agents (secondary).** Agents write the docs and run the quickstarts for newcomers, so they need explicit rules and short, reliable commands.

## Success criteria

**At launch:**

1. A newcomer goes from `github.com/Hexalith` to a first chat message in **20 minutes or less**, on a clean machine with Docker. A tester from outside the team times this human stranger test once Platform is finished.
2. "Use the package" quickstarts take **5 minutes or less**, and "Run it" quickstarts take **15 minutes or less**. These targets will be calibrated against the baseline measured in November.
3. In the agent stranger test, a fresh AI agent gets only the Platform README and the AI prompt, and completes "Try it".
4. All 20 current repositories pass the docs check.
5. Every NuGet package page shows the module's description and quickstart.
6. A running pipeline backs every badge.
7. The organization page shows only current repositories, and every one of them has the shared community files.

**After launch:** 1,000 GitHub stars across the organization by the end of 2027, up from 0 on 2026-11-09. Reaching that depends on outreach, which is outside this initiative.

## Scope

**In scope for launch** (the addendum has the checklists):

- **Foundations in Hexalith.Docs:** the standard, the README skeleton, the templates, and a migration prompt for agents.
- **`Hexalith/.github`:** the organization page (its profile README) and the shared community files.
- **Level 1, "Clean," for all 20 current repositories:** each README follows the skeleton, the About text is accurate, there's no internal planning content, and links and badges work.
- **Level 2, "Try-able":** Platform's "Try it" on Docker comes first, as the launch gate. Each module's "Run it" follows once it meets its time target. Platform also gets a Kubernetes how-to.
- **Shared CI and agent rules:** SonarQube Cloud and the docs check go into Hexalith.Builds, and the documentation rules go into Hexalith.AI.Tools.
- **Organization cleanup:**
  - Archive the reviewed stale repositories and forks.
  - Check `Hexalith.BmadSkills` for sensitive data in its 106 `.claude.json` files.
  - Make Hexalith.Docs and `Hexalith/.github` public.
  - Pin the key repositories.

**Out of scope for now:**

- Deployment to Azure, AWS, and Scaleway
- A documentation website
- A hosted demo
- Prebuilt container images, unless "Try it" misses its target
- Vale, organization-wide rulesets, Coverity, and Codacy
- Reorganizing existing `docs/` folders
- xppmodel, which belongs to the Itaneo organization

## Timeline and risks

Launch targets the end of 2026, but only once "Try it" works.

| When | Milestone |
|---|---|
| November | Foundations, baseline time measurement, review of the archive list |
| Late November to early December | Level 1 migration of all 20 repositories |
| Mid-December | Platform deploys the chatbot (reported on track) |
| December | Human stranger test by Phuong Duong (GitHub: `tinouit`), then launch |

**Risks:**

- **Platform completion.** This is the main risk. The docs can be ready on time, but "Try it" can't pass until Platform deploys the chatbot.
- **There is only one human stranger test.** Each person can be a first-time user only once. The baseline and every iteration therefore use the agent stranger test. If the human stranger test fails, a second outside tester is needed.
- **Build time.** Building Platform from source pulls in 17 repositories and might take longer than 20 minutes. If it does, prebuilt images become necessary, and that work isn't in this plan.
- **Review capacity.** Agents can write the Level 1 changes quickly. The bottleneck is human review of 20 repositories.

## Open questions

- **What does a newcomer need for "Try it" besides Docker?** Possibly an LLM provider key, a sign-in account, or a mailbox. Whatever's needed affects the 20-minute target and must appear in the quickstart.
- **Which stale repositories and forks get archived?** The candidate list in the addendum is waiting for review.

## Vision

People, or their AI agents, can adopt any Hexalith module in minutes. Hexalith deploys with one command to Docker or Kubernetes, and later to Azure, AWS, and Scaleway. A documentation website, a hosted demo, and prebuilt images come later, each one only when demand justifies the effort.
