from django.db import models

class People(models.Model):
    name = models.TextField(max_length=256, verbose_name="Имя")
    height = models.FloatField(verbose_name="Рост", null=True, blank=True)  # изменено на Float
    mass = models.FloatField(verbose_name="Масса", null=True, blank=True)   # изменено на Float
    hair_color = models.TextField(max_length=256, verbose_name="Цвет волос")
    skin_color = models.TextField(max_length=256, verbose_name="Цвет кожи")
    eye_color = models.TextField(max_length=256, verbose_name="Цвет глаз")
    birth_year = models.TextField(max_length=256, verbose_name="Дата рождения")
    gender = models.TextField(max_length=256, verbose_name="Пол")
    species = models.TextField(max_length=256, verbose_name="Вид")
    homeworld = models.TextField(max_length=256, verbose_name="Место рождения")
    # Убраны поля film_ids, starship_ids, vehicle_ids, так как в фикстурах их нет

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return self.name