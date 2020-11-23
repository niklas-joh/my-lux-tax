from slqalchemy import create_engine
from slqalchemy.orm import scoped_session, sessionmaker
from slqalchemy.ext.declarative import declarative_base

engine = create_engine('slqlite:///mydata.db'), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)