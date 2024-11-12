# Generated by Django 5.1.3 on 2024-11-12 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feature_details_feature_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('id_chauffeur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_chauffeur', models.CharField(max_length=100)),
                ('prenom_chauffeur', models.CharField(max_length=100)),
                ('etat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('nom_client', models.CharField(max_length=100)),
                ('prenom_client', models.CharField(max_length=100)),
                ('destination_client', models.CharField(max_length=255)),
                ('date_demande', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id_compte', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=100, unique=True)),
                ('mot_passe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id_vehicule', models.AutoField(primary_key=True, serialize=False)),
                ('immatriculation', models.CharField(max_length=20)),
                ('marque', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id_avis', models.AutoField(primary_key=True, serialize=False)),
                ('contenu', models.TextField()),
                ('date_avis', models.DateTimeField(auto_now_add=True)),
                ('heure_avis', models.TimeField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Colis',
            fields=[
                ('id_bagage', models.AutoField(primary_key=True, serialize=False)),
                ('libele', models.CharField(max_length=255)),
                ('prix_colis', models.DecimalField(decimal_places=2, max_digits=10)),
                ('masse', models.FloatField()),
                ('emetteur', models.CharField(max_length=255)),
                ('destinataire', models.CharField(max_length=255)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id_voyage', models.AutoField(primary_key=True, serialize=False)),
                ('heure_depart', models.DateTimeField()),
                ('heure_arriver', models.DateTimeField()),
                ('id_classe', models.CharField(max_length=50)),
                ('id_chauffeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.chauffeur')),
                ('id_vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Réserver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut_réserv', models.CharField(max_length=50)),
                ('date_réserv', models.DateField()),
                ('heure_réserv', models.TimeField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('date_reception', models.DateTimeField(blank=True, null=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
                ('id_colis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.colis')),
                ('id_voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.voyage')),
            ],
        ),
    ]