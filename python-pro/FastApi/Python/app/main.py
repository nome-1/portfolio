from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from passlib.context import CryptContext
from routers import posts,user,auth,vote
from config import settings


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
models.Base.metadata.create_all(bind=engine)
app=FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welecome to my Api project-1"}


#my_posts=[{"title":"King of fish","content":"content of post","id":1},
          #{"title":"lost cake","content":"content of post","id":2}]

#def find_post(id):
    #cursor.execute("""select * from posts where id=%s""",(str(id)))
    #postsid=cursor.fetchone()
    #return  {"data":postsid}

#def Find_index_post(id):
    #for a,b in enumerate(my_posts):
        #if b["id"]==id:
            #return a

