import sys, os, shutil, tarfile, time, glob
def P(s):
    return os.path.normpath(s)
BASE = P("C:/Users/31514/Desktop/3024/Bayes-PFL")
TAR = P("C:/Users/31514/Desktop/3024/data/VisA_20220922.tar")
SRC = P("C:/Users/31514/Desktop/3024/data/VisA4")

need = (os.path.exists(os.path.join(SRC, "split_csv", "1cls.csv")) and
        os.path.exists(os.path.join(SRC, "candle", "Data")) and
        os.path.exists(os.path.join(SRC, "pipe_fryum", "Data")))
if not need:
    os.makedirs(SRC, exist_ok=True)
    tf = tarfile.open(TAR)
    members = [m for m in tf.getmembers() if "image_anno.csv" not in m.name]
    print("extracting", len(members), "members (skip image_anno.csv) ...", flush=True)
    t0 = time.time()
    tf.extractall(SRC, members=members)
    print(f"extract done {time.time()-t0:.0f}s", flush=True)
else:
    print("already extracted", flush=True)

sys.path.insert(0, os.path.join(BASE, "dataset"))
os.chdir(os.path.join(BASE, "dataset"))
from datasets.VisA import Visa_dataset
from make_meta import metaSolver

DES = os.path.join(BASE, "dataset", "mvisa", "data", "visa")
META = os.path.join(BASE, "dataset", "mvisa", "data", "meta_visa.json")
if os.path.exists(DES):
    shutil.rmtree(DES)
t0 = time.time()
ds = Visa_dataset(SRC)
ds.make_VAND(binary=True, to_255=True, des_path_root=DES, id=0)
print(f"VAND done {time.time()-t0:.0f}s", flush=True)

runner = metaSolver(root=DES, meta_path=META, datasets="visa")
runner.run()
print("meta written", flush=True)

cats = sorted(os.listdir(DES))
n_train = sum(len(glob.glob(os.path.join(DES, c, "train", "good", "*"))) for c in cats)
n_test = sum(len(glob.glob(os.path.join(DES, c, "test", "*", "*"))) for c in cats)
print("cats:", cats, flush=True)
print(f"train_imgs={n_train} test_imgs={n_test}", flush=True)
print("PREP_DONE", flush=True)
