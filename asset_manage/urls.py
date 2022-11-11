from django.urls import path
from . import views
urlpatterns = [
    path('emp', views.emp),
    path('show',views.show),
    path('assetinfo',views.Assetinfo),
    path('department',views.Department),
    path('item',views.Item),
    path('category',views.Category),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('emplyeeList',views.emplyeeList),
    path('maintenanceProducts',views.maintenanceProducts)
]