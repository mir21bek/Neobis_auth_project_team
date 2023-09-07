from django.urls import path

from .views import *


urlpatterns = [
    path('signup/', UserProfileSignupSerializer.as_view(), name='signup'),
    path('signup/verify/', SignupVerify.as_view(), name='signup-verify'),

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
