# Generated by Django 4.2.1 on 2023-05-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Game_type',
            new_name='GameType',
        ),
        migrations.AlterField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(),
        ),
    ]
