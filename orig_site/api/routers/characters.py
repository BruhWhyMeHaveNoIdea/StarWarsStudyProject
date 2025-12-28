from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import crud, schemas
from database import get_db

router = APIRouter(prefix="/characters", tags=["characters"])

@router.post("/", response_model=schemas.Character)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    return crud.create_character(db=db, character=character)

@router.get("/", response_model=List[schemas.Character])
def read_characters(
    skip: int = 0, 
    limit: int = 100, 
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    characters = crud.get_characters(db, skip=skip, limit=limit, search=search)
    return characters

@router.get("/{character_id}", response_model=schemas.Character)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = crud.get_character(db, character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    
    # Преобразуем объект Character в словарь и добавляем ID связанных сущностей
    character_dict = {c.key: getattr(db_character, c.key) for c in db_character.__table__.columns}
    character_dict["film_ids"] = [film.id for film in db_character.films]
    character_dict["starship_ids"] = [starship.id for starship in db_character.starships]
    character_dict["vehicle_ids"] = [vehicle.id for vehicle in db_character.vehicles]
    
    return character_dict

@router.post("/{character_id}/starships/{starship_id}")
def add_starship_to_character(
    character_id: int, 
    starship_id: int, 
    db: Session = Depends(get_db)
):
    return crud.add_starship_to_character(db, character_id, starship_id)

@router.post("/{character_id}/films/{film_id}")
def add_film_to_character(
    character_id: int, 
    film_id: int, 
    db: Session = Depends(get_db)
):
    return crud.add_character_to_film(db, character_id, film_id)