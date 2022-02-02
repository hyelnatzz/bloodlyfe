from flask import Flask


app = Flask(__name__)

@app.errorhandler(404)
def errorhandler(error):
    return "Page not found", 404

@app.route('/')
def index():
    return "Homepage"


@app.route('/login')
def login():
    return "login page"


@app.route('/register')
def register():
    return "Registration Page"


@app.route('/reg-success')
def registerSuccess():
    return "Registration Success Page"


@app.route('/dashboard')
def dashboard():
    return "Main Dashboard"


@app.route('/profile-settings')
def profileSettings():
    return "Profile settings Page"


@app.route('/donation-home')
def donationHome():
    return "Donation Homepage"


@app.route('/match-success')
def matchSuccess():
    return "Match Success Page"


@app.route('/donation-portal')
def donationPortal():
    return "Donation Portal Page"


@app.route('/request-portal')
def requestPortal():
    return "Request Portal Page"


@app.route('/history')
def medicalHistory():
    return "Medical History Page"


if __name__ == '__main__':
    app.run(debug=True)


