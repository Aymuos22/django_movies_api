# Generated by Django 5.0 on 2023-12-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='not-available', max_length=100),
            preserve_default=False,
        ),
    ]
