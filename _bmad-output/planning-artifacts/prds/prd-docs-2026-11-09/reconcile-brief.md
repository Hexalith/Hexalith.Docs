---
title: "Reconciliation: brief + initial brief vs PRD draft"
created: 2026-11-10
inputs:
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/brief.md
  - _bmad-output/planning-artifacts/briefs/brief-docs-2026-11-09/inputs/initial-brief.md
compared_against:
  - prd.md
  - addendum.md
  - .memlog.md
---

# Reconciliation: brief.md and initial-brief.md vs PRD

Scope: `brief.md` and `inputs/initial-brief.md` only. The brief's addendum and memlog are reconciled separately, but I checked the brief addendum before calling anything "ungrounded". Memlog `decision` and `assumption` entries count as deliberate. They appear under "Deliberate changes to confirm" only where I think they need a second look.

## Gaps

### G1. "Written for people", "simple", "clear", "easy to read" become unverified style mechanics (HIGH)

- **Source:** initial-brief.md L13: "**Written for people.** Documentation must be clear and easy to read." brief.md L21: "one documentation standard: simple, clear, and written for people."
- **PRD:** NFR-1 (prd.md L726) keeps the label "Written for people", but reduces it to mechanics: most important point first, second person, active voice, sentence case, numbered steps, short, global audience. The words "simple", "clear", and "easy to read" don't appear anywhere in the PRD. No FR, success metric, or launch gate checks the result:
  - FR-57 (Level 1 done, L702-713) doesn't include NFR-1.
  - The maintainer review in FR-57 has no readability criterion.
  - The FR-7 migration audit (L176-185) doesn't audit style.
  - The friction logs (FR-53, FR-55) don't tag "unclear writing", although the brief addendum gives catching unclear writing as the reason for the stranger test.

  This is the author's first principle, and it currently has no acceptance check. Agents write the docs and a mechanical check gates them, so readability is the quality most likely to slip.
- **Suggested fix:**
  1. Restate NFR-1 in the author's words: "Docs are simple, clear, and easy to read, written for people first." Keep the mechanics as the definition.
  2. Add an FR-57 consequence: the reviewing maintainer confirms the README reads clearly for a newcomer, using a short NFR-1 checklist that the standard publishes.
  3. Add an "unclear writing" category to the friction log, and route every such item to the owning repository.
  4. Have the FR-7 migration audit report NFR-1 findings for the reviewer.

### G2. The "self-sufficient README" principle is never tested (MEDIUM)

- **Source:** initial-brief.md L15: "**Self-sufficient README.** The README must contain everything needed to understand the repository, without being too long."
- **PRD:** Only length limits (FR-10) and section presence (FR-9) are enforced. No consequence checks that a reader can understand the repository from the README alone. That matters most on nuget.org, where every `docs/` link takes the reader away from the page. SM-C1 (L811) protects only what the quickstart needs, not what a reader needs to understand the module. The PRD never uses the word "self-sufficient".
- **Suggested fix:** Add an FR-9 or FR-10 consequence. Reading only the README (as rendered on nuget.org), a newcomer can say what the module does, who it's for, how to start, which packages exist, how to get help or contribute, and what the license is, without following a link. The maintainer review in FR-57 verifies it. Widen SM-C1 to cover "understanding", not only the quickstart.

### G3. The README's purpose ("overview only, details in sub-documents") is missing from the standard (MEDIUM)

- **Source:** initial-brief.md L14: "**Concise at the top level.** The README and its table of contents give an overview only. Details go in dedicated sub-documents linked from the README." brief.md L37: "nothing tells them what a README is for."
- **PRD:** FR-47 (L601-609) puts "what a README is for" in the agent rules. FR-1 (L120), the standard's own list of rules, leaves it out. Under NFR-5 (one source per rule), the agent rules then carry a rule that has no source in the standard. No rule states the general principle that a README is an overview and that details go to `docs/`. FR-14 covers only release history and runbooks.
- **Suggested fix:** Add "README purpose: an overview that stands on its own, with details in linked `docs/` pages" to FR-1's rule list. Point FR-47 to it.

### G4. The 20-minute "Try it" target can be calibrated away (MEDIUM)

- **Source:** brief.md L76: success criterion 2 says only the "Use the package" and "Run it" targets "will be calibrated against the baseline". The 20 minutes is the headline promise (L21, L75). The risk at L125 says that if the build exceeds 20 minutes, "prebuilt images become necessary". In other words, the solution changes, not the target.
- **PRD:** FR-51 (L651) says "Targets can change only through calibration". FR-52 (L658-660) calibrates every target, including Platform's "Try it" path. Nothing prevents relaxing the 20-minute launch gate, which contradicts R-3 (L823).
- **Suggested fix:** State in FR-51 and FR-52 that the 20-minute "Try it" target is fixed. A baseline miss triggers R-3 (the prebuilt images decision), not a target change. Only the 5-minute and 15-minute targets, plus "Use the tool", can be calibrated.

### G5. "The organization page shows only current repositories" is narrowed to the front door list (MEDIUM)

- **Source:** brief.md L81: success criterion 7, "The organization page shows only current repositories." L31: "the 20 current repositories sit among 40 stale or forked ones."
- **PRD:** SM-7 (L803) and FR-25 (L381) check only the profile README list. FR-29 (L411) promises "A visitor sees only current work in the organization", but its consequences only archive repositories, and they forbid deletion. Archived repositories and forks still appear in the repository listing at `github.com/Hexalith`, with a "Public archive" label. So the outcome a visitor sees isn't verified, and archiving alone may not deliver it.
- **Suggested fix:** Define "organization page" in the glossary as the profile README plus the pinned set plus the repository listing, or as the profile README only. Then add a matching FR-29 consequence. If the listing matters, add an option per candidate (archive, make private, or transfer) and let the archive review in Open Question 2 choose.

### G6. The named human tester is dropped, and no backup tester is planned (MEDIUM)

- **Source:** brief.md L119: "Human stranger test by Phuong Duong (GitHub: `tinouit`), then launch." L124: "If the human stranger test fails, a second outside tester is needed."
- **PRD:** §7.4 (L788), FR-55 (L680-688), and §10 (L841) say only "An outside tester who is available once Platform deploys the chatbot". That wording reads as if no tester has been recruited, so story writers may plan recruitment work. FR-55 requires a second tester on failure, but no open question or dependency says who that is. With a December launch, a late search would move the date.
- **Suggested fix:** In §10 and §7.4, record that the first outside tester is already identified: the person named in the brief. If the name was left out on purpose because `_bmad-output/` is public, log that decision in the memlog. Add an open question, owned by a maintainer and due before mid-December, to line up a backup outside tester.

### G7. The launch gate omits brief items that are in scope for launch (MEDIUM)

- **Source:** brief.md L87-98, "In scope for launch": the community files (L90), "Platform also gets a Kubernetes how-to" (L92), and "Pin the key repositories" (L98). Success criterion 7 (L81): "every one of them has the shared community files."
- **PRD:** The §7.3 launch gate (L770-779) doesn't include:
  - FR-33: the organization community files exist. FR-57 covers FR-34 to FR-39, not FR-33.
  - FR-24: the Kubernetes how-to. FR-58 explicitly makes "Try it" the only Level 2 item in the gate.
  - FR-30: pinning.
  - FR-8: the cross-module guide.

  Each of these can slip past launch without anyone deciding that it should.
- **Suggested fix:** Add FR-33 and FR-30 to §7.3. Then either add FR-24 and FR-8 to the gate, or mark them "in scope, not gating" in §7.1 with a reason.

### G8. "About text is accurate" becomes "checked for typos" (LOW)

- **Source:** brief.md L91: "the About text is accurate."
- **PRD:** FR-28 (L407): "A maintainer has checked every About description for typos." FR-2 (L132) has a maintainer confirm categories only, not descriptions. Agents will write the descriptions, and nothing confirms they're accurate.
- **Suggested fix:** Extend FR-2: a maintainer confirms that each registry description accurately describes the module before the front door is published.

### G9. "GitHub open-source best practices" is never named as the baseline (LOW)

- **Source:** initial-brief.md L5: "All documentation, especially the README files, must follow GitHub open-source best practices."
- **PRD:** The PRD never names this anchor. It departs from the practice the brief's research cites, without saying so: Standard Readme requires a table of contents above 100 lines, and the PRD allows 150 lines with no table of contents.
- **Suggested fix:** Add an FR-1 consequence: the standard names the GitHub open-source practices it follows (Community Standards, Standard Readme order, and similar) and lists its deliberate departures.

### G10. Cross-module guides shrink to one overview guide (LOW)

- **Source:** brief.md L41: "Guides that span several modules live in Hexalith.Docs."
- **PRD:** FR-8 (L192) sets a minimum of one overview guide, as an `[ASSUMPTION]` that the memlog doesn't record.
- **Suggested fix:** Confirm with the author, or name the minimum set: an overview plus one concepts or architecture guide.

### G11. The longer-term direction of the vision is dropped (LOW)

- **Source:** brief.md L135: "Hexalith deploys with one command to Docker or Kubernetes, and later to Azure, AWS, and Scaleway. A documentation website, a hosted demo, and prebuilt images come later, each one only when demand justifies the effort."
- **PRD:** §1 (L27-35) states only the launch vision. §6 lists these items as flat non-goals. The "only when demand justifies" principle and the one-command Kubernetes direction are lost, so downstream readers may treat the exclusions as permanent.
- **Suggested fix:** Add a short "Later" paragraph to §1 or §6 that keeps that sentence.

### G12. "Across the organization" becomes "across current repositories" for the stars metric (LOW)

- **Source:** brief.md L83: "1,000 GitHub stars across the organization by the end of 2027."
- **PRD:** SM-8 (L807) says "across current repositories". The change isn't logged.
- **Suggested fix:** Restore "across the organization", or log the narrowing as a decision.

### G13. "Artifacts" narrows to NuGet packages (LOW)

- **Source:** initial-brief.md L19-21: "The README must link to the project's artifacts and quality indicators, for example: NuGet packages…"
- **PRD:** Only the Packages section, which applies only when a repository publishes packages (FR-9 item 5, FR-10). Repositories whose artifacts aren't NuGet packages have no place to link them. Examples are GitHub Releases, tools, and future images.
- **Suggested fix:** Either confirm that NuGet is the only artifact type at launch, or allow the Packages section to list other published artifacts, still NuGet-safe.

### G14. "Each repository adds its own development guide" narrows to repositories with code (LOW)

- **Source:** brief.md L53: "Each repository adds its own development guide."
- **PRD:** FR-36 (L479) covers only "every in-scope repository that contains code". The exempt repositories aren't named. Docs, CiCd, AI.Tools, and BmadSkills are likely candidates.
- **Suggested fix:** Add a "development guide: yes or no" column to the module registry (FR-2), so that each exemption is explicit.

### G15. Which path the human tester uses is unspecified (LOW)

- **Source:** brief.md L21: "One command, or one prompt to an AI coding agent, deploys Hexalith."
- **PRD:** FR-23 (L348) promises both paths in 20 minutes. Agent stranger tests cover the prompt path. FR-55 doesn't say which path the human uses, so the command-only human path may never be validated.
- **Suggested fix:** Have FR-55 name the path the tester follows. The command path is the natural choice, because the agent test already covers the prompt.

### G16. The PRD's frontmatter omits the initial brief as an input (LOW)

- **Source:** The memlog L6 lists `initial-brief` among the inputs.
- **PRD:** The `inputs:` list in the frontmatter (L6-9) leaves it out, which loses the trace back to the author's original principles.
- **Suggested fix:** Add `briefs/brief-docs-2026-11-09/inputs/initial-brief.md` to `inputs:`.

## Deliberate changes to confirm

- **"Run it" blocks are not a launch gate** (memlog L20). **Medium.** Brief success criterion 2 (L76) lists "'Run it' quickstarts take 15 minutes or less" as a launch criterion. Under the PRD, SM-4 (L800) can pass with zero "Run it" blocks published. Keep the decision, but make it visible. For example, add a secondary metric: the number of AppHost repositories with a published "Run it" block at launch, against the total of eleven.
- **No table of contents** (FR-9, L217, an `[ASSUMPTION]` probably covered by "apply recommended" in memlog L12). **Low.** initial-brief.md L14 says "The README and its table of contents give an overview only". Confirm that the outline GitHub generates from headings meets the author's intent. Note that nuget.org shows no such outline.
- **The "Try it" link appears after the agent test, before the human test** (memlog L25, FR-26). **Low.** The order is justified, because the human tester has to start at the front door. Still, the brief's honesty rule (L62) suggests that the front door shouldn't state "20 minutes" until the human test passes, and the organization should stay unannounced in the meantime. Confirm that a live link backed only by the agent test meets "honesty is a rule".

## Ungrounded additions (not in the brief, the initial brief, or the brief addendum, or stricter than them)

- **§7.4 (L785)** loads much more into November than the brief's November row (L116 lists foundations, baseline, and archive review). The PRD adds the docs check in warn mode everywhere, SonarQube Cloud in shared CI, the documentation rules, and the BmadSkills check. Today is November 10, so the month has become much heavier.
- **FR-33 (L455) and SM-7 (L803)** rely on GitHub's Community Standards page to show "all six" files. SUPPORT isn't on that checklist, per the research in the brief addendum. The checklist also includes the description, README, license, and content reports, so "complete for all 21" means more than the six files, and content reports were not adopted. As written, neither can be verified.
- **FR-34 (L462-464)** removes every local community file, including the one existing CODE_OF_CONDUCT and any SECURITY or SUPPORT file, and says "no exceptions before launch". The brief names only CONTRIBUTING removal. The rule is grounded in the "apply to every repository" mechanism, but the strictness is new.
- **New test and automation duties:**
  - FR-24 (L365): an agent stranger test on a local Kubernetes cluster.
  - FR-36 (L480): an agent builds and tests every repository from its development guide.
  - FR-45 (L579): a central weekly external link run that opens issues.
- **Numeric thresholds the author never set:**
  - Quickstart section: 40 lines (FR-10).
  - Front door: 60 lines, with "Try it" in the first 10 (FR-25).
  - Up to six pins, with Platform first (FR-30).
  - Documentation rules file: 100 lines (FR-49).
  - Docs check: 2 minutes (NFR-7).
  - "Use the tool": 5 minutes (FR-21 and FR-51, Open Question 7).
- **Names and constraints with no source:** the topic names (FR-28), and the rule that planning-content and badge rules can't be suppressed (FR-46).
- **A non-goal from the research only:** the per-repository `llms.txt` (§6, L747) comes from `research-landscape.md`, not from the inputs. It's harmless.
- **SM-C5 (L815), "no marketing copy":** this fits the honesty intent, but the author didn't ask for it.
- **The "Maintainer" persona (§2.1, L46) and NFR-9 (contained agent actions):** both are sensible additions without a source.

## Covered well

Front door, the "Try it" gate and its 20-minute start point, the date moving instead of the gate, the honesty rules for badges and the announcement, command plus prompt, dev container and exact toolchain, NuGet-safe single README and republishing, community files, docs check and agent rules, the out-of-scope list, the four brief risks, both open questions, and the four audiences are all faithfully carried, and usually sharpened into testable FRs.
