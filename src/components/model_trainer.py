from src.logger import logging
from src.exception import CustomException
from src.ml.model import LinearRegression
from src.utils.utils import get_features_target
from src.constants import *
from src.entity.artifact_entity import ModelTrainerArtifacts, DataTransformationArtifacts
from src.entity.config_entity import DataTransformationConfig, ModelTrainerConfig
import pandas as pd
import sys
import pickle
import os


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifacts: DataTransformationArtifacts):
        self.model_trainer_config=model_trainer_config
        self.data_transformation_artifacts=data_transformation_artifacts

    def training(self):
        try:
            logging.info("Reading the training data from the artifact")
            train_data=pd.read_csv(self.data_transformation_artifacts.train_transform_file_path)

            X_train, y_train=get_features_target(train_data,DEPENDENT_VARIABLE)

            # Initialize the model
            logging.info("Initiating model training")
            model=LinearRegression()
            model.fit(X_train.values, y_train.values)
            logging.info("Model training completed")

            return model

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_model_trainer(self):
        try:
            logging.info("Enter in the model trainer components")
            model=self.training()
            os.makedirs(self.model_trainer_config.MODEL_TRAINER_ARTIFACTS_DIR, exist_ok=True)
            with open(self.model_trainer_config.MODEL_PATH, 'wb') as file:
                pickle.dump(model, file)

            model_path=ModelTrainerArtifacts(self.model_trainer_config.MODEL_PATH)
            logging.info("Exited from model training component")

            return model_path
        except Exception as e:
            raise CustomException(e,sys)
