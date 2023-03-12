from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title MUAHAH"}))
  description = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
        "placeholder": "Your description",
        "class": "new-class-name two",
        "id": "my-id-for-textarea",
        "rows": 20,
        "cols": 120
      }
    )
  )
  price = forms.DecimalField(initial=199.99)
  email = forms.EmailField()
  
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price'
    ]
    
  def clean_title(self, *args, **kwargs):
    # Django clean the form data, and then get the title.
    title = self.cleaned_data.get("title")
    print(title)
    if not "CFE" in title:
      print("yooo")
      raise forms.ValidationError("This is not a valid title")

    return title
    
  def clean_email(self, *args, **kwargs):
    # Django clean the form data, and then get the title.
    email = self.cleaned_data.get("email")
    if not "edu" in email:
      raise forms.ValidationError("This is not a valid email")

    return email