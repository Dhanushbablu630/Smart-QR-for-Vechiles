from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    vehicles = db.relationship('Vehicle', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    phone_shared = db.Column(db.Boolean, default=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    messages = db.relationship('Message', backref='vehicle', lazy=True)
    contact_requests = db.relationship('ContactRequest', backref='vehicle', lazy=True)
    trip_photos = db.relationship('TripPhoto', backref='vehicle', lazy=True)
    incident_reports = db.relationship('IncidentReport', backref='vehicle', lazy=True)
    albums = db.relationship('Album', backref='vehicle', lazy=True)
    #new feature
class MedicalInfo(db.Model):
    __tablename__ = 'medical_info'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    blood_type = db.Column(db.String(10))  # A+, B-, O+, etc.
    medical_conditions = db.Column(db.Text)  # Diabetes, Heart condition, etc.
    allergies = db.Column(db.Text)  # Drug allergies, food allergies
    emergency_medication = db.Column(db.Text)  # Insulin, EpiPen, etc.
    emergency_contact_name = db.Column(db.String(100))
    emergency_contact_phone = db.Column(db.String(20))
    emergency_contact_relation = db.Column(db.String(50))  # Spouse, Parent, Child, etc.
    
    # Relationship back to vehicle
    vehicle = db.relationship('Vehicle', backref='medical_info')

class MaintenanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    service_type = db.Column(db.String(100))
    service_date = db.Column(db.Date)
    next_due_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    vehicle = db.relationship('Vehicle', backref='maintenance_records')

class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

    photos = db.relationship('TripPhoto', backref='album', lazy=True, cascade='all, delete-orphan')


class TripPhoto(db.Model):
    __tablename__ = 'trip_photo'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100))
    is_pinned = db.Column(db.Boolean, default=False)

    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100))
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)


class ContactRequest(db.Model):
    __tablename__ = 'contact_request'
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)


class IncidentReport(db.Model):
    __tablename__ = 'incident_report'
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    image_filename = db.Column(db.String(100))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
