from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class MundialFootball(Base):
    __tablename__ = 'mundial2018'
    id = Column(Integer, primary_key=True)
    fifa_display_name = Column(String, nullable=false)
    country = Column(String, nullable=false)
    last_name = Column(String, nullable=false)
    first_name = Column(String, nullable=false)
    shirt_name = Column(String, nullable=false)
    pos = Column(String, nullable=false)
    height = Column(Integer, nullable=false)
    caps = Column(Integer, nullable=false)
    goals = Column(Integer, nullable=false)
   
    
    def __repr__(self):
        return "Mundial 2018: Fifa display name=%s - Country=%s - Last Name=%s -  First Name=%s - Shirt Name=%s - Pos=%s - Height =%d - Caps=%d - Goals=%d \n" % (
                          self.fifa_display_name, 
                          self.country,
                          self.last_name,
                          self.first_name,
                          self.shirt_name,
                          self.pos,
                          self.height,
                          self.caps,
                          self.goals)

Base.metadata.create_all(engine)