from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_
import models
import schemas

# Character CRUD
def get_character(db: Session, character_id: int):
    return db.query(models.Character)\
        .options(joinedload(models.Character.films),
                 joinedload(models.Character.starships),
                 joinedload(models.Character.vehicles))\
        .filter(models.Character.id == character_id).first()

def get_characters(db: Session, skip: int = 0, limit: int = 100, search: str = None):
    query = db.query(models.Character)\
        .options(joinedload(models.Character.films),
                 joinedload(models.Character.starships),
                 joinedload(models.Character.vehicles))
    
    if search:
        query = query.filter(models.Character.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

# Film CRUD
def get_film(db: Session, film_id: int):
    return db.query(models.Film)\
        .options(joinedload(models.Film.characters))\
        .filter(models.Film.id == film_id).first()

def get_films(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Film)\
        .options(joinedload(models.Film.characters))\
        .offset(skip).limit(limit).all()

# Starship CRUD
def get_starship(db: Session, starship_id: int):
    return db.query(models.Starship)\
        .options(joinedload(models.Starship.pilots))\
        .filter(models.Starship.id == starship_id).first()

def get_starships(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Starship)\
        .options(joinedload(models.Starship.pilots))\
        .offset(skip).limit(limit).all()

# Vehicle CRUD
def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle)\
        .options(joinedload(models.Vehicle.pilots))\
        .filter(models.Vehicle.id == vehicle_id).first()

def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicle)\
        .options(joinedload(models.Vehicle.pilots))\
        .offset(skip).limit(limit).all()