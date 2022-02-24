# Generated by Django 3.0.8 on 2021-07-24 13:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0006_auto_20210723_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recenzja',
            fields=[
                ('cialo', models.TextField(blank=True, null=True)),
                ('wartosc', models.CharField(choices=[('gora', 'gora'), ('dol', 'dol')], max_length=50)),
                ('aktualizacja', models.DateTimeField(auto_now=True)),
                ('stworzenie', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('poj_wpis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wpisy.Wpis')),
            ],
        ),
    ]