from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    def __repr__(self) -> str:
        return super().__repr__()

class Ambulance(db.Model):
    amb_id = db.Column(db.String(20), primary_key=True)
    org_name = db.Column(db.String(1000))
    address = db.Column(db.String(1000))
    phone = db.Column(db.String(20), unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()

class Doctors(db.Model):
    doc_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True)
    specialization = db.Column(db.String(1000))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()

class Hospitals(db.Model):
    hosp_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    website = db.Column(db.String(100))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()

class Medical_cond(db.Model):
    med_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(5000))
    symptoms = db.Column(db.String(5000))
    cure = db.Column(db.String(5000))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()

class blood_req(db.Model):
    blood_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    location = db.Column(db.String(50))
    blood_group = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()