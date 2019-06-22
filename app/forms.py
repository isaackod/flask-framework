from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length


class SelectionForm(FlaskForm):
    ticker = StringField('Ticker', validators = [DataRequired()])
    group_id = SelectMultipleField(u'Group', choices=[('a', 'b'), ('c', 'd')])
    submit = SubmitField('Do it')

