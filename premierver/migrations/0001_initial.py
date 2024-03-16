# Generated by Django 5.0.2 on 2024-02-13 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dechets",
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
                ("Type_dechet", models.CharField(max_length=50)),
                ("Description", models.TextField()),
                ("Date_ajout", models.DateField()),
                ("Etat", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Fournisseurs_de_services",
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
                ("Nom_entreprise", models.CharField(max_length=100)),
                ("Adresse", models.TextField()),
                ("Type_service_offert", models.CharField(max_length=100)),
                ("Contact", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Points_de_collecte",
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
                ("Nom_point_collecte", models.CharField(max_length=100)),
                ("Adresse", models.TextField()),
                ("Type_dechets_acceptes", models.CharField(max_length=100)),
                ("Capacite_stockage", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Collectes",
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
                ("Date_collecte", models.DateField()),
                (
                    "Poids_total_collecte",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("Type_dechets_collectes", models.CharField(max_length=100)),
                (
                    "ID_point_collecte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="premierver.points_de_collecte",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Traitement",
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
                ("Type_traitement", models.CharField(max_length=100)),
                ("Date_traitement", models.DateField()),
                ("Destination_traitement", models.CharField(max_length=100)),
                (
                    "ID_dechet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="premierver.dechets",
                    ),
                ),
            ],
        ),
    ]