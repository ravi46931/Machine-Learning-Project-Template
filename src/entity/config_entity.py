import os
from dataclasses import dataclass
from src.constants import *


@dataclass
class DataIngestionConfig:
        DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS,DATA_INGESTION_ARTIFACTS_DIR)
        NEW_DATA_ARTIFACTS_DIR: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR,RAW_FILE_NAME)


@dataclass
class DataTransformationConfig:
        DATA_TRANSFORM_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS,DATA_TRANSFORM_ARTIFACTS_DIR)
        TRANSFORMED_FILE_PATH = os.path.join(DATA_TRANSFORM_ARTIFACTS_DIR,TRANSFORMED_FILE_NAME)
        TRAIN_TRANSFORMED_FILE_PATH: str = os.path.join(DATA_TRANSFORM_ARTIFACTS_DIR, TRAIN_TRANSFORMED_FILE_NAME)
        TEST_TRANSFORMED_FILE_PATH: str = os.path.join(DATA_TRANSFORM_ARTIFACTS_DIR, TEST_TRANSFORMED_FILE_NAME)


@dataclass
class ModelTrainerConfig:
        MODEL_TRAINER_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS,MODEL_TRAINER_ARTIFACTS_DIR)
        MODEL_PATH = os.path.join(MODEL_TRAINER_ARTIFACTS_DIR,MODEL_FILE_NAME)


@dataclass
class ModelEvaluationConfig:
        MODEL_EVALUATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS,MODEL_EVALUATION_ARTIFACTS_DIR)
        ACCURACY_FILE_PATH = os.path.join(MODEL_EVALUATION_ARTIFACTS_DIR,ACCURACY_FILE_NAME)