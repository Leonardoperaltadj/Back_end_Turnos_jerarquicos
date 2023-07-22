from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from database.db import DATEBASE_CONNECTION_URI
from config import config
from database.db import db

# Routes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  DATEBASE_CONNECTION_URI
#db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    db.init_app(app)
    db.create_all()

CORS(app, resources={"*": {"origins": "http://localhost:5000"}})



def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints


    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()