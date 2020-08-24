from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class PayloadForm(FlaskForm):
    payload = StringField('Payload', validators=[validators.input_required(), validators.Length(max=40)])
    submit = SubmitField('Enter')
