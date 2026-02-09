from flask import Blueprint, jsonify, request
from flask import render_template
from datetime import datetime
from extensions import mongo

projetcs_bp = Blueprint("projects", __name__)

# Home page 
@projetcs_bp.route("/")
def home():
    projects = list(mongo.db.projects.find())
    for p in projects:
        p["_id"] = str(p["_id"])
    data = jsonify(projects)
    return render_template("index.html", data=data)

# Create the project
@projetcs_bp.route("", methods=["POST"])
def create_project():
    data = request.json
    project = {
        "name":data["name"],
        "description": data.get("description", ""),
        "created_at":datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "is_archieved":False
        }
    mongo.db.projects.insert_one(project)
    return jsonify({"message":"Project created"}), 201