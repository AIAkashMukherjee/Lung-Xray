import os
from dataclasses import dataclass

from torch import device

from src.constants import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.collection_name = collection_name
        self.train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.training_image_dir = training_image_dir
        self.validation_image_dir = validation_image_dir
        
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)

        self.data_path: str = os.path.join(self.artifact_dir, "data_ingestion")

        self.train_data_path: str = os.path.join(self.data_path, "train")

        self.val_data_path: str = os.path.join(self.data_path, "validation")

        # self.data_path: str = os.path.join(
        #     self.artifact_dir, "data_ingestion", self.s3_data_folder
        # )

        # self.train_data_path: str = os.path.join(self.data_path, "train")

        # self.test_data_path: str = os.path.join(self.data_path, "test")

        # train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        # collection_name:str = DATABASE_NAME