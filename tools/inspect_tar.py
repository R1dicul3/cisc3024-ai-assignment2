import tarfile, os
tf = tarfile.open(os.path.normpath("C:/Users/31514/Desktop/3024/data/VisA_20220922.tar"))
for m in tf.getmembers():
    if "image_anno.csv" in m.name:
        print("MEMBER:", m.name)
        print("  type:", m.type, "| isfile:", m.isfile(), "| isdir:", m.isdir())
        print("  islink:", m.issym(), "| islnk:", m.islnk(), "| linkname:", repr(m.linkname))
        print("  mode:", oct(m.mode), "| size:", m.size)
nonreg = [m for m in tf.getmembers() if not (m.isfile() or m.isdir())]
print("non-regular members:", len(nonreg))
for m in nonreg[:30]:
    print("  ", m.name, "| type", m.type, "| linkname", repr(m.linkname))
# csv write test
for p in ["C:/Users/31514/Desktop/3024/data/test_a.csv",
          "C:/Users/31514/Desktop/3024/data/VisA2/test_b.csv",
          "C:/Users/31514/Desktop/3024/test_c.csv"]:
    try:
        with open(os.path.normpath(p), "w") as f:
            f.write("x")
        print("CSV_WRITE_OK", p)
        os.remove(os.path.normpath(p))
    except Exception as e:
        print("CSV_WRITE_FAIL", p, type(e).__name__, str(e)[:90])
