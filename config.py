from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s >>> %(message)s',
    }},
    'handlers': {
        'console': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':'logging.log',
            'maxBytes':1000000,
            'backupCount': 6,
            'formatter':'default',
        }
    },
    
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']}
})

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nehecode@localhost:5432/student'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ywngitnotw@!'

db  = SQLAlchemy(app)
migrate = Migrate(app,db)

