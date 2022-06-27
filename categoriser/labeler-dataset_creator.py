# Use labeled set to label unlabeled set, making a bigger data dataset

#from sklearn.datasets import make_classification
#from sklearn.model_selection import train_test_split

from pymongo import MongoClient
import subprocess

client = MongoClient('mongodb://localhost:27017/')
db = client["DWProject"]["DW_URLs"]

new_client = MongoClient('mongodb://localhost:27017/')
new_db = new_client["DWProject"]
colletion = new_db["DW_dataset"]

# Information retrieval
while True:
    entries = []
    # TODO: update old one to say already pulled
    urls = db.find({'status': 200, 'checked': None}, {'url': 1, 'data': 1, 'keywords': 1, 'score': 1}).limit(1)

    for url in urls:
        if url["data"] != "" and len(url["keywords"]) != 0 and any("hack" in s for s in url["keywords"]):  
            while True:
                print("================================================")
                try:
                    subprocess.call('cls', shell=True)
                except:
                    pass
                
                print("Labeled:", colletion.count_documents({}, {}))
                print("Url:", url["url"])
                print("")
                print("Data:", url["data"])
                print("")
                print("Keywords:", url["keywords"])
                print("")
                print("Score:", url["score"])
                print("")
                
                labels = input("Labels: ")
                if labels != "":
                    labels = labels.split(", ")
                else:
                    labels = []


                print("All labels:")
                for e in labels:
                    print(e)

                english = input("English? y/n: ")
                r = input("Relevant? y/n: ")
                relevant = False

                if english == "y":
                    english = True
                else:
                    english = False
                if r == "y":
                    relevant = True

                print("")
                print("Push the following?")
                print("Url:", url["url"])
                print("Labels:", labels)
                print("Relevant:", relevant)

                print("")

                cont = input("y/n: ")

                if cont == "y":
                    try:
                        colletion.insert_one({
                            'url': url["url"],
                            'data': url["data"],
                            'english': english,
                            'categories': labels,
                            'relevant': relevant,
                        })
                    except Exception as e:
                        print(e)
                    db.update_one(
                        {'url': url["url"]},
                         { '$set':
                             {
                                'checked': True
                            }
                        }
                    )
                    break
        else:
            db.update_one(
                {'url': url["url"]},
                 { '$set':
                     {
                        'checked': True
                    }
                }
            )
            

