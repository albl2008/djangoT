from django.db import models


# Create your models here.
class Newnumber(models.Model):
    
    number = models.IntegerField()

    def publish(self):
        self.save()
