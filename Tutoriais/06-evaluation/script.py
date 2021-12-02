# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd

QRELS_FILE = "information_systems_qrels.txt"
QUERY_URL = "http://localhost:9200/courses/_search"
QUERY_FILE = "query2.json"

query_json = json.load(open(QUERY_FILE))

# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance

results = requests.get(QUERY_URL, json=query_json).json()['hits']['hits']

