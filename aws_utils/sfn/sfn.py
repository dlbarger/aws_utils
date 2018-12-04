"""
Package:    aws_utils
Module:     aws_utils.sfn
Created:    12/3/2019
"""

import pandas as pd
import numpy as np
import boto3
import json

def describeSfnExec(boto_client, execution_arn):
    '''
    Describes execution, including status, of previous aws state machine
    execution.

    Parameters:
    -   boto_client = instantiated aws boto3 client
    -   execution_arn = Arn of specific state machine execution

    Return Values:
    {
        'executionArn': 'string',
        'stateMachineArn': 'string',
        'name': 'string',
        'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
        'startDate': datetime(2015, 1, 1),
        'stopDate': datetime(2015, 1, 1),
        'input': 'string',
        'output': 'string'
    }

    '''
    try:
        response = boto_client.describe_execution(executionArn = execution_arn)

        return {
            "status_code": 400,
            "body": response
        }

    except Exception as e:
        return {
            "status_code": 200,
            "body": json.dumps(e)
        }
