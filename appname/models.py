from django.db import models

# Create your models here.
class Heroe(models.Model):
    id_external = models.IntegerField(unique=True,null=True)
    name = models.CharField(max_length=40)
    intelligence = models.IntegerField()
    strength = models.IntegerField()
    speed = models.IntegerField()
    durability = models.IntegerField()
    power = models.IntegerField()
    combat = models.IntegerField()
    race = models.CharField(max_length=40,null=True)
    gender = models.CharField(max_length=40,null=True)
    alignment = models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.name

