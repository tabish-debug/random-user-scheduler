from web import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='country', lazy=True)

    def __str__(self) -> str:
        return self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    def __str__(self) -> str:
        return self.name