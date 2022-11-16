# Generated by Django 4.1.1 on 2022-10-31 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Nome do Atleta')),
                ('athlete_code', models.IntegerField(verbose_name='Id do Atleta')),
                ('birth_date', models.DateField(verbose_name='Nascimento')),
            ],
            options={
                'verbose_name': 'Atleta',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Nome do Arquivo')),
                ('age', models.IntegerField(verbose_name='Idade de Corte')),
                ('genre', models.TextField(max_length=255, verbose_name='Sexo')),
                ('importation_file_name', models.TextField(max_length=255, verbose_name='Nome do Arquivo de Importação')),
            ],
            options={
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Campeonato',
            },
        ),
        migrations.CreateModel(
            name='ChampionshipSheetImportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Importação de Planilha de Importação',
            },
        ),
        migrations.CreateModel(
            name='ClassificationScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Pontuação de Classificação',
            },
        ),
        migrations.CreateModel(
            name='ConfigurationModelRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Configuração de Modelo de Ranking',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Ranking',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Time',
            },
        ),
        migrations.CreateModel(
            name='TeamChampionshipStageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Categorias de fase do campeonado por equipes',
            },
        ),
    ]