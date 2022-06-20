_base_ = [
    '../_base_/models/pspnet_swin.py',
    '../_base_/datasets/pascal_voc12_aug.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_20k.py'
]


model = dict(
    pretrained='/root/newmmsegmentation/pretrain/swin_small_patch4_window7_224.pth',
    backbone=dict(
        embed_dims=96,
        depths=[2, 2, 18, 2],
        num_heads=[3, 6, 12, 24],
        window_size=7,
        use_abs_pos_embed=False,
        drop_path_rate=0.3,
        patch_norm=True),
   # decode_head=dict(shrink_factor=1))
    decode_head=dict(num_classes=5), auxiliary_head=dict(num_classes=5))




