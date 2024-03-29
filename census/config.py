import pymongo
import pandas as pd
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.
import os
@dataclass
class EnvironmentVariable:
    print(os.getenv('MONGO_DB_URL'))
    mongo_db_url:str = os.getenv('MONGO_DB_URL')
    #aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    #aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")


env_var = EnvironmentVariable()
print(env_var.mongo_db_url)
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "income"