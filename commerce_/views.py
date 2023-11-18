from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
	products = Product.objects.all()
	return render(request, 'commerce/home.html', {'products':products})

def index(request):
	products = Product.objects.all()
	return render(request, 'commerce/index.html', {'products':products})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.filter(username=username).exists()
		print(user)
		if user is True:

			#if not user.check_password():
			#	messages.success(request, ('wrong password'))
			#	return redirect(request.META.get("HTTP_REFERER"))
			
			user_ = authenticate(request, username=username, password=password)
			if user_ is not None:
				login(request, user_)
				return redirect('/')
			else:
				messages.success(request, ('invalid details'))
				return redirect(request.META.get("HTTP_REFERER"))
		else:
			return redirect('register')
	return render(request, 'commerce/login.html', {})


def create_account(request):
	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				a = User.objects.filter(username=username).first()
				return render(request, 'commerce/create_account.html', {'first_name':first_name, 'username':username, 'last_name':last_name, 'email':email, 'a':a})
			elif User.objects.filter(email=email).exists():
				b = User.objects.filter(email=email).exists()
				return render(request, 'commerce/create_account.html', {'first_name':first_name, 'username':username, 'last_name':last_name, 'email':email, 'b':b})
			else:
				user = User.objects.create_user(first_name=first_name, username=username, last_name=last_name, email=email, password=password2)
				user.save()
				login(request, user)
				return redirect('/')
		else:
			c = password1==password2
			return render(request, 'commerce/create_account.html', {'first_name':first_name, 'username':username, 'last_name':last_name, 'email':email, 'c':c})
	return render(request, 'commerce/create_account.html', {})


def product(request, pk):
	item = Product.objects.get(id=pk)
	return render(request, 'commerce/product.html', {"item":item})


def category(request, foo):
	foo = foo.replace('-', ' ')
	try:
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'commerce/category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("Category doesn't exist"))
		return redirect('home')
