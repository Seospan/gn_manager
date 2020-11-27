from django.db import models
from django.db import models
from polymorphic.models import PolymorphicModel
# Create your models here.


# Pour le calcul de la fiche : pour le perso, lister toutes les carac, les modificateurs liés à ce perso.
# Si aucun modificateur, la valeur prend la base value. Sinon appliquer les modifs.
class AttributeType(models.Model):
    name = models.CharField(max_length=128)
    base_value = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Attribut"
        verbose_name_plural = "Attributs"



class CharacterSheetLine(PolymorphicModel):
    class Meta:
        verbose_name = '1 - Ligne de fiche perso'
        verbose_name_plural = '1 - Lignes de fiches perso'
    #def __str__(self):
     #   return "a "


class Race(CharacterSheetLine):
    name = models.CharField(max_length=128)
    mother_race = models.ForeignKey('self', blank=True, null=True,  on_delete=models.CASCADE, related_name="inherited_mother_race")

    def __str__(self):
        if isinstance( self.mother_race, Race ):
            return "[Sous-race] " + self.name
        else:
            return "[Race] " + self.name

    class Meta:
        verbose_name = 'Spec unique > Race'
        verbose_name_plural = 'Specs uniques > Races'

class CharacterSheetMultipleLine(CharacterSheetLine):
    pass


class Archetype(CharacterSheetMultipleLine):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "[Archetype] "+self.name

    class Meta:
        verbose_name = 'Spec multiple > Archetype'
        verbose_name_plural = 'Specs multiples > Archetypes'


class Skill(CharacterSheetMultipleLine):
    name = models.CharField(max_length=256)

    def __str__(self):
        return "[Compétence] " + self.name

    class Meta:
        verbose_name = 'Spec multiple > Compétence'
        verbose_name_plural = 'Specs multiples > Compétences'


class Equipment(CharacterSheetMultipleLine):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipable'
        verbose_name_plural = 'Equipables'

    def __str__(self):
        return "[Equipable] "+self.name


class EquipmentObject(Equipment):
    class Meta:
        verbose_name = 'Equipable > Objet'
        verbose_name_plural = 'Equipables > Objets'

    def __str__(self):
        return "[Objet] "+self.name


class EquipmentEffect(Equipment):
    class Meta:
        verbose_name = 'Equipable > Effet'
        verbose_name_plural = 'Equipables > Effets'

    def __str__(self):
        return "[Objet] "+self.name

#class CharacterSheetModifier(models.Model):

 #   class Meta:
  #      abstract = True


# class AttributeModifier(CharacterSheetModifier):

