
from werkzeug.security import generate_password_hash

from app.extensions import db 
from app.models.user import User


def generate_payload_hash(plain_password: str) -> str:
    return generate_password_hash(plain_password)

def login(payload):
    email = payload.get("email")
    password = payload.get("password")

    if not email or not password:
        return {"error": "email and password are required"}, 400

    hashed_password = generate_payload_hash(password)

    user = User(
        email=email,
        hashed_password=hashed_password,
        role=payload.get("role", "viewer"),
    )

    db.session.add(user)
    db.session.commit()

    return {
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "status": "inserted",
    }