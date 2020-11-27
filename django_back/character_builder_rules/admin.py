from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import AttributeType, CharacterSheetLine, Race, Archetype, Skill, Equipment, EquipmentObject, EquipmentEffect

# Register your models here.

admin.site.register(AttributeType)


class CharacterSheetLineChildAdmin(PolymorphicChildModelAdmin):
    base_model = CharacterSheetLine
    show_in_index = True


@admin.register(Race)
class RaceAdmin(CharacterSheetLineChildAdmin):
    base_model = Race


@admin.register(Archetype)
class ArchetypeAdmin(CharacterSheetLineChildAdmin):
    base_model = Archetype


@admin.register(Skill)
class SkillAdmin(CharacterSheetLineChildAdmin):
    base_model = Skill


class EquipmentChildAdmin(CharacterSheetLineChildAdmin):
#class EquipmentAdmin(CharacterSheetLineChildAdmin):
    base_model = Equipment


@admin.register(EquipmentEffect)
class EquipmentEffectAdmin(EquipmentChildAdmin):
    base_model = EquipmentEffect


@admin.register(EquipmentObject)
class EquipmentObjectAdmin(EquipmentChildAdmin):
    base_model = EquipmentObject


@admin.register(Equipment)
class EquipmentParentAdmin(PolymorphicParentModelAdmin):
#class EquipmentAdmin(CharacterSheetLineChildAdmin):
    base_model = Equipment
    child_models = (EquipmentObject, EquipmentEffect )
    polymorphic_list = True


@admin.register(CharacterSheetLine)
class CharacterSheetLineParentAdmin(PolymorphicParentModelAdmin):
    base_model = CharacterSheetLine
    #Not listing Equipment avoids errors when trying to create equipments (equipents being a virtually abstract class)
    child_models = (Race, Archetype, Skill, EquipmentObject, EquipmentEffect)
    list_filter = (PolymorphicChildModelFilter,)
    polymorphic_list = True
