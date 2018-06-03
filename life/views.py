from django.shortcuts import render
from django.http import HttpResponse
from .models import House
# Create your views here.
def life(request):
    list = House.objects.all()
    context = {'House_list':list}
    return render(request,'life.html',context=context)

def content(request,id):
    list = House.objects.get(pk=id)
    context = {'list': list}
    return render(request, 'lifecontent.html', context=context)
    # return HttpResponse("The param is : " + id)

