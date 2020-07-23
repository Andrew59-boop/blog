from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer ,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    blogs  = db.relationship('Blog', backref = 'user' , lazy = 'dynamic')
    comments = db.relationship('Comment' , backref = 'user', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
         return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer ,primary_key = True)
    title  = db.Column(db.String(255))
    description = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments = db.relationship('Comment' , backref = 'blog', lazy = 'dynamic')


    def __repr__(self):
        return f'Blog {self.title}'


class Comment(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Comment {self.description}'


class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
        