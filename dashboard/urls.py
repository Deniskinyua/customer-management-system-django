from django.urls import path
from  . import views



urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('customer/', views.staff, name='dashboard-customer'),
    path('product/', views.product, name='dashboard-product'),
    path('orders/', views.orders, name='dashboard-orders'),

    #logout

]
