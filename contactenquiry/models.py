from django.db import models


# Create your models here.
class ContactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=50)
    msg=models.TextField()
