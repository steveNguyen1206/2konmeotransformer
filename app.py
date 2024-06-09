from flask import Flask, request, render_template, jsonify
from model.model import get_entities
import numpy as np
import json

app = Flask(__name__)

def convert_to_serializable(result):
    # Convert any numpy.float32 to Python float
    for item in result:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, np.float32):
                    item[key] = float(value)
    return result

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    entities = get_entities(text)
    entities = convert_to_serializable(entities)
    print(entities)
    return json.dumps(entities)

if __name__ == '__main__':
    app.run(debug=True)
