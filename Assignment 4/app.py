from flask import Flask, jsonify, request
from db_utils import get_daily_affirmation, add_affirmation_to_db, get_affirmations_for_category, DbConnectionError

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

    try:
        add_affirmation_to_db(text, author, category)
        return jsonify({'confirmation' : 'Affirmation added successfully'})

    except DbConnectionError as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/affirmations/category/<category>', methods=['GET'])
def affirmations_by_category(category):
    try:
        affirmations = get_affirmations_for_category(category)
        return jsonify({'category': category, 'affirmations': affirmations})
    except DbConnectionError as e:
        return jsonify({'Error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)