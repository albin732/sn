# Generated by Django 3.0.7 on 2020-09-18 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderManagement',
            new_name='OrderStack',
        ),
    ]