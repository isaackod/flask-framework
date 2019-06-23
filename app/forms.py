from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, widgets
from wtforms.validators import ValidationError, DataRequired, Length

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SelectionForm(FlaskForm):
    default_fields  = [('open', 'open'),
                        ('high', 'high'),
                        ('low', 'low'),
                        ('close', 'close'),
                        ('volume', 'volume'),
                        ('ex-dividend', 'ex-dividend'),
                        ('split_ratio', 'split_ratio'),
                        ('adj_open', 'adj_open'),
                        ('adj_high', 'adj_high'),
                        ('adj_low', 'adj_low'),
                        ('adj_close', 'adj_close'),
                        ('adj_volume', 'adj_volume')]
    ticker = StringField('Ticker', validators = [DataRequired(), Length(max = 5)])
    plot_choices = MultiCheckboxField(u'Plot Values', choices=default_fields, default = 'open')
    options = MultiCheckboxField(u'Additional Options', choices=[('head', 'Show Table Head'),
                        ('stats', 'Show Stats')])
    submit = SubmitField('Do it')

