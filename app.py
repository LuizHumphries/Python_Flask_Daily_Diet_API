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
    food_list = [food.to_dict() for food in Food.query.all()]
    return jsonify(food_list)

@app.route('/food/<int:food_id>', methods=['GET'])
def get_food(food_id):
    pass




if __name__ == "__main__":
    app.run(debug=True)