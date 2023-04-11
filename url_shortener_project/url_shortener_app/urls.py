from django.urls import path
from .views import URLShortenView

urlpatterns = [
    path('', URLShortenView.as_view()),
]
