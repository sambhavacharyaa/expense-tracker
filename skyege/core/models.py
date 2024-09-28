from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    Description = models.TextField(blank=True, null=True)

class Reciept(models.Model):
    Vendor = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Date = models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    Description = models.TextField(blank=True, null = True)
    Email_Subject = models.CharField(max_length= 255)
    Email_Date = models.DateTimeField()