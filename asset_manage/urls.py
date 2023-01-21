from django.urls import path
from . import views
urlpatterns = [
    path('emp', views.emp),
    path('show',views.show),
    path('assetinfoshow',views.assetinfoshow),
    path('assetinfo',views.Assetinformation),
    path('assetstatus',views.Assetstatusinformation),
    path('assetstatusshow',views.assetstatusshow),
    path('department',views.Departmentinformation),
    path('departmentshow',views.departmentshow),
    path('employeeinfo',views.Employeeinformation),
    path('employeeinfoshow',views.employeeinfoshow),
    path('item',views.Iteminformation),
    path('itemshow',views.itemshow),
    path('category',views.Categoryinformation,name='category'),
    path('categoryshow',views.categoryshow),
    path('employeeinfo',views.Employeeinfo),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('emplyeeList',views.emplyeeList),
    path('maintenanceProducts',views.maintenanceProducts),
    path('staff/', views.staffdashboard, name='staff'),
    path('totalasset',views.Totalasset),
    path('employeewisereport',views.Employeewisereport),
    path('update_status/<int:id>', views.Update_status),
    path('maintenancerequest/',views.maintenancerequest, name='maintenancerequest'),
    path('maintenanceshow',views.maintenanceshow),

    
]