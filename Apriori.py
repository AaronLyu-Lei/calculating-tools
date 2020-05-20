import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
df = pd.read_csv('data_apriori.csv',header=None)
df

record = df.stack().groupby(level=0).apply(list).tolist()
print(record)

# Set your minimum support
association_rules = apriori(record, min_support=0.3)
association_results = list(association_rules)

# Find all frequent items
i = 1
while True:
    items_collection = []
    for item in association_results:
        if len(item[0])==i:
            items_collection.append(item)
        
    items = []   
    for item in items_collection:
        pair = item[0] 
        token = [x for x in pair]
        items.append(token)
        support = round(item[1],4)
        print(f"frequent {i}-item {token}--support {support*100}%")
    i += 1
    if items == []:
        break
# Set your confidence
association_rules = apriori(record, min_support=0.3, min_confidence=0.6999)
association_results = list(association_rules)

# Find all rules
i = 2
j = 1
while True:
    items_collection = []
    for item in association_results:
        if len(item[0])==i:
            items_collection.append(item)
    items = []
    for item in items_collection:
        pair = item[0]
        token = [x for x in pair]
        items.append(token)
        for a in item[2]:
            pair1 = a[0]
            pair2 = a[1]
            token1 = [y for y in pair1]
            token2 = [z for z in pair2]
            support = round(item[1],4)
            confidence = round(item[2][0][2],4)
            if token1 != []:
                print(f"Rule{j}: {token1}==>{token2}: S={support*100}% C={confidence*100}%")
                j += 1
            else:
                j += 0
    i += 1
    if items == []:
        break
