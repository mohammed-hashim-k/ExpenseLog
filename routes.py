# routes.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
from database import Database

# Initialize the Flask app
app = Flask(__name__)

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
    return jsonify({'message': 'Expense added successfully'}), 201

# Get all expenses route
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expense_Database = Database('expenses.db')
    expenses = expense_Database.select('expenses','*')
    return jsonify({'expenses': expenses}), 200

# Get expense by ID route
@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense_by_id(expense_id):
    expense_Database = Database('expenses.db')
    expense = expense_Database.select_where('expenses','*',f'id = {expense_id}')
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
    payment_method_Database.insert('payment_methods','name',f"'{name}'")
    return jsonify({'message': 'Payment method added successfully'}), 201
