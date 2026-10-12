$ErrorActionPreference = "Continue"
$py = "C:\Users\31514\AppData\Local\Programs\Python\Python313\python.exe"
$venv = "C:\Users\31514\Desktop\3024\Bayes-PFL\.venv"
if (-not (Test-Path "$venv\Scripts\python.exe")) {
  Write-Output "creating venv..."
  & $py -m venv --system-site-packages $venv
}
$vpy = "$venv\Scripts\python.exe"
& $vpy -m pip install --upgrade pip -q 2>&1 | Out-Null
Write-Output "installing deps..."
& $vpy -m pip install albumentations scikit-image timm transformers ftfy regex tqdm pandas tabulate 2>&1 | Tee-Object -FilePath "C:\Users\31514\Desktop\3024\logs\pip_install.log" | Select-Object -Last 5
Write-Output "PIP_EXIT=$LASTEXITCODE"
Write-Output "--- import check ---"
& $vpy -c "import torch, torchvision, cv2, numpy, sklearn, scipy, timm, transformers, albumentations, skimage; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), 'vision', torchvision.__version__); print('ALL_IMPORTS_OK')" 2>&1
Write-Output "DONE"
