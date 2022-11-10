from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls')),
    path('asset/', include('asset_manage.urls')),
    # path('user/', include('usermanage.urls')),
]
admin.site.site_header = "Assets Management Dashboard"
admin.site.site_title = "Assets Management Dashboard"
admin.site.index_title = "Welcome to Assets Management Dashboard"