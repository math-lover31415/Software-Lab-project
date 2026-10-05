from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False, index=True)
    hashed_password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default="viewer")  # viewer | admin
