import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'hbsfyhwfv34yhv23j4hvyhv234'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# JWT создает токен
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire.isoformat()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
