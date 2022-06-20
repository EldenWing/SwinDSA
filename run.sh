


#Vaihingen 
python tools/test.py configs/psanet/my_psanet_concat234_reduce_80k.py   work_dirs/vaihingen/my_psanet_concat234_reduce_80k/iter_28000.pth   --show-dir work_dirs/vaihingen_output/my_psanet_chapter4  --opacity 1

python tools/test.py configs/psanet/my_psanet_concat234_reduce_80k.py   work_dirs/vaihingen/my_psanet_concat234_reduce_80k/iter_28000.pth --eval mFscore mIoU  --opacity 1


#Potsdam 
#python tools/test.py configs/psanet/my_psanet_concat234_reduce_80k.py   work_dirs/potsdam/my_psanet_concat234_reduce_80k/iter_56000.pth   --show-dir work_dirs/potsdam_output/my_psanet_chapter4  --opacity 1

#python tools/test.py configs/psanet/my_psanet_concat234_reduce_80k.py   work_dirs/potsdam/my_psanet_concat234_reduce_80k/iter_56000.pth --eval mFscore mIoU  --opacity 1



#Potsdam 
#python tools/test.py configs/psanet/my_psanet_concat234_reduce_80k.py   work_dirs/potsdam/my_psanet_swin_80k/iter_56000.pth   --show-dir work_dirs/potsdam_output/my_psanet_chapter3  --opacity 1

#python tools/test.py configs/psanet/my_psanet_concat234_reduce_80k.py   work_dirs/potsdam/my_psanet_swin_80k/iter_56000.pth --eval mFscore mIoU  --opacity 1






