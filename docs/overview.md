# How Hexalith fits together

A Hexalith business module owns the rules and vocabulary for one area of work. For example, Tenants represents tenants, Parties represents people and organizations, and Projects owns project workspaces. A technical module supplies capabilities several business modules share. EventStore supplies the event-sourced runtime, Commons supplies general .NET helpers, and FrontComposer brings module interfaces into a common application.

## Follow one operation

1. A client asks to change something in a tenant, such as creating a project. Module contracts define the command and its data. McpCli exposes operations that have been enrolled for the environment.
2. The runtime routes the command to its module and aggregate. An aggregate uses its current state to decide which events to emit. Events describe changes that happened.
3. EventStore persists those events. A projection consumes them and builds a read model for queries. A query can therefore show a change after the command has completed.
4. The client reads the result through the operation exposed for its tenant. An operator needs the gateway, tenant identity and authorization appropriate to that environment.

## Select an entry point

| If you want to | Start with |
|---|---|
| Use a standalone .NET library | The module README and the corresponding NuGet package. Try Commons for utilities or PolymorphicSerializations for type-aware JSON. |
| Work on a business capability | The business repository's contracts, domain behavior, README and development guide where available. |
| Understand local hosting | Platform's README. The Aspire AppHost composes selected services and infrastructure. Dapr supplies runtime services such as state and messaging. The available topology depends on the selected modules and their prerequisites. |
| Operate an existing deployment | The module's operations instructions. McpCli documents the gateway and credential handoff for operator access. |

Check the module before choosing a deployment path. Availability of a package alone does not establish that its full topology or interactive quickstart is ready. [Platform](https://github.com/Hexalith/Hexalith.Platform) · [EventStore](https://github.com/Hexalith/Hexalith.EventStore) · [McpCli](https://github.com/Hexalith/Hexalith.McpCli) · [Module registry](module-registry.json)
