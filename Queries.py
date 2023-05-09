from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print("-" * 60)
query = {"name": "Pikachu"}
results = pokemonColl.find(query)
for result in results:
    print(result)

print("-" * 60)
query = {"attack": {"$gt": 150}}
results = pokemonColl.find(query)
for result in results:
    print(result)

print("-" * 60)
query = {"abilities": {'$regex': ".*Overgrow.*"}}
results = pokemonColl.find(query)
for result in results:
    print(result)
