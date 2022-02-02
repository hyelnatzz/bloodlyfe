from flask import Flask, render_template
from forms import *


app = Flask(__name__)

@app.errorhandler(404)
def errorhandler(error):
    return "Page not found", 404

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('authpages/login.html')


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('authpages/register.html', form=form)


@app.route('/reg-success')
def registerSuccess():
    return render_template('authpages/regsuccess.html')


@app.route('/dashboard')
def dashboard():
    return render_template('userpages/maindashboard.html')


@app.route('/profile-settings')
def profileSettings():
    return render_template('userpages/profilepersonaldetails.html')


@app.route('/history')
def medicalHistory():
    return render_template('userpages/medicalhistory.html')


@app.route('/donation-home')
def donationHome():
    return render_template('donationpages/donationhome.html')


@app.route('/match-success')
def matchSuccess():
    return render_template('donationpages/donationnotify.html')


@app.route('/donation-portal')
def donationPortal():
    return render_template('donationpages/donationportal.html')


@app.route('/request-portal')
def requestPortal():
    return render_template('donationpages/requestportal.html')





if __name__ == '__main__':
    app.run(debug=True)


