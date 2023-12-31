from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import HTTPException, Security
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


security= HTTPBearer()
pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')
secret='SECRET'

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):

    return pwd_context.verify(plain_password, hashed_password)



def encode_token(user_id, user_role):
    payload={
        'exp':datetime.utcnow()+ timedelta(days=1, minutes=5),
        'iat':datetime.utcnow(),
        'sub':user_id, 
        'role':user_role

    }
    return jwt.encode(
        payload,
        secret,
        algorithm='HS256'
    )

def decode_token(token):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        user_id = payload['sub']
        user_role = payload.get('role')
        
        return {
            'id':user_id,
            'role':user_role
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='SU sesión ha finalzado')
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail='Token inválido')

def auth_wrapper(auth: HTTPAuthorizationCredentials= Security(security)):
    user=decode_token(auth.credentials)
    return user