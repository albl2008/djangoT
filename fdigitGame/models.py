from django.db import models


# Create your models here.
class Newnumber(models.Model):
    
    numberR = models.IntegerField()

    def publish(self):
        self.save()

class Guess(models.Model):
    intento = models.IntegerField()

