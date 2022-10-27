from . import db


class Players(db.Model):
    playerID = db.Column(db.Integer, primary_key = True)
    playerName = db.Column(db.String(100))
    teamShort = db.Column(db.String(50))
    #teamName = db.Column(db.String(100))
    position = db.Column(db.String(10))
    height = db.Column(db.String(10))
    weight = db.Column(db.Integer)
    college = db.Column(db.String(50))

    
    