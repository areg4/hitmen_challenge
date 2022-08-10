from random import choices
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.

class Hitmen(AbstractBaseUser):
    STATUS_HITMAN_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive")
    )
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True, max_length=250)
    password = models.CharField(max_length=250, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    isActive = models.CharField(choices=STATUS_HITMAN_CHOICES, 
                                default='Active', max_length=8)
    isManager = models.BooleanField(default=False)
    managedBy = models.IntegerField(null=True)
    isBoss = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    class Meta:
        verbose_name = 'Hitmen'
    