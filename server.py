from flask import Flask, request
import json
from http import HTTPStatus

app = Flask(__name__)

catalog = []

@app.get('/')
def welcome():
    return "Welcome to the Product Catalog"

@app.get('/api/catalog')
def get_catalog():
    return json.dumps(catalog)

@app.post('/api/catalog')
def add_product():
    product = request.json
    catalog.append(product)
    return json.dumps({"message": "Product added successfully"}), 201

@app.get('/api/reports/total')
def get_total_value():
    total_value = sum(item.get('price', 0) * item.get('quantity', 1) for item in catalog)
    return json.dumps({"total_value": total_value})

@app.get('/api/products/<category>')
def get_products_by_category(category):
    filtered_products = [product for product in catalog if product.get('category') == category]
    return json.dumps(filtered_products)


app.run(debug=True)
