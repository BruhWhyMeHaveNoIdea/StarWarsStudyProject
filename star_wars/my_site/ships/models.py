from django.db import models
from people.models import People

class Spaceships(models.Model):
    name = models.TextField(max_length=256, verbose_name="Название")
    model = models.TextField(verbose_name="Модель")
    manufacturer = models.TextField(verbose_name="Создатель")
    cost_in_credits = models.TextField(max_length=256, verbose_name="Стоимость в кредитах", blank=True)  # изменено на Text
    length = models.FloatField(verbose_name="Длина")
    max_atmosphering_speed = models.TextField(max_length=256, verbose_name="Макс. скорость", blank=True)  # изменено на Text
    crew = models.TextField(max_length=256, verbose_name="Экипаж", blank=True)  # изменено на Text
    passengers = models.TextField(max_length=256, verbose_name="Пассажиры", blank=True)  # исправлена опечатка
    cargo_capacity = models.TextField(max_length=256, verbose_name="Грузоподъёмность", blank=True)  # исправлена опечатка
    consumables = models.TextField(max_length=256, verbose_name="Объём прод. запасов", blank=True)  # исправлена опечатка
    hyperdrive_rating = models.TextField(max_length=256, verbose_name="Рейтинг гипердвигателя", blank=True)  # изменено на Text
    MGLT = models.TextField(max_length=256, verbose_name="MGLT", blank=True)  # переименовано для соответствия фикстурам
    starship_class = models.TextField(max_length=256, verbose_name="Класс корабля")
    pilot_ids = models.ManyToManyField(
        to=People,
        verbose_name="ID пилотов",
        blank=True
    )

    class Meta:
        verbose_name = "Корабль"
        verbose_name_plural = "Корабли"

    def __str__(self):
        return self.name