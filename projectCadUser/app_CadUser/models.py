from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(max_length=255)
    user_email = models.EmailField()
    user_birth_year = models.IntegerField()
    user_course = models.TextField(max_length=128)
    
