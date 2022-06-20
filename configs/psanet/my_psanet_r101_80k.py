_base_ = [
    '../_base_/models/psanet_r50-d8.py',
    '../_base_/datasets/pascal_voc12_aug.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_80k.py'
]


model = dict(
    pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101),
    decode_head=dict(num_classes=6), auxiliary_head=dict(num_classes=6))
