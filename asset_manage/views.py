from urllib import request
from xml.dom.minidom import TypeInfo
from django.shortcuts import render, redirect
from .forms import AssetForm,InfoForm,DepartmentForm,ItemForm,CategoryForm
from .models import Asset
from django.contrib.auth.models import User


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/asset/show')
            except:
                pass
    else:
        form = AssetForm()
    return render(request, 'index.html', {'form': form})


def Assetinfo(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/asset/assetinfo')
            except:
                print("Saved problem")
                pass
    else:
        form = InfoForm()
        return render(request, 'assetinfo.html', {'form': form})

def Department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/asset/department')
            except:
                print("Saved problem")
                pass
    else:
        form = DepartmentForm()
        return render(request, 'department.html', {'form': form})

def Item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/asset/item')
            except:
                print("Saved problem")
                pass
    else:
        form = ItemForm()
        return render(request, 'item.html', {'form': form})

def Category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/asset/item')
            except:
                print("Saved problem")
                pass
    else:
        form = CategoryForm()
        return render(request, 'category.html', {'form': form})



def show(request):
    products = Asset.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "show.html", {'employees':products})


def edit(request, id):
    employee = Asset.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Asset.objects.get(id=id)
    form = AssetForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/asset/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Asset.objects.get(id=id)
    employee.delete()
    return redirect("/asset/show")

def emplyeeList(request):
    employees = User.objects.all()
    return render(request,'employeeList.html',{'employeeList':employees})

def maintenanceProducts(request):
    products = Asset.objects.all().order_by('date').values()
    print(type(products))
    count =0
    return render(request, "maintenanceProducts.html", {'products':products,"count":count})
