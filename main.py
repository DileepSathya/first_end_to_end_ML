from src.MLOPS import logger
from src.MLOPS.pipeline.Data_ingestion import data_ingestion_pipeline
from src.MLOPS.pipeline.Data_transformation import DataTransformationPipeline
def data_ingestion():
    STAGE="Data_Ingestion_phase"

    try:
        logger.info(f"-----{STAGE}-----")
        data_ingestion=data_ingestion_pipeline
        data_ingestion.data_ingestion()
        logger.info(f"{STAGE} sucessful")
    except Exception as e:
        logger.exception(e)
        raise e

def data_transform():
    STAGE="Data_Transformation_phase"
    try:
        logger.info(f"-----{STAGE}-----")
        data_transformation=DataTransformationPipeline
        data_transformation.data_transformation()
        logger.info(f"{STAGE} sucessful")
    except Exception as e:
        logger.exception(e)
        raise e


if __name__=="__main__":
    data_transform()