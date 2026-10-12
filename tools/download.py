import urllib.request, sys, os, time
url, out = sys.argv[1], sys.argv[2]
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=60) as r, open(out, "wb") as f:
    total = int(r.headers.get("Content-Length", 0) or 0)
    done, t0 = 0, time.time()
    while True:
        chunk = r.read(1024 * 1024 * 16)
        if not chunk:
            break
        f.write(chunk); done += len(chunk)
        if total:
            spd = done / 1e6 / max(time.time() - t0, 1e-6)
            print(f"{done/1e6:7.0f}/{total/1e6:7.0f} MB ({done/total*100:4.0f}%) {spd:6.1f} MB/s", flush=True)
print("DONE", out, done, "bytes", flush=True)
