$ErrorActionPreference = "Continue"
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
Write-Output "=== add key via gh ==="
gh ssh-key add "C:\Users\31514\.ssh\id_ed25519.pub" --title "dsh-laptop-3024" 2>&1 | Out-String -Width 160
Write-Output "add exit: $LASTEXITCODE"
Write-Output "=== write ssh config ==="
$cfg = "C:\Users\31514\.ssh\config"
Set-Content -Path $cfg -Encoding ascii -Value "Host github.com`n  HostName ssh.github.com`n  Port 443`n  User git`n  IdentityFile ~/.ssh/id_ed25519"
Write-Output "=== test ssh ==="
ssh -o StrictHostKeyChecking=no -o ConnectTimeout=15 -p 443 -T git@ssh.github.com 2>&1 | Out-String -Width 160
Write-Output "ssh test exit: $LASTEXITCODE"