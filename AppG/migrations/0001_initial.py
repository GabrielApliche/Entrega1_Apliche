# Generated by Django 4.1.1 on 2022-09-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
                ('publicacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancion', models.CharField(max_length=30)),
                ('disco', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('año', models.IntegerField()),
            ],
        ),
    ]
