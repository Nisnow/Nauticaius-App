
from django.db import models

class Npc(models.Model):
    name = models.TextField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    age = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    alignment = models.TextField(blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)
    first_appearance = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    str = models.IntegerField(blank=True, null=True)
    dex = models.IntegerField(blank=True, null=True)
    con = models.IntegerField(blank=True, null=True)
    int = models.IntegerField(blank=True, null=True)
    wis = models.IntegerField(blank=True, null=True)
    cha = models.IntegerField(blank=True, null=True)
    description = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nauticaius_bronzewater_npc_table'
