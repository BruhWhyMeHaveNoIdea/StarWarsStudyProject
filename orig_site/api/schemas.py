from pydantic import BaseModel
from datetime import date
from typing import List, Optional

# Character Schemas
class CharacterBase(BaseModel):
    name: str
    height: Optional[int] = None
    mass: Optional[float] = None
    hair_color: Optional[str] = None
    skin_color: Optional[str] = None
    eye_color: Optional[str] = None
    birth_year: Optional[str] = None
    gender: Optional[str] = None
    species: Optional[str] = None
    homeworld: Optional[str] = None

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int
    film_ids: List[int] = []
    starship_ids: List[int] = []
    vehicle_ids: List[int] = []
    
    class Config:
        orm_mode = True

# Film Schemas
class FilmBase(BaseModel):
    title: str
    episode_id: Optional[int] = None
    opening_crawl: Optional[str] = None
    director: Optional[str] = None
    producer: Optional[str] = None
    release_date: Optional[date] = None

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    id: int
    character_ids: List[int] = []
    
    class Config:
        orm_mode = True

# Starship Schemas
class StarshipBase(BaseModel):
    name: str
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    cost_in_credits: Optional[str] = None
    length: Optional[float] = None
    max_atmosphering_speed: Optional[str] = None
    crew: Optional[str] = None
    passengers: Optional[str] = None
    cargo_capacity: Optional[str] = None
    consumables: Optional[str] = None
    hyperdrive_rating: Optional[str] = None
    MGLT: Optional[str] = None
    starship_class: Optional[str] = None

class StarshipCreate(StarshipBase):
    pass

class Starship(StarshipBase):
    id: int
    pilot_ids: List[int] = []
    
    class Config:
        orm_mode = True

# Vehicle Schemas
class VehicleBase(BaseModel):
    name: str
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    cost_in_credits: Optional[str] = None
    length: Optional[float] = None
    max_atmosphering_speed: Optional[str] = None
    crew: Optional[str] = None
    passengers: Optional[str] = None
    cargo_capacity: Optional[str] = None
    consumables: Optional[str] = None
    vehicle_class: Optional[str] = None

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int
    pilot_ids: List[int] = []
    
    class Config:
        orm_mode = True