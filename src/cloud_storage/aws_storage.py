import os
import sys

from src.exception.expection import CustomException


class S3Operation:
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:  # upload
        try:
            command: str = (
                f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ "
            )

            os.system(command)

        except Exception as e:
            raise CustomException(e, sys)

    def sync_folder_from_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:  # download
        try:
            command: str = (
                f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder} "
            )

            os.system(command)

        except Exception as e:
            raise CustomException(e, sys)