from django.shortcuts import render, redirect
from .forms import ProductAddForm
from .models import Product
from django.contrib import messages

# Create your views here.
def index(request):
    items = Product.objects.all()
    return render(request, 'StoreIndex.html', {'items': items})

def AddProduct(request):
    form = ProductAddForm(data=request.POST or None)
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Added')
            return redirect("Store:store_index")
    except Exception as e:
        messages.warning(request, 'Error :(; The specified Item could not be created. Error {}'.format(e))
    context = {'form':form}
    return render(request, 'addProduct.html', context)

def RemoveProduct(request):
    pass

def ProductManagementPage(request):
    pass
