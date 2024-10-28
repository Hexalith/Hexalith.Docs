# Creating a New Module in Hexalith

This guide explains how to create a new module in the Hexalith framework. There are two approaches available:

## 1. Using a Template Project

> ⚠️ This feature is currently under development and not yet available.

## 2. Creating a Module by Cloning an Existing One

This approach involves copying and customizing an existing module that has similar features to what you want to build.

### Step-by-Step Guide

1. **Select a Source Module**
   - Choose an existing module that closely matches your requirements
   - For example, you might use the Contacts module as a starting point

2. **Clone the Source Module**

   ```powershell
   git clone https://github.com/Hexalith/Hexalith.Contacts.git
   ```

3. **Create and Clone Your New Module Repository**

   ```powershell
   git clone https://github.com/{your-organization}/Hexalith.{YourModuleName}.git
   ```

   Replace `{your-organization}` with your GitHub organization name and `{YourModuleName}` with your module name (e.g., `Hexalith.MyTodo`)

4. **Copy Module Contents**
   Use the provided PowerShell script to copy the source module files while excluding unnecessary directories:

   ```powershell
   ./copy_module_sources.ps1 -SourceDir "Hexalith.Contacts" -DestinationDir "Hexalith.{YourModuleName}"
   ```

### Source Copy Script

Save the following PowerShell script as `copy_module_sources.ps1`:

```powershell
param (
    [string]$SourceDir,
    [string]$DestinationDir
)

# Define paths to exclude from copying
$excludedPaths = @(
    "$SourceDir\.git",
    "$SourceDir\.vs",
    "$SourceDir\.gitmodules"
)

# Copy files while respecting exclusions
Get-ChildItem -Path $SourceDir -Recurse -Force |
    Where-Object { 
        $item = $_
        $isExcludedHexalith = $item.PSIsContainer -and 
                             $item.FullName.Substring($SourceDir.Length).TrimStart('\').StartsWith('Hexalith')
        -not ($excludedPaths | Where-Object { $item.FullName -like $_ }) -and
        -not $isExcludedHexalith
    } |
    ForEach-Object {
        $destinationPath = $_.FullName.Replace($SourceDir, $DestinationDir)
        if (-not $_.PSIsContainer) {
            $null = New-Item -Path (Split-Path $destinationPath -Parent) -ItemType Directory -Force
            Copy-Item -Path $_.FullName -Destination $destinationPath -Force
        }
    }
```

### What Gets Copied

The script will copy all files from the source module except for:

- `.git` directory (version control data)
- `.vs` directory (Visual Studio settings)
- `Hexalith*` folders
- `.gitmodules` file

After copying, you can begin customizing the module for your specific needs while maintaining the Hexalith framework structure.

### Rename the module components and replace the contact name by MyTodo.

   ```powershell
   ./renameFiles.ps1 -OldValue "Contacts" -NewValue "MyTodo"
   ```

**The rename files script (renameFiles.ps1) :**

```powershell
param (
    [Parameter(Mandatory=$true)]
    [string]$OldValue,

    [Parameter(Mandatory=$true)]
    [string]$NewValue
)

# Enable verbose output
$VerbosePreference = "Continue"

Write-Verbose "Current working directory: $(Get-Location)"

# Function to delete directories
function Remove-Directories {
    param (
        [string]$DirectoryName
    )
    
    $dirs = Get-ChildItem -Path . -Recurse -Directory -Filter $DirectoryName
    foreach ($dir in $dirs) {
        try {
            Remove-Item -Path $dir.FullName -Recurse -Force
            Write-Verbose "Deleted directory: $($dir.FullName)"
        }
        catch {
            Write-Error "Failed to delete directory $($dir.FullName): $_"
        }
    }
}

# Delete 'bin' and 'obj' directories
Write-Host "Deleting 'bin' and 'obj' directories..."
Remove-Directories -DirectoryName "bin"
Remove-Directories -DirectoryName "obj"

$renamedCount = 0
$errorCount = 0

# Function to rename item (file or directory)
function Rename-ItemIfNeeded {
    param (
        [System.IO.FileSystemInfo]$Item
    )
    
    if ($Item.Name -like "*$OldValue*") {
        $newName = $Item.Name -replace "(?i)$([regex]::Escape($OldValue))", $NewValue
        
        # Construct new path
        if ($Item.PSIsContainer) {
            # For directories
            $parentPath = Split-Path -Path $Item.FullName -Parent
            $newPath = [System.IO.Path]::Combine($parentPath, $newName)
        } else {
            # For files
            $newPath = [System.IO.Path]::Combine($Item.DirectoryName, $newName)
        }
        
        try {
            Rename-Item -Path $Item.FullName -NewName $newPath -Force -ErrorAction Stop
            Write-Verbose "Renamed: $($Item.FullName) to $newPath"
            $script:renamedCount++
        }
        catch {
            Write-Error "Failed to rename $($Item.FullName): $_"
            $script:errorCount++
        }
    }
}

# Get all items (files and directories) in the current directory and subdirectories
$allItems = Get-ChildItem -Path . -Recurse

Write-Verbose "Found $($allItems.Count) items in total."

# Rename files first
$allItems | Where-Object { -not $_.PSIsContainer } | ForEach-Object { Rename-ItemIfNeeded -Item $_ }

# Rename directories from the bottom up
$allDirs = $allItems | Where-Object { $_.PSIsContainer } | Sort-Object -Property FullName -Descending
$allDirs | ForEach-Object { Rename-ItemIfNeeded -Item $_ }

Write-Host "Renaming complete. Renamed $renamedCount item(s). Encountered $errorCount error(s)."
Write-Host "Current location: $(Get-Location)"
Write-Host "Items in current directory:"
Get-ChildItem | Select-Object Name, PSIsContainer
```

### Rename files and projects in the solution file

Open the solution file in the directory, for example Hexalith.MyTodo.sln with Visual Code or any other text editor. Replace "Contact" by "MyTodo".

### Add Hexalith submodules to the project

```powershell
git checkout main
git submodule add https://github.com/Hexalith/Hexalith.git
git submodule add https://github.com/Hexalith/HexalithApp.git
git submodule add https://github.com/Hexalith/Hexalith.EasyAuthentication.git
git submodule update
Set-Location .\Hexalith
git checkout main
Set-Location ..\HexalithApp
git checkout main
Set-Location ..\Hexalith.EasyAuthentication
git checkout main
Set-Location ..
git add .
git commit -m "intialize hexalith submodules"
git push
```


### Change the project name in the props files

Open all props files in the root directory of the repository in Visual Studio and change the source module name "Contact" by the new module name "MyTodo". Then change "contact" by "mytodo". Choose change in all open files and set the case sensitive option.

- Directory.Build.props
- Hexalith.Modules.Client.props
- Hexalith.Modules.Server.props
- Hexalith.Modules.Shared.props
- Hexalith.Modules.StoreApp.props
- Hexalith.props
 

### Customise the Events, Commands and Aggregates

In the Events, Commands and Domain projects do the changes so that the elements reflects the domain of the new module.

Start with Events, then Aggragates. For the commands you can copy your events and rename them so they reflect an action to do insted of a past action for events.




