from django.urls import path

from application1 import views

urlpatterns = [
    path('suc',views.suc),
    path('h/',views.add,name='asset-add'),

    

]
