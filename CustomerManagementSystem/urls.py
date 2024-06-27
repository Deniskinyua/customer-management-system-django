
from django.contrib import admin
from django.urls import path, include
from user import views as users
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from dashboard import views as views



#from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/',users.register,name = 'users'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
   # path('logout/', TemplateView.as_view(template_name='user/logout.html'), name='user-logout'),
   path('logout/', users.logout, name='user-logout' ),
   path('invoice/', views.add_invoice, name='invoice'),
   path('invoice_view/', views.list_invoice, name='invoice_view'),
   path('update/<str:pk>/', views.update_invoice, name='update_invoice'),
   path('delete/<str:pk>/', views.delete_invoice, name='delete_invoice'),
   #
   path('oauth/', include('social_django.urls', namespace='social')),
  




    #From authentication project
   # path("register/", views.index, name="index"),
    #path("login", views.login, name="login"),
    #path("logout", views.logout, name="logout"),
    #path("callback", views.callback, name="callback"),

]
