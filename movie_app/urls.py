from django.urls import path
from .views import *

urlpatterns = [
    path('directors/', directors_view),
    path('directors/<int:id>/', directors_detail_view),
    path('movies/', movies_view),
    path('movies/<int:id>', movies_detail_view),
    path('reviews/', reviews_view),
    path('reviews/<int:id>', reviews_detail_view)
]
