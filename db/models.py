from .database import Base
from sqlalchemy import Column, Integer, String

#Creal la clase modelo(Entidad)
class Categoria(Base):
    __tablename__= "categorias"
    id = Column(Integer, primary_key=True,)

    nombre = Column(String(50))