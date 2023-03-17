from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Userinfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    image = models.FileField(upload_to='',  blank=True)
    bgimage = models.FileField(upload_to='',  blank=True)
    follow = models.ManyToManyField(User, related_name="takip")
    follower = models.ManyToManyField(User, related_name='takipci')
    
    def __str__(self):
        return self.user.username
    