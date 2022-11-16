from django.db import models
from api.models import Athlete


class Team(models.Model):
    id_athlete_1: models.ForeignKey(Athlete,
                                    on_delete=models.CASCADE,
                                    verbose_name='Atleta 1')
    id_athlete_2: models.ForeignKey(Athlete,
                                    on_delete=models.CASCADE,
                                    verbose_name='Atleta 2')
    name: models.TextField(max_length=255,
                           verbose_name='Nome')

    class Meta:
        verbose_name = 'Time'

    def __str__(self):
        return self.name
