"""efsblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from . import views
from django.urls import path

app_name='portfolio'

urlpatterns = [
    path('',views.home,name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/delete/$', views.customer_delete, name='customer_delete'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    #url(r'^customer/(?P<pk>\d+)/portfolio/$', views.portfolio, name='portfolio'),
    path('stock/', views.stock_list, name='stock_list'),
    path('stock/<int:pk>/delete/$', views.stock_delete, name='stock_delete'),
    path('stock/<int:pk>/edit/$', views.stock_edit, name='stock_edit'),
    path('stock/create/$', views.stock_new, name='stock_new'),
    url(r'^investment/$', views.investment_list, name='investment_list'),
    url(r'^investment/(?P<pk>\d+)/delete/$', views.investment_delete, name='investment_delete'),
    url(r'^invstment/(?P<pk>\d+)/edit/$', views.investment_edit, name='investment_edit'),
    url(r'^investment/create/$', views.investment_new, name='investment_new'),
    url(r'^portfolio/(?P<pk>\d+)/portfolio/$', views.portfolio, name='portfolio'),
    #url(r'^customers_json/', views.CustomerList.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='success'),




]