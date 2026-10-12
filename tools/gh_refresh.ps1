$ErrorActionPreference = "Continue"
$gh = "C:\Users\31514\AppData\Local\Microsoft\WinGet\Packages\GitHub.cli_Microsoft.Winget.Source_8wekyb3d8bbwe\bin\gh.exe"
$NL = [string][char]10
$in = $NL + "Y" + $NL
$in | & $gh auth refresh -h github.com -s admin:public_key 2>&1