import app

db = app.db
class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(50))
    ssn = db.Column(db.String(10))