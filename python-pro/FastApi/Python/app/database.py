from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from config import settings

sqlalacmey_databass_url=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine=create_engine(sqlalacmey_databass_url)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#while True:
   #try:
        #con=psycopg2.connect(host='localhost',database='fastapi',user='postgres',
       #password='kinkgbbrom3',cursor_factory=RealDictCursor)
        #cursor=con.cursor()
        #print("database connection was succesful")
        #break
    #except Exception as error:
        #print("database failed to connect")
        #print("Error:",error)
        #time.sleep(5)