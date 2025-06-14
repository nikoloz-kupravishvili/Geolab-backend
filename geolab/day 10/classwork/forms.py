from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,DateField,IntegerField,SelectField,SubmitField,RadioField
from wtforms.validators import DataRequired,length,equal_to
from flask_wtf.file import FileField ,FileRequired,FileAllowed,FileSize





class RegisterForm(FlaskForm):
    image =FileField('pick a profile image',validators=[FileRequired(),FileSize(1024*1024*4),FileAllowed(['jpg', 'png','jpeg',])])
    username = StringField("Enter Username",validators=[DataRequired()])
    password = PasswordField('Enter Password',validators=[DataRequired(), length(min=8,max=64)])
    confirmPassword = PasswordField('confirm Password',validators=[DataRequired(), equal_to('password') ])
    birthdate  = DateField('')
    number = IntegerField('+995 555 55 55 55')
    gender = RadioField('choose gender',choices = ['Male','Female'],validators=[DataRequired()])
    country = SelectField(choices = ['choose country','georgia','japan','uganda'],validators=[DataRequired()])
    submit = SubmitField('Confirm')