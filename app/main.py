from fastapi import FastAPI
from .import models
from .database import engine
from .routers import journal, user, mood, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

print(settings.database_hostname)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(journal.router)
app.include_router(user.router)
app.include_router(mood.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}




