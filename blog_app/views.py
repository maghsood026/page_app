from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Posts
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Posts
    template_name = 'home.html'
    object_context_name = 'post_list'

class HomePageDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Posts
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Posts
    template_name = 'update_post.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Posts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')