# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # initialize SQLA to interact with the DB

def create_app(): # function to create and configure the flask app
    app = Flask(__name__) # creates an instance of the flask app
    # configures flask app with DB URL(instance)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///db.sqlite'
    db.init_app(app) # initialize the AQLA extenson with flask app

    # blueprint from views and registers it with app
    from .views import my_view
    app.register_blueprint(my_view)

    # todo model so its availble when creating DB(tables in DB)
    from .models import Todo
    with app.app_context():
        db.create_all()
    
    return app