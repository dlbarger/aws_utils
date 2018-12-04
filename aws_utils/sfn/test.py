"""
Script:     s3_test.py
Author:     Dennis Barger
Created:    12/3/2018

Description:
Test harness for validating s3.py.

User Credentials:
Defined as environment variables
"""

import sfn
import pandas as pd
import boto3

BUCKET = 'aws-ca-ds'
KEY = 'dbarger/dsCloud9Prototype/data/iris.csv'
EXEC_ARN = 'arn:aws:states:us-east-1:678977883400:execution:dsCloud9PrototypeStateMachine-j3lp72wQLpfz:cd32f24e-c038-8e38-8aa7-a6e1ac396691'

client = boto3.client('stepfunctions')
response = sfn.describeSfnExec(client, EXEC_ARN)

print(response)
