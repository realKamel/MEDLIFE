from django.db import models

# Create your models here.

class product_item(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='Product_photos/%y/%m/%d')
    status = models.BooleanField(default=True)
    
    def __str__ (self):
        return self.name