import app

db = app.db
class User(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    ssn = db.Column(db.String(10))
    posts = db.relationship('Post', cascade="all, delete, delete-orphan")


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    text_content = db.Column(db.String(150))
    
    


    