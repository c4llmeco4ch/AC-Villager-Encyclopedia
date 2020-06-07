import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Villager(Base):
    __tablename__ = 'villagers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    personality = Column(String)
    species = Column(String)
    birthday = Column(String)
    catchphrase = Column(String)
    hobbies = Column(String)


def fill_tables(s: Session) -> Session:
    pass


def spin_up_db(filePath: str = 'ac-encyclopedia.db') -> Session:
    """If a database at the provided filepath does not exist, create one and insert all villagers

    Keyword Arguments:
        filePath {str} -- Where the database is to be created (default: {'./villagers.sqlite3'})
    """
    engine = create_engine(f'sqlite:///{str}', echo=True)
    names = engine.table_names()
    Session = sessionmaker(bind=engine)
    sess = Session()
    if not names:
        can_create = input('We noticed you have not created the necessary tables.\
                            Would you like them to be initialized (Y/N)? ').lower()
        if can_create != 'y' or can_create != 'yes':
            sys.exit('Aborting due to lack of needed tables...')
        sess = fill_tables(sess)
    return sess
