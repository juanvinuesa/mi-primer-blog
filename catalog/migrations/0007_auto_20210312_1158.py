# Generated by Django 2.2.18 on 2021-03-12 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210312_1138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autor',
            new_name='Authors',
        ),
        migrations.RenameModel(
            old_name='Libro',
            new_name='Books',
        ),
        migrations.RenameModel(
            old_name='Claves',
            new_name='Keys',
        ),
    ]