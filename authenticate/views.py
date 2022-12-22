from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from django.contrib.auth.models import User
from .forms import SignUpForm, EditProfileForm
from .decorators import authentication_not_required
from .models import Usertype
def home(request):
	return render(request, 'authenticate/home.html', {})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			emptype=user.is_staff
			print(Usertype.user)
			login(request, user)
			messages.success(request, ('You Have Been Logged In!'))
			if emptype==True:
				return redirect('asset/staff')
		    
			return redirect('home')
		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('/')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		user_type=request.POST.get("type_of_user")
		print(user_type)
		if form.is_valid():
			
			user = form.save(commit=False)
			
			user.save()
			Usertype.objects.create(user=user, user_type=user_type)
			print(user.is_staff)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)

			login(request, user)
			messages.success(request, ('You Have Registered...'))
			return redirect('/')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

# @authentication_not_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)


def asset(request):
	return render(request, 'authenticate/add_asset.html')

