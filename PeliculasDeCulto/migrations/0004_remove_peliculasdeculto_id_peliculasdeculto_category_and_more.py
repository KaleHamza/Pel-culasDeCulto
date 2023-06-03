# Generated by Django 4.1.3 on 2023-06-03 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PeliculasDeCulto', '0003_peliculasdeculto_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculasdeculto',
            name='id',
        ),
        migrations.AddField(
            model_name='peliculasdeculto',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='PeliculasDeCulto.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='peliculasdeculto',
            name='slug',
            field=models.SlugField(blank=True, default='', primary_key=True, serialize=False, unique=True),
        ),
    ]