from django.contrib import admin
from .models import Asset,Assetinfo,Department,Item,Category

admin.site.register(Asset)
admin.site.register(Assetinfo)
admin.site.register(Department)
admin.site.register(Item)
admin.site.register(Category)

# Register your models here.
