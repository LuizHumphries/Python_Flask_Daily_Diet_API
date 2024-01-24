from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin@127.0.0.1:3306/daily-diet-crud"
db.init_app(app)


if "__name__" == "__main__":
    app.run(debug=True)