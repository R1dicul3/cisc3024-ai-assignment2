import tarfile, collections
tf = tarfile.open(r"C:\Users\31514\Desktop\3024\data\VisA_20220922.tar")
tops = collections.Counter()
for m in tf.getmembers():
    parts = m.name.split("/")
    tops[parts[0] if len(parts) > 1 else "(file)"] += 1
print("top-level entries:")
for k, v in tops.most_common(20):
    print("  ", k, v)
# check for split_csv
has = [m.name for m in tf.getmembers() if "split_csv/1cls.csv" in m.name or m.name.endswith("1cls.csv")]
print("1cls.csv entries:", has[:3])
print("total members:", len(tf.getmembers()))
