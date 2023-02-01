from django.urls import path
from modelapp import views

urlpatterns = [
    path('home/',views.createview,name='home'),
    path('sucess/',views.successpage,name='success'),
]