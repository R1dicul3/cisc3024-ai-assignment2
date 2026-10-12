import sys, os
os.chdir(r"C:\Users\31514\Desktop\3024\Bayes-PFL")
sys.path.insert(0, r"C:\Users\31514\Desktop\3024\Bayes-PFL")
import torch
print("torch", torch.__version__, "cuda", torch.cuda.is_available())
mods = ["datasets", "models.model_CLIP", "models.PFL", "models.VPB", "loss",
        "models.evaluate", "models.metric_and_visualization", "models.EMA", "perlin"]
for m in mods:
    try:
        __import__(m)
        print("OK   ", m)
    except Exception as e:
        print("FAIL ", m, "->", type(e).__name__, str(e)[:160])
print("DONE")
