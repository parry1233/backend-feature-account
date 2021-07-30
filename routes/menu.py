from flask import jsonify, request
from . import routes, db
import json
from bson import json_util


# factory table 
# {
#     name: (string)
#     stores: []
# }

# menu table
# {
#     store: (string)
#     drinks: []
# }

@routes.route('/Menu/ListFactory/', methods=['GET'])
def show_all_factories():
    fab_table = db['factory']
    menu_table = db['menu']
    
    output = {}

    for fab in fab_table.find():
        store_menu = {}
        for store in fab['stores']:
            fd_dr = menu_table.find({'name': store}, { "_id": 0, "name": 0 })[0]
            store_menu[store] = fd_dr

        output[fab['name']] = store_menu
    

    result = json.loads(json_util.dumps(output))
    return result

@routes.route('/Menu/ListRestaurant/<string:fab>', methods=['GET'])
def list_restaurants(fab):
    fab_table = db['factory']
    menu_table = db['menu']

    store_list = fab_table.find({'name': fab}, {"_id": 0, "name": 0})[0]

    output = {}

    for store in store_list['stores']:
        fd_dr = menu_table.find({'name': store}, {'_id': 0, 'name': 0})[0]
        output[store] = fd_dr['food_drink']
    
    return output