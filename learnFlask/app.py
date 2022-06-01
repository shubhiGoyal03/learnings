from flask import Flask, jsonify, request, render_template

app=Flask(__name__)
stores=[
    {
        'name': "D mart",
        'items': [
            {
                'name': "Coke",
                'price': 35
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index1.html')
#POST: to create store
@app.route('/store', methods=['POST'])
def create_post():
    request_data=request.get_json()
    new_data={
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_data)
    return jsonify(new_data)

#GET: to send store details
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name==store['name']:
            return jsonify(store)
    return jsonify({"message": "Store not found"})

#GET: to get all stores
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})

#POST: to create item in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if name==store['name']:
            new_data = {
                'name': request_data['name'],
                'price': []
            }
            store['items'].append(new_data)
            return jsonify(new_data)
    return jsonify({"message": "Store not found"})

#GET: to get items in store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if name==store['name']:
            return jsonify({"items": store['items']})
    return jsonify({"message": "Store not found"})


app.run(port=5000)