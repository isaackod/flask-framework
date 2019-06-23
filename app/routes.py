
from datetime import datetime
from flask import render_template, flash, redirect,url_for,request
from werkzeug.urls import url_parse
from app import app
from app.forms import SelectionForm
from app.ticker_processing import ticker_df
from bokeh.embed import components
from bokeh.plotting import figure
import pandas as pd



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SelectionForm()
    head_prev, summary = "", ""
    script =""
    div = ""
    if form.validate_on_submit(): # false for a GET request
        ticker = form.ticker.data
        stock = ticker_df(ticker)
        stock = stock[stock.date>= stock.date.max()-pd.Timedelta(days=30)]  # could also request less data... should probably cache this so we don't make an api call every time
        print(form.options.data)
     
        if stock.size > 0 and form.plot_choices.data: # valid ticker returns a table
            head_prev = stock.head().to_html()
            summary = stock.describe().to_html()
             # create a new plot with a title and axis labels
            p = figure(title="Stock Market Data", x_axis_type='datetime',x_axis_label='Date')
            p.xaxis.axis_label_text_font_size = "18pt"
            p.xaxis.axis_label_text_font = "times"
            p.yaxis.axis_label_text_font_size = "18pt"
            p.yaxis.axis_label_text_font = "times"
            p.xaxis.major_label_text_font_size = "12pt"
            p.yaxis.major_label_text_font_size = "12pt"
            p.title.text_font_size="22pt"
            colors = iter(['red','green','blue','olive', 'darkgrey'])
            for data in form.plot_choices.data:
                if data == 'volume':
                    p.line(stock.date,stock[data], legend="Volume (number of trades)", line_width=2, color = next(colors))
                    p.yaxis.axis_label = ""
                else:
                # add a line renderer with legend and line thickness
                    p.line(stock.date,stock[data], legend=data+" USD($)", line_width=2,color = next(colors))
        
                    p.yaxis.axis_label = "USD($)"
            # Embed plot into HTML via Flask Render
            script, div = components(p)
        elif stock.size == 0:
            form.ticker.errors.append("No valid ticker found with that name!")
        else: 
            form.plot_choices.errors.append("Please select at least one thing to plot.")

    return render_template('index.html', title='Home Page', form=form, 
                        head_prev = head_prev,summary = summary,script=script, div=div)


