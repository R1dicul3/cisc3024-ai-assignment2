base = "C:/Users/31514/Desktop/3024/Bayes-PFL/"
p = base + "test.py"
src = open(p, encoding="utf-8").read().splitlines()
src[119] = '    test_dataloader, obj_list = Make_dataset_test.mask_dataset(name = dataset_name, product_list= args.product_list, batchsize = 1, shuf= False)'
src.insert(197, '    parser.add_argument("--product_list", type=str, nargs="+", default=None, help="categories to evaluate (None = all)")')
open(p, "w", encoding="utf-8").write(chr(10).join(src) + chr(10))
print("patched test.py")
