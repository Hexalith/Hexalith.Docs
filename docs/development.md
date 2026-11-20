# Work on Hexalith Docs

## Prerequisites

Use Git and Python 3.11 or later. Reading this repository and running the registry validator requires only the Docs checkout. The source audit also reads the first-level repositories in `.gitmodules`.

## Set up

From the repository root, initialize the agent guidance if you are using a coding agent.

```sh
git -c submodule.recurse=false submodule update --init -- references/Hexalith.AI.Tools
```

The documentation standard specifies the public pages. The registry records which modules, packages and source files those pages describe. [Documentation standard](documentation-standard.md) · [Registry](module-registry.json)

## Build and test

The guide is Markdown rendered by GitHub. Validate the registry offline after each change.

```sh
python3 scripts/validate_registry.py
```

To check every declared source path and release manifest against local files, initialize the direct dependencies and run the source check.

```sh
git -c submodule.recurse=false -c fetch.recurseSubmodules=false submodule update --init
python3 scripts/validate_registry.py --check-sources
```

The source check uses the available checkout and requires every declared direct module. The package inventory lists product package IDs. The primary package and quickstart selections are editorial proposals until approved. An empty package list means the registry has no product packages for that row. An empty quickstart list selects “Start here.” A null category or badge source awaits evidence. Paths for guides, AppHosts and containers refer to checked-in files. CI ownership describes the intended delivery owner. Each module's actual workflow determines current enforcement.

## Review a change

Review the README in GitHub's Markdown preview and follow every changed link. For a package README, inspect the README file selected by the package's nuspec and run the displayed example in a fresh consumer project. Once the maintainer starts the release, check the listed stable package archives against the source READMEs. From the Docs root, the following command checks both pilots:

```sh
python3 scripts/verify_published_readmes.py
```

For one release, add `--module Hexalith.Commons --version <published-stable-version>`. Then inspect the public NuGet page for rendering and working links.

For the pilot documentation checks, initialize Builds and the target repository, then run from the Docs root:

```sh
python3 references/Hexalith.Builds/Github/lib/docs_check.py --root references/Hexalith.Commons --mode warn
```

The pilot checker becomes available to other checkouts after the corresponding Builds revision is delivered. If the validator reports a missing module or path, compare the registry entry with the direct repository's gitlink and source tree. Correct the inventory or the guide in its owning repository.
