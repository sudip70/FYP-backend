import imp
import os
from flask import Flask, request
from flask_jwt_extended import JWTManager
from src.signup import signup_blueprint
from src.login import login_blueprint
from src.ambulances import ambulance_blueprint
from src.profile import profile_blueprint
from src.doctors import doctors_blueprint
from src.hospitals import hospitals_blueprint
from src.covid import covid_blueprint
from src.hiv import hiv_blueprint
from src.std import std_blueprint
from src.med_condition import med_condition_blueprint
from flask_sqlalchemy import SQLAlchemy
from src.medicsdb import db, Users


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,

            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(signup_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(ambulance_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(doctors_blueprint)
    app.register_blueprint(hospitals_blueprint)
    app.register_blueprint(covid_blueprint)
    app.register_blueprint(hiv_blueprint)
    app.register_blueprint(std_blueprint)
    app.register_blueprint(med_condition_blueprint)


    @app.route("/")
    def index():
        return {
            "Login": "/login/ [POST]",
            "Signup": "/signup/ [POST]",
            "Profile": "/profile/ [GET]",
            "Ambulance": "/ambulances/ [GET]",
            "Covid": "/covid/ [GET]",
            "Doctors": "/doctors/ [GET]",
            "Feedback": "/feedback/ [POST]",
            "HIV": "/hiv/ [GET]",
            "Hospitals": "/hospitals/ [GET]",
            "Medical Conditions": "/med_condition/ [GET]",
            "STD": "/std/ [GET]"
        }

    db.app = app
    db.init_app(app)

    JWTManager(app)

    return app

