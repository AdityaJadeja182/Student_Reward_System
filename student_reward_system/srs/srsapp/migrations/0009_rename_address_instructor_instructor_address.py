# Generated by Django 4.1.3 on 2022-11-22 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srsapp', '0008_remove_performance_id_alter_performance_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='address',
            new_name='instructor_address',
        ),
    ]
