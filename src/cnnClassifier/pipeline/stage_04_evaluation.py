## Data Ingestion Pipeline
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.evaluation import Evaluation
from src.cnnClassifier.logging import logger




STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            config = ConfigurationManager()
            val_config = config.get_validation_config()
            evaluation = Evaluation(config=val_config)
            evaluation.evaluation()
            evaluation.save_score()
        except Exception as e:
            raise e




if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    