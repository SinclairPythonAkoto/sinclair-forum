from sqlalchemy.orm import sessionmaker, relationship

# # this part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
meta = MetaData()
engine = create_engine("postgresql://postgres:jason2017@localhost/test_db", echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()HomeHome

from datetime import datetime
# this is added to create a date stamp for SQL
# done in such a way that the data is stored in a String format
# instead of using Date data-type

# database here

class SinTest(Base):
    __tablename__ = 'sin_test'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(20))
    age = Column('age', Integer)
    comment =  Column('comment', String(480))
    stamp = Column('stamp', String(), nullable=False, default = datetime.now().today())
