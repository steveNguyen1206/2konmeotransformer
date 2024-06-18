# from model.init import vivitb_electra_classifier
from transformers import pipeline 
import csv
import os

CURRENT_DIRECTORY = os.getcwd()
VITB_ELECTRA_MODEL_PATH = os.path.join(CURRENT_DIRECTORY, "model/vivtb_electra-based_model/checkpoint-880")
TEENCODE_PATH = os.path.join(CURRENT_DIRECTORY, "model/teencode.txt")

def load_db_from_text_file(file_path):
    db = {}
    with open(file_path, encoding="utf8", mode='r') as file:
        for line in file:
            # Split each line into key and value using space as the delimiter
            key, value = line.strip().split('\t')
            db[key] = value
    return db

teencode_db = load_db_from_text_file(TEENCODE_PATH)


def model_get_entities(text):
    vivitb_electra_classifier = pipeline("ner", model=VITB_ELECTRA_MODEL_PATH)
    return vivitb_electra_classifier(text)


def process_teencode (text):
    # check if word in text is teencode:
    teencode = {}
    formal_text = text
    for index, word in enumerate(text.split()):
        if word in teencode_db:
            teencode[index] = word
            formal_text = formal_text.replace(word, teencode_db[word])
    
    return formal_text, teencode


def get_entities(text):
    vivitb_electra_classifier = pipeline("ner", model=VITB_ELECTRA_MODEL_PATH)
    
    # formmalize text
    fomarl_text, teencode = process_teencode(text)

    if len(teencode) > 0:
        text = fomarl_text
        entities = vivitb_electra_classifier(text)

        # restruct the original text
        # for index, word in teencode.items():
        #     entities[index]['word'] = word
        return entities

    return vivitb_electra_classifier(text)