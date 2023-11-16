from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
	products = Product.objects.all()
	return render(request, 'commerce/home.html', {'products':products})

def login_user(request):
	return render(request, 'commerce/login.html', {})
