from urllib import request
from xml.dom.minidom import TypeInfo
from django.shortcuts import render, redirect
from .forms import AssetForm,InfoForm,DepartmentForm,ItemForm,CategoryForm,EmployeeinfoForm,AssetstatusForm
from .models import Asset,Assetinfo,Department,Employeeinfo,Category,Item,Assetstatus
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


def Assetinformation(request):
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

def Departmentinformation(request):
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

def Iteminformation(request):
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

def Categoryinformation(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/asset/category')
            except:
                print("Saved problem")
                pass
    else:
        form = CategoryForm()
        return render(request, 'category.html', {'form': form})

def Employeeinformation(request):
    if request.method == "POST":
        form = EmployeeinfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/asset/employeeinfo')
            except:
                pass
    else:
        form = EmployeeinfoForm()
    return render(request, 'employeeinfo.html', {'form': form})

def Assetstatusinformation(request):
    if request.method == "POST":
        form = AssetstatusForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Saved")
                return redirect('/asset/assetstatus')
            except:
                print("Saved problem")
                pass
    else:
        form = AssetstatusForm()
        return render(request, 'assetstatus.html', {'form': form})


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
def assetinfoshow(request):
    products = Assetinfo.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "assetinfoshow.html", {'employees':products})

def departmentshow(request):
    products = Department.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "departmentshow.html", {'employees':products})

def employeeinfoshow(request):
    products = Employeeinfo.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "employeeinfoshow.html", {'employees':products})

def categoryshow(request):
    products = Category.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "categoryshow.html", {'employees':products})

def itemshow(request):
    products = Item.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "itemshow.html", {'employees':products})

def assetstatusshow(request):
    products = Assetstatus.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "assetstatusshow.html", {'employees':products})

def staffdashboard(request):
    emp_id = request.user.id
    print(emp_id)
    emp_Info = Asset.objects.filter(owner_id=emp_id).values()
    print(emp_Info)
    return render(request,'employeedashboard.html', {'emploo':emp_Info})

def Totalasset(request):
    report_val=None
    distinct_option=None
    if request.method == "POST":
        report_val=request.POST.get('searchtype')
        distinct_option=Asset.objects.filter(title=report_val).count()

        print(distinct_option)
        return render(request, 'totalassetreport.html', {'reports':report_val,'reportscount':distinct_option})
    # print(distinct_option)
    
    return render(request, 'totalassetreport.html', {'reports':report_val,'reportscount':distinct_option})

def Employeewisereport(request):
    # distinct_opt=Asset.objects.filter(owner=1).count()
    # print(distinct_opt)
    wise_report={}
    for x in User.objects.all():
        distinct_opt=Asset.objects.filter(owner=x.id).count()
        wise_report[x.username]=distinct_opt
        
        print(x.id)
        print(x.username)
    print(wise_report)
    print(len(wise_report))
    
    return render(request, 'employeewisereport.html',{'wisereports':wise_report})
    