## Data Ingestion Pipeline
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.logging import logger



STAGE_NAME = "Data Ingestion Satge"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingetsion = DataIngestion(config=data_ingestion_config)
            data_ingetsion.download_file()
            data_ingetsion.extract_zip_file()
        except Exception as e:
            raise e



if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    