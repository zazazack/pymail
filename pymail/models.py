from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, BLOB

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class Mailbox(Base):
    __tablename__: str = 'mailboxes'
    id: int = Column(Integer, primary_key=True)
    name = Column(String)
    items = Column(BLOB)
