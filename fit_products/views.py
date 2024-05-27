from django.shortcuts import render
from .models import Product, Category, MainCategory

def all_products(request):
     """ A view to show all available products, including sorting and search queries """

