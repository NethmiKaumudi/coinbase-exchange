# /trading/app/app.py

from flask import Flask
from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5002)
