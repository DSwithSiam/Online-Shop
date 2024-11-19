from django.urls import path
from account.views import Register, CustomerLogin


app_name = "account"
urlpatterns = [
    path('register/', Register, name = 'register'),
    path('login/', CustomerLogin, name = 'login'),
]