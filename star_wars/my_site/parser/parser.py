import requests
import json
import os


def parser():
    url = "http://0.0.0.0:8000"
    answer = dict()
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        endpoints = data["endpoints"]
        
        for key, value in endpoints.items():
            endpoint_url = "http://0.0.0.0:8000" + value
            response = requests.get(endpoint_url)
            information = json.loads(response.text)
            answer[key] = information
        json_string = json.dumps(answer, indent=2)
        return json_string
    except Exception as e:
        print(f"Ошибка в функции parser: {e}")
        return None


def save_to_file(json_string):
    """
    Сохраняет JSON-строку в файл 'output.json'
    
    Args:
        json_string (str): JSON-строка для сохранения
    """
    try:
        # Создаем папку files, если она не существует
        os.makedirs('files', exist_ok=True)
        
        # Проверяем, что переданная строка не пустая
        if json_string:
            with open('files/output.json', 'w', encoding='utf-8') as file:
                file.write(json_string)
            print("Данные успешно сохранены в файл 'files/output.json'")
            return True
        else:
            print("Ошибка: пустая JSON-строка")
            return False
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")
        return False


def convert_to_fixtures():
    try:
        with open('files/output.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Ошибка: файл 'files/output.json' не найден")
        print("Возможно, данные не были получены из API")
        return
    except json.JSONDecodeError as e:
        print(f"Ошибка при чтении JSON: {e}")
        return
    
    fixtures = []
    
    # Фикстуры для персонажей
    for character in data.get('characters', []):
        fixture = {
            "model": "people.People",
            "pk": character['id'],
            "fields": {
                "name": character['name'],
                "height": character['height'],
                "mass": character['mass'],
                "hair_color": character['hair_color'],
                "skin_color": character['skin_color'],
                "eye_color": character['eye_color'],
                "birth_year": character['birth_year'],
                "gender": character['gender'],
                "species": character['species'],
                "homeworld": character['homeworld']
            }
        }
        fixtures.append(fixture)
    
    # Фикстуры для фильмов
    for film in data.get('films', []):
        fixture = {
            "model": "films.Films",
            "pk": film['id'],
            "fields": {
                "title": film['title'],
                "episode_id": film['episode_id'],
                "opening_crawl": film['opening_crawl'],
                "director": film['director'],
                "producer": film['producer'],
                "release_date": film['release_date']
            }
        }
        fixtures.append(fixture)
    
    # Фикстуры для звездолетов
    for starship in data.get('starships', []):
        fixture = {
            "model": "ships.Spaceships",
            "pk": starship['id'],
            "fields": {
                "name": starship['name'],
                "model": starship['model'],
                "manufacturer": starship['manufacturer'],
                "cost_in_credits": starship['cost_in_credits'],
                "length": starship['length'],
                "max_atmosphering_speed": starship['max_atmosphering_speed'],
                "crew": starship['crew'],
                "passengers": starship['passengers'],
                "cargo_capacity": starship['cargo_capacity'],
                "consumables": starship['consumables'],
                "hyperdrive_rating": starship['hyperdrive_rating'],
                "MGLT": starship['MGLT'],
                "starship_class": starship['starship_class']
            }
        }
        fixtures.append(fixture)
    
    # Фикстуры для транспортных средств
    for vehicle in data.get('vehicles', []):
        fixture = {
            "model": "vehicles.Vehicles",
            "pk": vehicle['id'],
            "fields": {
                "name": vehicle['name'],
                "model": vehicle['model'],
                "manufacturer": vehicle['manufacturer'],
                "cost_in_credits": vehicle['cost_in_credits'],
                "length": vehicle['length'],
                "max_atmosphering_speed": vehicle['max_atmosphering_speed'],
                "crew": vehicle['crew'],
                "passengers": vehicle['passengers'],
                "cargo_capacity": vehicle['cargo_capacity'],
                "consumables": vehicle['consumables'],
                "vehicle_class": vehicle['vehicle_class']
            }
        }
        fixtures.append(fixture)
    
    # Сохраняем в файл
    with open('files/fixtures.json', 'w') as f:
        json.dump(fixtures, f, indent=2)
    
    print(f"Создано {len(fixtures)} фикстур")
    print("Фикстуры сохранены в files/fixtures.json")


if __name__ == "__main__":
    print("Начинаем парсинг API...")
    result = parser()
    
    if result:
        print("Парсинг завершен успешно")
        saved = save_to_file(result)
        
        if saved:
            print("Конвертация в фикстуры...")
            convert_to_fixtures()
        else:
            print("Не удалось сохранить файл, пропускаем конвертацию")
    else:
        print("Не удалось получить данные из API")
        print("Проверьте, запущен ли сервер на http://localhost:8000")