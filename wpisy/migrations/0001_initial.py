# Generated by Django 3.0.8 on 2021-07-17 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wpis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=255)),
                ('podtytul', models.CharField(max_length=255)),
                ('miniaturka', models.ImageField(blank=True, null=True, upload_to='')),
                ('data_utworzenia', models.DateTimeField(default=django.utils.timezone.now)),
                ('opis', models.TextField()),
            ],
        ),
    ]