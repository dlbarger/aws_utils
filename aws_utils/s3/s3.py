"""
Package:    aws_utils
Module:     aws_utils.s3
Created:    12/3/2019
"""

import pandas as pd
import numpy as np
import boto3
import json

def getDFS3Object(bucket, key):
    """
    Read S3 object and return data frame

    Parameters:
    -   bucket = target S3 bucket
    -   key = target S3 object

    Return Values:
    -   data frame representing contents of target S3 object.
    """

    try:
        s3 = boto3.client('s3')
        obj = s3.get_object(
            Bucket = bucket,
            Key = key
        )
        df = pd.read_csv(obj['Body'])

        if isinstance(df, pd.DataFrame):
            return(df)
        else:
            return {
                "status_code": 400,
                "body": "Failed to read S3 object"
            }
    except Exception as e:
        return {
            "status_code": 400,
            "body": json.dumps(e)
        }
