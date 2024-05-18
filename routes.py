# routes.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
from database import Database
import hashlib
import logging

# Initialize the Flask app
app = Flask(__name__)

logging.basicConfig(filename="app.log", level = logging.INFO)

@app.before_request
def log_request_info():
    logging.info('Request URL: %s', request.url)
    logging.info('Request method: %s', request.method)
    logging.info('Request data: %s', request.data)

@app.after_request
def log_response_info(response):
    logging.info('Response status: %s', response.status_code)
    return response



# Register user route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    password = hashlib.md5(password.encode()).hexdigest()
    
    user_Database = Database('expenses.db')
    user_Database.insert('users','username, password',f"'{username}', '{password}'")
    user_Database.close_connections()
    return jsonify({'message': 'User registered successfully'}), 201

# Login user route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    password = hashlib.md5(password.encode()).hexdigest()
    
    user_Database = Database('expenses.db')
    user = user_Database.select_where('users','*',f"username = '{username}' AND password = '{password}'")
    user_Database.close_connections()
    if user:
        return jsonify({'message': 'User logged in successfully'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401



# Add expense route
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    category = data.get('category')
    amount = data.get('amount')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    shop_name = data.get('shop_name')
    description = data.get('description')
    currency = data.get('currency')
    payment_method = data.get('payment_method')
    location = data.get('location')
    receipt_url = data.get('receipt_url')
    
    expense_Database = Database('expenses.db')
    expense_Database.insert('expenses','category, amount, date, shop_name, description, currency, payment_method, location, receipt_url',
                            f"'{category}', {amount}, '{date}', '{shop_name}', '{description}', '{currency}', '{payment_method}', '{location}', '{receipt_url}'")
    expense_Database.close_connections()
    return jsonify({'message': 'Expense added successfully'}), 201

# Get all expenses route
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expense_Database = Database('expenses.db')
    expenses = expense_Database.select('expenses','*')
    expense_Database.close_connections()
    return jsonify({'expenses': expenses}), 200

# Get expense by ID route
@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense_by_id(expense_id):
    expense_Database = Database('expenses.db')
    expense = expense_Database.select_where('expenses','*',f'id = {expense_id}')
    expense_Database.close_connections()
    if expense:
        return jsonify({'expense': expense}), 200
    else:
        return jsonify({'message': 'Expense not found'}), 404

# Add payment method route
@app.route('/payment_methods', methods=['POST'])
def add_payment_method():
    data = request.get_json()
    name = data.get('name')
    
    payment_method_Database = Database('expenses.db')
    payment_method_Database.insert('payment_method','name',f"'{name}'")
    payment_method_Database.close_connections()
    return jsonify({'message': 'Payment method added successfully'}), 201

# Get all payment methods route
@app.route('/payment_methods', methods=['GET'])
def get_payment_methods():
    payment_method_Database = Database('expenses.db')
    payment_methods = payment_method_Database.select('payment_method','*')
    payment_method_Database.close_connections()
    return jsonify({'payment_method': payment_methods}), 200

