from src.logger import logging
from src.exception import CustomException
from src.constants import *
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifacts

class DataIngestion:
    def __init__(self, ingestion_config: DataIngestionConfig):
        self.ingestion_config=ingestion_config

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the data ingestion component ")
        try:
            # Reading the data from the source
            df=pd.read_csv('data/Real-estate.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(self.ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
            df.to_csv(self.ingestion_config.NEW_DATA_ARTIFACTS_DIR, index=False, header=True)

            data_ingestion_artifacts = DataIngestionArtifacts(
                raw_data_file_path=self.ingestion_config.NEW_DATA_ARTIFACTS_DIR
            )
            
            logging.info("Data ingested (saved) successfully")
            
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion(DataIngestionConfig())
    obj.initiate_data_ingestion()