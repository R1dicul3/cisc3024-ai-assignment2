$ErrorActionPreference = "Continue"
$sshDir = "$env:USERPROFILE\.ssh"
New-Item -ItemType Directory -Force -Path $sshDir | Out-Null
if (-not (Test-Path "$sshDir\id_ed25519")) {
  ssh-keygen -t ed25519 -f "$sshDir\id_ed25519" -N '""' -C "R1dicul3@dsh" 2>&1 | Out-String
}
Write-Output ("key exists: " + (Test-Path "$sshDir\id_ed25519.pub"))
Get-Content "$sshDir\id_ed25519.pub"