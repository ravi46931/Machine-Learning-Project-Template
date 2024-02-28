from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from src.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from src.constants import *

if __name__ == "__main__":
    obj=DataIngestion(DataIngestionConfig())
    data_ingestion_artifacts=obj.initiate_data_ingestion()

    obj2=DataTransformation(DataTransformationConfig(),data_ingestion_artifacts)
    data_transformation_artifacts=obj2.initiate_data_transform()

    obj3=ModelTrainer(ModelTrainerConfig(),data_transformation_artifacts)
    model_path=obj3.initiate_model_trainer()
    
    obj4=ModelEvaluation(ModelEvaluationConfig(), model_path, data_transformation_artifacts)
    accuracy=obj4.initiate_model_evaluation()



    


