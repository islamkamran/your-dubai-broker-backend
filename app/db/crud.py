import random
from sqlalchemy.orm import Session
from app.db.models import *
from app.helper.emails import send_user_details_to_client

def generate_password():
    return ''.join(random.choices('0123456789', k=6))

def create_user(db: Session, data):
    try:
        newUser = User(**data.model_dump())
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
    except Exception as e:
        return str(e)

    try:
        """Create a notification and store in Notification Table"""
        notification = Notification(
            fk_user_id=newUser.id,
            message=f'New employee {newUser.firstname} has been created by Admin',
            read = False
        )
        db.add(notification)
        db.commit()
    
        send_user_details_to_client(newUser.firstname, newUser.lastname, newUser.email, newUser.original_password, newUser.role)
        # send_user_details_to_admin(new_user.id,new_user.firstname, new_user.lastname, new_user.email, new_user.role)
    
        return newUser.id
    except Exception as e:
        return str(e)
