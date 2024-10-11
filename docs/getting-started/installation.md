# Getting started with Hexalith

In this article, we are going to see how easy it is to create micro-services applications using the NuGet packages provided by Hexalith.

## Prerequisites

### Install Docker Desktop

Docker Desktop is an easy-to-install application for your Mac or Windows environment that enables you to build and share containerized applications and microservices. Docker Desktop includes Docker Engine, Docker CLI client, Docker Compose, Notary, Kubernetes, and Credential Helper.
Get the latest version of Docker Desktop from the [Docker Web Site](https://www.docker.com/products/docker-desktop/).

### Install DAPR

To run Hexalith applications, you need to have DAPR installed on your machine. You can find the CLI installation instructions [here](https://docs.dapr.io/getting-started/install-dapr-cli/).

#### Install CLI from Command Prompt
Install the latest windows Dapr cli to $Env:SystemDrive\dapr and add this directory to the User PATH environment variable:
```powershell 
powershell -Command "iwr -useb https://raw.githubusercontent.com/dapr/cli/master/install/install.ps1 | iex"
```

Note: Updates to PATH might not be visible until you restart your terminal application

#### Initialize Dapr in your local environment with Docker
Dapr runs as a sidecar alongside your application. In self-hosted mode, this means it is a process on your local machine. By initializing Dapr, you:

- Fetch and install the Dapr sidecar binaries locally.
- Create a development environment that streamlines application development with Dapr.

Dapr initialization includes:

- Running a **Redis container instance** to be used as a local state store and message broker.
- Running a **Zipkin container instance** for observability.
- Creating a **default components folder** with component definitions for the above.
- Running a **Dapr placement service container instance** for local actor support.
- Running a **Dapr scheduler service container instance** for job scheduling.

``` 
dapr init
```

For more information on DAPR setup, see [Dapr initialization](https://docs.dapr.io/getting-started/install-dapr-selfhost/).

## Create an Hexalith module repository

Create an empty repository on GitHub. Ex: `MyTodo`.

Clone the repository on your local machine.

```
git clone https://github.com/{Organization}/MyTodo.git
cd MyTodo
git checkout main
```

Add Hexalith submodule to your repository.

```
git submodule add https://github.com/Hexalith/Hexalith.git
cd Hexalith
git checkout main
cd ..
```

Add Hexalith client/server application submodule to your repository.

```
git submodule add https://github.com/Hexalith/HexalithApp.git
cd HexalithApp
git checkout main
cd ..
```

If you use Azure Container App integrated authentication, add Hexalith.EasyAuthentication submodule to your repository.

```
git submodule add https://github.com/Hexalith/Hexalith.EasyAutehtication.git
cd Hexalith.EasyAuthentication
git checkout main
cd ..
```

