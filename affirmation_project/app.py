from flask import Flask, jsonify, request
from db_utils import get_daily_affirmation, add_affirmation_to_db, get_affirmations_for_category

app = Flask(__name__)

# route to retrieve a random daily affirmation
@app.route('/affirmations', methods=['GET'])
def daily_affirmations():
    affirmations = get_daily_affirmation() # get a affirmation from the database
    return jsonify(affirmations) # return in JSON format

# route to add a new affirmation to the database
@app.route('/new_affirmation', methods=['POST'])
def add_affirmation():
    data = request.get_json()
    text = data.get('text')
    author = data.get('author')
    category = data.get('category')

# check if the affirmation text has been inputted
    if not text:
        return jsonify({'Error': 'Affirmation text is required'}), 400 # returns error message if text in the input is missing
    else:
        add_affirmation_to_db(text, author, category) # if text is inputted, then add the affirmation to the database
        return jsonify({'Confirmation' : 'Affirmation added successfully'}) # return confirmation message

# route to get affirmations by category
@app.route('/affirmations/category/<category>', methods=['GET'])
def affirmations_by_category(category):
        affirmations = get_affirmations_for_category(category) # returns affirmations by specified category
        return jsonify({'category': category, 'affirmations': affirmations}) # return affirmations with the category name

if __name__ == '__main__':
    app.run(debug=True, port=5001)