# Generated by Django 3.1.3 on 2020-11-13 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('character_builder_rules', '0002_auto_20201113_1142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EquipentEffect',
            new_name='EquipmentEffect',
        ),
    ]