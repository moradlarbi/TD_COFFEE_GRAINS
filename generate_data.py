import random
import pymongo
from pymongo import MongoClient
from grain import Grain

def generate_valid_grain():
    grain = Grain()
    grain.origine = random.choice(grain.origines)
    grain.arome = random.choice(grain.aromes)
    grain.annee = random.randint(1950, 2022)
    return grain

if __name__ == "__main__":
    client = MongoClient(host="mongodb", port=27017)
    db = client["my_db"]
    col = db["ma_collection"]

    for _ in range(20): 
        grain = generate_valid_grain()
        if grain.is_valid(): 
            grain_info = {
                "origine": grain.origine,
                "arôme": grain.arome,
                "année": grain.annee,
                "corps": grain.corps
            }
            res = col.insert_one(grain_info)
            print(f'Les informations pour le grain {res.inserted_id} ont été ajoutées avec succès')
        else:
            print("Le grain n'est pas valide et ne sera pas ajouté à la base de données.")
