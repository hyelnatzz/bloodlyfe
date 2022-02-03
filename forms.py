from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField,TextAreaField
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[
                        InputRequired(message="first name is required")])
    last_name = StringField("Last Name", validators=[
                        InputRequired(message="last name is required")])
    email = EmailField("Email", validators=[
                        InputRequired(message="email is required")])
    password = PasswordField("Password", validators=[
                        InputRequired(message="password is required"),
                        Length(min=8, message="minimum of 8 characters")])
    phone = TelField("Phone", validators=[InputRequired(message="phone number is required")])
    email = EmailField("Email", validators=[
        InputRequired(message="email is required")])
    address = StringField("Primary Address", validators=[
        InputRequired(message="primary address is required")])
    country = SelectField("Country", choices=[("Nigeria", "Nigeria"),
                                              ("Cameroun", "Cameroun")])
    city = SelectField("City", choices=[("Abuja", "Abuja"),
                                        ("Lagos", "Lagos")])
    bloodgroup = SelectField("Blood Group", choices=[(
        "A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O")])
    rhesus = SelectField("Rhesus Factor", choices=[("+", "+"), ("-", "-")])
    genotype = SelectField("Genotype", choices=[(
        "AA", "AA"), ("AS", "AS"), ("SS", "SS")])
    register = SubmitField("CREATE ACCOUNT")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        InputRequired(message="email is required")])
    password = PasswordField("Password", validators=[
        InputRequired(message="password is required")])
    login = SubmitField("LOG IN")


class ProfileUpdateForm(FlaskForm):
    full_name = StringField("Full Name", validators=[
        InputRequired(message="first name is required")])
    email = EmailField("Email", validators=[
        InputRequired(message="email is required")])
    address = StringField("Primary Address", validators=[
        InputRequired(message="primary address is required")])
    country = SelectField("Country", choices=[("Nigeria", "Nigeria"),
                                            ("Cameroun", "Cameroun")])
    city = SelectField("City", choices=[("Abuja", "Abuja"), 
                                        ("Lagos", "Lagos")])
    blood_group = SelectField("Blood Group", choices=[("A", "A"), ("B", "B"), ("AB", "AB"),("O","O")])
    rhesus = SelectField("Rhesus Factor", choices=[("+", "+"), ("-", "-")])
    genotype = SelectField("Genotype", choices=[("AA", "AA"), ("AS", "AS"), ("SS", "SS")])
    update = SubmitField("Update")

class DonationForm(FlaskForm):
    laboratory = SelectField("Select a Laboratory", choices=[(
        "General Laboratory", "General Laboratory"),
        ("Federal Laboratory", "Federal Laboratory"),
        ("International Laboratory", "International Laboratory"),
        ("Local Laboratory", "Local Laboratory")])
    landmark = SelectField("Landmark", choices=[
            ("Tall Building", "Tall Building")])
    consent = BooleanField("By clicking this box, you have agreed to donate blood and save a life around your landmark")
    donate = SubmitField("Donate")


class RequestForm(FlaskForm):
    hospital = SelectField("Hospital", choices=[(
        "General Hospital", "General Hospital"),
        ("Federal Hospital", "Federal Hospital"),
        ("International Hospital", "International Hospital"), 
        ("Local Hospital", "Local Hospital")])
    landmark = SelectField("Landmark", choices=[("Tall Building", "Tall Building")])
    consent = BooleanField("By clicking this box, you have agreed to donate blood and save a life around your landmark")
    message = TextAreaField("Message")
    request = SubmitField("Request")
