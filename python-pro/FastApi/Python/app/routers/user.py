from typing import List
import models,schemas,utils,sqlalchemy
from fastapi import Body, FastAPI, Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine,get_db


router=APIRouter(
    prefix="/user",
    tags=['user']

)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):

    hashpassword=utils.hash(user.password)
    user.password=hashpassword
    newuser=models.User(**user.dict())
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"message: the id {id} does not exist")
    return user

@router.get("/",response_model=List[schemas.UserOut])
def get_post(db:Session=Depends(get_db)):
    posts=db.query(models.User).all()
    print(posts)
    return posts

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db)):
    index=db.query(models.User).filter(models.User.id==id)
    if index.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"message:your id {id} does not exist")
    index.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)