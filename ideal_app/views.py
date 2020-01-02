from django.shortcuts import render

# Create your views here.

def fn_index(request):
    return render(request,'index.html')

def fn_home(request):
    return render(request,'admin_home.html')

def fn_saveUser(request):
    return render(request,'user_reg.html')