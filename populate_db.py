import pymongo
from pymongo import MongoClient

client = MongoClient(host="mongodb", port=27017)

db = client["my_db"]

col = db["ma_collection"]

grain_info = {
    "origine": "Vietnam",
    "arôme": "Floral",
    "année": 2022,
    "corps": 7
}


res = col.insert_one(grain_info)

print(f'Les informations pour le grain {res.inserted_id} ont été ajoutées avec succès')

print(col.find_one())
