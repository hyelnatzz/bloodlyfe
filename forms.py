from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import InputRequired, Length


class RegisterForm(Form):
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
    register = SubmitField("Register")


class ProfileUpdateForm(Form):
    full_name = StringField("Full Name", validators=[
        InputRequired(message="first name is required")])
    email = EmailField("Email", validators=[
        InputRequired(message="email is required")])
    address = StringField("Primary Address", validators=[
        InputRequired(message="primary address is required")])
    country = SelectField("Country", choices=[])
    city = SelectField("City", choices=[])
    blood_group = SelectField("Blood Group", choices=[])
    rhesus = SelectField("Rhesus Factor", choices=[])
    genotype = SelectField("Genotype", choices=[])
    update = SubmitField("Update")

class DonationForm(Form):
    laboratory = SelectField("Laboratory", choices=[])
    landmark = SelectField("Landmark", choices=[])
    consent = BooleanField("By clicking this box, you have agreed to donate blood and save a life around your landmark")
    donate = SubmitField("Donate")


class RequestForm(Form):
    hospital = SelectField("Hospital", choices=[])
    landmark = SelectField("Landmark", choices=[])
    consent = BooleanField("By clicking this box, you have agreed to donate blood and save a life around your landmark")
    request = SubmitField("Request")
