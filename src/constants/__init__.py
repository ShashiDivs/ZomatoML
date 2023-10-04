import os, sys
from datetime import datetime

#artifact -> pipelinefolder -> timestamp -> output

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"


CURRENT_TIME_STAMP = get_current_time_stamp()
ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finaltrain.csv"

ARTIFACT_DIR_KEY = "Artifact"

#Data ingestion related variables
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_IMGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"


#Data transformation related variables
DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORMATION_DIR = "trnasformation"
TRANSFORMATION_TRAIN_DIR_KEY = "train.csv"
TRANSFORMATION_TEST_DIR_KEY = "test.csv"


#artifact / data_transformation /processor->processor.pkl-> and transforamtion
#train.csv and test.csv



