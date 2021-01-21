from django.urls import path
from  app1 import views

urlpatterns = [
    path('signup/',views.signup,name='sign'),
    path('home',views.home,name='home'),
]

