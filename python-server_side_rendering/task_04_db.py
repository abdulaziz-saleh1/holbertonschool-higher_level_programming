from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_products_from_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_products_from_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items = []
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception as e:
        print("Error reading items.json:", e)
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error_message = None
    data = []

    if source == 'json':
        data = read_products_from_json('products.json')
    elif source == 'csv':
        data = read_products_from_csv('products.csv')
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if product_id:
                cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
            else:
                cursor.execute("SELECT * FROM Products")

            rows = cursor.fetchall()
            data = [dict(row) for row in rows]
            conn.close()

            if product_id and not data:
                error_message = "Product not found"
        except Exception as e:
            error_message = f"Database error: {e}"
            data = []
    else:
        error_message = "Wrong source. Please use 'json', 'csv', or 'sql'."
        data = []

    return render_template('product_display.html', products=data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
