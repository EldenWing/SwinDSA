# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class PascalVOCDataset(CustomDataset):
    """Pascal VOC dataset.

    Args:
        split (str): Split txt file for Pascal VOC.
    

    CLASSES = ('background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
               'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog',
               'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
               'train', 'tvmonitor')

    PALETTE = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128],
               [128, 0, 128], [0, 128, 128], [128, 128, 128], [64, 0, 0],
               [192, 0, 0], [64, 128, 0], [192, 128, 0], [64, 0, 128],
               [192, 0, 128], [64, 128, 128], [192, 128, 128], [0, 64, 0],
               [128, 64, 0], [0, 192, 0], [128, 192, 0], [0, 64, 128]]
    """
    #Potsdam
    #CLASSES = ('Impervious surfaces', 'Building', 'Low vegetation', 'Tree', 'Car')
    #PALETTE = [[255, 255, 255],[0, 0,255], [0,255, 255], [0,255, 0],[255, 255, 0]]

    CLASSES = ('ClutterBackground ','Impervious surfaces', 'Building', 'Low vegetation', 'Tree', 'Car')
    PALETTE = [[255,0,0],[255, 255, 255],[0, 0,255], [0,255, 255], [0,255, 0],[255, 255, 0]]  
    
    #CLASSES = ('Other ','Tree', 'Road', 'Building', 'Water')
    #PALETTE = [[255,255,255],[0, 255, 0],[0, 0, 0], [139,139,131], [19,69,139]] 
   
    #cp
    #CLASSES =('Urban land','Agriculture land', 'Rangeland', 'Forest land', 'Water', 'Barren land','Unknown')
    #PALETTE =[[0,255,255],[255,255,  0],[255,  0,255],[ 0,255,  0],[0,  0,255],[255,255,255],[0,  0,  0]]
    #CLASSES =('background','ship', 'storage_tank', 'baseball_diamond', 'tennis_court', 'basketball_court','ground_Track_Field','bridge','large_Vehicle', 'small_Vehicle', 'helicopter', 'swimming_pool', 'roundabout','soccer_ball_field','plane','harbor')
    #PALETTE =[[0, 0, 0],[0, 0, 63],[0, 191, 127],[0, 63, 0],[0, 63, 127],[0, 63, 191],[0, 63, 255],[0, 127, 63],[0, 127, 127],[0, 0, 127],[0, 0, 191],[0, 0, 255],[0, 63, 63],[0, 127, 191],[0, 127, 255],[0, 100, 155]]


    def __init__(self, split, **kwargs):
        super(PascalVOCDataset, self).__init__(
            img_suffix='.png', seg_map_suffix='.png', split=split, **kwargs)
        assert osp.exists(self.img_dir) and self.split is not None
