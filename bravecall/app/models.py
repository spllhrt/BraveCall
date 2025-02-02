from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    role = models.CharField(max_length=255, default='admin')
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/profile-user.png')  # Fix default image path

    def __str__(self):
        return self.name

