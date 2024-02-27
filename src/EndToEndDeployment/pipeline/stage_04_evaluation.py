from EndToEndDeployment.config import ConfigurationManager
from EndToEndDeployment.components import Evaluation
from EndToEndDeployment import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
            