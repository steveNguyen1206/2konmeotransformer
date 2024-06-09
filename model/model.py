# from model.init import vivitb_electra_classifier
from transformers import pipeline 
import os

CURRENT_DIRECTORY = os.getcwd()
VITB_ELECTRA_MODEL_PATH = os.path.join(CURRENT_DIRECTORY, "model/vivtb_electra-based_model/checkpoint-880")

def get_entities(text):
    vivitb_electra_classifier = pipeline("ner", model=VITB_ELECTRA_MODEL_PATH)
    return vivitb_electra_classifier(text)