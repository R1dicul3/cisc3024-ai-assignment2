import json
m = json.load(open(r"C:\Users\31514\Desktop\3024\Bayes-PFL\dataset\mvisa\data\meta_visa.json", encoding="utf-8"))
print("top keys:", list(m.keys()))
for phase in ("train", "test"):
    cats = m[phase]
    total = 0
    for c in sorted(cats):
        n = len(cats[c])
        total += n
        print(f"  {phase:5s} {c:12s} {n}")
    print(f"  {phase} TOTAL {total}")
aux = ["candle","capsules","cashew","chewinggum","fryum","macaroni1","macaroni2"]
held = ["pcb1","pcb2","pcb3","pcb4","pipe_fryum"]
print("aux test imgs:", sum(len(m["test"][c]) for c in aux))
print("held test imgs:", sum(len(m["test"][c]) for c in held))
# sample entry
print("sample entry:", m["test"]["candle"][0])
