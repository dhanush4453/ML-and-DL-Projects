from django.shortcuts import render
from django.http import JsonResponse
from textblob import TextBlob
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Global list to store sentiments
sentiments = []

def home(request):
    return render(request,'home.html')

def new(request):
    return render(request,'add.html')

def home1(request):
    return render(request,'home1.html')

def model(request):
    return render(request,'model.html')

def working(request):
    return render(request,'working.html')

def about(request):
    return render(request,'about.html')

def track(request):
    return render(request,'track.html')

def senti(request):
    global sentiments
    if request.method == 'POST' and 'work' in request.POST:
        user_input = request.POST.get('work')
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        sentiments.append(polarity)  # Store sentiment
        if polarity > 0:
            sentiment = "positive"
            feedback = "Thank you for the review, I hope you enjoy your product."
        elif polarity < 0:
            sentiment = "negative"
            feedback = "We apologize for the inconvenience you have faced by the product we have delivered and following are the options you can follow \n1. Return the Product\n 2. Exchange the Product"
        else:
            sentiment = "neutral"
            feedback = "Thank you for the review. We will definitely look at the inappropriates and try to minimize the problems."
        
        return JsonResponse({'sentiment': sentiment, 'feedback': feedback})
    else:
        return JsonResponse({'error': 'Invalid request'})
