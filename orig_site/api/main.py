from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import characters, films, starships, vehicles
import models

# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Star Wars API",
    description="API для информации о вселенной Звездных Войн",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(characters.router)
app.include_router(films.router)
app.include_router(starships.router)
app.include_router(vehicles.router)

@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в API Звездных Войн!",
        "endpoints": {
            "characters": "/characters",
            "films": "/films",
            "starships": "/starships",
            "vehicles": "/vehicles"
        },
        "documentation": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}