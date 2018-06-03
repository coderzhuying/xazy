from django.shortcuts import render
from .models import Information
# Create your views here
def advice(request):
    list = Information.objects.all()
    context = {'Information_list':list}
    return render(request,'advice.html',context=context)