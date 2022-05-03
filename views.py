
from flask import Flask,render_template


app=Flask(__name__)


@app.route('/')
def home():
    name='News is news'
    title='News is news'
    return render_template("index.html",name=name,title=title)