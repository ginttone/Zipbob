"""web_config URL Configuration

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

from home import views
from ip.functions import home_process

urlpatterns = [

    path('home', views.home,name='home'),
    path('test', views.test ,name='test'),
    path('', views.index,name='index'),
    path('premium', views.premium,name='premium'),
    path('frame_test', views.frame_test,name='frame_test'),

    path('emailchk', home_process.emailchk, name='emailchk'),
    path('regi_view', home_process.regi_view, name='regi_view'),
    path('login', home_process.login, name='login'),
    path('this_week', home_process.this_week, name='this_week'),
    path('next_week_pred', home_process.next_week_pred, name='next_week_pred'),

]
