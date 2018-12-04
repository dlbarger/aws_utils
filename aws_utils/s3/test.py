"""
Script:     s3_test.py
Author:     Dennis Barger
Created:    12/3/2018

Description:
Test harness for validating s3.py.

User Credentials:
Defined as environment variables
"""

import s3
import pandas as pd

BUCKET = 'aws-ca-ds'
KEY = 'dbarger/dsCloud9Prototype/data/iris.csv'

df = s3.getDFS3Object(BUCKET, KEY)

if isinstance(df, pd.DataFrame):
    print(df)
else:
    print('Empty Data Frame')
