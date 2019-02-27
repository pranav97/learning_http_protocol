from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    @property
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id
        }


engine = create_engine('sqlite:///city.db')
Base.metadata.create_all(engine)
