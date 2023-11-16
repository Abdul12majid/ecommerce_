from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	products = Product.objects.all()
	return render(request, 'commerce/home.html', {'products':products})

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
