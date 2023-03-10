# Generated by Django 4.1.7 on 2023-03-02 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Juego",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(default="", max_length=250)),
                ("urlportada", models.CharField(default="", max_length=250)),
                ("lanzamiento", models.CharField(default="", max_length=25)),
                ("plataforma", models.CharField(default="", max_length=50)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
            options={
                "verbose_name_plural": "Juegos",
            },
        ),
        migrations.CreateModel(
            name="Captura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numero_pokemon",
                    models.IntegerField(default=0, verbose_name="Número"),
                ),
                (
                    "nombre_pokemon",
                    models.CharField(max_length=250, verbose_name="Nombre"),
                ),
                ("vida_pokemon", models.IntegerField(default=0, verbose_name="Vida")),
                ("ataque_pokemon", models.IntegerField(default=0)),
                ("defensa_pokemon", models.IntegerField(default=0)),
                ("ataqueesp_pokemon", models.IntegerField(default=0)),
                ("defensaesp_pokemon", models.IntegerField(default=0)),
                ("velocidad_pokemon", models.IntegerField(default=0)),
                ("nivel_pokemon", models.IntegerField(default=0)),
                ("url_pokemon", models.CharField(default="", max_length=250)),
                ("comentarios", models.TextField(null=True)),
                ("shiny", models.BooleanField(default=False)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "juego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="capturas.juego"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Capturas",
            },
        ),
    ]
