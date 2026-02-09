from flask import Flask
from config import Config
from extensions import mongo
from routes.projects import projetcs_bp
from routes.tasks import task_bp


def create_app():
    app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")
    app.config.from_object(Config)
    mongo.init_app(app)
    
    app.register_blueprint(projetcs_bp, url_prefix="/")
    app.register_blueprint(task_bp, url_prefix="/api")
    
    return app

app = create_app()    

if __name__ == "__main__":
    app.run(debug=True)