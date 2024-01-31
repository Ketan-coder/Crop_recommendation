from django import forms
from .models import CropRecommendation

class CropRecommendationForm(forms.ModelForm):
    class Meta:
        model = CropRecommendation
        fields = ['Nitrogen', 'Phosphorous', 'Potassium', 'Temperature', 'Humidity', 'Ph', 'Rainfall']

    def __init__(self, *args, **kwargs):
        super(CropRecommendationForm, self).__init__(*args, **kwargs)
        # You can customize the form fields here if needed
