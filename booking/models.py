from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    image= models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField()
    