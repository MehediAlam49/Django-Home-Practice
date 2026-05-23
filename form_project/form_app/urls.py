from django.urls import path
from form_app.views import *

urlpatterns = [
    path('', product_list, name='product_list'),
]