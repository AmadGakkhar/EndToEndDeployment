from EndToEndDeployment.pipeline import DataIngestionTrainingPipeline
from EndToEndDeployment import logger

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"<<<<<< STAGE NAME : {STAGE_NAME} >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
except Exception as e:
    logger.exception(e)