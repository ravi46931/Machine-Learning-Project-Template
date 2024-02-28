from src.logger import logging
from src.exception import CustomException
from src.ml.model import LinearRegression
import pickle
import os
import pandas as pd
import sys
import json
from src.constants import *
from src.utils.utils import get_features_target
from src.entity.artifact_entity import ModelTrainerArtifacts, DataTransformationArtifacts, ModelEvaluationArtifacts
from src.entity.config_entity import ModelEvaluationConfig
from src.ml.metrice import mae, mse, rmse, r2_score, adjusted_r2_score, mape, med_ae

class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig, model_trainer_artifacts: ModelTrainerArtifacts, data_transformation_artifacts: DataTransformationArtifacts):
        self.model_evaluation_config=model_evaluation_config
        self.model_trainer_artifacts=model_trainer_artifacts
        self.data_transformation_artifacts=data_transformation_artifacts


    def evaluation(self):
        try:
            logging.info("Loading the model...")
            with open(self.model_trainer_artifacts.model_path, 'rb') as file:
                model = pickle.load(file)

            test_data=pd.read_csv(self.data_transformation_artifacts.test_transform_file_path)
            X_test, y_test=get_features_target(test_data,DEPENDENT_VARIABLE)
            
            # Prediction on test data
            logging.info("Model evaluation started")
            y_pred=model.predict(X_test.values)

            MAE=mae(y_test, y_pred)
            MSE=mse(y_test, y_pred)
            RMSE=rmse(y_test, y_pred)
            R2_SCORE=r2_score(y_test, y_pred)
            ADJUSTED_R2_SCORE=adjusted_r2_score(y_test, y_pred, X_test)
            MAPE=mape(y_test, y_pred)
            MED_AE=med_ae(y_test, y_pred)
            logging.info("Model evaluation completed")
            
            accuracy_score={
                'MAE':MAE,
                'MSE':MSE,
                'RMSE':RMSE,
                'R2_SCORE':R2_SCORE,
                'ADJUSTED_R2_SCORE':ADJUSTED_R2_SCORE,
                'MAPE':MAPE,
                'MED_AE':MED_AE
            }

            return accuracy_score
            
        except Exception as e:
            raise CustomException(e, sys)
        
    
    def initiate_model_evaluation(self):
        try:
            logging.info("Enter in the model evaluation components")
            accuracy_score=self.evaluation()
            os.makedirs(self.model_evaluation_config.MODEL_EVALUATION_ARTIFACTS_DIR, exist_ok=True)

            with open(self.model_evaluation_config.ACCURACY_FILE_PATH, 'w') as json_file:
                json.dump(accuracy_score, json_file)

            accuracy_file_path=ModelEvaluationArtifacts(self.model_evaluation_config.ACCURACY_FILE_PATH)

            logging.info("Exited from the model evaluation components")

            return accuracy_file_path

        except Exception as e:
            raise CustomException(e, sys)
