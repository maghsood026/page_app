from django.urls import path
from .views import (
                     HomeView,
                     HomePageDetailView,
                     BlogCreateView,
                     BlogUpdateView,
                     BlogDeleteView
                     )

urlpatterns = [
    path('post/<pk>/delete', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new' ),
    path('post/<pk>/', HomePageDetailView.as_view(), name='post_detail'),
    path('', HomeView.as_view(), name='home')
]