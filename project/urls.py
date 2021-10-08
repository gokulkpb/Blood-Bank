from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('add-donor', views.add_donor, name='add_donor'),
    path('login', views.login, name='login'),
    path('display', views.display, name='display'),
    path('logout', views.logout, name='logout')
    
]
