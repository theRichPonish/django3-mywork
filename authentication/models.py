from django.db import models
class SignUpUser(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    confirm_email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
class SignInUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
class ChangePassword(models.Model):
    current_password = models.CharField(max_length=50)
    new_password = models.CharField(max_length=50)
    confirm_new_password = models.CharField(max_length=50)
