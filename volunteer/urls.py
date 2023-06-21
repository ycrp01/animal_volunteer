from django.urls import path

from .views import *

app_name = 'volunteer'

urlpatterns = [
    path('upload/', PlaceUploadView.as_view(), name='place_upload'),
    path('<region_slug>/', place_in_region, name='place_in_region'),
    path('<int:id>/<place_slug>/', place_detail, name='place_detail'),
    path('delete/<int:pk>/', PlaceDeleteView.as_view(), name='place_delete'),
    path('update/<int:pk>/', PlaceUpdateView.as_view(), name='place_update'),
    path('', place_in_region, name='place_all'),
]
