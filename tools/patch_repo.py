import sys
def patch(path, remove_lines):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    removed = []
    out = []
    for i, l in enumerate(lines):
        if i in remove_lines:
            removed.append(l.rstrip()[:60])
            continue
        out.append(l)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.writelines(out)
    print(f"patched {path}: removed {len(removed)} lines")
    for r in removed:
        print("   -", r)

base = "C:/Users/31514/Desktop/3024/Bayes-PFL/"
patch(base + "datasets.py", set([10] + list(range(50, 63))))
patch(base + "train.py", set([18]))
patch(base + "test.py", set([14]))
print("ALL PATCHES DONE")
