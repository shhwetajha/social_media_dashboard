from django.db import models
import uuid
from accounts.models import *
# Create your models here.

class CommentPost(models.Model):
    user=models.ForeignKey(account,on_delete=models.CASCADE)
    post_id=models.CharField(max_length=500,default=None)
    comment=models.TextField(max_length=100)
    date_added=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class post(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    caption=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    no_of_likes=models.IntegerField(default=0)
    comments=models.ForeignKey(CommentPost,on_delete=models.CASCADE,default=None,null=True,blank=True)


    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username

