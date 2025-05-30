# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "task_name": self.task_name,
            "status": self.status
        }
