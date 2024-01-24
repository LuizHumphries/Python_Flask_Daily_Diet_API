from flask import Flask, request, jsonify
from database import db
from models.food import Food


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin@127.0.0.1:3306/daily-diet-crud"
db.init_app(app)

@app.route('/food', methods=['POST'])
def create_food():
    """ Function responsible for the food creation in DB - MySQL """    
    request_data = request.json   
    
    food_name = request_data.get("name") # non nullable
    food_description = request_data.get("description") # non nullable
    food_calories = request_data.get("calories") # non nullable
    food_diet = request_data.get("diet") # default insertion as False
    food_time = request_data.get("time") # non nullable
    
    if food_name and food_description and food_calories:        
        food_to_db = Food(name=food_name, description=food_description,
                        calories=food_calories, diet=food_diet,
                        time=food_time)        
        db.session.add(food_to_db)
        db.session.commit()
        return jsonify({"message": "Food sucessifuly created"})

@app.route('/food', methods=['GET'])
def get_foods():
    """Get the total food list"""   
    food_list = [food.to_dict() for food in Food.query.all()]
    return food_list

@app.route('/food/<int:id>', methods=['GET'])
def get_food(id):
    """Get a specific food from db using index/id"""   
    food = Food.query.get(id)
    if food:
        return food.to_dict()
    return jsonify({"message": "Food id not found"}), 404

@app.route('/food/<int:id>', methods=['PUT'])
def update_food(id):
    """Update a specific food from index/id""" 
    request_data = request.json #new data
    food = Food.query.get(id) #data from database 
    if food:   
        food.name = request_data.get('name', food.name)
        food.description = request_data.get('description', food.description)
        food.calories = request_data.get('calories', food.calories)
        food.time = request_data.get('time', food.time)
        food.diet = request_data.get('diet', food.diet)
        db.session.commit()
        return jsonify({"message": "Food updated successfully"})
    return jsonify({"message": "Food id not found"})

@app.route('/food/<int:id>', methods=['DELETE'])
def delete_food(id):
    """Delete a specific food from db usin index/id"""   
    food = Food.query.get(id)
    if food:
        db.session.delete(food)
        db.session.commit()
        return jsonify({"message": f"{food.name} deleted successfully"})
    return jsonify({"message": "Food id not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)