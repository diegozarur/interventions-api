import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restless import APIManager
from pre_processors import patch_single_preprocessor
from decouple import config

app = Flask(__name__)
db = SQLAlchemy(app)

# SQLAlchemy configuration
# Flask configuration
db_user = config('DB_USER', default='postgres')
db_pass = config('DB_PASS', default='postgres')
db_host = config('DB_HOST', default='db')
db_port = config('DB_PORT', default='5432')
db_name = config('DB_NAME', default='nautiluxdb')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/nautiluxdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
    db_user,
    db_pass,
    db_host,
    db_port,
    db_name
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-Migrate configuration
migrate = Migrate(app, db)

# Flask-CORS configuration
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize Flask-Restless
manager = APIManager(app, flask_sqlalchemy_db=db)


# Moodel
class Intervention(db.Model):
    __tablename__ = 'interventions'

    id = db.Column(db.Integer, primary_key=True)
    wording = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    speaker = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    date_of_intervention = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Enum('Draft', 'Validated', 'Completed', name='intervention_status'),
                       server_default=db.text("'Draft'"))


# Create API
manager.create_api(Intervention,
                   methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                   preprocessors={
                       'POST': [patch_single_preprocessor],
                       'PUT_SINGLE': [patch_single_preprocessor],
                       'PATCH_SINGLE': [patch_single_preprocessor],
                       'PUT': [patch_single_preprocessor]
                   },
                   url_prefix='/api/v1'
                   )


# Flask routes for rendering the template
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)
