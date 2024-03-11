import string
import random
from django.db import models
from django.contrib.auth.models import AbstractUser, Group

ADMIN_GROUP_NAME = 'Admin'
ACCOUNTANT_GROUP_NAME = 'Accountant'
SALESPERSON_GROUP_NAME = 'Salesperson'

def create_groups():
    Group.objects.get_or_create(name=ADMIN_GROUP_NAME)
    Group.objects.get_or_create(name=ACCOUNTANT_GROUP_NAME)
    Group.objects.get_or_create(name=SALESPERSON_GROUP_NAME)
    
class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  
    address = models.CharField(max_length=255, blank=True)  
    domain = models.CharField(max_length=255, blank=True)  
    logo = models.ImageField(upload_to='store_logos/', blank=True)  
    email = models.EmailField(blank=True)  
    phone_number = models.CharField(max_length=20, blank=True)  
    currency = models.CharField(max_length=10, blank=True)  
    timezone = models.CharField(max_length=50, blank=True)  
    is_active = models.BooleanField(default=True)  # Flag to indicate active store

    def __str__(self):
        return self.name


class User(AbstractUser):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True) 
    groups = models.ManyToManyField(Group)
    phonenumber = models.CharField(max_length=13)
    
    def code_generator(self):
        length = 5
        chars = string.ascii_uppercase + string.digits
        while True:
            code = ''.join(random.choice(chars) for _ in range(length))
            if not User.objects.filter(code=code).exists():
                return code
    
    def save(self, *args, **kwargs):
        if not self.code:  # Generate code only if it's not already set
            self.code = self.code_generator()
        super().save(*args, **kwargs) 
    
    def __str__(self) -> str:
        return self.username