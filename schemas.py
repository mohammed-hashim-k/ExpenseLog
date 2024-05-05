
payment_method_schema = "name TEXT PRIMARY KEY NOT NULL"


expense_schema = "id INTEGER PRIMARY KEY AUTOINCREMENT,\
        category TEXT NOT NULL,\
        amount REAL NOT NULL,\
        date TEXT NOT NULL,\
        shop_name TEXT,\
        description TEXT,\
        currency TEXT NOT NULL DEFAULT 'INR',\
        payment_method TEXT,\
        location TEXT,\
        receipt_url TEXT,\
        FOREIGN KEY (payment_method) REFERENCES payment_methods(name)"