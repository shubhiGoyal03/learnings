from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required

from security import authentication,identify

app=Flask(__name__)
app.secret_key='jose'
api=Api(app)

jwt= JWT(app,authentication,identify)

items=[]

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field can not be blank")
    @jwt_required()
    def get(self,name):
        item=next(filter(lambda x: x['name']==name,items),None)
        return {"item": item}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x['name']==name,items),None):
            return {"message" : f'An item with name {name} already exists!'}, 400
        data = Item.request.get_json()
        item={
            'name':name,
            'price': data['price']
        }
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items=list(filter(lambda x: x['name']!=name,items))
        return {"message": "Item deleted"}

    def put(self,name):
        data=Item.parser.parse_agrs()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {
                'name': name,
                'price': data['price']
            }
            items.append(item)
        else:
            item.update(data)
        return item


class Items(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')

app.run(debug=True)