from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path("",views.index,name='home'),
   path("transactions/<int:cust_id>/",views.transaction,name='transactions'),
   path("view_users",views.view_users,name='view_users'),
   path("view_transactions",views.view_transactions,name='view_transactions'),
]