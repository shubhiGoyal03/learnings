import sys
from elasticsearch import Elasticsearch
import pandas as pd
import json
from ast import literal_eval
from tqdm import tqdm
import datetime
import os
import numpy as np
from elasticsearch import helpers

es = Elasticsearch(hosts = "http://localhost:9200")

print(es.ping())

#to create an index
#es.indices.create(index = 'es_test_1', ignore = 400)
#es.indices.create(index = 'es_test_2', ignore = 400)

#to delete an specific index
#print(es.indices.delete(index = 'test-index', ignore = [400,404]))

e1={
    "first_name" : "Shubhi",
    "last_name" : "Goyal",
    "age" : "25",
    "about" : "melorist",
    "interests" : ["music", "food", "travel"]
}

#to insert a document at index
#print(es.index(index="es_test_1", document=e1, id=1))

#read file and convert to dict format
df = pd.read_csv("songs_normalize.csv")
#print(df.shape)
#df1 = pd.read_json("72c74fb3-a9fa-4e29-ba0d-568b215bbf69__1650377204145_0.31686374587957733__console.askalden.io__1650377205926.json")
df2=df.to_dict('records')
#print(df2[0])
#print(df2[1])

def generator(df2):
    for c,line in enumerate(df2):
        yield{
            '_index' : 'es_first',
            '_source' : {
                "artist" : line.get("artist", ""),
                "song" : line.get("song", ""),
                "genre" : line.get("genre", ""),
                "duration" : line.get("duration_ms", None)
            }
        }
    raise StopIteration

#mycustom=generator(df2)
#print(type(next(mycustom)))

Settings = {
    "settings" : {
        "number of shards" : 1,
        "number of replicas" : 0
    },
    "mappings" : {
        "properties" : {
            "artist" : {
                "type" : "text"
            }
        }
    }
}

try:
    es.indices.create(index = "es_first", ignore = [400,404])
except Exception as e:
    print("----------------")
    print(e)

try:
    res = helpers.bulk(es, generator(df2))
    print("Working")
except Exception as e:
    print(e)

myquery = {
    "_source" : [],
    "size" : 10,
    "query" : {
        "match" : {
            'genre' : 'pop'
        }
    }
}

#query
res= es.search(index = 'es_first', body= myquery)


for i in res['hits']['hits']:
    print(i['_source']['artist']," : ",i['_source']['song'])
