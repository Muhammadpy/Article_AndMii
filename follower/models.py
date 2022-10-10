from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

# from blog.models import Article

# Create your models here.

# class CustomUser(AbstractUser):
#     age=models.PositiveIntegerField(null=True, blank=True)
#     name=models.CharField(max_length=100)
#     surname=models.CharField(max_length=100)



class Fallower(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Ismi", unique=True, max_length=55,blank=True)
    surname = models.CharField(max_length=55)
    age = models.PositiveIntegerField(default=0)
    liked_articles = models.ManyToManyField('blog.Article',blank=True)
    rating = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    adress = models.CharField(max_length=500)

    def __str__(self):
        return self.name 


import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None ):
        if not email:
            raise ValueError("foydalanuchi emailiga ega bolishi kk")
        if not username:
            raise ValueError("foydalanuchi ismi  ega bolishi kk")
        
        user=self.model(
            email=self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user=self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=  password, 
            first_name = first_name, 
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        
        user.is_superadmin =True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=100, unique=True)
    phone_number=models.CharField(max_length=50)
    
    #requriment
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name']
    objects= MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
