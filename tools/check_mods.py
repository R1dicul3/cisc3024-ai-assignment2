import importlib.util as iu, sys
mods = ['torch','torchvision','cv2','numpy','sklearn','scipy','pandas','matplotlib',
        'timm','transformers','albumentations','skimage','ftfy','regex','tqdm','tabulate','imgaug']
for m in mods:
    print(m, 'OK' if iu.find_spec(m) else 'MISSING')
try:
    import torch
    print('torch', torch.__version__, 'cuda', torch.cuda.is_available())
    import torchvision
    print('torchvision', torchvision.__version__)
except Exception as e:
    print('torch import err', type(e).__name__, str(e)[:120])
