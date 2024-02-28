import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files=[
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/ml/__init__.py",
    "src/ml/model.py",
    "src/ml/metrics.py",
    "src/ml/standardization.py",
    "src/constants/__init__.py",
    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/entity/artifact_entity.py",
    "src/logger/__init__.py",
    "src/exception/__init__.py",
    "requirements.txt",
    "app.py",
    "main.py",
    "demo.py",
    "README.md",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)
    print(os.path.split(filepath))

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        pass
            
