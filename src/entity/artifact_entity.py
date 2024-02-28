from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    raw_data_file_path: str

@dataclass
class DataTransformationArtifacts:
    train_transform_file_path: str
    test_transform_file_path: str

@dataclass
class ModelTrainerArtifacts:
    model_path: str
    
@dataclass
class ModelEvaluationArtifacts:
    evaluation_info_path: str
