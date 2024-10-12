# Installing Hexalith

This guide provides detailed instructions for setting up your development environment and installing Hexalith. For a quicker start, you may refer to our [Quick Start Guide](quick-start.md).

## Prerequisites

Before installing Hexalith, ensure you have the following tools and software installed on your system:

1. **.NET 8.0 SDK or later**
   - Download and install from [.NET Download Page](https://dotnet.microsoft.com/download/dotnet/8.0)

2. **Docker Desktop**
   - Visit the [Docker Website](https://www.docker.com/products/docker-desktop/)
   - Download and install the latest version for your operating system (Windows, macOS, or Linux)

3. **Dapr CLI**
   - For Windows, run the following command in PowerShell:

     ```powershell
     powershell -Command "iwr -useb https://raw.githubusercontent.com/dapr/cli/master/install/install.ps1 | iex"
     ```

   - For other operating systems, follow the instructions in the [Dapr documentation](https://docs.dapr.io/getting-started/install-dapr-cli/)

## Step 1: Initialize Dapr

After installing the Dapr CLI, initialize Dapr in your local environment:

```bash
dapr init
```

This command sets up your development environment by:

- Installing Dapr sidecar binaries
- Setting up a Redis container for state store and message broker
- Setting up a Zipkin container for observability
- Creating a default components folder

## Step 2: Install Hexalith Templates

Install the Hexalith project templates using the .NET CLI:

```bash
dotnet new --install Hexalith.Templates
```

## Step 3: Create a Hexalith Project

1. Create a new directory for your project and navigate to it:

   ```bash
   mkdir MyHexalithProject
   cd MyHexalithProject
   ```

2. Create a new Hexalith project using the template:

   ```bash
   dotnet new hexalith
   ```

## Step 4: Explore the Project Structure

After creating your project, take some time to explore its structure:

- `src/`: Contains the main application code
- `tests/`: Contains unit and integration tests
- `Dockerfile`: For containerizing your application
- Various configuration files for Dapr, Docker, and .NET

## Step 5: Build and Run the Project

1. Build the project:

   ```bash
   dotnet build
   ```

2. Run the application:

   ```bash
   dotnet run --project src/YourProjectName.Api
   ```

3. Open a web browser and navigate to `https://localhost:5001` to see your Hexalith application running.

## Next Steps

Now that you have Hexalith installed and a basic project set up, you can:

1. Explore the [Hexalith documentation](../index.md) to learn more about its features and capabilities.
2. Check out our [tutorials](../tutorials/index.md) for step-by-step guides on building applications with Hexalith.
3. Learn about Hexalith's [core concepts](../concepts/index.md) and [architecture](../architecture/overview.md).
4. Join the Hexalith community on [GitHub](https://github.com/Hexalith/Hexalith) to get support and contribute to the project.

If you encounter any issues during installation or have questions, please refer to our [troubleshooting guide](../troubleshooting.md) or open an issue on our GitHub repository.

Happy developing with Hexalith!
