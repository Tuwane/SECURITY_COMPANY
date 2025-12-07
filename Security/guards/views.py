from django.shortcuts import render



# Create your views here.

def guards_list(request):
    return render(request, 'guard/guards_list.html')    
    
    
    
def profiles(request):
        return render(request, 'guard/profiles.html')
    
    

def add(request):
    return render(request, 'guard/add_guards.html')