from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, schemas
from database import get_db

router = APIRouter(prefix="/films", tags=["films"])

@router.post("/", response_model=schemas.Film)
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db)):
    return crud.create_film(db=db, film=film)

@router.get("/", response_model=List[schemas.Film])
def read_films(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    films = crud.get_films(db, skip=skip, limit=limit)
    return films

@router.get("/{film_id}", response_model=schemas.Film)
def read_film(film_id: int, db: Session = Depends(get_db)):
    db_film = crud.get_film(db, film_id=film_id)
    if db_film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    
    film_dict = {c.key: getattr(db_film, c.key) for c in db_film.__table__.columns}
    film_dict["character_ids"] = [character.id for character in db_film.characters]
    
    return film_dict