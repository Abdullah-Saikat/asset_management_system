import functools
from django.shortcuts import redirect
from django.contrib import messages
from .models import Usertype

def authentication_not_required(view_func, redirect_url="accounts:profile"):

    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print (request.user.is_superuser)
        user_type=Usertype.objects.get(user=request.user)
        if  user_type.user_type=='Admin':
            return view_func(request,*args, **kwargs)
        messages.info(request, "You need to be logged out")
        print("You need to be logged out")
        return redirect(redirect_url)
    return wrapper