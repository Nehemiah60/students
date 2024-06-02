from flask_wtf import FlaskForm, Form
from wtforms import (StringField, SubmitField, IntegerField, 
                    FileField, PasswordField, DateTimeField, BooleanField)
from wtforms.validators import (DataRequired, Email, 
                                EqualTo, Length, ValidationError)
from flask_wtf.file import FileField, FileAllowed
from models import*

class StudentForm(FlaskForm):
    first_name    = StringField('First Name',  validators=[DataRequired(), Length(min=2, max=20)])
    second_name   = StringField('Second Name', validators=[DataRequired()])
    email         = StringField('Email Address', validators=[DataRequired()])
    image         = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png' ,'jpeg'])])
    fee_paid      = IntegerField('Fee Paid', default=0,validators=[DataRequired()])
    submit        = SubmitField()