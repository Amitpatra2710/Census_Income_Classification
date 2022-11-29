import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://amitpatra:amit27@cluster0.cqlj9.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH="D:/AreaZ/ML/Projects/Census_Income_Classification/Census_Income_Classification/adult.csv"
DATABASE_NAME="cip"
COLLECTION_NAME="census"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)