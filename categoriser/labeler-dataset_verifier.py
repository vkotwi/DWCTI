# Use labeled set to label unlabeled set, making a bigger data dataset

#from sklearn.datasets import make_classification
#from sklearn.model_selection import train_test_split

from pymongo import MongoClient
import subprocess

client = MongoClient('mongodb://localhost:27017/')
db_dataset_pseudo_labelled = client["DWProject"]["DW_dataset_unlabelled"]

# Information retrieval
while True:
    entries = []
    # TODO: update old one to say already pulled
    urls = db_dataset_pseudo_labelled.find(
        {"verified": {'$exists': False}, 'categories': {'$ne': []}},
        {
            'url': 1,
            'data': 1,
            'categories': 1
        }
    ).limit(10)

    for url in urls:
        
        while True:
            print("================================================")
            try:
                subprocess.call('cls', shell=True)
            except:
                pass
            
            print("Url:", url["url"])
            print("")
            print("Data:", url["data"])
            print("")
            print("")
            print("categories:", url["categories"])

            
            labels = input("Correct? (Y/N): ")
            if labels == "Y":
                new = url["categories"]
            else:
                i = input("Enter new categories: ")
                if len(i) == 0:
                    new = []
                else:
                    new = i.split(", ") 
                

            print("All labels:")
            for e in new:
                print(e)
            print("")
            print("Push the following?")
            print("Url:", url["url"])
            print("Old labels:", url["categories"])
            print("New labels:", new)
            print("")

            cont = input("y/n: ")

            if cont == "y":
                db_dataset_pseudo_labelled.update_one(
                    {'url': url["url"]},
                     { '$set':
                         {
                            'new': new,
                            'verified': True
                        }
                    }
                )
                break

