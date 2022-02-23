from application import db

class Coursework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brief = db.Column(db.String(30), nullable=False)
    finished = db.Column(db.Boolean, nullable=False, default=False)
