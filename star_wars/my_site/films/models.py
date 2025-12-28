from django.db import models

class Films(models.Model):
    title = models.TextField(max_length=512, verbose_name="Название")
    episode_id = models.IntegerField(verbose_name="Номер эпизода", null=True, blank=True)
    opening_crawl = models.TextField(verbose_name="Вступительный текст", blank=True)
    director = models.TextField(max_length=256, verbose_name="Режиссёр")
    producer = models.TextField(max_length=512, verbose_name="Продюсер")
    release_date = models.DateField(verbose_name="Дата выхода")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title