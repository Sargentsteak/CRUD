from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = 'postgresql://postgres:123@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True: 
#     try :
#         conn  = psycopg2.connect(host = 'localhost' , database = 'fastapi' , user = 'postgres', password = '123' , cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print( "Error : " , error)
#         time.sleep(2)
