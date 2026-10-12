import os
# forward-slash path, normalized
p = os.path.normpath("C:/Users/31514/Desktop/3024/data/VisA/_test.txt")
os.makedirs(os.path.dirname(p), exist_ok=True)
try:
    with open(p, "w") as f:
        f.write("ok")
    print("NORM_WRITE_OK", p)
    os.remove(p)
except Exception as e:
    print("FAIL", type(e).__name__, str(e)[:120])
