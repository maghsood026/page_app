from django.urls import path
from .views import HomeView, HomePageDetailView

urlpatterns = [
    path('post/<pk>/', HomePageDetailView.as_view(), name='post_detail'),
    path('', HomeView.as_view(), name='home')
]