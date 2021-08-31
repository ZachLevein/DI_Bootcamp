from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import  RawProductForm, ProductForm

# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description, 
    # }
    context = {'object': obj}

    return render(request,"product/detail.html", context)

###### VALIDATING FORMS 

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {'form': form}
    return render(request,"product/create.html", context)

# # Raw HTML form (1)
# def product_create_view(request):
#     title = request.POST.get('title')
#     print(title)
#     context = {}
#     return render(request,"product/create.html", context)

# # Raw Django form (1) & (2)
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method =='POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request,"product/create.html", context)


##### Rendering and editing form DATA (Initital)
def render_initial_data(request):
    initial_data = { 
        'title': "This is my awesome title"
    }
    obj = Product.objects.get(id=21)
    form = ProductForm(request.POST or None, initial = initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,"product/create.html", context)


