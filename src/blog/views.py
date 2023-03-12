from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleModelForm
from django.urls import reverse

# Create your views here.

# Class-based views
# Class-based views inherit from a lot of different classes.
# To overwtire its primary function, we have to use get_object() method.
# Primary function of a DetailView is to render template from a specific object.
 
class ArticleListView(ListView):
  template_name = 'articles/article_list.html'
  queryset = Article.objects.all() # Looks for <blog>/<modelname>_list.html
  
class ArticleDetailView(DetailView):
  template_name = 'articles/article_detail.html'
  queryset = Article.objects.all() # Looks for <blog>/<modelname>_list.html
  
  # This is the primary function of a DetailView. In URL, instead of writing int:pk, we write int:id.
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Article, id=id_)
  

# Once a form is created, we automatically route to the form's detail page. e.g. /articles/1/. The class inherits get_absolute_url() method from models.py.
# This is the same for UpdateView.
# To change this routing, use get_success_url() method.
class ArticleCreateView(CreateView):
  template_name = 'articles/article_create.html'
  form_class = ArticleModelForm
  queryset = Article.objects.all()
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
  # If you want to change the routing after a form is created, you can use get_success_url() method.
  # def get_success_url(self):
  #   return '/'
  
class ArticleUpdateView(UpdateView):
  template_name = 'articles/article_create.html'
  form_class = ArticleModelForm
  queryset = Article.objects.all()
  
  # Grabs the object of the thing that you're trying to change.
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Article, id=id_)
    
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
  
  
# This time, we cannot ust get_absolute_url() method. We have to make a new method.
class ArticleDeleteView(DeleteView):
  template_name = 'articles/article_delete.html'
  queryset = Article.objects.all() # Looks for <blog>/<modelname>_list.html
  
  # This is the primary function of a DetailView. In URL, instead of writing int:pk, we write int:id.
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Article, id=id_)
  
  def get_success_url(self):
    return reverse('articles:article-list')
  


