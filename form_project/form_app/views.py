from django.shortcuts import render,redirect
from form_app.models import *

# Create your views here.
def product_list(request):
    product_data=productModel.objects.all()
    
    context={
        'product_data':product_data
    }
    return render(request, 'product_list.html',context)