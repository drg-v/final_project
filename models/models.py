"""
Module containing SQLAlchemy models

Classes:
    User(db.Model)
    Team(db.model)
    Match(db.model)
"""

from app import db


class User(db.Model):
    """
    A class used to represent User model

    Attributes
    __________
    id_ : db.Integer
        a primary key for user table
    username : db.String(20)
        the name of the user
    password : db.String(90)
        encrypted password of the user
    status : db.String(10)
        the status of the user. Can be active or blocked
    is_subscriber : db.Boolean
        indicates the user`s subscription
    trial_attempts : db.Integer
        the number of free predictions for not subscribed user
    is_admin : db.Boolean
        indicates admin status
    """

    id_ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(90), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    is_subscriber = db.Column(db.Boolean, nullable=False)
    trial_attempts = db.Column(db.Integer, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)


matches = db.Table('matches',
                   db.Column('team_id', db.Integer, db.ForeignKey('team.id_'), primary_key=True),
                   db.Column('match_id', db.Integer, db.ForeignKey('match.id_'), primary_key=True))


class Team(db.Model):
    """
    A class used to represent Team model

    Attributes
    __________
    id_ : db.Integer
        a primary key for team table
    name : db.String(20)
        the name of the team
    goals_for : db.Integer
        the number of goals scored
    goals_against : db.Integer
        the number of goals conceded
    wins : db.Integer
        the number of wins
    losses : db.Integer
        the number of losses
    value : db.Integer
        the value of the team on transfermarkt
    points : db.Integer
        the number of points scored by the team
    matches : db. relationship
        matches of the team
    """

    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    goals_for = db.Column(db.Integer, nullable=False)
    goals_against = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    matches = db.relationship('Match', secondary=matches, lazy='subquery',
                              backref=db.backref('teams', lazy=True))


class Match(db.Model):
    """
    A class used to represent Match model

    Attributes
    __________
    id_ : db.Integer
        a primary key for match table
    date : db.DateTime
        the date of the match
    """

    id_ = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
