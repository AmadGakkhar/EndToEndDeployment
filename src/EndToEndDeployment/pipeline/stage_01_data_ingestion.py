from EndToEndDeployment.config import ConfigurationManager
from EndToEndDeployment.components import DataIngestion
from EndToEndDeployment import logger

class TrainingPipeline():
    def __init__(self):
        pass
    def main():
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()