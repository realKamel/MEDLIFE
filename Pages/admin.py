from django.contrib import admin

from .models import product_item
from .models import client

# Register your models here.


admin.site.register(product_item)
admin.site.register(client)