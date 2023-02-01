from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    
    def __str__(self):
        return self.name