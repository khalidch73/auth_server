from sqlmodel import Field, SQLModel 
from typing import Annotated

class AuthServer(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key=True)
    name: str = Field(index=True)
    username : str = Field(index=True)
    email : str = Field(index=True)
    password : str = Field(index=True)
    

# Define a Pydantic model for the user sign-up data
class SignUpData(SQLModel):
    name: Annotated[str, "Name of the user"]
    username: Annotated[str, "Username for authentication"]
    email: Annotated[str, "Email address of the user"]
    password: Annotated[str, "Password for authentication"]

# Define a Pydantic model for the user login data
class LoginData(SQLModel):
    username: Annotated[str, "Username for authentication"]
    password: Annotated[str, "Password for authentication"]