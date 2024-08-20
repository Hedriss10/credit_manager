from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CreditForm(FlaskForm):
    client_name = StringField('Client Name', validators=[DataRequired()])
    credit_amount = FloatField('Credit Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    submit = SubmitField('Submit')
