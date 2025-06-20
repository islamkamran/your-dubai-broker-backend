from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(userpassword):
    return pwd_context.hash(userpassword)