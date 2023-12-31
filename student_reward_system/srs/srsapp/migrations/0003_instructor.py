# Generated by Django 4.1.3 on 2022-11-21 18:04

import _operator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srsapp', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('instructor_ID', models.IntegerField(primary_key=_operator.truediv, serialize=False)),
                ('instructor_name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('admin_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srsapp.admin')),
            ],
        ),
    ]
