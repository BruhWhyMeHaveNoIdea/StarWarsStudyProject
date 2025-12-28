from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from datetime import date

# Создаем все таблицы
models.Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    
    try:
        print("Начинаю инициализацию базы данных Звездных Войн...")
        
        # Создаем фильмы (все 9 основных фильмов + Rogue One и Solo)
        films_data = [
            models.Film(
                title="Star Wars: Episode I - The Phantom Menace",
                episode_id=1,
                director="George Lucas",
                producer="Rick McCallum",
                release_date=date(1999, 5, 19),
                opening_crawl="Turmoil has engulfed the Galactic Republic..."
            ),
            models.Film(
                title="Star Wars: Episode II - Attack of the Clones",
                episode_id=2,
                director="George Lucas",
                producer="Rick McCallum",
                release_date=date(2002, 5, 16),
                opening_crawl="There is unrest in the Galactic Senate..."
            ),
            models.Film(
                title="Star Wars: Episode III - Revenge of the Sith",
                episode_id=3,
                director="George Lucas",
                producer="Rick McCallum",
                release_date=date(2005, 5, 19),
                opening_crawl="War! The Republic is crumbling..."
            ),
            models.Film(
                title="Star Wars: Episode IV - A New Hope",
                episode_id=4,
                director="George Lucas",
                producer="Gary Kurtz",
                release_date=date(1977, 5, 25),
                opening_crawl="It is a period of civil war..."
            ),
            models.Film(
                title="Star Wars: Episode V - The Empire Strikes Back",
                episode_id=5,
                director="Irvin Kershner",
                producer="Gary Kurtz",
                release_date=date(1980, 5, 21),
                opening_crawl="It is a dark time for the Rebellion..."
            ),
            models.Film(
                title="Star Wars: Episode VI - Return of the Jedi",
                episode_id=6,
                director="Richard Marquand",
                producer="Howard G. Kazanjian",
                release_date=date(1983, 5, 25),
                opening_crawl="Luke Skywalker has returned to his home planet..."
            ),
            models.Film(
                title="Star Wars: Episode VII - The Force Awakens",
                episode_id=7,
                director="J.J. Abrams",
                producer="Kathleen Kennedy, J.J. Abrams, Bryan Burk",
                release_date=date(2015, 12, 18),
                opening_crawl="Luke Skywalker has vanished..."
            ),
            models.Film(
                title="Star Wars: Episode VIII - The Last Jedi",
                episode_id=8,
                director="Rian Johnson",
                producer="Kathleen Kennedy, Ram Bergman",
                release_date=date(2017, 12, 15),
                opening_crawl="The FIRST ORDER reigns..."
            ),
            models.Film(
                title="Star Wars: Episode IX - The Rise of Skywalker",
                episode_id=9,
                director="J.J. Abrams",
                producer="Kathleen Kennedy, J.J. Abrams, Michelle Rejwan",
                release_date=date(2019, 12, 20),
                opening_crawl="The dead speak!..."
            ),
            models.Film(
                title="Rogue One: A Star Wars Story",
                episode_id=None,
                director="Gareth Edwards",
                producer="Kathleen Kennedy, Allison Shearmur, Simon Emanuel",
                release_date=date(2016, 12, 16),
                opening_crawl="It is a period of civil war..."
            ),
            models.Film(
                title="Solo: A Star Wars Story",
                episode_id=None,
                director="Ron Howard",
                producer="Kathleen Kennedy, Allison Shearmur, Simon Emanuel",
                release_date=date(2018, 5, 25),
                opening_crawl="It is a lawless time..."
            ),
            models.Film(
                title="Star Wars: The Clone Wars",
                episode_id=None,
                director="Dave Filoni",
                producer="Catherine Winder",
                release_date=date(2008, 8, 15),
                opening_crawl="Under the leadership of Obi-Wan Kenobi..."
            )
        ]
        
        for film in films_data:
            db.add(film)
        db.commit()
        print(f"Создано {len(films_data)} фильмов")
        
        # Создаем всех 82 персонажей
        characters_data = [
            # Оригинальная трилогия
            models.Character(name="Luke Skywalker", height=172, mass=77, hair_color="blond", 
                           skin_color="fair", eye_color="blue", birth_year="19BBY", gender="male",
                           species="Human", homeworld="Tatooine"),
            models.Character(name="Leia Organa", height=150, mass=49, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="19BBY", gender="female",
                           species="Human", homeworld="Alderaan"),
            models.Character(name="Han Solo", height=180, mass=80, hair_color="brown", 
                           skin_color="fair", eye_color="brown", birth_year="29BBY", gender="male",
                           species="Human", homeworld="Corellia"),
            models.Character(name="Darth Vader", height=202, mass=136, hair_color="none", 
                           skin_color="white", eye_color="yellow", birth_year="41.9BBY", gender="male",
                           species="Human", homeworld="Tatooine"),
            models.Character(name="Obi-Wan Kenobi", height=182, mass=77, hair_color="auburn, white", 
                           skin_color="fair", eye_color="blue-gray", birth_year="57BBY", gender="male",
                           species="Human", homeworld="Stewjon"),
            models.Character(name="Yoda", height=66, mass=17, hair_color="white", 
                           skin_color="green", eye_color="brown", birth_year="896BBY", gender="male",
                           species="Yoda's species", homeworld="Unknown"),
            models.Character(name="R2-D2", height=96, mass=32, hair_color="n/a", 
                           skin_color="white, blue", eye_color="red", birth_year="33BBY", gender="n/a",
                           species="Droid", homeworld="Naboo"),
            models.Character(name="C-3PO", height=167, mass=75, hair_color="n/a", 
                           skin_color="gold", eye_color="yellow", birth_year="112BBY", gender="n/a",
                           species="Droid", homeworld="Tatooine"),
            models.Character(name="Chewbacca", height=228, mass=112, hair_color="brown", 
                           skin_color="unknown", eye_color="blue", birth_year="200BBY", gender="male",
                           species="Wookiee", homeworld="Kashyyyk"),
            models.Character(name="Emperor Palpatine", height=170, mass=75, hair_color="grey", 
                           skin_color="pale", eye_color="yellow", birth_year="82BBY", gender="male",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Lando Calrissian", height=177, mass=79, hair_color="black", 
                           skin_color="dark", eye_color="brown", birth_year="31BBY", gender="male",
                           species="Human", homeworld="Socorro"),
            models.Character(name="Boba Fett", height=183, mass=78, hair_color="black", 
                           skin_color="fair", eye_color="brown", birth_year="31.5BBY", gender="male",
                           species="Human", homeworld="Kamino"),
            models.Character(name="Jabba the Hutt", height=175, mass=1358, hair_color="n/a", 
                           skin_color="green-tan, brown", eye_color="orange", birth_year="600BBY", gender="hermaphrodite",
                           species="Hutt", homeworld="Nal Hutta"),
            
            # Приквелы
            models.Character(name="Anakin Skywalker", height=188, mass=84, hair_color="blond", 
                           skin_color="fair", eye_color="blue", birth_year="41.9BBY", gender="male",
                           species="Human", homeworld="Tatooine"),
            models.Character(name="Padmé Amidala", height=165, mass=45, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="46BBY", gender="female",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Mace Windu", height=188, mass=84, hair_color="none", 
                           skin_color="dark", eye_color="brown", birth_year="72BBY", gender="male",
                           species="Human", homeworld="Haruun Kal"),
            models.Character(name="Qui-Gon Jinn", height=193, mass=89, hair_color="brown", 
                           skin_color="fair", eye_color="blue", birth_year="92BBY", gender="male",
                           species="Human", homeworld="Coruscant"),
            models.Character(name="Darth Maul", height=175, mass=80, hair_color="none", 
                           skin_color="red", eye_color="yellow", birth_year="54BBY", gender="male",
                           species="Zabrak", homeworld="Dathomir"),
            models.Character(name="Count Dooku", height=193, mass=86, hair_color="white", 
                           skin_color="fair", eye_color="brown", birth_year="102BBY", gender="male",
                           species="Human", homeworld="Serenno"),
            models.Character(name="General Grievous", height=216, mass=159, hair_color="none", 
                           skin_color="brown, white", eye_color="green, yellow", birth_year="unknown", gender="male",
                           species="Kaleesh", homeworld="Kalee"),
            
            # Сиквелы
            models.Character(name="Rey", height=170, mass=54, hair_color="brown", 
                           skin_color="light", eye_color="hazel", birth_year="15ABY", gender="female",
                           species="Human", homeworld="Jakku"),
            models.Character(name="Kylo Ren", height=189, mass=89, hair_color="black", 
                           skin_color="pale", eye_color="hazel", birth_year="5ABY", gender="male",
                           species="Human", homeworld="Chandrila"),
            models.Character(name="Finn", height=178, mass=73, hair_color="black", 
                           skin_color="dark", eye_color="dark", birth_year="unknown", gender="male",
                           species="Human", homeworld="unknown"),
            models.Character(name="Poe Dameron", height=172, mass=80, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="2ABY", gender="male",
                           species="Human", homeworld="Yavin 4"),
            models.Character(name="BB-8", height=67, mass=18, hair_color="none", 
                           skin_color="none", eye_color="black", birth_year="unknown", gender="none",
                           species="Droid", homeworld="unknown"),
            models.Character(name="Maz Kanata", height=95, mass=30, hair_color="none", 
                           skin_color="green", eye_color="yellow", birth_year="unknown", gender="female",
                           species="unknown", homeworld="Takodana"),
            models.Character(name="Supreme Leader Snoke", height=240, mass=90, hair_color="none", 
                           skin_color="pale", eye_color="blue", birth_year="unknown", gender="male",
                           species="unknown", homeworld="unknown"),
            models.Character(name="Captain Phasma", height=200, mass=86, hair_color="unknown", 
                           skin_color="unknown", eye_color="unknown", birth_year="unknown", gender="female",
                           species="Human", homeworld="unknown"),
            models.Character(name="General Hux", height=180, mass=70, hair_color="red", 
                           skin_color="pale", eye_color="green", birth_year="unknown", gender="male",
                           species="Human", homeworld="Arkanis"),
            
            # Другие важные персонажи
            models.Character(name="Wedge Antilles", height=170, mass=77, hair_color="brown", 
                           skin_color="fair", eye_color="hazel", birth_year="21BBY", gender="male",
                           species="Human", homeworld="Corellia"),
            models.Character(name="Admiral Ackbar", height=180, mass=83, hair_color="none", 
                           skin_color="brown mottle", eye_color="orange", birth_year="unknown", gender="male",
                           species="Mon Calamari", homeworld="Mon Cala"),
            models.Character(name="Mon Mothma", height=150, mass=50, hair_color="auburn", 
                           skin_color="fair", eye_color="blue", birth_year="48BBY", gender="female",
                           species="Human", homeworld="Chandrila"),
            models.Character(name="Jyn Erso", height=160, mass=52, hair_color="brown", 
                           skin_color="fair", eye_color="green", birth_year="22BBY", gender="female",
                           species="Human", homeworld="Vallt"),
            models.Character(name="Cassian Andor", height=185, mass=77, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="26BBY", gender="male",
                           species="Human", homeworld="Fest"),
            models.Character(name="Chirrut Îmwe", height=185, mass=80, hair_color="black", 
                           skin_color="fair", eye_color="blue", birth_year="52BBY", gender="male",
                           species="Human", homeworld="Jedha"),
            models.Character(name="Baze Malbus", height=190, mass=90, hair_color="black", 
                           skin_color="dark", eye_color="brown", birth_year="unknown", gender="male",
                           species="Human", homeworld="Jedha"),
            models.Character(name="K-2SO", height=213, mass=110, hair_color="none", 
                           skin_color="white", eye_color="red", birth_year="unknown", gender="male",
                           species="Droid", homeworld="unknown"),
            models.Character(name="Director Krennic", height=183, mass=80, hair_color="white", 
                           skin_color="fair", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="unknown"),
            models.Character(name="Qi'ra", height=165, mass=50, hair_color="brown", 
                           skin_color="light", eye_color="blue", birth_year="unknown", gender="female",
                           species="Human", homeworld="unknown"),
            models.Character(name="Tobias Beckett", height=178, mass=75, hair_color="brown", 
                           skin_color="fair", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="Glee Anselm"),
            models.Character(name="L3-37", height=200, mass=110, hair_color="none", 
                           skin_color="white", eye_color="red", birth_year="unknown", gender="female",
                           species="Droid", homeworld="unknown"),
            models.Character(name="Dryden Vos", height=180, mass=85, hair_color="black", 
                           skin_color="pale", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="unknown"),
            
            # Персонажи Клонических войн
            models.Character(name="Ahsoka Tano", height=170, mass=55, hair_color="white", 
                           skin_color="orange, white", eye_color="blue", birth_year="36BBY", gender="female",
                           species="Togruta", homeworld="Shili"),
            models.Character(name="Captain Rex", height=183, mass=79, hair_color="blond", 
                           skin_color="fair", eye_color="brown", birth_year="32BBY", gender="male",
                           species="Human", homeworld="Kamino"),
            models.Character(name="Commander Cody", height=183, mass=79, hair_color="black", 
                           skin_color="fair", eye_color="brown", birth_year="32BBY", gender="male",
                           species="Human", homeworld="Kamino"),
            models.Character(name="Asajj Ventress", height=180, mass=67, hair_color="none", 
                           skin_color="white", eye_color="yellow", birth_year="unknown", gender="female",
                           species="Dathomirian", homeworld="Dathomir"),
            models.Character(name="Savage Opress", height=210, mass=115, hair_color="black", 
                           skin_color="red", eye_color="yellow", birth_year="unknown", gender="male",
                           species="Dathomirian", homeworld="Dathomir"),
            models.Character(name="Pre Vizsla", height=185, mass=85, hair_color="black", 
                           skin_color="pale", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="Concord Dawn"),
            
            # Другие персонажи
            models.Character(name="Nien Nunb", height=160, mass=68, hair_color="none", 
                           skin_color="grey", eye_color="black", birth_year="unknown", gender="male",
                           species="Sullustan", homeworld="Sullust"),
            models.Character(name="Greedo", height=173, mass=74, hair_color="n/a", 
                           skin_color="green", eye_color="black", birth_year="44BBY", gender="male",
                           species="Rodian", homeworld="Rodia"),
            models.Character(name="Wicket W. Warrick", height=88, mass=20, hair_color="brown", 
                           skin_color="brown", eye_color="brown", birth_year="8BBY", gender="male",
                           species="Ewok", homeworld="Endor"),
            models.Character(name="Salacious B. Crumb", height=79, mass=30, hair_color="orange", 
                           skin_color="brown", eye_color="orange", birth_year="unknown", gender="male",
                           species="Kowakian monkey-lizard", homeworld="Kowak"),
            models.Character(name="Bib Fortuna", height=180, mass=70, hair_color="none", 
                           skin_color="pale", eye_color="pink", birth_year="unknown", gender="male",
                           species="Twi'lek", homeworld="Ryloth"),
            models.Character(name="Watto", height=137, mass=45, hair_color="black", 
                           skin_color="blue, grey", eye_color="yellow", birth_year="unknown", gender="male",
                           species="Toydarian", homeworld="Toydaria"),
            models.Character(name="Sebulba", height=112, mass=40, hair_color="none", 
                           skin_color="grey, red", eye_color="orange", birth_year="unknown", gender="male",
                           species="Dug", homeworld="Malastare"),
            models.Character(name="Shmi Skywalker", height=163, mass=60, hair_color="black", 
                           skin_color="fair", eye_color="brown", birth_year="72BBY", gender="female",
                           species="Human", homeworld="Tatooine"),
            models.Character(name="Darth Plagueis", height=188, mass=84, hair_color="none", 
                           skin_color="pale", eye_color="yellow", birth_year="147BBY", gender="male",
                           species="Muun", homeworld="Mygeeto"),
            models.Character(name="Bail Organa", height=191, mass=85, hair_color="black", 
                           skin_color="tan", eye_color="brown", birth_year="67BBY", gender="male",
                           species="Human", homeworld="Alderaan"),
            models.Character(name="Breha Organa", height=165, mass=55, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="unknown", gender="female",
                           species="Human", homeworld="Alderaan"),
            models.Character(name="Jango Fett", height=183, mass=79, hair_color="black", 
                           skin_color="tan", eye_color="brown", birth_year="66BBY", gender="male",
                           species="Human", homeworld="Concord Dawn"),
            
            # Дополнительные персонажи
            models.Character(name="Zam Wesell", height=168, mass=55, hair_color="blonde", 
                           skin_color="fair, green, yellow", eye_color="yellow", birth_year="unknown", gender="female",
                           species="Clawdite", homeworld="Zolan"),
            models.Character(name="Dexter Jettster", height=198, mass=102, hair_color="none", 
                           skin_color="brown", eye_color="yellow", birth_year="unknown", gender="male",
                           species="Besalisk", homeworld="Ojom"),
            models.Character(name="Lama Su", height=229, mass=88, hair_color="none", 
                           skin_color="grey", eye_color="black", birth_year="unknown", gender="male",
                           species="Kaminoan", homeworld="Kamino"),
            models.Character(name="Taun We", height=213, mass=80, hair_color="none", 
                           skin_color="grey", eye_color="black", birth_year="unknown", gender="female",
                           species="Kaminoan", homeworld="Kamino"),
            models.Character(name="Jocasta Nu", height=167, mass=65, hair_color="white", 
                           skin_color="fair", eye_color="blue", birth_year="unknown", gender="female",
                           species="Human", homeworld="Coruscant"),
            models.Character(name="Ratts Tyerell", height=79, mass=15, hair_color="none", 
                           skin_color="grey, blue", eye_color="unknown", birth_year="unknown", gender="male",
                           species="Aleena", homeworld="Aleen"),
            models.Character(name="R4-P17", height=96, mass=32, hair_color="none", 
                           skin_color="silver, red", eye_color="red, blue", birth_year="unknown", gender="female",
                           species="Droid", homeworld="unknown"),
            models.Character(name="Wat Tambor", height=193, mass=48, hair_color="none", 
                           skin_color="green, grey", eye_color="unknown", birth_year="unknown", gender="male",
                           species="Skakoan", homeworld="Skako"),
            models.Character(name="San Hill", height=191, mass=48, hair_color="none", 
                           skin_color="grey", eye_color="gold", birth_year="unknown", gender="male",
                           species="Muun", homeworld="Scipio"),
            models.Character(name="Shaak Ti", height=178, mass=57, hair_color="none", 
                           skin_color="red, blue, white", eye_color="black", birth_year="unknown", gender="female",
                           species="Togruta", homeworld="Shili"),
            models.Character(name="Grievous' Bodyguard", height=196, mass=112, hair_color="none", 
                           skin_color="brown, white", eye_color="green, yellow", birth_year="unknown", gender="male",
                           species="Kaleesh", homeworld="Kalee"),
            models.Character(name="General Tagge", height=183, mass=84, hair_color="brown", 
                           skin_color="fair", eye_color="brown", birth_year="unknown", gender="male",
                           species="Human", homeworld="unknown"),
            models.Character(name="Bren Derlin", height=170, mass=72, hair_color="brown", 
                           skin_color="fair", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="Hoth"),
            models.Character(name="Admiral Piett", height=170, mass=70, hair_color="none", 
                           skin_color="fair", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="Axxila"),
            models.Character(name="Oola", height=178, mass=55, hair_color="black", 
                           skin_color="green", eye_color="orange", birth_year="unknown", gender="female",
                           species="Twi'lek", homeworld="Ryloth"),
            models.Character(name="Aayla Secura", height=170, mass=55, hair_color="none", 
                           skin_color="blue", eye_color="hazel", birth_year="47BBY", gender="female",
                           species="Twi'lek", homeworld="Ryloth"),
            models.Character(name="Plo Koon", height=188, mass=80, hair_color="none", 
                           skin_color="orange", eye_color="black", birth_year="22BBY", gender="male",
                           species="Kel Dor", homeworld="Dorin"),
            models.Character(name="Ki-Adi-Mundi", height=198, mass=82, hair_color="white", 
                           skin_color="pale", eye_color="yellow", birth_year="92BBY", gender="male",
                           species="Cerean", homeworld="Cerea"),
            models.Character(name="Kit Fisto", height=196, mass=87, hair_color="none", 
                           skin_color="green", eye_color="black", birth_year="unknown", gender="male",
                           species="Nautolan", homeworld="Glee Anselm"),
            models.Character(name="Eeth Koth", height=171, mass=77, hair_color="black", 
                           skin_color="brown", eye_color="brown", birth_year="unknown", gender="male",
                           species="Zabrak", homeworld="Iridonia"),
            models.Character(name="Adi Gallia", height=184, mass=50, hair_color="none", 
                           skin_color="dark", eye_color="blue", birth_year="unknown", gender="female",
                           species="Tholothian", homeworld="Coruscant"),
            models.Character(name="Saesee Tiin", height=188, mass=86, hair_color="none", 
                           skin_color="pale", eye_color="orange", birth_year="unknown", gender="male",
                           species="Iktotchi", homeworld="Iktotch"),
            models.Character(name="Yarael Poof", height=264, mass=70, hair_color="none", 
                           skin_color="white", eye_color="yellow", birth_year="unknown", gender="male",
                           species="Quermian", homeworld="Quermia"),
            models.Character(name="Luminara Unduli", height=170, mass=56, hair_color="black", 
                           skin_color="yellow", eye_color="blue", birth_year="58BBY", gender="female",
                           species="Mirialan", homeworld="Mirial"),
            models.Character(name="Barriss Offee", height=166, mass=50, hair_color="black", 
                           skin_color="yellow", eye_color="blue", birth_year="40BBY", gender="female",
                           species="Mirialan", homeworld="Mirial"),
            models.Character(name="Dormé", height=165, mass=50, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="unknown", gender="female",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Dooku's Assassin", height=170, mass=60, hair_color="black", 
                           skin_color="pale", eye_color="brown", birth_year="unknown", gender="female",
                           species="Human", homeworld="unknown"),
            models.Character(name="Agen Kolar", height=180, mass=80, hair_color="black", 
                           skin_color="green", eye_color="blue", birth_year="unknown", gender="male",
                           species="Zabrak", homeworld="Iridonia"),
            models.Character(name="Jar Jar Binks", height=196, mass=66, hair_color="none", 
                           skin_color="orange", eye_color="orange", birth_year="52BBY", gender="male",
                           species="Gungan", homeworld="Naboo"),
            models.Character(name="Roos Tarpals", height=224, mass=82, hair_color="none", 
                           skin_color="grey", eye_color="orange", birth_year="unknown", gender="male",
                           species="Gungan", homeworld="Naboo"),
            models.Character(name="Rugor Nass", height=206, mass=None, hair_color="none", 
                           skin_color="green", eye_color="orange", birth_year="unknown", gender="male",
                           species="Gungan", homeworld="Naboo"),
            models.Character(name="Ric Olié", height=183, mass=80, hair_color="brown", 
                           skin_color="fair", eye_color="blue", birth_year="unknown", gender="male",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Quarsh Panaka", height=183, mass=80, hair_color="black", 
                           skin_color="dark", eye_color="brown", birth_year="62BBY", gender="male",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Gregar Typho", height=185, mass=85, hair_color="black", 
                           skin_color="dark", eye_color="brown", birth_year="unknown", gender="male",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Cordé", height=157, mass=50, hair_color="brown", 
                           skin_color="light", eye_color="brown", birth_year="unknown", gender="female",
                           species="Human", homeworld="Naboo"),
            models.Character(name="Cliegg Lars", height=183, mass=80, hair_color="brown", 
                           skin_color="fair", eye_color="blue", birth_year="82BBY", gender="male",
                           species="Human", homeworld="Tatooine"),
            models.Character(name="Boba Fett (Young)", height=120, mass=30, hair_color="black", 
                           skin_color="fair", eye_color="brown", birth_year="31.5BBY", gender="male",
                           species="Human", homeworld="Kamino"),
            models.Character(name="Zam Wesell's Droid", height=100, mass=50, hair_color="none", 
                           skin_color="silver", eye_color="red", birth_year="unknown", gender="none",
                           species="Droid", homeworld="unknown"),
        ]
        
        for character in characters_data:
            db.add(character)
        db.commit()
        print(f"Создано {len(characters_data)} персонажей")
        
        # Создаем все корабли
        starships_data = [
            # Истребители Альянса/Новой Республики
            models.Starship(name="X-wing Starfighter", model="T-65B X-wing", manufacturer="Incom Corporation",
                          cost_in_credits="149999", length=12.5, max_atmosphering_speed="1050", crew="1",
                          passengers="0", cargo_capacity="110", consumables="1 week", hyperdrive_rating="1.0",
                          MGLT="100", starship_class="Starfighter"),
            models.Starship(name="Y-wing Starfighter", model="BTL Y-wing", manufacturer="Koensayr Manufacturing",
                          cost_in_credits="134999", length=14, max_atmosphering_speed="1000", crew="2",
                          passengers="0", cargo_capacity="110", consumables="1 week", hyperdrive_rating="1.0",
                          MGLT="80", starship_class="Starfighter"),
            models.Starship(name="A-wing Starfighter", model="RZ-1 A-wing Interceptor", manufacturer="Kuat Systems Engineering",
                          cost_in_credits="175000", length=9.6, max_atmosphering_speed="1300", crew="1",
                          passengers="0", cargo_capacity="40", consumables="1 week", hyperdrive_rating="1.0",
                          MGLT="120", starship_class="Starfighter"),
            models.Starship(name="B-wing Starfighter", model="A/SF-01 B-wing", manufacturer="Slayn & Korpil",
                          cost_in_credits="220000", length=16.9, max_atmosphering_speed="950", crew="1",
                          passengers="0", cargo_capacity="45", consumables="1 week", hyperdrive_rating="2.0",
                          MGLT="91", starship_class="Assault Starfighter"),
            
            # Истребители Империи/Первого Ордена
            models.Starship(name="TIE Fighter", model="Twin Ion Engine/Ln Starfighter", manufacturer="Sienar Fleet Systems",
                          cost_in_credits="75000", length=6.4, max_atmosphering_speed="1200", crew="1",
                          passengers="0", cargo_capacity="65", consumables="2 days", hyperdrive_rating="None",
                          MGLT="100", starship_class="Starfighter"),
            models.Starship(name="TIE Interceptor", model="Twin Ion Engine/IN Interceptor", manufacturer="Sienar Fleet Systems",
                          cost_in_credits="unknown", length=9.6, max_atmosphering_speed="1250", crew="1",
                          passengers="0", cargo_capacity="75", consumables="2 days", hyperdrive_rating="None",
                          MGLT="111", starship_class="Starfighter"),
            models.Starship(name="TIE Bomber", model="Twin Ion Engine/sa Bomber", manufacturer="Sienar Fleet Systems",
                          cost_in_credits="unknown", length=7.8, max_atmosphering_speed="850", crew="1",
                          passengers="0", cargo_capacity="none", consumables="2 days", hyperdrive_rating="None",
                          MGLT="60", starship_class="Starfighter"),
            models.Starship(name="TIE Advanced x1", model="Twin Ion Engine Advanced x1", manufacturer="Sienar Fleet Systems",
                          cost_in_credits="unknown", length=9.2, max_atmosphering_speed="1200", crew="1",
                          passengers="0", cargo_capacity="150", consumables="5 days", hyperdrive_rating="1.0",
                          MGLT="105", starship_class="Starfighter"),
            models.Starship(name="TIE Silencer", model="First Order TIE Silencer", manufacturer="Sienar-Jaemus Fleet Systems",
                          cost_in_credits="unknown", length=17.2, max_atmosphering_speed="unknown", crew="1",
                          passengers="0", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="unknown",
                          MGLT="unknown", starship_class="Starfighter"),
            
            # Грузовые корабли
            models.Starship(name="Millennium Falcon", model="YT-1300 light freighter", manufacturer="Corellian Engineering Corporation",
                          cost_in_credits="100000", length=34.37, max_atmosphering_speed="1050", crew="4",
                          passengers="6", cargo_capacity="100000", consumables="2 months", hyperdrive_rating="0.5",
                          MGLT="75", starship_class="Light freighter"),
            models.Starship(name="Slave I", model="Firespray-31-class patrol and attack", manufacturer="Kuat Systems Engineering",
                          cost_in_credits="unknown", length=21.5, max_atmosphering_speed="1000", crew="1",
                          passengers="6", cargo_capacity="70000", consumables="1 month", hyperdrive_rating="3.0",
                          MGLT="70", starship_class="Patrol craft"),
            models.Starship(name="Razor Crest", model="ST-70 class Razor Crest M-111", manufacturer="unknown",
                          cost_in_credits="unknown", length=80, max_atmosphering_speed="unknown", crew="1",
                          passengers="5", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="unknown",
                          MGLT="unknown", starship_class="Gunship"),
            
            # Крупные военные корабли
            models.Starship(name="Imperial Star Destroyer", model="Imperial I-class Star Destroyer", manufacturer="Kuat Drive Yards",
                          cost_in_credits="150000000", length=1600, max_atmosphering_speed="975", crew="47060",
                          passengers="0", cargo_capacity="36000000", consumables="2 years", hyperdrive_rating="2.0",
                          MGLT="60", starship_class="Star Destroyer"),
            models.Starship(name="Super Star Destroyer", model="Executor-class Star Dreadnought", manufacturer="Kuat Drive Yards",
                          cost_in_credits="1143350000", length=19000, max_atmosphering_speed="n/a", crew="279144",
                          passengers="38000", cargo_capacity="250000000", consumables="6 years", hyperdrive_rating="2.0",
                          MGLT="40", starship_class="Star Dreadnought"),
            models.Starship(name="MC80 Liberty type Star Cruiser", model="MC80 Liberty type Star Cruiser", manufacturer="Mon Calamari shipyards",
                          cost_in_credits="unknown", length=1200, max_atmosphering_speed="unknown", crew="5400",
                          passengers="1200", cargo_capacity="unknown", consumables="2 years", hyperdrive_rating="1.0",
                          MGLT="60", starship_class="Star Cruiser"),
            models.Starship(name="MC85 Star Cruiser", model="MC85 Star Cruiser", manufacturer="Mon Calamari shipyards",
                          cost_in_credits="unknown", length=3438, max_atmosphering_speed="unknown", crew="unknown",
                          passengers="unknown", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="unknown",
                          MGLT="unknown", starship_class="Star Cruiser"),
            
            # Корабли Республики
            models.Starship(name="Jedi Starfighter", model="Delta-7 Aethersprite-class light interceptor", manufacturer="Kuat Systems Engineering",
                          cost_in_credits="180000", length=8, max_atmosphering_speed="1150", crew="1",
                          passengers="0", cargo_capacity="60", consumables="7 days", hyperdrive_rating="1.0",
                          MGLT="unknown", starship_class="Starfighter"),
            models.Starship(name="Naboo Royal Starship", model="J-type 327 Nubian royal starship", manufacturer="Theed Palace Space Vessel Engineering Corps",
                          cost_in_credits="unknown", length=76, max_atmosphering_speed="920", crew="8",
                          passengers="unknown", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="1.8",
                          MGLT="unknown", starship_class="yacht"),
            models.Starship(name="Naboo Star Skiff", model="J-type star skiff", manufacturer="Theed Palace Space Vessel Engineering Corps",
                          cost_in_credits="unknown", length=29.2, max_atmosphering_speed="1050", crew="3",
                          passengers="3", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="0.5",
                          MGLT="unknown", starship_class="yacht"),
            models.Starship(name="Republic Cruiser", model="Consular-class cruiser", manufacturer="Corellian Engineering Corporation",
                          cost_in_credits="unknown", length=115, max_atmosphering_speed="900", crew="9",
                          passengers="16", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="2.0",
                          MGLT="unknown", starship_class="Space cruiser"),
            models.Starship(name="Republic Attack Cruiser", model="Acclamator I-class assault ship", manufacturer="Rothana Heavy Engineering",
                          cost_in_credits="unknown", length=752, max_atmosphering_speed="unknown", crew="700",
                          passengers="16000", cargo_capacity="unknown", consumables="2 years", hyperdrive_rating="0.6",
                          MGLT="unknown", starship_class="assault ship"),
            
            # Другие знаменитые корабли
            models.Starship(name="Death Star", model="DS-1 Orbital Battle Station", manufacturer="Imperial Department of Military Research",
                          cost_in_credits="1000000000000", length=120000, max_atmosphering_speed="n/a", crew="342953",
                          passengers="843342", cargo_capacity="1000000000000", consumables="3 years", hyperdrive_rating="4.0",
                          MGLT="10", starship_class="Deep Space Mobile Battlestation"),
            models.Starship(name="Home One", model="MC80 Liberty type Star Cruiser", manufacturer="Mon Calamari shipyards",
                          cost_in_credits="unknown", length=1200, max_atmosphering_speed="unknown", crew="5400",
                          passengers="1200", cargo_capacity="unknown", consumables="2 years", hyperdrive_rating="1.0",
                          MGLT="60", starship_class="Star Cruiser"),
            models.Starship(name="Ghost", model="VCX-100 light freighter", manufacturer="Corellian Engineering Corporation",
                          cost_in_credits="unknown", length=43.9, max_atmosphering_speed="unknown", crew="4",
                          passengers="unknown", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="unknown",
                          MGLT="unknown", starship_class="Light freighter"),
            models.Starship(name="Tantive IV", model="CR90 corvette", manufacturer="Corellian Engineering Corporation",
                          cost_in_credits="3500000", length=150, max_atmosphering_speed="950", crew="165",
                          passengers="600", cargo_capacity="unknown", consumables="1 year", hyperdrive_rating="2.0",
                          MGLT="60", starship_class="Corvette"),
            models.Starship(name="Star Destroyer Resurgent", model="Resurgent-class Star Destroyer", manufacturer="Kuat-Entralla Engineering",
                          cost_in_credits="unknown", length=2915.81, max_atmosphering_speed="unknown", crew="unknown",
                          passengers="unknown", cargo_capacity="unknown", consumables="unknown", hyperdrive_rating="unknown",
                          MGLT="unknown", starship_class="Star Destroyer"),
        ]
        
        for starship in starships_data:
            db.add(starship)
        db.commit()
        print(f"Создано {len(starships_data)} космических кораблей")
        
        # Создаем весь наземный транспорт
        vehicles_data = [
            # Имперская техника
            models.Vehicle(name="AT-AT", model="All Terrain Armored Transport", manufacturer="Kuat Drive Yards",
                         cost_in_credits="unknown", length=20, max_atmosphering_speed="60", crew="5",
                         passengers="40", cargo_capacity="1000", consumables="unknown", vehicle_class="assault walker"),
            models.Vehicle(name="AT-ST", model="All Terrain Scout Transport", manufacturer="Kuat Drive Yards",
                         cost_in_credits="unknown", length=2, max_atmosphering_speed="90", crew="2",
                         passengers="0", cargo_capacity="200", consumables="none", vehicle_class="walker"),
            models.Vehicle(name="AT-AP", model="All Terrain Attack Pod", manufacturer="Kuat Drive Yards",
                         cost_in_credits="unknown", length=13.2, max_atmosphering_speed="60", crew="3",
                         passengers="0", cargo_capacity="unknown", consumables="unknown", vehicle_class="walker"),
            models.Vehicle(name="AT-TE", model="All Terrain Tactical Enforcer", manufacturer="Rothana Heavy Engineering",
                         cost_in_credits="unknown", length=13.2, max_atmosphering_speed="60", crew="6",
                         passengers="36", cargo_capacity="10000", consumables="21 days", vehicle_class="walker"),
            
            # Республиканская техника
            models.Vehicle(name="TX-130 Saber-class fighter tank", model="TX-130 Saber-class fighter tank", manufacturer="Rothana Heavy Engineering",
                         cost_in_credits="unknown", length=9.54, max_atmosphering_speed="90", crew="2",
                         passengers="0", cargo_capacity="unknown", consumables="unknown", vehicle_class="repulsorcraft"),
            models.Vehicle(name="LAAT/i", model="Low Altitude Assault Transport/infantry", manufacturer="Rothana Heavy Engineering",
                         cost_in_credits="unknown", length=17.4, max_atmosphering_speed="620", crew="6",
                         passengers="30", cargo_capacity="170", consumables="unknown", vehicle_class="gunship"),
            models.Vehicle(name="LAAT/c", model="Low Altitude Assault Transport/carrier", manufacturer="Rothana Heavy Engineering",
                         cost_in_credits="unknown", length=28.82, max_atmosphering_speed="620", crew="1",
                         passengers="0", cargo_capacity="40000", consumables="unknown", vehicle_class="gunship"),
            
            # Спидеры
            models.Vehicle(name="Speeder bike", model="74-Z speeder bike", manufacturer="Aratech Repulsor Company",
                         cost_in_credits="8000", length=3, max_atmosphering_speed="360", crew="1",
                         passengers="1", cargo_capacity="4", consumables="1 day", vehicle_class="speeder"),
            models.Vehicle(name="Imperial Speeder Bike", model="Imperial speeder bike", manufacturer="Aratech Repulsor Company",
                         cost_in_credits="8000", length=3, max_atmosphering_speed="360", crew="1",
                         passengers="1", cargo_capacity="4", consumables="1 day", vehicle_class="speeder"),
            models.Vehicle(name="Swoop bike", model="Swoop", manufacturer="Various", cost_in_credits="unknown",
                         length=3, max_atmosphering_speed="unknown", crew="1", passengers="1",
                         cargo_capacity="unknown", consumables="unknown", vehicle_class="speeder"),
            
            # Грузовые транспортные средства
            models.Vehicle(name="Sand Crawler", model="Digger Crawler", manufacturer="Corellia Mining Corporation",
                         cost_in_credits="150000", length=36.8, max_atmosphering_speed="30", crew="46",
                         passengers="30", cargo_capacity="50000", consumables="2 months", vehicle_class="wheeled"),
            models.Vehicle(name="Juggernaut", model="HAVw A6 Juggernaut", manufacturer="Kuat Drive Yards",
                         cost_in_credits="unknown", length=49.4, max_atmosphering_speed="160", crew="12",
                         passengers="50", cargo_capacity="unknown", consumables="unknown", vehicle_class="wheeled"),
            
            # Летательные аппараты
            models.Vehicle(name="TIE bomber", model="Twin Ion Engine/sa Bomber", manufacturer="Sienar Fleet Systems",
                         cost_in_credits="unknown", length=7.8, max_atmosphering_speed="850", crew="1",
                         passengers="0", cargo_capacity="none", consumables="2 days", vehicle_class="airspeeder"),
            models.Vehicle(name="Snowspeeder", model="T-47 airspeeder", manufacturer="Incom Corporation",
                         cost_in_credits="unknown", length=4.5, max_atmosphering_speed="650", crew="2",
                         passengers="0", cargo_capacity="10", consumables="none", vehicle_class="airspeeder"),
            
            # Планетарные транспортные средства
            models.Vehicle(name="BARC speeder", model="Biker Advanced Recon Commando", manufacturer="Aratech Repulsor Company",
                         cost_in_credits="unknown", length=3.5, max_atmosphering_speed="unknown", crew="1",
                         passengers="1", cargo_capacity="unknown", consumables="unknown", vehicle_class="speeder"),
            models.Vehicle(name="K79-S80 Imperial Troop Transport", model="K79-S80 Imperial Troop Transport", manufacturer="unknown",
                         cost_in_credits="unknown", length=None, max_atmosphering_speed="unknown", crew="2",
                         passengers="20", cargo_capacity="unknown", consumables="unknown", vehicle_class="transport"),
            models.Vehicle(name="Vulture Droid", model="Variable Geometry Self-Propelled Battle Droid, Mark I", manufacturer="Haor Chall Engineering",
                         cost_in_credits="unknown", length=3.5, max_atmosphering_speed="1200", crew="0",
                         passengers="0", cargo_capacity="none", consumables="none", vehicle_class="starfighter"),
            
            # Гражданские транспортные средства
            models.Vehicle(name="X-34 landspeeder", model="X-34 landspeeder", manufacturer="SoroSuub Corporation",
                         cost_in_credits="10550", length=3.4, max_atmosphering_speed="250", crew="1",
                         passengers="1", cargo_capacity="5", consumables="unknown", vehicle_class="speeder"),
            models.Vehicle(name="Droid Tri-Fighter", model="Droid Tri-Fighter", manufacturer="Colicoid Creation Nest",
                         cost_in_credits="unknown", length=5.4, max_atmosphering_speed="1180", crew="0",
                         passengers="0", cargo_capacity="0", consumables="none", vehicle_class="droid starfighter"),
            models.Vehicle(name="Corporate Alliance tank droid", model="NR-N99 Persuader-class droid enforcer", manufacturer="Techno Union",
                         cost_in_credits="unknown", length=10.96, max_atmosphering_speed="100", crew="0",
                         passengers="0", cargo_capacity="none", consumables="none", vehicle_class="droid tank"),
            models.Vehicle(name="Multi-Troop Transport", model="Multi-Troop Transport", manufacturer="Baktoid Armor Workshop",
                         cost_in_credits="unknown", length=31, max_atmosphering_speed="35", crew="4",
                         passengers="112", cargo_capacity="unknown", consumables="unknown", vehicle_class="transport"),
            models.Vehicle(name="Armored Assault Tank", model="Armoured Assault Tank", manufacturer="Baktoid Armor Workshop",
                         cost_in_credits="unknown", length=9.75, max_atmosphering_speed="55", crew="4",
                         passengers="6", cargo_capacity="unknown", consumables="unknown", vehicle_class="tank"),
            
            # Транспорт из сиквелов
            models.Vehicle(name="First Order All Terrain Armored Transport", model="First Order AT-AT", manufacturer="Kuat-Entralla Engineering",
                         cost_in_credits="unknown", length=33.71, max_atmosphering_speed="70", crew="5",
                         passengers="40", cargo_capacity="unknown", consumables="unknown", vehicle_class="assault walker"),
            models.Vehicle(name="First Order All Terrain Scout Transport", model="First Order AT-ST", manufacturer="Kuat-Entralla Engineering",
                         cost_in_credits="unknown", length=7.57, max_atmosphering_speed="90", crew="2",
                         passengers="0", cargo_capacity="unknown", consumables="unknown", vehicle_class="walker"),
            models.Vehicle(name="First Order All Terrain MegaCaliber Six", model="First Order AT-M6", manufacturer="Kuat-Entralla Engineering",
                         cost_in_credits="unknown", length=36.87, max_atmosphering_speed="60", crew="3",
                         passengers="40", cargo_capacity="unknown", consumables="unknown", vehicle_class="walker"),
            models.Vehicle(name="Quadjumper", model="Quadrijet transfer spacetug", manufacturer="SoroSuub Corporation",
                         cost_in_credits="unknown", length=8.3, max_atmosphering_speed="unknown", crew="2",
                         passengers="0", cargo_capacity="unknown", consumables="unknown", vehicle_class="space tug"),
            
            # Специальные транспортные средства
            models.Vehicle(name="Raddaugh Gnasp fluttercraft", model="Raddaugh Gnasp fluttercraft", manufacturer="Appazanna Engineering Works",
                         cost_in_credits="unknown", length=7, max_atmosphering_speed="310", crew="2",
                         passengers="0", cargo_capacity="20", consumables="none", vehicle_class="air speeder"),
            models.Vehicle(name="Flitknot speeder", model="Flitknot speeder", manufacturer="Huppla Pasa Tisc Shipwrights Collective",
                         cost_in_credits="unknown", length=2, max_atmosphering_speed="634", crew="1",
                         passengers="0", cargo_capacity="unknown", consumables="unknown", vehicle_class="speeder"),
            models.Vehicle(name="Geonosian starfighter", model="Nantex-class territorial defense starfighter", manufacturer="Huppla Pasa Tisc Shipwrights Collective",
                         cost_in_credits="unknown", length=9.8, max_atmosphering_speed="20000", crew="1",
                         passengers="0", cargo_capacity="unknown", consumables="unknown", vehicle_class="starfighter"),
        ]
        
        for vehicle in vehicles_data:
            db.add(vehicle)
        db.commit()
        print(f"Создано {len(vehicles_data)} наземных транспортных средств")
        
        # Устанавливаем связи между сущностями
        print("Устанавливаю связи между сущностями...")
        
        #Получаем фильмы
        phantom_menace = db.query(models.Film).filter(models.Film.episode_id == 1).first()
        attack_clones = db.query(models.Film).filter(models.Film.episode_id == 2).first()
        revenge_sith = db.query(models.Film).filter(models.Film.episode_id == 3).first()
        new_hope = db.query(models.Film).filter(models.Film.episode_id == 4).first()
        empire_strikes = db.query(models.Film).filter(models.Film.episode_id == 5).first()
        return_jedi = db.query(models.Film).filter(models.Film.episode_id == 6).first()
        force_awakens = db.query(models.Film).filter(models.Film.episode_id == 7).first()
        last_jedi = db.query(models.Film).filter(models.Film.episode_id == 8).first()
        rise_skywalker = db.query(models.Film).filter(models.Film.episode_id == 9).first()
        rogue_one = db.query(models.Film).filter(models.Film.title.like("%Rogue One%")).first()
        solo = db.query(models.Film).filter(models.Film.title.like("%Solo%")).first()

        # Получаем персонажей
        luke = db.query(models.Character).filter(models.Character.name == "Luke Skywalker").first()
        leia = db.query(models.Character).filter(models.Character.name == "Leia Organa").first()
        han = db.query(models.Character).filter(models.Character.name == "Han Solo").first()
        vader = db.query(models.Character).filter(models.Character.name == "Darth Vader").first()
        obiwan = db.query(models.Character).filter(models.Character.name == "Obi-Wan Kenobi").first()
        yoda = db.query(models.Character).filter(models.Character.name == "Yoda").first()
        r2d2 = db.query(models.Character).filter(models.Character.name == "R2-D2").first()
        c3po = db.query(models.Character).filter(models.Character.name == "C-3PO").first()
        chewie = db.query(models.Character).filter(models.Character.name == "Chewbacca").first()
        palpatine = db.query(models.Character).filter(models.Character.name == "Emperor Palpatine").first()
        lando = db.query(models.Character).filter(models.Character.name == "Lando Calrissian").first()
        boba = db.query(models.Character).filter(models.Character.name == "Boba Fett").first()
        jabba = db.query(models.Character).filter(models.Character.name == "Jabba the Hutt").first()
        anakin = db.query(models.Character).filter(models.Character.name == "Anakin Skywalker").first()
        padme = db.query(models.Character).filter(models.Character.name == "Padmé Amidala").first()
        mace = db.query(models.Character).filter(models.Character.name == "Mace Windu").first()
        quigon = db.query(models.Character).filter(models.Character.name == "Qui-Gon Jinn").first()
        maul = db.query(models.Character).filter(models.Character.name == "Darth Maul").first()
        dooku = db.query(models.Character).filter(models.Character.name == "Count Dooku").first()
        grievous = db.query(models.Character).filter(models.Character.name == "General Grievous").first()
        rey = db.query(models.Character).filter(models.Character.name == "Rey").first()
        kylo = db.query(models.Character).filter(models.Character.name == "Kylo Ren").first()
        finn = db.query(models.Character).filter(models.Character.name == "Finn").first()
        poe = db.query(models.Character).filter(models.Character.name == "Poe Dameron").first()
        bb8 = db.query(models.Character).filter(models.Character.name == "BB-8").first()

        # Получаем дополнительных персонажей для связей
        jar_jar = db.query(models.Character).filter(models.Character.name == "Jar Jar Binks").first()
        watto = db.query(models.Character).filter(models.Character.name == "Watto").first()
        sebulba = db.query(models.Character).filter(models.Character.name == "Sebulba").first()
        shmi = db.query(models.Character).filter(models.Character.name == "Shmi Skywalker").first()
        jango = db.query(models.Character).filter(models.Character.name == "Jango Fett").first()
        zam = db.query(models.Character).filter(models.Character.name == "Zam Wesell").first()
        dex = db.query(models.Character).filter(models.Character.name == "Dexter Jettster").first()
        lama = db.query(models.Character).filter(models.Character.name == "Lama Su").first()
        taun = db.query(models.Character).filter(models.Character.name == "Taun We").first()
        bail = db.query(models.Character).filter(models.Character.name == "Bail Organa").first()
        shaak = db.query(models.Character).filter(models.Character.name == "Shaak Ti").first()
        kit = db.query(models.Character).filter(models.Character.name == "Kit Fisto").first()
        aayla = db.query(models.Character).filter(models.Character.name == "Aayla Secura").first()
        tarkin = db.query(models.Character).filter(models.Character.name == "General Tagge").first()  # Используем Tagge вместо Tarkin, так как Tarkin нет в списке
        wedge = db.query(models.Character).filter(models.Character.name == "Wedge Antilles").first()
        ackbar = db.query(models.Character).filter(models.Character.name == "Admiral Ackbar").first()
        mon_mothma = db.query(models.Character).filter(models.Character.name == "Mon Mothma").first()
        wicket = db.query(models.Character).filter(models.Character.name == "Wicket W. Warrick").first()
        maz = db.query(models.Character).filter(models.Character.name == "Maz Kanata").first()
        snoke = db.query(models.Character).filter(models.Character.name == "Supreme Leader Snoke").first()
        phasma = db.query(models.Character).filter(models.Character.name == "Captain Phasma").first()
        hux = db.query(models.Character).filter(models.Character.name == "General Hux").first()
        jyn = db.query(models.Character).filter(models.Character.name == "Jyn Erso").first()
        cassian = db.query(models.Character).filter(models.Character.name == "Cassian Andor").first()
        chirrut = db.query(models.Character).filter(models.Character.name == "Chirrut Îmwe").first()
        baze = db.query(models.Character).filter(models.Character.name == "Baze Malbus").first()
        k2so = db.query(models.Character).filter(models.Character.name == "K-2SO").first()
        krennic = db.query(models.Character).filter(models.Character.name == "Director Krennic").first()
        qi_ra = db.query(models.Character).filter(models.Character.name == "Qi'ra").first()
        beckett = db.query(models.Character).filter(models.Character.name == "Tobias Beckett").first()
        l3_37 = db.query(models.Character).filter(models.Character.name == "L3-37").first()
        dryden = db.query(models.Character).filter(models.Character.name == "Dryden Vos").first()

        # Получаем корабли
        millennium_falcon = db.query(models.Starship).filter(models.Starship.name == "Millennium Falcon").first()
        xwing = db.query(models.Starship).filter(models.Starship.name == "X-wing Starfighter").first()
        ywing = db.query(models.Starship).filter(models.Starship.name == "Y-wing Starfighter").first()
        awing = db.query(models.Starship).filter(models.Starship.name == "A-wing Starfighter").first()
        bwing = db.query(models.Starship).filter(models.Starship.name == "B-wing Starfighter").first()
        tie_fighter = db.query(models.Starship).filter(models.Starship.name == "TIE Fighter").first()
        tie_interceptor = db.query(models.Starship).filter(models.Starship.name == "TIE Interceptor").first()
        tie_bomber = db.query(models.Starship).filter(models.Starship.name == "TIE Bomber").first()
        tie_advanced = db.query(models.Starship).filter(models.Starship.name == "TIE Advanced x1").first()
        slave1 = db.query(models.Starship).filter(models.Starship.name == "Slave I").first()
        jedi_starfighter = db.query(models.Starship).filter(models.Starship.name == "Jedi Starfighter").first()
        death_star = db.query(models.Starship).filter(models.Starship.name == "Death Star").first()
        star_destroyer = db.query(models.Starship).filter(models.Starship.name == "Imperial Star Destroyer").first()

        # Получаем транспорт
        atat = db.query(models.Vehicle).filter(models.Vehicle.name == "AT-AT").first()
        atst = db.query(models.Vehicle).filter(models.Vehicle.name == "AT-ST").first()
        speeder_bike = db.query(models.Vehicle).filter(models.Vehicle.name == "Speeder bike").first()
        sand_crawler = db.query(models.Vehicle).filter(models.Vehicle.name == "Sand Crawler").first()
        snowspeeder = db.query(models.Vehicle).filter(models.Vehicle.name == "Snowspeeder").first()

        # Устанавливаем связи фильмов с персонажами (только для персонажей, которые существуют)

        # Фильм 1: Призрачная угроза
        phantom_chars = [obiwan, quigon, padme, anakin, palpatine, maul, jar_jar, r2d2, c3po, yoda, mace, watto, sebulba, shmi]
        phantom_menace.characters.extend([c for c in phantom_chars if c])

        # Фильм 2: Атака клонов
        attack_chars = [anakin, obiwan, padme, yoda, palpatine, dooku, jango, mace, jar_jar, r2d2, c3po, zam, dex, lama, taun]
        attack_clones.characters.extend([c for c in attack_chars if c])

        # Фильм 3: Месть ситхов
        revenge_chars = [anakin, obiwan, padme, yoda, palpatine, dooku, grievous, mace, r2d2, c3po, bail, jar_jar, shaak, kit, aayla]
        revenge_sith.characters.extend([c for c in revenge_chars if c])

        # Фильм 4: Новая надежда
        new_hope_chars = [luke, leia, han, obiwan, vader, r2d2, c3po, chewie, tarkin, wedge, ackbar]
        new_hope.characters.extend([c for c in new_hope_chars if c])

        # Фильм 5: Империя наносит ответный удар
        empire_chars = [luke, leia, han, vader, yoda, r2d2, c3po, chewie, lando, boba, palpatine, wedge]
        empire_strikes.characters.extend([c for c in empire_chars if c])

        # Фильм 6: Возвращение джедая
        return_chars = [luke, leia, han, vader, palpatine, r2d2, c3po, chewie, lando, boba, jabba, wicket, ackbar, mon_mothma]
        return_jedi.characters.extend([c for c in return_chars if c])

        # Фильм 7: Пробуждение силы
        force_chars = [rey, finn, poe, kylo, han, leia, chewie, r2d2, c3po, bb8, maz, snoke, phasma, hux]
        force_awakens.characters.extend([c for c in force_chars if c])

        # Фильм 8: Последние джедаи
        last_chars = [rey, finn, poe, kylo, leia, luke, r2d2, c3po, bb8, snoke, hux, maz]
        last_jedi.characters.extend([c for c in last_chars if c])

        # Фильм 9: Скайуокер. Восход
        rise_chars = [rey, finn, poe, kylo, leia, palpatine, chewie, r2d2, c3po, bb8, lando, hux]
        rise_skywalker.characters.extend([c for c in rise_chars if c])

        # Rogue One
        rogue_chars = [jyn, cassian, chirrut, baze, k2so, krennic]
        rogue_one.characters.extend([c for c in rogue_chars if c])

        # Solo
        solo_chars = [han, chewie, lando, qi_ra, beckett, l3_37, dryden]
        solo.characters.extend([c for c in solo_chars if c])

        # Устанавливаем связи персонажей с кораблями
        if han and millennium_falcon:
            han.starships.extend([millennium_falcon])
        if chewie and millennium_falcon:
            chewie.starships.extend([millennium_falcon])
        if luke and xwing:
            luke.starships.extend([xwing])
        if wedge and xwing:
            wedge.starships.extend([xwing])
        if poe and xwing:
            poe.starships.extend([xwing])
        if vader and tie_advanced:
            vader.starships.extend([tie_advanced])
        if boba and slave1:
            boba.starships.extend([slave1])
        if obiwan and jedi_starfighter:
            obiwan.starships.extend([jedi_starfighter])
        if anakin and jedi_starfighter:
            anakin.starships.extend([jedi_starfighter])
        
        # Устанавливаем связи персонажей с транспортом
        luke.vehicles.extend([speeder_bike, snowspeeder])
        leia.vehicles.extend([speeder_bike])
        han.vehicles.extend([speeder_bike])
        chewie.vehicles.extend([atat])  # как пленный
        
        # Связываем императора с Звездой Смерти
        palpatine.starships.extend([death_star])
        
        # Связываем офицеров с Звездными Разрушителями
        tarkin_char = db.query(models.Character).filter(models.Character.name == "Grand Moff Tarkin").first()
        if tarkin_char:
            tarkin_char.starships.extend([star_destroyer, death_star])
        
        db.commit()
        
        print("База данных успешно инициализирована!")
        print(f"Всего создано:")
        print(f"- Фильмов: {len(films_data)}")
        print(f"- Персонажей: {len(characters_data)}")
        print(f"- Космических кораблей: {len(starships_data)}")
        print(f"- Наземного транспорта: {len(vehicles_data)}")
        
    except Exception as e:
        db.rollback()
        print(f"Ошибка при инициализации базы данных: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()