import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
db.init_app(app)
app.config["SLQALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:test123@host.docker.internal:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()