# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI
from models import db, Task

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#for rendering issue
with app.app_context():
    db.create_all()
    
@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = Task(task_name=data['task_name'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added"}), 201

@app.route("/get_tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.route("/update_task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    
    if 'task_name' in data:
        task.task_name = data['task_name']
    if 'status' in data:
        task.status = data['status']

    db.session.commit()
    return jsonify({"message": "Task updated"})


@app.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
