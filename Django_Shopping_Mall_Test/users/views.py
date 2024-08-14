from django.shortcuts import render,redirect

# Create your views here.
from .forms import MemberShipForm
from django.contrib.auth import login,logout,authenticate

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup(request):
    if request.method == "POST":
        form = MemberShipForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            return redirect("user:login")
    else:
        form = MemberShipForm()

    return render(request,"users/signup.html",{"form":form})