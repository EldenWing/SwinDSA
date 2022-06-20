

## Introduction

We use the [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) as the framework

## Installation

Please refer to [get_started.md](docs/get_started.md#installation) for installation and [dataset_prepare.md](docs/dataset_prepare.md#prepare-datasets) for dataset preparation.

## Get Started

Please see [train.md](docs/train.md) and [inference.md](docs/inference.md) for the basic usage of MMSegmentation.
There are also tutorials for [customizing dataset](docs/tutorials/customize_datasets.md), [designing data pipeline](docs/tutorials/data_pipeline.md), [customizing modules](docs/tutorials/customize_models.md), and [customizing runtime](docs/tutorials/customize_runtime.md).
We also provide many [training tricks](docs/tutorials/training_tricks.md) for better training and [useful tools](docs/useful_tools.md) for deployment.


## Dataset 

You can get dataset [here](https://www.isprs.org/education/benchmarks/UrbanSemLab/default.aspx)


## Pretrain Model

Pretrain Model can be downloaded [here](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth).
And you can use [swin2mmseg.py](https://github.com/open-mmlab/mmsegmentation/blob/master/tools/model_converters/swin2mmseg.py) to convert it to mmseg format.
