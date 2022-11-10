from django import forms
from .models import Asset,Assetinfo,Department


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