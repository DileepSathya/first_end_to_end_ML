from src.MLOPS import logger
from src.MLOPS.pipeline.Data_ingestion import data_ingestion_pipeline

STAGE="Data_Ingestion_phase"

try:
    logger.info(f"-----{STAGE}-----")
    data_ingestion=data_ingestion_pipeline
    data_ingestion.data_ingestion()
    logger.info(f"{STAGE} sucessful")
except Exception as e:
    logger.exception(e)
    raise e




