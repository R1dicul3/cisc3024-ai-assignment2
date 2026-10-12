import sys, os, torch, types
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
    num_flows=10, sample_num=5, alpha=0.999, image_size=224,
)
model, _, _ = Load_CLIP(image_size, r"C:\Users\31514\Desktop\3024\Bayes-PFL\pretrained_weight\ViT-B-16.pt", device=device)
model.eval()
mymodel = Context_Prompting(args=args).to(device)
text_enc = TextEncoder(model, args)
print("backbone + prompt-flow model ready")

# ---- TRAIN MODE, batch=2 ----
mymodel.train()
img = torch.randn(2, 3, image_size, image_size, device=device)
names = ["candle", "capsules"]
with torch.no_grad():
    image_features, proj_patch, patch_tokens = model.encode_image(img, features_list)
text_emb, loss_reg = mymodel.forward_ensemble(text_enc, image_features, patch_tokens, names, device, tokenize, mode="train")
pro_img, anomaly_maps = mymodel(text_emb, image_features, patch_tokens, stage=1, mode="train")
loss = loss_reg[1] + loss_reg[2] + loss_reg[3]
for am in anomaly_maps:
    loss = loss + am.mean()
loss = loss + pro_img.mean()
loss.backward()
print("TRAIN MODE OK  text_emb", tuple(text_emb.shape), "pro_img", tuple(pro_img.shape), "loss", round(loss.item(), 4))
print("  grad flow (prompt_context):", mymodel.prompt_context.grad is not None and mymodel.prompt_context.grad.abs().sum().item() > 0)

# ---- TEST MODE, batch=1 (official test.py uses batchsize=1) ----
mymodel.eval()
mymodel.zk_n = None; mymodel.zk_a = None
img1 = torch.randn(1, 3, image_size, image_size, device=device)
with torch.no_grad():
    image_features, proj_patch, patch_tokens = model.encode_image(img1, features_list)
    text_emb, _ = mymodel.forward_ensemble(text_enc, image_features, patch_tokens, ["candle"], device, tokenize, mode="test")
    pro_img, anomaly_maps = mymodel(text_emb, image_features, patch_tokens, stage=1, mode="test")
print("TEST MODE OK  text_emb", tuple(text_emb.shape), "pro_img", tuple(pro_img.shape), "maps", len(anomaly_maps), tuple(anomaly_maps[0].shape))
print("ALL_SMOKE_OK")
