from django.views.generic import ListView, DetailView
from .models import Posts


class HomeView(ListView):
    model = Posts
    template_name = 'home.html'
    object_context_name = 'post_list'

class HomePageDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'
