from django.shortcuts import render,redirect
from .models import users
def index(request):
    return render(request,'semi_rested/index.html')
def new(request):
    
    return render(request,'semi_rested/new.html')
def create(request):
    users.objects.create(full_name=request.GET['first_name']+request.GET['last_name'],email=request.GET['email'])
    return redirect('/users')
# Create your views here.
