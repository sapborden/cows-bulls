# Generated by Django 3.0.7 on 2020-07-10 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowsbulls', '0008_prevguess'),
    ]

    operations = [
        migrations.AddField(
            model_name='prevguess',
            name='choices',
            field=models.CharField(default=[], max_length=20000, validators=[django.core.validators.int_list_validator]),
        ),
    ]
