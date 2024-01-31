from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


Base = declarative_base()
engine = create_engine('sqlite:///scoreboard.db')
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    timer = Column(Integer)
    status = Column(String(10))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()