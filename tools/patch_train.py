base = "C:/Users/31514/Desktop/3024/Bayes-PFL/"
p = base + "train.py"
src = open(p, encoding="utf-8").read().splitlines()
new = [
    '    if args.dataset == "visa":',
    '        # AI adaptation: within-VisA zero-shot protocol (train aux categories, validate held-out unseen)',
    '        train_product_list = ["candle", "capsules", "cashew", "chewinggum", "fryum", "macaroni1", "macaroni2"]',
    '        val_dataset_name = "visa"',
    '        val_product_list = ["pcb1", "pcb2", "pcb3", "pcb4", "pipe_fryum"]',
    '    elif args.dataset == "mvtec":',
    '        train_product_list = None',
    '        val_dataset_name = "visa"',
    '        val_product_list = ["chewinggum", "cashew", "pipe_fryum", "capsules", "candle"]',
    '    else:',
    '        train_product_list = None',
    '        val_dataset_name = "mvtec"',
    '        val_product_list = ["bottle", "hazelnut", "wood", "zipper", "leather"]',
    '    post_dataloader, post_obj_list = Make_dataset.mask_dataset(name=args.dataset, batchsize=args.batch_size, product_list=train_product_list, shuf=True)',
    '    val_post_dataloader, val_obj_list_post = Make_dataset_val_post.mask_dataset(name=val_dataset_name, product_list=val_product_list, batchsize=1, shuf=False)',
]
src[169:180] = new
open(p, "w", encoding="utf-8").write(chr(10).join(src) + chr(10))
print("patched train.py")
