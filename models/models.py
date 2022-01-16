from app import db


class User(db.Model):
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
    id_ = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
