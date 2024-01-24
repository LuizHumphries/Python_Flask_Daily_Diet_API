from flask import Flask, request
from database import db
from models.food import Food

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin@127.0.0.1:3306/daily-diet-crud"
db.init_app(app)


@app.route('/food', methods=['POST'])
def create_food():
    request_data = request.json    
    pass







if "__name__" == "__main__":
    app.run(debug=True)