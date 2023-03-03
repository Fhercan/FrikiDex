# Generated by Django 4.1.7 on 2023-03-03 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("capturas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Logro",
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
                ("titulo", models.CharField(max_length=250, verbose_name="Título")),
                ("foto", models.ImageField(null=True, upload_to="miplace/fotos")),
                ("comentarios", models.TextField(null=True)),
                ("megustas", models.IntegerField(default=0)),
                ("nomegusta", models.IntegerField(default=0)),
                ("publicar", models.BooleanField(default=False)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "captura",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="capturas.captura",
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
                "verbose_name_plural": "Logros",
            },
        ),
    ]
