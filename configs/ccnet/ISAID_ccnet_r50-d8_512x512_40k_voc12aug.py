_base_ = [
    '../_base_/models/ccnet_r50-d8.py',
    '../_base_/datasets/pascal_voc12.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
model = dict(
    decode_head=dict(num_classes=16), auxiliary_head=dict(num_classes=16),
    test_cfg=dict(mode='slide',crop_size=(500,500),stride=(500,500)))
