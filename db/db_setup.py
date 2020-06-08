import sys
import ac_villager_types.parse_villagers as pv
from sqlalchemy import create_engine, Engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Villager(Base):
    __tablename__ = 'villagers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    personality = Column(String)
    species = Column(String)
    birthday = Column(String)
    catchphrase = Column(String)
    hobbies = Column(String)


def fill_tables(e: Engine) -> Session:
    Base.metadata.create_all(e)
    Session = sessionmaker(bind=e)
    sess = Session()
    vills = pv.find_villager_list()
    for name, attr in vills.items():
        current = Villager(
            name=name,
            personality=attr[0],
            species=attr[1],
            birthday=attr[2],
            catchphrase=attr[3],
            hobbies=attr[4]
        )
        sess.add(current)
    sess.commit()
    return sess


def spin_up_db(filePath: str = 'ac-encyclopedia.db') -> Session:
    """
    If a database at the provided filepath does not exist,
    create one and insert all villagers

    Keyword Arguments:
        filePath {str} -- Where the database is to be created (
            default: {'ac-encyclopedia.db'})
    """
    engine = create_engine(f'sqlite:///{str}', echo=True)
    names = engine.table_names()
    if not names:
        can_create = input('We noticed you have not created the necessary tables.\
                            Allow for initialization? (Y/N) ').lower()
        if can_create != 'y' or can_create != 'yes':
            sys.exit('Aborting due to lack of needed tables...')
        sess = fill_tables(engine)
    else:
        Session = sessionmaker(bind=engine)
        sess = Session()
    return sess
