# Generated by Django 2.2 on 2021-04-22 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp2', '0004_auto_20210422_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentss',
            new_name='course',
        ),
    ]