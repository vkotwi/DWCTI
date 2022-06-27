### Creates and populates a new database with the inital URLs list.
### This file should only run once at the start of the program and once
### during the NLP  phase ???

### TODO###
# Shutdown.py - should close session, shut down tor.exe etc
# Take in parameters cause of phase 2?

### IMPORTS ###
from pymongo import MongoClient
from pymongo.collation import Collation

from datetime import date, datetime
import time


# TODO: start mongodb as a service

collection = {
    'locale': 'en_US',
    'strength': 2,
    'numericOrdering': True,
    'backwards': False
}

#create_collection(collection)
client = MongoClient('mongodb://localhost:27017/')
db = client["DWProject"]

# Checks if collection exists, if not creates new one
collist = db.list_collection_names()
if "DW_URLs" not in collist:
    print("Database empty! Populating...")
    # Copies all initial urls to the URLs list to be added to the database
    urls = []
    with open('prelim_links.txt', 'r') as pl:
        for l in pl:
            urls.append(l)

    ### Populates the new database with the inital URLs list if it's empty
    # Adds all URLs with the default data to a dict to be psuhed to the dbn
    entries = []
    for url in urls:
        entries.append({
                'url': url.strip(),
                'visited': False,
        })

    # 'url': url.strip(),
    # 'title': None,
    # 'redirects': "",
    # 'dateLastChecked': None,
    # 'parent_sites': [],
    # 'status': None,
    # 'topics': [],
    # 'data': [],
    # 'categories': [],
    # 'relevant': None,
    # 'visited': False,
        
    colletion = db["DW_URLs"]
    colletion.insert_many(entries)
    colletion.create_index('url',  unique=True)
    print("Populated database")
    
else:
    print("Database already populated")

client.close()

