# Generated by Django 4.0.8 on 2024-02-03 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_course_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='categoty',
            new_name='category',
        ),
    ]
