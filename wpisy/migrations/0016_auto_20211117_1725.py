# Generated by Django 3.0.8 on 2021-11-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpisy', '0015_tag_when'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='when',
            field=models.CharField(default='Poza czasem', max_length=280),
        ),
    ]
