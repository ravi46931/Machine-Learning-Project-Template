
# common constants
ARTIFACTS='artifacts'

# Data Ingestion constant
RAW_FILE_NAME='data.csv'
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"


# Data Transformation constant
DATA_TRANSFORM_ARTIFACTS_DIR = "DataTransformationArtifacts"
TRANSFORMED_FILE_NAME='final.csv'
TRAIN_TRANSFORMED_FILE_NAME="train.csv"
TEST_TRANSFORMED_FILE_NAME="test.csv"
COLUMNS_TO_DROP=['No']
COLUMN_MAPPING={
                'X1 transaction date':'Transaction date', 
                'X2 house age':'House age',
                'X3 distance to the nearest MRT station': 'Distance',
                'X4 number of convenience stores': 'No. of Stores',
                'X5 latitude':'Latitude',
                'X6 longitude':'Longitude',
                'Y house price of unit area':'Price'
            }
TEST_SIZE_PERCENTAGE=0.2
DEPENDENT_VARIABLE='Price'

# Model Trainer constant
MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"
MODEL_FILE_NAME='model.pkl'
ITERATION=100
ALPHA=0.11

# Model Evaluation constant
MODEL_EVALUATION_ARTIFACTS_DIR="ModelEvaluationArtifacts"
ACCURACY_FILE_NAME='accuracy.json'