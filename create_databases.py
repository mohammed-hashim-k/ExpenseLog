

from database import Database
from schemas import *

def initialize_databases():
    
    # Expense Database
    expense_Database = Database("expenses.db")
    
    expense_Database.createtable("payment_method", payment_method_schema)
    expense_Database.createtable("expenses", expense_schema)
    expense_Database.createtable("users", user_schema)
    expense_Database.close_connections()
    