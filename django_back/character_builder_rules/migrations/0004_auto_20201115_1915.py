# Generated by Django 3.1.3 on 2020-11-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder_rules', '0003_auto_20201113_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('base_value', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Attribut',
                'verbose_name_plural': 'Attributs',
            },
        ),
        migrations.AlterModelOptions(
            name='archetype',
            options={'verbose_name': 'Spec multiple > Archetype', 'verbose_name_plural': 'Specs multiples > Archetypes'},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Equipable', 'verbose_name_plural': 'Equipables'},
        ),
        migrations.AlterModelOptions(
            name='equipmenteffect',
            options={'verbose_name': 'Equipable > Effet', 'verbose_name_plural': 'Equipables > Effets'},
        ),
        migrations.AlterModelOptions(
            name='equipmentobject',
            options={'verbose_name': 'Equipable > Objet', 'verbose_name_plural': 'Equipables > Objets'},
        ),
        migrations.AlterModelOptions(
            name='race',
            options={'verbose_name': 'Spec unique > Race', 'verbose_name_plural': 'Specs uniques > Races'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Spec multiple > Compétence', 'verbose_name_plural': 'Specs multiples > Compétences'},
        ),
    ]
