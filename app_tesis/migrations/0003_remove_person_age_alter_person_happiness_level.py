# Generated by Django 4.1.7 on 2023-04-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tesis', '0002_person_happiness_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AlterField(
            model_name='person',
            name='happiness_level',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]