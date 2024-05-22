from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,first_name=None,last_name=None,password=None):
        if not email:
            raise ValueError('user must have an email')
        if not username:
            raise ValueError('user must have an username')


        user=self.model(
            email=self.normalize_email(email),
            username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,username,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.first_name=first_name
        user.last_name=last_name
        user.is_active=True
        user.is_admin=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user


class account(AbstractBaseUser):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)

    # required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=MyAccountManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.email


    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True 


class Profile(models.Model):
    user=models.OneToOneField(account,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg=models.ImageField(upload_to='profile_picture',default='blankprofile.png')
    location=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.user.username