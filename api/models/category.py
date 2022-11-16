from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=255,
                            verbose_name='Nome do Arquivo')
    age = models.IntegerField(verbose_name='Idade de Corte')
    genre = models.TextField(max_length=255,
                             verbose_name='Sexo')
    importation_file_name = models.TextField(max_length=255,
                                             verbose_name='Nome do Arquivo de Importação')

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name
