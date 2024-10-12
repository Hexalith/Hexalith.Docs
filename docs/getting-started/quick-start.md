# Quick Start Guide

This guide will help you quickly get started with Hexalith, setting up your development environment and creating a simple application.

## Prerequisites

Before you begin, ensure you have the following installed:

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/)

## Step 1: Install Hexalith

1. Open a terminal or command prompt.
2. Run the following command to install the Hexalith project template:

   ```
   dotnet new --install Hexalith.Templates
   ```

## Step 2: Create a New Hexalith Project

1. Create a new directory for your project and navigate to it:

   ```
   mkdir MyHexalithApp
   cd MyHexalithApp
   ```

2. Create a new Hexalith project using the template:

   ```
   dotnet new hexalith
   ```

## Step 3: Run the Application

1. Build and run the application:

   ```
   dotnet run
   ```

2. Open a web browser and navigate to `https://localhost:5001` to see your Hexalith application running.

## Step 4: Explore the Project Structure

Take a moment to explore the generated project structure. You'll find:

- `src/` directory containing the main application code
- `tests/` directory for unit and integration tests
- `Dockerfile` for containerization
- Various configuration files for Dapr, Docker, and .NET

## Step 5: Add a Simple Feature

Let's add a simple "Hello, World!" API endpoint:

1. Open `src/MyHexalithApp.Api/Controllers/HelloController.cs` (create it if it doesn't exist) and add the following code:

   ```csharp
   using Microsoft.AspNetCore.Mvc;

   namespace MyHexalithApp.Api.Controllers
   {
       [ApiController]
       [Route("[controller]")]
       public class HelloController : ControllerBase
       {
           [HttpGet]
           public string Get()
           {
               return "Hello, Hexalith World!";
           }
       }
   }
   ```

2. Run the application again and navigate to `https://localhost:5001/hello` to see your new endpoint in action.

## Next Steps

Congratulations! You've created your first Hexalith application. Here are some next steps to continue your journey:

1. Explore the [Hexalith documentation](../index.md) to learn more about its features and capabilities.
2. Check out the [Installation Guide](installation.md) for a more detailed setup process.
3. Learn about Hexalith's [core concepts](../concepts/index.md) and [architecture](../architecture/overview.md).
4. Join the Hexalith community on [GitHub](https://github.com/Hexalith/Hexalith) to get support and contribute to the project.

Happy coding with Hexalith!
