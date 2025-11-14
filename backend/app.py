from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Mock data
recipes = [
    {"id": 1, "name": "Comfort Food Delight", "category": "comfort", "ingredients": ["pasta", "cheese"]},
    {"id": 2, "name": "Energizing Salad", "category": "energized", "ingredients": ["lettuce", "nuts"]},
    {"id": 3, "name": "Relaxing Soup", "category": "relaxed", "ingredients": ["carrots", "ginger"]}
]

# Map moods to recipe categories
mood_to_category = {
    "happy": "energized",
    "sad": "comfort",
    "relaxed": "relaxed",
    "angry": "comfort"
}

# In-memory favorites per user
user_favorites = {}

# In-memory user profiles
user_profiles = {}

# In-memory user interaction history
user_history = {}

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get('mood')
    if not mood or mood not in mood_to_category:
        return jsonify({"error": "Invalid mood"}), 400
    category = mood_to_category[mood]
    matched = [r for r in recipes if r['category'] == category]
    return jsonify(matched)

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(recipe)

@app.route('/api/users/<string:user_id>/favorites', methods=['GET', 'POST'])
def favorites(user_id):
    if request.method == 'POST':
        data = request.get_json()
        recipe_id = data.get('recipe_id')
        if not recipe_id:
            return jsonify({"error": "Missing recipe_id"}), 400
        user_favorites.setdefault(user_id, set()).add(recipe_id)
        return jsonify({"message": "Added to favorites"})
    else:
        favs = user_favorites.get(user_id, set())
        fav_recipes = [r for r in recipes if r['id'] in favs]
        return jsonify(fav_recipes)

@app.route('/api/users/<string:user_id>/preferences', methods=['PUT'])
def update_preferences(user_id):
    data = request.get_json()
    user_profiles[user_id] = data.get('preferences', {})
    return jsonify({"message": "Preferences updated"})

@app.route('/api/users/<string:user_id>/history', methods=['GET'])
def get_history(user_id):
    history = user_history.get(user_id, [])
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
