import os
from flask import Flask, render_template, request
from fatsecret import Fatsecret

app = Flask(__name__)

api_key = os.getenv('nutrition_api_key')
api_secret = os.getenv('nutrition_api_secret')
fs = Fatsecret(api_key, api_secret)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    foods = fs.foods_search(search_term)
    return render_template('results.html', foods=foods)

@app.route('/nutrition/<food_id>')
def nutrition(food_id):
    food = fs.food_get(food_id)
    return render_template('nutrition.html', food=food)

if __name__ == '__main__':
    app.run(debug=True)
