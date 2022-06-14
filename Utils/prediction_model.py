#!pip uninstall -y torchtext
#!pip install 'icevision' 'lightning-flash[image]'

import torch
import flash
from flash.image import ImageClassificationData, ImageClassifier, ImageEmbedder
from flash import Trainer

#from torchmetrics import F1Score
import torch.nn.functional as F
import numpy as np
import albumentations as A
from albumentations.pytorch import ToTensorV2
import timm
from torchmetrics.functional import accuracy
import os
from torchvision import transforms as T
from typing import Callable, Tuple, Union
from flash.core.data.io.input_transform import InputTransform
from dataclasses import dataclass

base_model = "dla60x_c"

def model(train_files, val_files, test_files, base_model,predict_files):
    """
    We are using the ImageClassificationData class from FlashTorch to load the data from the folders we
    created earlier. We are using the ImageClassifier class from FlashTorch to create the model. We are
    using the Trainer class from FlashTorch to train the model. We are saving the model as
    Imageclassifier.pt
    
    :param train_files: The path to the training files
    :param val_files: The path to the validation files
    :param test_files: The path to the test files
    :param base_model: This is the model that you want to use. You can choose from a list of models that
    are available in the flash library
    :param predict_files: This is the folder where the images you want to predict are located
    :return: The model is being saved in the current directory.
    """
    @dataclass
    class ImageClassificationInputTransform(InputTransform):
        """Custom image transformations and augmentations"""

        image_size: Tuple[int, int] = (224, 224)
        mean: Union[float, Tuple[float, float, float]] = (0.485, 0.456, 0.406)
        std: Union[float, Tuple[float, float, float]] = (0.229, 0.224, 0.225)

        def input_per_sample_transform(self):
                return T.Compose([T.ToTensor(), T.Resize(self.image_size), T.Normalize(self.mean, self.std)])

        def train_input_per_sample_transform(self):
            return T.Compose(
                [
                    T.ToTensor(),
                    T.Resize(self.image_size),
                    T.Normalize(self.mean, self.std),
                    T.RandomHorizontalFlip(),
                    T.ColorJitter(),
                    T.RandomAutocontrast(),
                    T.RandomPerspective(),
                    ]
                )

        def target_per_sample_transform(self) -> Callable:
            return torch.as_tensor
            
    datamodule = ImageClassificationData.from_folders(
                train_folder="../input/cleaned-archive/archive_cleaned/vinted_train",
                val_folder="../input/cleaned-archive/archive_cleaned/vinted_val",
                test_folder="../input/cleaned-archive/archive_cleaned/vinted_test_only",
                predict_folder="../input/cleaned-archive/archive_cleaned/vinted_test_only",
                train_transform= ImageClassificationInputTransform,
                transform_kwargs=dict(image_size=(224, 224)),
                batch_size=128,
                num_workers=48,
            )

    model = ImageClassifier(backbone=base_model, 
                        labels=datamodule.labels,
                        multi_label=datamodule.multi_label,
                        num_classes=datamodule.num_classes,
                        pretrained=True,
                        #metrics=metrics
                       )

    trainer = flash.Trainer(max_epochs=16, gpus=torch.cuda.device_count(), precision=32,)
    trainer.finetune(model, datamodule=datamodule, strategy=("freeze_unfreeze", 8))
    trainer.save_checkpoint("./Imageclassifier.pt")
    return "Model has been saved"

def prediction(predict_files, saved_model):
    """
    It takes in a list of files to predict on, and a saved model, and returns a list of predictions
    
    :param predict_files: The path to the folder containing the images you want to predict on
    :param saved_model: The path to the saved model
    """

    trainer = Trainer()
    datamodule = ImageClassificationData.from_files(
    predict_files=predict_files,
    batch_size=1,
    num_workers=6,
    transform_kwargs={"image_size": (224, 224), "mean": (0.485, 0.456, 0.406), "std": (0.229, 0.224, 0.225)},
    )
    model = ImageClassifier.load_from_checkpoint(saved_model)
    predictions = trainer.predict(model, datamodule=datamodule, output="labels")
    return predictions
