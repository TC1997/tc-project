from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('sightings/', views.list, name='list'),
    # path('sightings/<int:unique_squirrel_id>/', views.update, name='update'),
    # path('sightings/add/', views.create, name='create'),
]
