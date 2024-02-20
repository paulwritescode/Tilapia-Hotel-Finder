from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime
import uuid

class Restaurants(Base):
    __tablename__ = 'restaurants'
    id = Column(String(64), primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(100), nullable=True)
    site_url = Column(String(200), nullable=True)
    draw = Column(Integer(), default=0)
    created_time = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)
    modified_time = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, name, description, site_url):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.site_url = site_url

    def __repr__(self):
        return '<Restaurant %r>' % (self.name)
