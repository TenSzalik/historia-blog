# Generated by Django 3.0.8 on 2021-11-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0017_mainpicture_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='shows',
            field=models.IntegerField(default=0),
        ),
    ]
