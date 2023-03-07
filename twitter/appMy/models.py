from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User, verbose_name=("kullanici"), on_delete=models.CASCADE)
    text=models.TextField(("tweet"),max_length=200)
    image=models.FileField(("tweet gorseli"), upload_to='', max_length=100,null=True)
    
    def __str__(self):
        return self.user