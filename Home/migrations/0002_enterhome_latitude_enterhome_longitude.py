# Generated by Django 4.1.4 on 2023-01-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterhome',
            name='latitude',
            field=models.CharField(default='17.265262', max_length=100),
        ),
        migrations.AddField(
            model_name='enterhome',
            name='longitude',
            field=models.CharField(default='78.3882381', max_length=100),
        ),
    ]
