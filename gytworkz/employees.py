from flask import Flask, jsonify
import json
app=Flask(__name__)

data=open("EmployeeData.json").read()
data=json.loads(data)


@app.route('/')
def employees():
    return jsonify(data)

@app.route('/employee/<int:id>')
def employee(id):
    result=json.loads(json.dumps(list(filter(lambda x:x["id"]==id,data))))
    if len(result)==0:
        return "No such user!"
    else:
        return jsonify(result)

@app.route('/female')
def female():
    return jsonify(json.loads(json.dumps(list(filter(lambda x:x["gender"]==1,data)))))

@app.route('/male')
def male():
    return jsonify(json.loads(json.dumps(list(filter(lambda x:x["gender"]==0,data)))))


if __name__=="__main__":
    app.run(debug=True)
