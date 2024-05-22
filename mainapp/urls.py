from django.urls import path
from .views import *
urlpatterns=[
    path('home/',view_home,name='home'),
    path('upload/',view_upload,name='upload'),
    path('likepost/',view_likepost,name='likepost'),
    path('commentpost/<str:post_id>/',view_commentpost,name='commentpost')
    
]