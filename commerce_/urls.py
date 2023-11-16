from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login-user'),   
   # path('checkout', views.checkout, name='checkout'),
    #path('update_item/', views.update_item, name='update_item'),
]