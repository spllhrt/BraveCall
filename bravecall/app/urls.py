from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),  
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'), 
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('profile/', views.update_profile, name='profile'), 
    path('logout/', views.logout_user, name='logout'),
]