import json
import random
import promptMaster as PM

import json

placesPath="./prompt/places.json"
levelPath="./prompt/level.json"

def extract_valid_jsons(text):
    valid_jsons = []  # List to store valid JSON objects

    start = 0  # Starting index for searching
    while True:
        try:
            start_index = text.index('{', start)  # Find the opening curly brace
            end_index = text.index('}', start_index) + 1  # Find the closing curly brace
            json_str = text[start_index:end_index]  # Extract the JSON string

            json_obj = json.loads(json_str)  # Try to parse the JSON string
            valid_jsons.append(json_obj)  # If successful, add to the list

            start = end_index  # Move the starting index to the end of the parsed JSON
        except ValueError:
            break  # Stop when no more opening curly braces are found
        except json.JSONDecodeError:
            start = end_index  # Move to the end of the current fragment if parsing fails

    return valid_jsons

def filter_json_list(jsonList_, pattern):
    result = []

    for item in jsonList_:
        # Check if the current item is a dictionary and all specified keys in the pattern
        # are present in the item and have matching non-empty values.
        if isinstance(item, dict) and all(key in item and item[key] for key, value in pattern.items()):
            result.append(item)

    return result

def save_json_to_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
def open_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

def select_values(lst, x):
    if x>=len(lst):
        selected=lst    
    else:
        selected = random.sample(lst, x)
    return selected

def places_(count_):
    places=open_json_file(placesPath)
    level=open_json_file(levelPath)
    prompt=f"""using the available levels: 
    {level} 
    generate {count_} examples. 
    Taking as an example: {select_values(places["places"], 10)}
    Remember to include limits for beast_amount {places['range_beast_amount']} and riches taking {places['range_riches']}.
    It's important that you return me only json"""
    completion=PM.chatCompletionCreate(prompt)
    jsonList_=extract_valid_jsons(str(completion.choices[0].message["content"]))
    jsonList_=filter_json_list(jsonList_, places["places"][0])
    places["places"].extend(jsonList_)
    save_json_to_file(places, placesPath)

# todo

# monster=''
# choices=''
# weapones=''
# armor=''
# loot=''
# card=''
# stats=''

places_(20)
