from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#flask.pocoo.org/docs/patterns/sqlalchemy

engine = create_engine('sqlite:///looreview.db', convert_unicode=True)
getsession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    #import all modules here that define models for the create_all
    import loo.models
    Base.metadata.create_all(bind=engine)
    print "Ok, created tables"

