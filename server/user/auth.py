import os, jwt

def create_token(user):
    key = os.environ.get("SECRET_KEY")
    payload = {"user_id": user.id}
    token = jwt.encode(payload, key, "HS256")

    return token
