from flask import Flask
from flask_cors import CORS
from models import db
from config import Config
from routes.auth_routes import auth_routes
from routes.student_routes import student_routes

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

app.register_blueprint(auth_routes)
app.register_blueprint(student_routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
