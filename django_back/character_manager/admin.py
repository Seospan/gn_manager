from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import CharacterSheet, XPLogType, XPLog
# Register your models here.

admin.site.register(CharacterSheet)
admin.site.register(XPLogType)
admin.site.register(XPLog)
