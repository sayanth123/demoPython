# Generated by Django 3.2.2 on 2021-05-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default='1990-05-05'),
            preserve_default=False,
        ),
    ]