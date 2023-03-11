from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
  print(request.user)
  return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
  return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
  # template context
  my_context = {
    "title": "this is about us",
    "my_number": 123,
    "my_list": [123, 312, 789, "abc"],
  }
  
  # django takes in the template and context and renders it together
  return render(request, "about.html", my_context)
