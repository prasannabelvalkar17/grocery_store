from flask import Flask, jsonify, request
import products_dao
from sql_connection import get_sql_connection
import uom_dao
import json
import orders_dao

app = Flask(__name__)
connection = get_sql_connection()


@app.route("/hello")
def hello():
    return "Hello, How are you?"


@app.route("/getProducts", methods=["GET"])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    return response


@app.route("/deleteProduct", methods=["POST"])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    return response


@app.route("/get_uoms", methods=["GET"])
def get_uoms():
    uoms = uom_dao.get_uoms(connection)
    response = jsonify(uoms)
    return response


@app.route("/insertProduct", methods=["POST"])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    return response


@app.route("/insertOrder", methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    return response


@app.route("/getOrders", methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    return jsonify(response)


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store management System")
    app.run(port=5000)
