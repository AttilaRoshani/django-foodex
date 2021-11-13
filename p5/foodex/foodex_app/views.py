from django.shortcuts import render
from .models import resturant

def get_resturant(request):
    
    context={'resturant': resturant.objects.all()}
    
    return render(request,'get_resturants.html',context)
def add_resturant(request):
    if request.method == "GET":
        return render(request,'form.html')
    if request.method == "POST":
        data=request.POST
        resturant.objects.create(name=data['name'],city_name=data['city_name'],adress=data['adress'],descriptions=data['descriptions'])
        return render(request,'finished.html')

def home_view(request):
    return render(request, 'home.html')
    


