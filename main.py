from src.MLOPS import logger
from src.MLOPS.pipeline.Data_ingestion import data_ingestion_pipeline
from src.MLOPS.pipeline.Data_transformation import DataTransformationPipeline
from src.MLOPS.pipeline.feature_engineering import feature_engineering_pipeline
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


def feature_eng():
    STAGE="Featue_engineeing_phase"
    try:
        logger.info(f"-------{STAGE}--------")
        feat_eng=feature_engineering_pipeline
        feat_eng.feature_engineering()
        logger.info(f"{STAGE} successful")
    except Exception as e:
        logger.exception(e)
        raise e
if __name__=="__main__":
    feature_eng()