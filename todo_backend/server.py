from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import os
from routes.user_routes import register_user_routes

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
print(app.config["SECRET_KEY"])
api = Api(app)

@app.route('/')
def home():
    return {"message": "welcome to the backend"}


register_user_routes(api)


if __name__ == '__main__':
    app.run()

