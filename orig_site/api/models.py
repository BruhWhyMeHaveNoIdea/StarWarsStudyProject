from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Таблица для связи многие-ко-многим между персонажами и фильмами
character_film = Table(
    'character_film',
    Base.metadata,
    Column('character_id', Integer, ForeignKey('characters.id')),
    Column('film_id', Integer, ForeignKey('films.id'))
)

# Таблица для связи многие-ко-многим между персонажами и кораблями
character_starship = Table(
    'character_starship',
    Base.metadata,
    Column('character_id', Integer, ForeignKey('characters.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

# Таблица для связи многие-ко-многим между персонажами и транспортом
character_vehicle = Table(
    'character_vehicle',
    Base.metadata,
    Column('character_id', Integer, ForeignKey('characters.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    height = Column(Integer)  # в сантиметрах
    mass = Column(Float)  # в килограммах
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    species = Column(String)
    homeworld = Column(String)
    
    # Связи
    films = relationship("Film", secondary=character_film, back_populates="characters")
    starships = relationship("Starship", secondary=character_starship, back_populates="pilots")
    vehicles = relationship("Vehicle", secondary=character_vehicle, back_populates="pilots")

class Film(Base):
    __tablename__ = "films"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    episode_id = Column(Integer)
    opening_crawl = Column(String)
    director = Column(String)
    producer = Column(String)
    release_date = Column(Date)
    
    characters = relationship("Character", secondary=character_film, back_populates="films")

class Starship(Base):
    __tablename__ = "starships"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(Float)  # в метрах
    max_atmosphering_speed = Column(String)
    crew = Column(String)
    passengers = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    hyperdrive_rating = Column(String)
    MGLT = Column(String)  # MegaLight per hour
    starship_class = Column(String)
    
    pilots = relationship("Character", secondary=character_starship, back_populates="starships")

class Vehicle(Base):
    __tablename__ = "vehicles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    length = Column(Float)  # в метрах
    max_atmosphering_speed = Column(String)
    crew = Column(String)
    passengers = Column(String)
    cargo_capacity = Column(String)
    consumables = Column(String)
    vehicle_class = Column(String)
    
    pilots = relationship("Character", secondary=character_vehicle, back_populates="vehicles")