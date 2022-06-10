#!pip uninstall -y torchtext
#!pip install 'icevision' 'lightning-flash[image]'

import torch
import flash
from flash.image import ImageClassificationData, ImageClassifier, ImageEmbedder
from flash import Trainer

#from torchmetrics import F1Score
import torch.nn.functional as F
import numpy as np
# import albumentations as A
# from albumentations.pytorch import ToTensorV2
# import timm

from torchmetrics.functional import accuracy
import os

base_model = "dla60x_c"

def model(train_files, val_files, test_files, base_model, predict_files):
    """
    We are creating a model from the ImageClassificationData class, which is a subclass of the
    DataModule class. We are passing in the train, validation, and test folders, as well as the base
    model we want to use. We are also passing in the batch size and the number of workers. 
    
    We are then creating a model from the ImageClassifier class, which is a subclass of the
    LightningModule class. We are passing in the base model, the labels, the number of classes, and the
    pretrained parameter. 
    
    We are then creating a trainer from the Trainer class, which is a subclass of the Trainer class. We
    are passing in the max epochs, the number of GPUs, and the precision. 
    
    We are then finetuning the model, passing in the model, the datamodule, and the strategy. 
    
    We are then saving the model.
    
    :param train_files: The path to the folder containing the training images
    :param val_files: The path to the validation folder
    :param test_files: The path to the folder containing the test images
    :param base_model: This is the model that you want to use. You can choose from a list of models that
    are available in the flashtorch library
    :param predict_files: This is the folder where the images you want to predict are stored
    :return: The model is being saved in the current directory.
    """
    datamodule = ImageClassificationData.from_folders(
        train_folder=train_files,
        val_folder=val_files,
        test_folder=test_files,
        predict_folder=predict_files,
        transform_kwargs={"image_size": (224, 224)},
        batch_size=128,
        num_workers=48
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

    trainer = Trainer(max_epochs=1, gpus=torch.cuda.device_count())
    datamodule = ImageClassificationData.from_files(
        predict_files=predict_files,
        batch_size=1,
        num_workers=4,
        transform_kwargs={"image_size": (224, 224), "mean": (0.485, 0.456, 0.406), "std": (0.229, 0.224, 0.225)},
    )
    model = ImageClassifier.load_from_checkpoint(saved_model)
    predictions = trainer.predict(model, datamodule=datamodule, output="labels")
    return predictions
