# Generated by Django 3.0.8 on 2021-07-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0009_auto_20210724_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]