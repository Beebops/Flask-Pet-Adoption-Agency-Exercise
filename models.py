from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app"""
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2015/08/28/15/rexfeatures_845638j.jpg?quality=75&width=1200&auto=webp"

class Pet(db.Model):
    """Model of a Pet"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def get_image_url(self):
        """Returns image for pet or the default photo"""
        return self.photo_url or DEFAULT_IMG_URL
    
    def __repr__(self):
        return f"Pet name: {self.name}, species: {self.species}"