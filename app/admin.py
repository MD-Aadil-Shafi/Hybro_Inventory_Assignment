from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Product,Location,ProductMovement
# Register your models here.

admin.site.unregister(Group)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(ProductMovement)
