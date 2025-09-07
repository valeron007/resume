import jwt
import time


def decode_jwt(token: str) -> dict:
    try:        
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])        
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:        
        return {}