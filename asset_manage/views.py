from urllib import request
from xml.dom.minidom import TypeInfo
from django.shortcuts import render, redirect
from .forms import AssetForm,InfoForm,DepartmentForm,ItemForm,CategoryForm,EmployeeinfoForm,AssetstatusForm,MaintenancerequestForm,AssetrequestForm
from .models import Asset,Assetinfo,Department,Employeeinfo,Category,Item,Assetstatus,Maintenancerequest,Assetrequest
from django.contrib.auth.models import User
from django.contrib import messages 



# Create your views here.
def emp(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        title = request.POST['title']
        asset_quantity = int(request.POST['asset_quantity'])
        asset_id=Asset.objects.filter(title=title).first()
        if form.is_valid():
            try:
               
                asset = Assetinfo.objects.filter(tag_no=asset_id.id).first()
                print(asset)
                print(asset.quantity)
                if asset:
                    
                    asset.quantity -= asset_quantity
                    asset.save()
                
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
        tag_no = request.POST['tag_no']
        quantity = int(request.POST['quantity'])
        
        if form.is_valid():
            try:
                asset=Assetinfo.objects.filter(tag_no=tag_no).first()
                if asset:
                    asset.quantity += quantity
                    asset.save()
                else:
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
    if request.POST:
        title= request.POST.get('title')
        description= request.POST.get('description')
        price= request.POST.get('price')
        quantity= request.POST.get('quantity')
        Asset.objects.filter(id=id).update(title=title,description=description,price=price,asset_quantity=quantity)
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
    wise_report = {x.username: {'distinct_opt': Asset.objects.filter(owner=x.id).count(), 'asset_name': list(Asset.objects.filter(owner=x.id).values_list('title', flat=True))} for x in User.objects.all()}
    return render(request, 'employeewisereport.html', {'wise_report': wise_report})
    
    

def Update_status(request, id):
    employee = Asset.objects.get(id=id)
    employee.status=True
    employee.save()
    print(employee.status)
    return redirect("/asset/show")

def maintenancerequest(request):
    if request.method == "POST":
        form = MaintenancerequestForm(request.POST)
        if form.is_valid():
            try:
                # form.save()
                data = form.save(commit=False)
                data.user_name=request.user
                data.save()
                print("Saved")
                messages.success(request, ('Request for maintenance successfully...'))
                return redirect('/asset/maintenancerequest')
            except:
                print("Saved problem")
                pass
        else:
            print(form.errors)
    else:
        form = MaintenancerequestForm()
        return render(request, 'maintenancerequest.html', {'form': form})

def maintenanceshow(request):
    products = Maintenancerequest.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "showmaintenancereq.html", {'employees':products})

def Approvemaintenance(request, id):
    employee = Maintenancerequest.objects.get(id=id)
    employee.delete()
    return redirect("/asset/maintenanceshow")

def requestasset(request):
    if request.method == "POST":
        form = AssetrequestForm(request.POST)
        if form.is_valid():
            
            try:
                # form.save()
                data = form.save(commit=False)
                data.User_id=request.user
                data.save()
                
                print("Saved")
                messages.success(request, ('Request asset successfully...'))
                return redirect('/asset/requestasset')
            except:
                print("Saved problem")
                pass
        else:
            print(form.errors)
    else:
        form = AssetrequestForm()
        return render(request, 'requestassetform.html', {'form': form})

def requestshow(request):
    products = Assetrequest.objects.all()
    # products = employees.order_by('date').values()
    # print("Product List Unsorted")
    # print(employees)
    print("Product List sorted")
    print(products)
    return render(request, "showrequestasset.html", {'employees':products})


def Approverequest(request, id):
    employee = Assetrequest.objects.get(id=id)
    employee.delete()
    return redirect("/asset/requestshow")