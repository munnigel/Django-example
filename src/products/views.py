from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
# Function-based views

def product_create_view(request):
  # instantiate ProductForm class
  form = ProductForm(request.POST or None) # Renders out the form with data if POST data comes through, or elee render an empty form for other requests (GET). There are now validation errors to make sure the data is valid.
  
  # after validation, if form is valid, save it
  if form.is_valid():
    form.save()
    form = ProductForm() # reset the form to be empty after saving
    
  # form is in context to render it in the template
  context = {
    'form': form
  }
  return render(request, "products/product_create.html", context)

def product_update_view(request, my_id):
  obj = get_object_or_404(Product, id=my_id)
  form = ProductForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
  context = {
    'form': form
  }
  return render(request, "products/product_create.html", context)

def product_detail_view(request, my_id):
  # obj = Product.objects.get(id=my_id)
  obj = get_object_or_404(Product, id=my_id)
  context = {
    'object': obj
  }
  return render(request, "products/product_detail.html", context)

def product_delete_view(request, my_id):
  obj = get_object_or_404(Product, id=my_id)
  # POST request
  if request.method == "POST":
    # confirm delete
    obj.delete()
    return redirect('../../')
  context = {
    'object': obj
  }
  return render(request, "products/product_delete.html", context)

def product_list_view(request):
  queryset = Product.objects.all() # list of objects
  context = {
    "object_list": queryset
  }
  return render(request, "products/product_list.html", context)
  
