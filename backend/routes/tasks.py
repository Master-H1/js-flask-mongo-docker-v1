from flask import jsonify, request, Blueprint
from bson import ObjectId
from datetime import datetime
from extensions import mongo

task_bp = Blueprint("tasks", __name__)

# get stored apps
@task_bp.route("/projects/<project_id>/tasks", methods=["GET"])
def get_tasks(project_id):
    tasks = list(mongo.db.tasks.find({"project_id":ObjectId(project_id)}))
    for t in tasks:
        t["_id"] = str(t["_id"])
        t["project_id"] = str(t["_id"])
    return jsonify(tasks), 200

# create a new task
@task_bp.route("/projects/<project_id>/tasks", methods=["POST"])
def create_task(project_id):
    data = request.json
    task = {
        "project_id": ObjectId(project_id),
        "title": data["title"],
        "description": data.get("description", ""),
        "status":"todo",
        "priority": data.get("priority", "medium"),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }    
    mongo.db.tasks.insert_one(task)
    return jsonify({"message":"Task created"}), 201