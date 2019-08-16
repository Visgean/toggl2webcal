from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://visgean@localhost')

Base = declarative_base()


class TimeEntry(Base):
    __tablename__ = 'time-entry'
    id = Column(Integer, primary_key=True)
    start = Column(TIMESTAMP)
    end = Column(TIMESTAMP)
    description = Column(Text)

    original_id = Column(String(length=128))
    source = Column(String(length=128))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)