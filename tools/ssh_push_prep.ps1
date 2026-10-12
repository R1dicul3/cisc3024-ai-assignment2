$ErrorActionPreference = "Continue"
$cfg = "C:\Users\31514\.ssh\config"
$content = "Host github.com`n  HostName ssh.github.com`n  Port 443`n  User git`n  IdentityFile ~/.ssh/id_ed25519`n  IdentitiesOnly yes`n"
Set-Content -Path $cfg -Encoding ascii -Value $content
Write-Output "=== ssh test (deploy key) ==="
ssh -o StrictHostKeyChecking=no -o ConnectTimeout=15 -T git@github.com 2>&1 | Out-String -Width 160
Write-Output "ssh exit: $LASTEXITCODE"