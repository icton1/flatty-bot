from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://ict:ictict@localhost/ict")

factory = sessionmaker(bind=engine)
session = scoped_session(factory)

Base = declarative_base()
import models
Base.metadata.create_all(engine)
