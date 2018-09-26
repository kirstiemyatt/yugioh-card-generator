import requests
import json

URL = "http://yugiohprices.com/"
CARD_DATA_ENDPOINT = URL + "api/card_data/"
SET_DATA_ENDPOINT = URL + "api/set_data/"

def get_card_names_by_card_type_for_set(set_name):          
    card_names = {"monster":[], "spell":[], "trap":[]}
    response = requests.get(f"{SET_DATA_ENDPOINT}{set_name}")
    data = response.json()

    for card in data["data"]["cards"]:
        card_type = card["card_type"]
        name = card["name"]
        type_and_mechanic = card["type"]
        # Spells and traps have null value for type. If The mechanic is included, then it's an extra deck monster which will need to be considered separately at a later date as the text contains information not useful to Markov Chain
        if type_and_mechanic is not None and ("Tuner" in type_and_mechanic or "Fusion" in type_and_mechanic or "Pendulum" in type_and_mechanic or "Synchro" in type_and_mechanic or "Xyz" in type_and_mechanic):
            continue
        else:
            card_names[card_type].append(name)

    return card_names

def create_text_files(card_names):
    for card_type in card_names:
        file = open(f"{card_type}.txt", "a", encoding="utf-8")
        for card_name in card_names[card_type]:
            response = requests.get(f"{CARD_DATA_ENDPOINT}{card_name}")
            data = response.json()

            text = data["data"]["text"]
            file.write(f"{text}\n")

print("Getting card names for set")
card_names = get_card_names_by_card_type_for_set("breakers of shadow")

print("Creating text files")
create_text_files(card_names)

print("Finished!")
