from flask import Flask, render_template
from forms import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

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
        print(form.email.data)
    return render_template('authpages/login.html', form = form)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.phone.data)
    return render_template('authpages/register.html', form=form)


@app.route('/reg-success')
def registerSuccess():
    return render_template('authpages/regsuccess.html')


@app.route('/dashboard')
def dashboard():
    return render_template('userpages/maindashboard.html')


@app.route('/profile-settings', methods=["POST", "GET"])
def profileSettings():
    form = ProfileUpdateForm()
    return render_template('userpages/profilepersonaldetails.html', form = form)


@app.route('/history')
def medicalHistory():
    return render_template('userpages/medicalhistory.html')


@app.route('/donation-home')
def donationHome():
    return render_template('donationpages/donationhome.html')


@app.route('/match-success')
def matchSuccess():
    return render_template('donationpages/donationnotify.html')


@app.route('/donation-portal', methods=["POST", "GET"])
def donationPortal():
    form = DonationForm()
    if form.validate_on_submit():
        print("done")
    return render_template('donationpages/donationportal.html', form = form)


@app.route('/request-portal', methods=["POST", "GET"])
def requestPortal():
    form = RequestForm()
    if form.validate_on_submit():
        print("done")
    return render_template('donationpages/requestportal.html', form = form)





if __name__ == '__main__':
    app.run(debug=True)


