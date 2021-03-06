from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
from app import views

file_handler = RotatingFileHandler('application.log', 'w', 1 * 1024 * 1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info('Application startup')
