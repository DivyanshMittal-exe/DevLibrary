"""DevLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import home_view
from Home.views import login_view
from users.views import signup_view,login_view,logout_view
from book.views import book_view,book_from_view #Yes, this is a typo, sorry




urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', signup_view, name='signup'),
    path('register/register', signup_view, name='register'),
    path('login/', login_view, name='signup'),
    path('login/login', login_view, name='register'),
     path('logout/', logout_view, name='logout'),
    path('book/', book_view, name='book'),
    path('create/', book_from_view, name='form'),
    path('admin/', admin.site.urls)
]