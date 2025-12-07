from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 




def home_view(request):
    return render(request, 'system/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.got('username')
        password = request.POST.got('password')
        
        user = authenticate(request, username='username', password='password')
        
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            return render(request, 'login.html', {'invalid':'try again'})
        
        
    return render(request, 'login.html')        