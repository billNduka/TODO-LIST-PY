from flask_restful import Resource
from flask import request, current_app
from markupsafe import escape
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from datetime import timezone, timedelta, datetime
import jwt
from models.user_model import User
from models.task_model import Task
from db_setup import db  


def get_username_from_token(request):
    auth_header = request.headers.get('Authorization', None)
    if not auth_header or not auth_header.startswith('Bearer '):
        return None
    token = auth_header.split(' ')[1]
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        return payload.get("username")
    except Exception:
        return None

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {"message": "Username already exists"}, 400
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            token = jwt.encode({
                "username": username,
                "exp": datetime.now(timezone.utc) + timedelta(hours=24)
            }, current_app.config['SECRET_KEY'], algorithm="HS256")
            return {"token": token}, 201
        return {"message": "Invalid credentials"}, 401
    
class Tasks(Resource):
    def post(self):
        username = get_username_from_token(request)
        if not username:
            return {"message": "Unauthorized"}, 401
        user = User.query.filter_by(username=username).first()
        if not user:
            return {"message": "User not found"}, 404
        data = request.get_json()
        if "parentIndex" in data:
            new_task = Task(
                user_id=user.id,
                title=data.get("title"),
                completed=data.get("completed", False),
                taskType=data.get("taskType"),
                parentIndex=data.get("parentIndex"),
                level=data.get("level"),
                index=data.get("index")
            )
        else:
            new_task = Task(
                user_id=user.id,
                title=data.get("title"),
                completed=data.get("completed", False),
                taskType=data.get("taskType"),
                index=data.get("index")
            )
        db.session.add(new_task)
        db.session.commit()
        return {"message": "Task saved", "task": new_task.toJSON()}, 201

    def get(self):
        username = get_username_from_token(request)
        if not username:
            return {"message": "Unauthorized"}, 401
        user = User.query.filter_by(username=username).first()
        if not user:
            return {"message": "User not found"}, 404
        tasks = Task.query.filter_by(user_id=user.id).all()
        tasks_json = [task.toJSON() for task in tasks]
        return tasks_json, 200

        