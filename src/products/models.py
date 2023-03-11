from django.db import models
from django.urls import reverse

# any change in the model, you need to run the following command:
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
# Model is a representation of a table in the database. It inherits from models.Model
class Product(models.Model):
  title = models.CharField(max_length=120) # max_length = required
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(decimal_places=2, max_digits=10000)
  summary = models.TextField()
  featured = models.BooleanField(default = False)
  
  def get_absolute_url(self):
    # return f"/products/{self.id}/"
    return reverse("products:product-detail", kwargs={"my_id": self.id}) 