import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME='aps' # Air Pressure System
COLLECTION_NAME='sensor'

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")
    
    #convert datafram to JSON so that we can dump these record in MongoDB
    
    df.reset_index(drop=True,inplace=True)
    
#   convert to JSON
#    json_records = df.T.to_json() 
#   
#    json.loads(json_records).values()
#    convert in list format --> list()
#   all combined in single line
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # insert converted JSON Record to MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)