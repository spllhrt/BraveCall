from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),  
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'), 
    path('navbar/', views.navbar, name='navbar'), 
    path('profile/', views.update_password, name='profile'), 
    path('logout/', views.logout_user, name='logout'),
]