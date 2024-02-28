# Data Ingestion component done

Fetched data from the data/real-state.csv and save into artifacts/DataIngestionArtifacts/data.csv

Steps covered: 
    constants: Data Ingestion constants (2 constants)
    config entity: DataIngestionConfig class (2 components)
    artifacts entity: DataIngestionArtifacts class (raw_data_file_path, location of the dataset that        are fetched from the source and saved into artifacts/DataIngestionArtifacts/data.csv)
    components: data ingestion - write the code that fetched the data from the source (data/Real-estate.csv) and save the data into the given location (artifacts/DataIngestionArtifacts/data.csv) and fetched the data path 
## Till here the code working fine


# Data Ingestion, Data Transformation, Model Trainer, Model Evaluation are done and running and produce artifacts

RUN: `python src\pipeline\train_pipeline.py` command on activating the env, this runs perfectly and the accuracy save into the *accuracy.json* file.

artifacts and Logs are generated during the running 

Code is saved on GitHub: https://github.com/ravi46931/Machine-Learning-Project-Template/

 