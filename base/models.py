from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Climax(models.Model):
    city = models.ForeignKey(City, on_delete= models.CASCADE)
    date = models.DateField()
    temperature = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
