from flask import Flask, render_template, request
from fatsecret import Fatsecret

app = Flask(__name__)

api_key = 'f3f939e92c2f4102986917ec969b2fe7'
api_secret = '54fb2c826d3a4b46b280cc76d3164faf'
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
    food = fs.food_get_v4(food_id)
    return render_template('nutrition.html', food=food)

if __name__ == '__main__':
    app.run(debug=True)
