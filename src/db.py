from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:Polyglot#2019@localhost:3307/db_recipe')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()