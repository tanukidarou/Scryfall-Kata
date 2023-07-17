#!/usr/bin/env python3

import requests
import json

class Card: # Estrcutura de datos de carta
	def __init__(self, id, oracle_id, name, manaCost):
		self.id = id
		self.oracle_id = oracle_id
		self.name = name
		self.manaCost = manaCost

requestRamdomCard = requests.get("https://api.scryfall.com/cards/random")
jsonRamdomCard = json.loads(requestRamdomCard.content) # Convertir la 

ramdomCardId = jsonRamdomCard["id"] # Leer el Json

requesCard = requests.get(f"https://api.scryfall.com/cards/{ramdomCardId}") # Nueva request con el Id de la carta
jsonCard = json.loads(requesCard.content)

card = Card(jsonCard["id"], jsonCard["oracle_id"], jsonCard["name"], jsonCard["mana_cost"]) # Crea el objeto carta

print(f"{card.name} {card.manaCost}")