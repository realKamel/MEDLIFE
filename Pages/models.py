from django.db import models


# Create your models here.

class product_item(models.Model):
    x = [
        ('Medicine','Medicine'),
        ('Equipment','Equipment'),
        ('Vitamins','Vitamins')
    ]
    name = models.CharField(max_length=20)
    content = models.TextField(blank=True,default='',null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='Product_photos/%y/%m/%d')
    status = models.BooleanField(default=True)
    category = models.CharField(max_length=50 , null=True ,blank=True ,choices=x)
    
    def __str__ (self):
        return self.name
    
    
class client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100,unique = True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'