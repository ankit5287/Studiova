from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Description = models.TextField(max_length=100)

    def __str__(self):
        return self.Name
    
class Signup(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    
class Loign(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Email
