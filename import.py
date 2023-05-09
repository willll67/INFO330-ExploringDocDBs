import pandas as pd
from pymongo import MongoClient

data = pd.read_csv('pokemon.csv')
data_dict = data.to_dict('records')

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pokemonColl.insert_many(data_dict)