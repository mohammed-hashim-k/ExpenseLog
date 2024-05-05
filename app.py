# app.py

from flask import Flask
from routes  import *
from create_databases import initialize_databases


if __name__ == '__main__':
    initialize_databases()
    app.run(debug=True, port=8080, host='localhost')
    