from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add',views.new,name = "add"),
    path('home1',views.home1,name = "home1"),
    path('model',views.model,name = "model"),
    path('working',views.working,name = "working"),
    path('about',views.about,name = "about"),
    path('track',views.track,name = "track"),
    path('senti',views.senti,name = "senti"),
]
