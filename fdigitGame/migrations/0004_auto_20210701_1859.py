# Generated by Django 2.2.24 on 2021-07-01 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdigitGame', '0003_guess'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newnumber',
            old_name='number',
            new_name='numberR',
        ),
    ]
