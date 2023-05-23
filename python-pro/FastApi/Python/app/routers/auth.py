
from typing import List
import models,schemas,utils,oauth2
from fastapi import Body, FastAPI, Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine,get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(
    tags=['Authentication']
)

@router.post("/login",response_model=schemas.Token)
def login(credentials: OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):

    user=db.query(models.User).filter(models.User.email==credentials.username).first()
    print(credentials)
    print(user)

    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"message: the user id {id} does not exist")
    
    if not utils.cerify(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"message: the user password {id} does not exist")
    
    access_token=oauth2.create_access_token(data={"user_id":user.id})


    return {"token":access_token,"token_type":"bear"}