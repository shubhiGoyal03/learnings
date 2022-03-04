from flask import Flask
from flask import escape

app=Flask(__name__)

@app.route('/')
def f1():
    return "Hey f1"

@app.route('/1')
def f2():
    return "<hey"

@app.route('/2')
def f3():
    return "hey>"

@app.route('/3')
def f4():
    return "& Hey"

@app.route('/4')
def f5():
    return "&copy hey"

@app.route('/5')
def f6():
    return escape("&copy hey")

@app.route('/6')
def f7():
    return "<h1> hey </h1>"

@app.route('/7')
def f8():
    return escape("<h1> hey </h1>")

if __name__=="__main__":
    app.run(debug=True)
