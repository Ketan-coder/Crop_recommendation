from django.db import models

# Storing the User Inputs by model
class CropRecommendation(models.Model):
    Nitrogen = models.IntegerField()
    Phosphorous = models.IntegerField()
    Potassium = models.IntegerField()
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ph = models.FloatField()
    Rainfall = models.FloatField()
    # This field is hidden by default
    label = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        # if label is not null then print label
        if self.label is not None and self.label.strip():
            return str(self.label)
        # else print id
        else:
            return str(self.id)
