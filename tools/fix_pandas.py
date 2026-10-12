import os
p = os.path.normpath("C:/Users/31514/Desktop/3024/Bayes-PFL/dataset/datasets/VisA.py")
s = open(p, encoding="utf-8").read()
for i in (2, 3, 4):
    s = s.replace("data[%d]" % i, "data.iloc[%d]" % i)
open(p, "w", encoding="utf-8").write(s)
print("fixed VisA.py integer indexing")
