"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite.views import HomePageView
from mysite.tests import TestView

urlpatterns = [
    path('', HomePageView.homepage),
    path('post/<slug:slug>/', HomePageView.showpost),
    path('admin/', admin.site.urls),
    path('mysite/', TestView.test_view, name="test_page"),
    path('mysite/nd21', TestView.test2_view, name="nd21page"),
    path('mysite/nd23', TestView.show_nd23_view, name="nd23page")


]
