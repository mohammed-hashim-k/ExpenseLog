# database.py

import sqlite3

class Database:
    def __init__ (self,db_name):
        print("Database : ",db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    
            
    def createtable(self,table_name,table_schema):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
            {table_schema}
        )
        ''')
        self.conn.commit()
        
    def insert(self,table_name,columns,values):
        self.cursor.execute(f'''
            INSERT INTO {table_name} ({columns})
            VALUES ({values})
        ''')
        self.conn.commit()
        
    def select(self,table_name,columns):
        self.cursor.execute(f'''
            SELECT {columns} FROM {table_name}
        ''')
        return self.cursor.fetchall()

        
    def select_where(self,table_name,columns,condition):
        self.cursor.execute(f'''
            SELECT {columns} FROM {table_name} WHERE {condition}
        ''')
        return self.cursor.fetchall()

        
    def update(self,table_name,columns,values,condition):
        self.cursor.execute(f'''
            UPDATE {table_name} SET {columns} = {values} WHERE {condition}
        ''')
        self.conn.commit()
   
    def delete(self,table_name,condition):
        self.cursor.execute(f'''
            DELETE FROM {table_name} WHERE {condition}
        ''')
        self.conn.commit()
 
    
