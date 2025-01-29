from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    role = models.CharField(max_length=255,default='admin')  # Role field added
    
    def __str__(self):
        return self.name
