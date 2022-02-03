from flask import Flask, render_template, redirect, flash, url_for, request
from flask_login import login_required, login_user, logout_user, LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import *
from config import Config
from models import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from util import bloodMatched

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = "login"
db = SQLAlchemy(app)



#MODELS
class User(db.Model, UserMixin):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                primary_key=True)
    username = db.Column(db.String,
                nullable=False,
                unique=True)
    first_name = db.Column(db.String,
                nullable=False,
                unique=False)
    last_name = db.Column(db.String,
                nullable=False,
                unique=False)
    email = db.Column(db.String(40),
                unique=True,
                nullable=False)
    password = db.Column(db.String(200),
                unique=False,
                nullable=False)
    address = db.Column(db.String,
                nullable=True,
                unique=False)
    donation_count = db.Column(db.String,
                nullable=False, 
                default=0)
    genotype = db.Column(db.String(2),
                nullable=True,
                unique=False)
    city = db.Column(db.String,
                nullable=True,
                unique=False)
    country = db.Column(db.String,
                nullable=True,
                unique=False)
    phone = db.Column(db.String,
                nullable=True,
                unique=False)
    
    bloodgroup_id = db.Column(db.Integer, db.ForeignKey('bloodgroups.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Bloodgroup(db.Model, UserMixin):
    __tablename__ = 'bloodgroups'
    id = db.Column(db.Integer,
                primary_key=True)
    name = db.Column(db.String(2), 
                nullable = False, 
                unique=True)
    users = db.relationship('User', 
                backref='bloodgroup', 
                lazy=True)

    def __repr__(self):
        return '<Bloodgroup {}>'.format(self.name)


#VIEW

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.errorhandler(404)
def errorhandler(error):
    return "Page not found", 404

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #try:
            user = User.query.filter_by(username = form.email.data.strip()).first()
            if user:
                if check_password_hash(user.password, form.password.data.strip()):
                    login_user(user)
                    return redirect(url_for("dashboard"))
                else:
                    flash("Username or Password invalid")
        #except:
            flash("Something went wrong")
    return render_template('authpages/login.html', form = form)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_exist = User.query.filter_by(email=form.email.data.strip()).first()
        if user_exist:
            flash("User email already exists")
            return redirect(url_for("register"))
        #try:
        user = User()
        user.username = form.email.data.strip()
        user.email = form.email.data.strip()
        user.password = generate_password_hash(form.password.data.strip())
        user.first_name = form.first_name.data.strip()
        user.last_name = form.last_name.data.strip()
        user.phone = form.phone.data.strip()
        user.address = form.address.data.strip()
        bloodgroup = Bloodgroup.query.filter_by(
            name=form.bloodgroup.data + form.rhesus.data).first()
        user.bloodgroup = bloodgroup
        user.genotype = form.genotype.data
        user.city = form.city.data.strip()
        user.country = form.country.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("registerSuccess"))
    #except:
        flash("Something went wrong, please retry")
    return render_template('authpages/register.html', form=form)


@app.route('/reg-success')
def registerSuccess():
    return render_template('authpages/regsuccess.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('userpages/maindashboard.html')


@app.route('/profile-settings', methods=["POST", "GET"])
@login_required
def profileSettings():
    form = ProfileUpdateForm()
    form.full_name.data = current_user.first_name + " " + current_user.last_name
    form.email.data = current_user.email
    form.address.data = current_user.address
    form.country.data = current_user.country

    if request.method== "POST":
            print("valid")
            current_user.username = form.email.data.strip()
            current_user.email = form.email.data.strip()
            current_user.first_name = form.full_name.data.strip().split(" ")[0]
            current_user.last_name = form.full_name.data.strip().split(" ")[1]
            current_user.address = form.address.data
            print(form.address.data)
            bloodgroup = Bloodgroup.query.filter_by(
                name=form.blood_group.data + form.rhesus.data).first()
            current_user.bloodgroup = bloodgroup
            current_user.genotype = form.genotype.data
            current_user.city = form.city.data
            print(form.country.data)
            current_user.country = form.country.data
            print(form.errors)
            db.session.add(current_user)
            db.session.commit()
            flash("Detail Updated")
        #except:
            flash("Something went wrong, please retry")
    return render_template('userpages/profilepersonaldetails.html', form = form)


@app.route('/history')
@login_required
def medicalHistory():
    return render_template('userpages/medicalhistory.html')


@app.route('/donation-home')
@login_required
def donationHome():
    return render_template('donationpages/donationhome.html')


@app.route('/match-success')
def matchSuccess(user):
    return render_template('donationpages/donationnotify.html', user = user)


@app.route('/donation-portal', methods=["POST", "GET"])
@login_required
def donationPortal():
    form = DonationForm()
    if form.validate_on_submit():
        current_user.donation_count = current_user.donation_count + 1
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template('donationpages/donationportal.html', form = form)


@app.route('/request-portal', methods=["POST", "GET"])
@login_required
def requestPortal():
    form = RequestForm()
    if form.validate_on_submit():
        users = db.session.query(User).all()
        for user in users:
            if current_user.email != user.email and bloodMatched(current_user.bloodgroup.name, user.bloodgroup.name) and user.city == current_user.city:
                print("Hurray matched")
                return redirect(url_for("matchSuccess", user=user))
            else: 
                print("No match found")

    return render_template('donationpages/requestportal.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == '__main__':
    # content = ""
    # try:
    #     content = db.session.query.all()
    # except:
    #     pass
    # if not content:
    #     db.create_all()
    #     lst = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    #     for i in lst:
    #         blood = Bloodgroup()
    #         blood.name = i
    #         db.session.add(blood)
    #         db.session.commit()
    #db.create_all()
    app.run(debug=True)
# if __name__ == '__main__':
    #     app.run(debug=True)
#     content = ""
#     try:
#         content = db.session.query.all()
#     except:
#         pass

#     if not content:
# db.create_all()
    # lst = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    # for i in lst:
    #     blood = Bloodgroup()
    #     blood.name = i
    #     db.session.add(blood)
    #     db.session.commit()

