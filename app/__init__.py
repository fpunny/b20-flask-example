from flask import Flask
app = Flask(__name__)

from app.pages import home, about