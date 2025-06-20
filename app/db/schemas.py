from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    firstname: str = Field(None, max_length=255)
    lastname: str = Field(None, max_length=255)
    email: str = Field(None, max_length=255)
    phonenumber: str = Field(None, max_length=255)
    


# some field will not be taken at the time signup the system will make it and will be sent to the client/admin depends on what clients want
class PublishUserSchema(BaseModel):
    role: str = Field(None, max_length=255)
    original_password: str = Field(None, min_length=6)
    password: str = Field(None, min_length=6)


class ResetPasswordRequestSchema(BaseModel):
    email: str


class VerifyOPTSchema(BaseModel):
    email: str
    otp: str


class ResetPasswordSchema(BaseModel):
    email: str
    password: str
    confirm_password: str