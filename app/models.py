from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    