from src.exception import CustomException
from src.logger import logging
from src.constants import *
from src.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts
from src.entity.config_entity import DataTransformationConfig
from src.utils.utils import date_modify, data_split, get_features_target
from src.ml.standardization import DataStandardizer

import pandas as pd
import numpy as np
import os
import sys

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifacts: DataIngestionArtifacts):
        self.data_transformation_config=data_transformation_config
        self.data_ingestion_artifacts=data_ingestion_artifacts
    
    def data_transform(self):
        try:
            logging.info("Fetching data from the ingested location")
            df=pd.read_csv(self.data_ingestion_artifacts.raw_data_file_path)

            # Rename the column for readability
            logging.info("Column mapping ")
            df.rename(columns=COLUMN_MAPPING, inplace=True)

            # Drop irrelevant columns
            logging.info("Dropping unnecessary columns")
            df.drop(COLUMNS_TO_DROP, axis=1, inplace=True)
            
            # Transform date column
            logging.info("Transforming the data column")
            df['Transaction date']=df['Transaction date'].apply(date_modify)

            # Split dataset
            logging.info("Split dataset into train and test")
            train_data, test_data=data_split(df,test_size_percentage=TEST_SIZE_PERCENTAGE)

            # Transform the data
            logging.info("Transforming data set")
            scaler=DataStandardizer()
            # Leaving the date column and target column
            transformed_train_data=scaler.fit_transform(train_data.iloc[:,1:-1])
            transformed_test_data=scaler.transform(test_data.iloc[:,1:-1])

            # Concat the transformed feature with target
            logging.info("Concat the transformed feature with target")
            transformed_train_data=pd.concat([transformed_train_data, train_data[DEPENDENT_VARIABLE]], axis=1)
            transformed_test_data=pd.concat([transformed_test_data, test_data[DEPENDENT_VARIABLE]], axis=1)
            logging.info("Data transformation completed")

            return df,transformed_train_data, transformed_test_data
        except Exception as e:
            raise CustomException(e, sys)



    def initiate_data_transform(self):
        try:

            logging.info("Enter in the data transformation components")
            df,transformed_train_data, transformed_test_data=self.data_transform()

            os.makedirs(self.data_transformation_config.DATA_TRANSFORM_ARTIFACTS_DIR, exist_ok=True)
            df.to_csv(self.data_transformation_config.TRANSFORMED_FILE_PATH,index=False,header=True)
            transformed_train_data.to_csv(self.data_transformation_config.TRAIN_TRANSFORMED_FILE_PATH,index=False,header=True)
            transformed_test_data.to_csv(self.data_transformation_config.TEST_TRANSFORMED_FILE_PATH,index=False,header=True)

            data_transformation_artifacts=DataTransformationArtifacts(
                train_transform_file_path=self.data_transformation_config.TRAIN_TRANSFORMED_FILE_PATH,
                test_transform_file_path=self.data_transformation_config.TEST_TRANSFORMED_FILE_PATH
            )
            logging.info("Exited from the data transformation components")
            return data_transformation_artifacts

        except Exception as e:
            raise CustomException(e, sys)
        







if __name__=="__main__":
    obj=DataTransformation(DataTransformationConfig(),DataIngestionArtifacts)
    obj.data_transform()