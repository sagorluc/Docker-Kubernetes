from django.urls import path, include
from accounts.views import (
    RegistrationView, 
    LoginView, 
    LogoutView,
    )
from rest_framework.routers import DefaultRouter


urlpatterns = [  
    path('', RegistrationView.as_view(), name='user_list'), # list of all users
    path('register/', RegistrationView.as_view(), name='register'),
    path('<int:id>/', RegistrationView.as_view(), name='register_user_details'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    

]
