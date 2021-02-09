from flask import Flask, request, render_template
from markupsafe import escape
app =Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return render_template('hello.html', name=name)
if __name__=="__main__":
    app.run()
