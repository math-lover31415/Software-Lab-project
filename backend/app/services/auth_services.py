
def login(payload):
    return {
        "access_token": None,
        "email": payload.get("email"),
        "status": "stub",
    }
