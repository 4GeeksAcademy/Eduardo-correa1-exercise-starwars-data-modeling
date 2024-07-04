import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'   
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    contraseña = Column(String(250), nullable=False)
    fecha_sub = Column(DateTime, nullable=False)

    favoritos = relationship('Favorito', back_populates='usuario')


class Personaje(Base):
    __tablename__ = 'personaje'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    descripcion = Column(String(250))

    favoritos = relationship('Favorito', back_populates='personaje')


class Planeta(Base):
    __tablename__ = 'planeta'
    id_planeta = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    descripcion = Column(String(250))

    favoritos = relationship('Favorito', back_populates='planeta')


class Favorito(Base):
    __tablename__ = 'favorito'
    id_favorito = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id_personaje'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id_planeta'), nullable=True)

    usuario = relationship('Usuario', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')