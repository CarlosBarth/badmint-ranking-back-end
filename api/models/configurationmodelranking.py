from django.db import models


class ConfigurationModelRanking(models.Model):
    name: models.TextField(max_length=255,
                           verbose_name='Nome')
    score_weeks_expiration: models.IntegerField(verbose_name='Semanas até a expiração')

    class Meta:
        verbose_name = 'Configuração de Modelo de Ranking'

    def __str__(self):
        return self.name
