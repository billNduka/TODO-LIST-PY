from db_setup import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    taskType = db.Column(db.String(50), nullable=False)
    parentIndex = db.Column(db.Integer, nullable=True)
    level = db.Column(db.Integer, default=0, nullable=True)
    index = db.Column(db.Integer, nullable=False)
    def toJSON(self):
        if self.parentIndex is not None:
            return {
                "index": self.index,
                "parentIndex": self.parentIndex,
                "title": self.title,
                "completed": self.completed,
                "level": self.level,
                "taskType": self.taskType
            }
        else:
            return {
                "index": self.index,
                "title": self.title,
                "completed": self.completed,
                "taskType": self.taskType
            }