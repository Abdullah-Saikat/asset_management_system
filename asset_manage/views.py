from django.shortcuts import render, redirect
from .forms import AssetForm
from .models import Asset


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


def show(request):
    employees = Asset.objects.all()
    return render(request, "show.html", {'employees': employees})


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
