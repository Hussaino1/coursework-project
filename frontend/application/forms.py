from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CourseworkForm(FlaskForm):
    brief = StringField("Coursework Brief", validators=[DataRequired()])
    submit = SubmitField("Add Coursework")