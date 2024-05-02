from contextlib import asynccontextmanager
from typing import Annotated
from app import settings 
from sqlmodel import Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends, HTTPException, Path
from app.models import AuthServer, SignUpData, LoginData


# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)


# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="Auth Server", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

def get_session():
    with Session(engine) as session:
        yield session

# 01 Define the route to read route
@app.get("/")
def read_root():
    return {"Hello World": "This is docker container development"}

# Define a route for user sign-up
@app.post("/signup")
def sign_up(data: SignUpData, session: Session = Depends(get_session)):
    # Check if the username or email already exists
    existing_user = session.exec(select(AuthServer).where(AuthServer.username == data.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = session.exec(select(AuthServer).where(AuthServer.email == data.email)).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Create a new user
    new_user = AuthServer(**data.dict())
    session.add(new_user)
    session.commit()

    return {"message": "User created successfully"}

# Define a route for user login
@app.post("/login")
def login(data: LoginData, session: Session = Depends(get_session)):
    # Retrieve the user from the database based on the provided username
    user = session.exec(select(AuthServer).where(AuthServer.username == data.username)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the provided password matches the user's password
    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    # If the username and password are correct, return a success message
    return {"message": "Login successful"}