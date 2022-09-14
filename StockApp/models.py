from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class StockUser(AbstractUser):
    full_name = models.CharField(max_length=200, null=False, blank=False, default='unknown')
    mobile=models.IntegerField(null=True, blank=True)
    is_active=models.BooleanField(default=True)


    class Meta:
        db_table = 'user_info'


class UserAuthTokens(models.Model):
    user_info = models.OneToOneField(StockUser, on_delete=models.CASCADE, related_name='user_tokens')
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_auth_tokens'



CHOICES = (
    ("1", "Available"),
    ("2", "Not Available")
)

class Brand(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    quantity = models.IntegerField()
    rate = models.FloatField(max_length=100)
    status = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.name


class UserQuerys(models.Model):
    name=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_name=models.ForeignKey(StockUser,on_delete=models.CASCADE)
    query=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
