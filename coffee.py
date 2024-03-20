import pymongo
from pymongo import MongoClient
from grain import Grain  # Importez la classe Grain depuis votre fichier grain.py

def check_grain_validity(grain_data):
    grain = Grain()
    grain.origine = grain_data["origine"]
    grain.arome = grain_data["arôme"]
    grain.annee = grain_data["année"]
    grain.corps = grain_data["corps"]
    
    if not grain.is_valid():
        print(f"Grain invalide: {grain_data}")

if __name__ == "__main__":
    client = MongoClient(host="mongodb", port=27017)
    db = client["my_db"]
    col = db["ma_collection"]

    grains = col.find()
    for grain_data in grains:
        check_grain_validity(grain_data)
