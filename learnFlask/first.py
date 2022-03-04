from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "<p>Hey! Welcome to Flask World!</p>"

app.run(debug=True)
