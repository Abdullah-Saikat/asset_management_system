from django import forms
from .models import Asset,Assetinfo,Department,Item,Category,Employeeinfo,Assetstatus


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = "__all__"
        
class InfoForm(forms.ModelForm):
    class Meta:
        model = Assetinfo
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"       

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"   

class EmployeeinfoForm(forms.ModelForm):
    class Meta:
        model = Employeeinfo
        fields = "__all__"

class AssetstatusForm(forms.ModelForm):
    class Meta:
        model = Assetstatus
        fields = "__all__"