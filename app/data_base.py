from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import current_app


db = SQLAlchemy()
db.init_app(current_app)
engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
print 'SQL path', current_app.config['SQLALCHEMY_DATABASE_URI']