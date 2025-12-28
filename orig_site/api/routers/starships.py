from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, schemas
from database import get_db

router = APIRouter(prefix="/starships", tags=["starships"])

@router.post("/", response_model=schemas.Starship)
def create_starship(starship: schemas.StarshipCreate, db: Session = Depends(get_db)):
    return crud.create_starship(db=db, starship=starship)

@router.get("/", response_model=List[schemas.Starship])
def read_starships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    starships = crud.get_starships(db, skip=skip, limit=limit)
    return starships

@router.get("/{starship_id}", response_model=schemas.Starship)
def read_starship(starship_id: int, db: Session = Depends(get_db)):
    db_starship = crud.get_starship(db, starship_id=starship_id)
    if db_starship is None:
        raise HTTPException(status_code=404, detail="Starship not found")
    
    starship_dict = {c.key: getattr(db_starship, c.key) for c in db_starship.__table__.columns}
    starship_dict["pilot_ids"] = [character.id for character in db_starship.pilots]
    
    return starship_dict