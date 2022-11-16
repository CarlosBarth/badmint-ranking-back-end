from django.db import models


class Ranking(models.Model):
    name: models.TextField(max_length=255,
                           verbose_name='Nome')

    class Meta:
        verbose_name = 'Ranking'

    def __str__(self):
        return self.name
