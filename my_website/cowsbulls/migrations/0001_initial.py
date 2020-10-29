# Generated by Django 3.0.7 on 2020-07-03 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cows', models.CharField(max_length=1)),
                ('bulls', models.CharField(max_length=1)),
                ('guess', models.CharField(editable=False, max_length=4)),
                ('choices', models.CharField(editable=False, max_length=20000, validators=[django.core.validators.int_list_validator])),
            ],
        ),
    ]
