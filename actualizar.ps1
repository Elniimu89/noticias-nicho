Write-Host "Subiendo cambios a GitHub..."

Set-Location -Path $PSScriptRoot

git add .

$hayCambios = git status --porcelain
if (-not $hayCambios) {
    Write-Host "No hay cambios para subir."
    exit 0
}

$mensaje = "Auto Commit - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git commit -m $mensaje

git push

Write-Host "Cambios subidos a GitHub correctamente."
Write-Host "Vercel se actualizará automáticamente con los últimos cambios."
