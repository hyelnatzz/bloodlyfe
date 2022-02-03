# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from app import app



# db = SQLAlchemy(app)


# class User(db.Model, UserMixin):
#     """Model for user accounts."""
#     __tablename__ = 'users'

#     id = db.Column(db.Integer,
#                 primary_key=True)
#     username = db.Column(db.String,
#                 nullable=False,
#                 unique=False)
#     first_name = db.Column(db.String,
#                 nullable=False,
#                 unique=False)
#     last_name = db.Column(db.String,
#                 nullable=False,
#                 unique=False)
#     email = db.Column(db.String(40),
#                 unique=True,
#                 nullable=False)
#     password = db.Column(db.String(200),
#                 primary_key=False,
#                 unique=False,
#                 nullable=False)
#     address = db.Column(db.String,
#                 nullable=True,
#                 unique=False)
#     donation_count = db.Column(db.String,
#                 nullable=False, 
#                 default=0)
#     genotype = db.Column(db.String(2),
#                 nullable=True,
#                 unique=False)
#     city = db.Column(db.String,
#                 nullable=True,
#                 unique=False)
#     country = db.Column(db.String,
#                 nullable=True,
#                 unique=False)
#     phone = db.Column(db.String,
#                 nullable=True,
#                 unique=False)
    
#     bloodgroup_id = db.Column(db.Integer, db.ForeignKey('bloodgroups.id'))

#     def __repr__(self):
#         return '<User {}>'.format(self.username)


# class Bloodgroup(db.Model, UserMixin):
#     __tablename__ = 'bloodgroups'
#     id = db.Column(db.Integer,
#                 primary_key=True)
#     name = db.Column(db.String(2), 
#                 nullable = False, 
#                 unique=True)
#     users = db.relationship('User', 
#                 backref='bloodgroup', 
#                 lazy=True)

#     def __repr__(self):
#         return '<Bloodgroup {}>'.format(self.name)


# # db.create_all()
# # lst = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
# # for i in lst:
# #     blood = Bloodgroup()
# #     blood.name = i
# #     db.session.add(blood)
# #     db.session.commit()
