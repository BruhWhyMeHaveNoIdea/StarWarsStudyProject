from django.db import models

class Vehicles(models.Model):
    name = models.TextField(max_length=256, verbose_name="Название")
    model = models.TextField(verbose_name="Модель")
    manufacturer = models.TextField(verbose_name="Создатель")
    cost_in_credits = models.TextField(max_length=256, verbose_name="Стоимость в кредитах", blank=True)
    length = models.FloatField(verbose_name="Длина", null=True, blank=True)
    max_atmosphering_speed = models.TextField(max_length=256, verbose_name="Макс. скорость", blank=True)
    crew = models.TextField(max_length=256, verbose_name="Экипаж", blank=True)
    passengers = models.TextField(max_length=256, verbose_name="Пассажиры", blank=True)
    cargo_capacity = models.TextField(max_length=256, verbose_name="Грузоподъёмность", blank=True)
    consumables = models.TextField(max_length=256, verbose_name="Объём прод. запасов", blank=True)
    vehicle_class = models.TextField(max_length=256, verbose_name="Класс транспорта")

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"

    def __str__(self):
        return self.name