from django.urls import path
from .views import map_view, about_view


urlpatterns = [
    path('', map_view, name='map'),
    path('about/', about_view, name='about'),
]