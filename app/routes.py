
from datetime import datetime
from flask import render_template, flash, redirect,url_for,request
from werkzeug.urls import url_parse
from app import app
from app.forms import SelectionForm
from app.ticker_processing import ticker_df
from bokeh.embed import components
from bokeh.plotting import figure



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SelectionForm()
    raw_table = ""
    script =""
    div = ""
    if form.validate_on_submit(): # false for a GET request
        ticker = form.ticker.data
        stock = ticker_df(ticker)
        raw_table = stock.head().to_html()

        # create a new plot with a title and axis labels
        p = figure(title="simple line example", x_axis_type='datetime',x_axis_label='x', y_axis_label='y')

        # add a line renderer with legend and line thickness
        p.line(stock.date,stock.open, legend="Temp.", line_width=2)

        # Embed plot into HTML via Flask Render
        script, div = components(p)

    return render_template('index.html', title='Home Page', form=form, 
                        raw_table = raw_table,script=script, div=div)


