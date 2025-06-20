from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from app.db.db_setup import get_db
from app.db.models import *
from app.db.schemas import *
from app.db.crud import *
from app.helper.passwordHashing import hashed_password


router = APIRouter()

@router.post("/user/v1/signup")
def Signup(data: UserSchema, db: Session = Depends(get_db)):
    # Make a password
    orignalpassword = generate_password()
    hashedpassword = hashed_password(orignalpassword)

    # convert the data received by schemas to dict to be stored in DB
    data = data.model_dump()
    
    # now as password and orignal was not part of schemas so we add them personaly to the dict
    data["role"] = "default"
    data["original_password"] = orignalpassword
    data["password"] = hashedpassword

    print(f'\nCombined Data: {data}\n')

    newUser = create_user(db, PublishUserSchema(**data))
    
    retval = {
        "message":"User Created Successfully",
        "id": newUser
    }

    return retval