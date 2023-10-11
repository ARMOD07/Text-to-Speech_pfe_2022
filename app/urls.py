from django.urls import include, path
from app.views import  get_sms, home
urlpatterns = [
    path('',home,name="index"),
    path('get_sms/',get_sms,name="get_sms"),

    
]

