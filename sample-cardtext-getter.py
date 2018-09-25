import requests
import json

URL = "http://yugiohprices.com/"
CARD_DATA_ENDPOINT = URL + "api/card_data/"
SET_DATA_ENDPOINT = URL + "api/set_data/"

def get_card_names_by_card_type_for_set(setname):
    card_names = {"monster":[], "spell":[], "trap":[]}
    response = requests.get(SET_DATA_ENDPOINT + setname)
    data = response.json()

    for card in data["data"]["cards"]:
       card_type = card["card_type"]
       name = card["name"]
       card_names[card_type].append(name)

    print(card_names)
    return card_names

get_card_names_by_card_type_for_set("breakers%20of%20shadow")
    
