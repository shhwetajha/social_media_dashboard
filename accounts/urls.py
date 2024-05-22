from django.urls import path
from .views import *
urlpatterns=[
path('signup/',view_signup,name='signup'),
path('signin/',view_signin,name='signin'),
path('logout/',view_logout,name='logout'),
path('setting/',view_setting,name='setting'),
path('profile/<str:pk>/',view_profile,name='profile')
]