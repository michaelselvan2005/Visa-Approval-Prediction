from us_visa.pipeline.training_pipeline import TrainPipeline
from us_visa.logger import logging


logging.info("Welcome to our Project")


pipline  = TrainPipeline()
pipline.run_pipeline()