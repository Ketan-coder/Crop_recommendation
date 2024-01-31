import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from .forms import CropRecommendationForm
from .models import CropRecommendation
import os
from django.utils.safestring import mark_safe

# Setting up base directory for easy access
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'Mainapp', 'files','Crop_recommendation.csv')

# Homepage/Landing Page 
def index(request):
    # Clear all objects in the CropRecommendation model
    CropRecommendation.objects.all().delete()
    
    # Render the index.html template (modify as needed)
    return render(request, "index.html")

# Function to train the model
def train_model():
    # Load data from the CSV file
    data = pd.read_csv(file_path)  # Update with your actual file path

    # Split the data into features (X) and target labels (y)
    X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = data['label']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the decision tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model

# Function to predict crop
def crop_recommendation(request):
    # If the form is submitted by Post method
    if request.method == 'POST':
        # Pass the form and take input from the user
        form = CropRecommendationForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Save the form data to the CropRecommendation model
            crop_recommendation_instance = form.save()

            # Load the trained model
            model = train_model()

            # Make prediction based on the user input
            user_input = [crop_recommendation_instance.Nitrogen, crop_recommendation_instance.Phosphorous,
                          crop_recommendation_instance.Potassium, crop_recommendation_instance.Temperature,
                          crop_recommendation_instance.Humidity, crop_recommendation_instance.Ph,
                          crop_recommendation_instance.Rainfall]

            predicted_crop = model.predict([user_input])[0]
            print(predicted_crop)
            # Display relevant information based on the predicted crop
            # crop_info = CropRecommendation.objects.filter(label=predicted_crop).first()
            crop_recommendation_instance.label = predicted_crop
            crop_recommendation_instance.save()

            # Create a new, empty form instance to clear the fields
            form = CropRecommendationForm()

            # Add a success message with relevant information
            messages.success(request, mark_safe(f'Predicted crop: <b>{predicted_crop.capitalize()}</b>'))
            return render(request, 'base.html', {'form': form, 'crop_info': predicted_crop.capitalize()})
    # If the form is not submitted, render the form
    else:
        form = CropRecommendationForm()
    # Render the base.html template with the form
    return render(request, 'base.html', {'form': form})
