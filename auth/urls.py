from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # We dont have to have a view with auth token,
    # it returns a token if provided correct credentials
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
