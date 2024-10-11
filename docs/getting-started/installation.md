# Getting Started with Hexalith

Hexalith is a powerful framework for building microservices applications. This guide will walk you through the process of setting up your environment and creating your first Hexalith module repository.

## Introduction

Hexalith simplifies the development of microservices applications by providing a set of NuGet packages and tools. It leverages technologies like Docker and Dapr to create a robust and scalable architecture for your applications.

## Prerequisites

Before you begin, ensure you have the following tools installed on your system:

### 1. Docker Desktop

Docker Desktop is essential for running containerized applications and microservices.

1. Visit the [Docker Web Site](https://www.docker.com/products/docker-desktop/)
2. Download and install the latest version for your operating system (Mac or Windows)

Docker Desktop includes:
- Docker Engine
- Docker CLI client
- Docker Compose
- Kubernetes
- And more

### 2. Dapr (Distributed Application Runtime)

Dapr is a portable, event-driven runtime that makes it easy to build resilient, stateless, and stateful applications.

#### Install Dapr CLI

For Windows, run the following command in PowerShell:

```powershell
powershell -Command "iwr -useb https://raw.githubusercontent.com/dapr/cli/master/install/install.ps1 | iex"
```

This command installs the latest Dapr CLI to `$Env:SystemDrive\dapr` and adds this directory to the User PATH environment variable.

Note: You may need to restart your terminal for PATH changes to take effect.

#### Initialize Dapr

After installing the CLI, initialize Dapr in your local environment:

```
dapr init
```

This command sets up your development environment by:
- Installing Dapr sidecar binaries
- Setting up a Redis container for state store and message broker
- Setting up a Zipkin container for observability
- Creating a default components folder
- Setting up containers for Dapr placement service and scheduler service

For more detailed information on Dapr setup, refer to the [Dapr initialization documentation](https://docs.dapr.io/getting-started/install-dapr-selfhost/).

## Creating a Hexalith Module Repository

Follow these steps to set up your Hexalith module repository:

1. Create an empty repository on GitHub (e.g., `MyTodo`)

2. Clone the repository to your local machine:
   ```
   git clone https://github.com/{Organization}/MyTodo.git
   cd MyTodo
   git checkout main
   ```

3. Add the Hexalith submodule to your repository:
   ```
   git submodule add https://github.com/Hexalith/Hexalith.git
   cd Hexalith
   git checkout main
   cd ..
   ```

4. Add the Hexalith client/server application submodule:
   ```
   git submodule add https://github.com/Hexalith/HexalithApp.git
   cd HexalithApp
   git checkout main
   cd ..
   ```

5. (Optional) If you're using Azure Container App integrated authentication, add the Hexalith.EasyAuthentication submodule:
   ```
   git submodule add https://github.com/Hexalith/Hexalith.EasyAuthentication.git
   cd Hexalith.EasyAuthentication
   git checkout main
   cd ..
   ```

## Next Steps

Now that you have set up your environment and created a Hexalith module repository, you're ready to start building your microservices application. Refer to the other documentation sections for guidance on how to develop, test, and deploy your Hexalith-based application.
