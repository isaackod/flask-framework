from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, widgets
from wtforms.validators import ValidationError, DataRequired, Length, Regexp

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SelectionForm(FlaskForm):
    default_fields  = [('open', 'Open'),
                        ('high', 'High'),
                        ('low', 'Low'),
                        ('close', 'Close'),
                        ('volume', 'Volume')]

    ticker = StringField('Ticker', validators = [DataRequired(), Length(max = 5), Regexp('^[a-zA-Z]+$',message="Ticker should contail only letters.")])
    plot_choices = SelectMultipleField(u'Plot Values (ctrl+click for multiple selection/deslection)', choices=default_fields, default = 'open')
    options = SelectMultipleField(u'Additional Options', choices=[('head', 'Show Table Head'),
                        ('stats', 'Show Stats')])
    submit = SubmitField('Click to return plot.')

