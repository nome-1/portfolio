from typing import List,Optional

from sqlalchemy import func
import models,schemas,oauth2
from fastapi import Body, FastAPI, Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine,get_db


router=APIRouter(
    prefix="/post",
    tags=['post']
)


@router.get("/",response_model=List[schemas.PostOut])
def get_post(db:Session=Depends(get_db),
             currentUser:int=Depends(oauth2.get_current_user),Limit:int=10,skip:int=0,search:Optional[str]=""):
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    return posts
    #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    #print(posts)
#def get_post():
    #cursor.execute("""select * from posts""")
    #posts=cursor.fetchall()

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(new_post:schemas.PostCreate,db:Session=Depends(get_db),
                currentUser:int=Depends(oauth2.get_current_user)):
    npost=models.Post(owner_id=currentUser.id,**new_post.dict())
    db.add(npost)
    db.commit()
    db.refresh(npost)
#def create_post(new_post:Post):
    #cursor.execute("""insert into posts (title,content,published) values(%s,%s,%s)
     #returning * """,(new_post.title,new_post.content,new_post.publish))
   # npost=cursor.fetchone()
    #con.commit()
    return npost

@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id:int,db:Session=Depends(get_db),currentUser:int=Depends(oauth2.get_current_user)):
    #ThePost=find_post(id)
    #ThePost=db.query(models.Post).filter(models.Post.id==id).first()
    #print(ThePost)
    ThePost = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    if ThePost==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"message: the id {id} does not exist")
    return ThePost

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),currentUser:int=Depends(oauth2.get_current_user)):
    #cursor.execute("""delete from posts where id=%s returning*""",(str(id)))
    #index=cursor.fetchone()
    #con.commit()
    index_query=db.query(models.Post).filter(models.Post.id==id)
    index=index_query.first()
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"message:your id {id} does not exist")
    if index.owner_id !=currentUser.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allowed")
    index_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,new_post:schemas.PostBase,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    #cursor.execute("""update posts set title=%s,content=%s,published=%s where id=%s
     #returning * """,(new_post.title,new_post.content,new_post.publish,str(id)))
    #index=cursor.fetchone()
    #con.commit()
    pq=db.query(models.Post).filter(models.Post.id==id)
    index=pq.first()
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"message:your id {id} does not exist")
    
    if index.owner_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allowed")
    pq.update(new_post.dict(),synchronize_session=False)
    db.commit()
    return pq.first()