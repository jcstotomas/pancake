import app

db = app.db
class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(50))
    ssn = db.Column(db.String(10))



class Posts(db.model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key=True)
    text_content = db.Column(db.String(150))
    