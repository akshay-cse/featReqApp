# Generated by Django 2.0.2 on 2018-03-12 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='feat_priority',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set(),
        ),
    ]
