# Prepare a documentation migration

Give the agent the target repository, the Docs checkout and the intended reader. Review one repository per change set.

1. Locate the registry row and the documentation standard. Inspect the target's checked-in README, package READMEs, linked pages, package configuration and repository instructions.
2. Record a pass or failure for each applicable rule ID with a file, line and fix. Confirm each package ID and selected README against the source. List unknown category, description, quickstart or owner decisions for the reviewer.
3. Keep the README focused on first use. Move developer instructions to the development guide, operator instructions to operations, planning material to its internal owner, and release history to the release channel. List content without a destination before removing it. Escalate when more than 20 such lines would be removed.
4. Respect CI ownership. Submit required workflow, shared Builds pin, policy or protected agent-instruction changes to CiCd. Leave those files untouched in the module change set.
5. Execute the displayed example with the locally packed package, compare all selected README contents with their packages, run the available local docs check, and verify links. Capture the command, positive result or first failure, and unresolved rule IDs.
6. Hand the reviewer the migration, proposed content destinations, unresolved decisions and republish inventory. A maintainer reviews the page, starts the release and verifies each public package.
