from django.db import models

# Create your models here.
class CropRecommendation(models.Model):
    Nitrogen = models.IntegerField()
    Phosphorous = models.IntegerField()
    Potassium = models.IntegerField()
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ph = models.FloatField()
    Rainfall = models.FloatField()
    label = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)