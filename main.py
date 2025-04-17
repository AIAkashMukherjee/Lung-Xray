 
from src.logger.custom_logging import logger
from src.exception.expection import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionPipe
# from src.pipline.stage_02_data_val_pipe import DataValidationPipe
# from src.pipline.stage_03_data_transformation import DataTransfromPipe
# from src.pipline.stage_04_model_trainer_pipe import ModelTrainerPipe
# from src.pipline.stage_05_model_Eval_pipe import ModelEvalPipe
# from src.pipline.stage_06_model_pusher_pipe import ModelPusherPipe
import sys

# class TrainPipeline:
#     def run_pipeline(self):
        # try:
        #     def run_stage(stage_name, pipeline_class, *args):
        #         logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        #         pipeline = pipeline_class(*args)
        #         artifact = pipeline.main()
        #         logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
        #         return artifact

        #     data_ingestion_artifact = run_stage("Data Ingestion", DataIngestionPipe)
        #     # data_validation_artifact = run_stage("Data Validation", DataValidationPipe, data_ingestion_artifact)
        #     # data_transformation_artifact = run_stage("Data Transformation", DataTransfromPipe, data_ingestion_artifact, data_validation_artifact)
        #     # model_trainer_artifact = run_stage("Model Trainer", ModelTrainerPipe, data_transformation_artifact)
        #     # model_eval_artifact = run_stage("Model Evaluation", ModelEvalPipe, data_ingestion_artifact, model_trainer_artifact)
        #     # model_pusher_artifact = run_stage("Model Pusher", ModelPusherPipe, model_eval_artifact)

        # except Exception as e:
        #     logger.exception(e)
        #     raise CustomException(e, sys) 

def run_stage(stage_name, pipeline_class,*args):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline = pipeline_class(*args)
        artifact=pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
        return artifact
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)
    
if __name__ == "__main__":
 
    # Stage 1: Data Ingestion
    data_ingestion_artifact = run_stage("Data Ingestion", DataIngestionPipe)        