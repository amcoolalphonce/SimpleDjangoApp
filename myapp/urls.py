from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about', views.about, name = 'about'),
        #authenticate
        path('login_user', views.login_user, name='login')
]