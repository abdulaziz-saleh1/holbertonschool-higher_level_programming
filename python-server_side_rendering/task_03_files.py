#!/usr/bin/python3
"""Flask app to display product data from JSON or CSV files."""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        print("Error reading JSON:", e)
        return []

def read_csv():
    products = []
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                products.append(product)
    except Exception as e:
        print("Error reading CSV:", e)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    data = []

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id is not None:
        filtered = [p for p in data if p["id"] == product_id]
        if not filtered:
            error = "Product not found"
        data = filtered

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
