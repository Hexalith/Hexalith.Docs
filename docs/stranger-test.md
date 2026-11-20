# Measure a newcomer's first result

Use one fresh environment for each attempt. A maintainer or silent observer operates the clock. The participant receives only the starting page and, for an agent run, the prompt printed on that page.

| Journey | Starting environment and page | First result | Target |
| --- | --- | --- | --- |
| Use the package | Fresh machine or container with the required .NET SDK, at the package README | The displayed sample returns the expected value | 5 minutes |
| Use the tool | Fresh machine or container with the required .NET SDK, at the tool README | The first documented command returns its expected output | 5 minutes |
| Run it | Machine with Docker and VS Code, or a newly created Codespace, at the module README | The first call succeeds | 15 minutes |
| Try it | Newcomer's own machine with Docker and VS Code, plus the declared agent for the prompt path | McpCli creates a project and lists that same project | 20 minutes |

## Prepare the run

1. Record the pinned source revision, starting page and path (setup command or agent prompt). For an agent run, record the tool, version, model and the exact public prompt or its immutable source link. Open a fresh session with empty conversation history and no project context.
2. Use a fresh image, user profile, or machine with no Hexalith checkout, built assets, package or image cache, credentials, or previous deployment. Verify Docker points to the participant's own engine when required. Use synthetic tenant data supplied by the documented setup. Keep evidence anonymous.
3. On a local host with Python 3, copy the [measurement helper](../tools/stranger-test.py) outside the project checkout and run the matching preflight. It checks local tools and likely warm state. Inspect any reported issue. Check the physical host or image provenance as well, including custom cache paths, running services and the supported editor or agent. For Codespaces, record its fresh provisioning and exact image. If Python is unavailable on the participant's device, perform these same checks manually and run the observer clock elsewhere.

```sh
python3 stranger-test.py preflight try-it
```

## Time the journey

1. Start the clock the instant the starting page opens. For agent rehearsals of Try it, start at the Platform README until the organization link goes live. For the human launch run, start at the organization page. Include reading, prerequisite acquisition, cold container start, build, readiness and the first operation in elapsed time.
2. Run the observer separately. Press Enter only when the corresponding event occurs. For Try it, mark container start request and completion, then full application build start and completion. Their elapsed differences give separate cold-start and cold-build durations. Check health for the seven expected modules and match the created project to the list result in the same tenant. Observe only the synthetic identity match. Record elapsed time for each intervening step in the friction log.
3. Type `stop` at the next milestone if a prerequisite fails, if the participant needs help, or if an agent requests a secret in chat. Record the failed step and elapsed time. Keep secrets, transcripts, tenant identifiers and personal details out of the result.
4. Repeat an agent test in three independent clean environments. A pass requires at least two unaided runs within target. After the agent gate passes, a maintainer confirms an eligible outside tester and backup, declares the path in advance and runs the human trial. If it fails, address the friction and requalify the agent route before the backup trial.

```sh
python3 stranger-test.py observe try-it > timing.json
```

Use `package`, `tool` or `run` in place of `try-it` for the other journeys. A stopwatch and the same milestone record work when an observer cannot run Python. Completion of the timer records an observation. The maintainer evaluates the timing, independence, identity match and friction before recording a pass.

## Record the outcome

Store the run summary with the launch ledger. Keep private evidence with its owner. Record one friction row per participant step.

| Run | Date, revision, role, environment and preflight | Starting page, path and public prompt | Agent tool, version and model | Elapsed seconds, first result and outcome |
| --- | --- | --- | --- | --- |
| | | | | |

| Elapsed seconds | Step and observed result | Green (as documented), amber (confusing), or red (blocked or helped) | Issue reference |
| --- | --- | --- | --- |
| | | | |

Open an issue for each red item. For a human trial, track every friction item. Repeat the applicable test when a published command or prerequisite changes.
