from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.

# class Logs(models.Model):
#    date_creation = models.DateTimeField(auto_now_add=True)
#    date_last_edit = models.DateTimeField(auto_now=True)


class CharacterSheet(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class XPLogType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class XPLog(models.Model):
    type = models.ForeignKey(XPLogType, on_delete=models.CASCADE)
    character = models.ForeignKey(CharacterSheet, on_delete=models.CASCADE)
    value = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_edition = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[" + self.character.name +"] " + str(self.value) + " " + self.type.name

