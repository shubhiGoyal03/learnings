from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template("index1.html")
@app.route('/about')
def about():
    name="harry"
    return render_template("about.html",name=name)

@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")

if __name__=="__main__":
app.run(debug=True)
