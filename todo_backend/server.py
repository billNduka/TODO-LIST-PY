from flask import Flask
from flask_restful import Api
from db_setup import db
from dotenv import load_dotenv
import os
from routes.user_routes import register_user_routes

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
api = Api(app)

@app.route('/')
def home():
    return {"message": "welcome to the backend"}


register_user_routes(api)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()

