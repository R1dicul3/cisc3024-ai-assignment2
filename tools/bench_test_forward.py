import sys, os, torch, types, time
os.chdir(r"C:\Users\31514\Desktop\3024\Bayes-PFL")
sys.path.insert(0, r"C:\Users\31514\Desktop\3024\Bayes-PFL")
from models.model_CLIP import Load_CLIP, tokenize
from models.VPB import Context_Prompting, TextEncoder

device = "cuda"
image_size = 224
features_list = [3, 6, 9, 12]
args = types.SimpleNamespace(
    prompt_context_len=5, prompt_num=3, prompt_state_len=5,
    features_list=features_list, vision_width=768, text_width=512, embed_dim=512,
    num_flows=10, sample_num=5, alpha=0.6, image_size=224,
)
model, _, _ = Load_CLIP(image_size, r"C:\Users\31514\Desktop\3024\Bayes-PFL\pretrained_weight\ViT-B-16.pt", device=device)
model.eval()
mymodel = Context_Prompting(args=args).to(device)
text_enc = TextEncoder(model, args)

img = torch.randn(1, 3, image_size, image_size, device=device)
# warmup
mymodel.eval(); mymodel.zk_n = None; mymodel.zk_a = None
with torch.no_grad():
    image_features, _, patch_tokens = model.encode_image(img, features_list)
    text_emb, _ = mymodel.forward_ensemble(text_enc, image_features, patch_tokens, ["candle"], device, tokenize, mode="test")
    mymodel(text_emb, image_features, patch_tokens, stage=1, mode="test")
torch.cuda.synchronize()

N = 30
t0 = time.time()
for _ in range(N):
    mymodel.zk_n = None; mymodel.zk_a = None
    with torch.no_grad():
        image_features, _, patch_tokens = model.encode_image(img, features_list)
        text_emb, _ = mymodel.forward_ensemble(text_enc, image_features, patch_tokens, ["candle"], device, tokenize, mode="test")
        mymodel(text_emb, image_features, patch_tokens, stage=1, mode="test")
torch.cuda.synchronize()
dt = (time.time() - t0) / N
print(f"per-image test forward: {dt*1000:.0f} ms  ->  {dt:.2f} s/img")
print(f"2500 held-out images would take {2500*dt/60:.1f} min")
