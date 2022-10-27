from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from .page import page

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    app.register_blueprint(page, url_prefix = '/')

    from .apiStuff import apiCall
    teamNames, playerInfo = apiCall()
    #rint(playerInfo)
    create_database(app, playerInfo)
    
    from .models import Players
    newP = Players(playerID = 10, playerName = "Matt Prater", teamShort = "Ravens", position = "K", height = "6'/10", weight = 100, college = "Texas State")
    db.session.add(newP)
    db.session.commit()
    
    exists = Players.query.filter_by(playerID = 10).first() is not None
    print(exists)
    
    return app


def create_database(app, playerInfo):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    
        # from .models import Players

        # for pID, info in playerInfo.items():
        #     # ['Matt Prater', 'ARI', 'K', '5\'10"', 201, '1984-08-10T00:00:00', 'Central Florida']
        #     print(info[0])
        #     newPlayer = Players(playerID = pID, playerName = info[0], teamShort = info[1], position = info[2], height = info[3], weight = info[4], college = info[5])
        #     db.session.add(newPlayer)
        #     db.session.commit()
    
    #idk if we can do this 
    # p1 = Players.query.filter_by(playerID=22501).first()
    # if p1:
    #     print("PLAYER FOUND")
    # else:
    #     print("NOT FOUND")