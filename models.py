from django.db import models

# Create your models here.
class article1(models.Model):
    icon = models.CharField(max_length=50)
    head = models.CharField(max_length=100)
    para = models.CharField(max_length=300)
    link = models.CharField(max_length=50)
    
class article2(models.Model):
    img = models.ImageField(upload_to="pic/")
    head = models.CharField(max_length=100)
    para = models.CharField(max_length=300)
    offer = models.BooleanField(default=False)
    