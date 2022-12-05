from django.urls import path
from . import views
urlpatterns = [
    path('emp', views.emp),
    path('show',views.show),
    path('assetinfoshow',views.assetinfoshow),
    path('assetinfo',views.Assetinformation),
    path('department',views.Departmentinformation),
    path('departmentshow',views.departmentshow),
    path('employeeinfo',views.Employeeinformation),
    path('employeeinfoshow',views.employeeinfoshow),
    path('item',views.Item),
    path('category',views.Category),
    path('employeeinfo',views.Employeeinfo),
    path('assetstatus',views.Assetstatus),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('emplyeeList',views.emplyeeList),
    path('maintenanceProducts',views.maintenanceProducts)
]