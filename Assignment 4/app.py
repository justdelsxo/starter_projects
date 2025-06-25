from flask import Flask, jsonify, request
from db_utils import get_daily_affirmation, add_affirmation_to_db, get_affirmations_for_category

app = Flask(__name__)

@app.route('/affirmations', methods=['GET'])
def daily_affirmations():
    affirmations = get_daily_affirmation()
    return jsonify(affirmations)

@app.route('/new_affirmation', methods=['POST'])
def add_affirmation():
    data = request.get_json()
    text = data.get('text')
    author = data.get('author')
    category = data.get('category')

    if not text:
        return jsonify({'Error': 'Affirmation text is required'}), 400
    else:
        add_affirmation_to_db(text, author, category)
        return jsonify({'Confirmation' : 'Affirmation added successfully'})

@app.route('/affirmations/category/<category>', methods=['GET'])
def affirmations_by_category(category):
        affirmations = get_affirmations_for_category(category)
        return jsonify({'category': category, 'affirmations': affirmations})

if __name__ == '__main__':
    app.run(debug=True, port=5001)