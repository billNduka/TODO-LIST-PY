from flask_restful import Resource
from flask import request, current_app
from markupsafe import escape
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from datetime import timezone, timedelta, datetime
import jwt
from models.user_model import users

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if any(u["username"] == username for u in users):
            return {"message": "Username already exists"}, 400
        
        hashed_password = generate_password_hash(password)
        users.append({
            "username": username,
            "password": hashed_password
        })
        return {"message": "User registered successfully"}, 201
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = next((u for u in users if u["username"] == username), None)
        if user and check_password_hash(user["password"], password):
            token = jwt.encode({
                "username": username,
                "exp": datetime.now(timezone.utc) + timedelta(hours=24)
            }, current_app.config['SECRET_KEY'], algorithm="HS256")
            return {"token": token}, 201
        return {"message": "Invalid credentials"}, 401