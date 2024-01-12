from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
