'''This is the models module

all model are defined here
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    saltid = db.Column(db.String(255))
    profile = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    categories = db.relationship(
        'Category',
        backref='user',
        lazy='dynamic'
    )
    products = db.relationship(
        'Product',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, saltid, profile, nickname):
        self.saltid = saltid
        self.profile = profile
        self.nickname = nickname

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
class Category(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(36))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, name):
        self.name = name
    
class Product(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(36))
    state = db.Column(db.Integer())
    image_path = db.Column(db.String(36))
    price = db.Column(db.Float())
    inventory = db.Column(db.Integer())
    sale = db.Column(db.Integer())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, title):
        self.name = title
        self.state = 1

# class Order(db.Model):
#     pass