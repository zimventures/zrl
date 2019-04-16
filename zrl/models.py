from sqlalchemy import Column, Integer, String
from zrl.database import Base


class Mapping(Base):
    __tablename__ = 'mapping'

    id = Column(Integer, primary_key=True)
    tag = Column(String(2048), unique=True)
    url = Column(String(2048), unique=False)
    hits = Column(Integer, default=0)

    def __init__(self, tag=None, url=None):
        self.tag = tag
        self.url = url

    def __repr__(self):
        return f'{self.tag} - {self.url}'
