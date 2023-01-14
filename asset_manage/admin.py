from django.contrib import admin
from .models import Asset,Assetinfo,Department,Item,Category,Employeeinfo,Assetstatus,Assetrequest

admin.site.register(Asset)
admin.site.register(Assetinfo)
admin.site.register(Department)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Employeeinfo)
admin.site.register(Assetstatus)
admin.site.register(Assetrequest)

# Register your models here.
