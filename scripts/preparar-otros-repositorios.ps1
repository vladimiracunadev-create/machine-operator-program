param(
    [string]$Owner = "vladimiracunadev-create",
    [string]$Destino = "C:\dev\vladimir-repos"
)

$ErrorActionPreference = "Stop"

Write-Host "Comprobando acceso a GitHub..."
gh auth status
if ($LASTEXITCODE -ne 0) {
    throw "GitHub no esta autenticado en esta ventana de PowerShell."
}

New-Item -ItemType Directory -Path $Destino -Force | Out-Null

$reposJson = gh repo list $Owner --limit 100 --json nameWithOwner,isArchived
if ($LASTEXITCODE -ne 0) {
    throw "No se pudo obtener la lista de repositorios de $Owner."
}

$repos = $reposJson | ConvertFrom-Json | Where-Object { -not $_.isArchived }

foreach ($repo in $repos) {
    $name = ($repo.nameWithOwner -split "/")[-1]
    $localPath = Join-Path $Destino $name

    if (Test-Path (Join-Path $localPath ".git")) {
        Write-Host "Actualizando $($repo.nameWithOwner)..."
        git -C $localPath pull --ff-only
    } else {
        Write-Host "Descargando $($repo.nameWithOwner)..."
        gh repo clone $repo.nameWithOwner $localPath
    }

    if ($LASTEXITCODE -ne 0) {
        throw "No se pudo preparar $($repo.nameWithOwner)."
    }
}

Write-Host ""
Write-Host "Repositorios listos en: $Destino"
Write-Host "Abre esa carpeta como proyecto en Codex."
