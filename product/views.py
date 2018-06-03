from django.shortcuts import render
from .models import Housekeeping,Car,People
# Create your views here.
def product(request):
    Housekeeping_list = Housekeeping.objects.all()
    Car_list = Car.objects.all()
    People_list = People.objects.all()
    context = {'Housekeeping_list':Housekeeping_list,'Car_list':Car_list,'People_list':People_list}
    return render(request,'product.html',context=context)