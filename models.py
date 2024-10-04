from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
#from flask import Flask
#from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash
#from datetime import datetime



db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Player(db.Model):

    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    age = db.Column(db.)
    height
    weight
    college
    group
    position
    number
    salary
    experience
    image
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Applicant {self.username}>'


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    industry = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    applicants = db.relationship('Applicant', backref='company')
    jobs = db.relationship('Job', backref='company')
    interviews = db.relationship('Interview', backref='company_int')

    def __repr__(self):
        return f'<Company {self.name}>'



class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.Text, nullable=False)
    job_title = db.Column(db.Text, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    applications = db.relationship('Applied', backref='applicant')
    tasks = db.relationship('Task', backref='applicant_list')


    def __repr__(self):
        return f'<Applicant {self.username}>'
    
class Player_Stats(db.Model):

    __tablename__ = "players_stats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Applied applicant_id={self.application_id} job_id={self.job_id} applied_at={self.applied_at}>'

class Team_Stats(db.Model):

    __tablename__ = "teams_stats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Task id={self.id} notes={self.notes}>'