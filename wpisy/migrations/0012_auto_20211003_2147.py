# Generated by Django 3.0.8 on 2021-10-03 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0011_auto_20210921_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='count_shares',
            new_name='heart_count',
        ),
    ]