
from django.db import models


class Service(models.Model):
    Service_icon=models.CharField(max_length=50)
    Serice_title=models.CharField(max_length=50)
    Service_des=models.TextField()



