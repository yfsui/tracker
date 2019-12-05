from django.urls import path
from . import views

app_name ='tracker'

urlpatterns = [
    path('sightings/', views.all, name = "all"),
    path('sightings/add/',views.add, name = "add"),
    path('sightings/stats/',views.stats,name='stats'),
    path('sightings/<Unique_Squirrel_ID>/', views.update, name = "update"),
    path('map/',views.map, name ='map'),
]
