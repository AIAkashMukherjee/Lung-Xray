from dotenv import load_dotenv
from typing import List
from datetime import datetime
import os
load_dotenv()
uri = os.getenv('MONGODB_URI')




AWS_BUCKET_NAME='lung-xray-yt'
MONGODB_URI=uri
db_name='akash'
DATABASE_NAME='lung_xray_db'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO=.20
collection_name="fs.files"
training_image_dir="artifacts/data/train"
validation_image_dir="artifacts/data/validation"
TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Data Ingestion Constants
ARTIFACT_DIR: str = "artifacts"


# data trasnforamtion
CLASS_LABEL_1: str = "NORMAL"

CLASS_LABEL_2: str = "PNEUMONIA"

BRIGHTNESS: int = 0.10

CONTRAST: int = 0.1

SATURATION: int = 0.10

HUE: int = 0.1

RESIZE: int = 224

CENTERCROP: int = 224

RANDOMROTATION: int = 10

NORMALIZE_LIST_1: List[int] = [0.485, 0.456, 0.406]

NORMALIZE_LIST_2: List[int] = [0.229, 0.224, 0.225]

TRAIN_TRANSFORMS_KEY: str = "xray_train_transforms"

TRAIN_TRANSFORMS_FILE: str = "train_transforms.pkl"

TEST_TRANSFORMS_FILE: str = "test_transforms.pkl"

BATCH_SIZE: int = 2

SHUFFLE: bool = False

PIN_MEMORY: bool = True

