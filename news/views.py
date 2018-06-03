from django.shortcuts import render
from .models import LocalNews,CompanyNews,MediaNews

# Create your views here.


def news(request):

    CompanyNews_list = CompanyNews.objects.all()

    LocalNews_list = LocalNews.objects.all()

    MediaNews_list = MediaNews.objects.all()


    context = {'CompanyNews_list':CompanyNews_list,'LocalNews_list':LocalNews_list,'MediaNews_list':MediaNews_list}

    return render(request,'news.html',context=context)

def companycontent(request,id):
    list = CompanyNews.objects.get(pk=id)
    context = {'list': list}
    return render(request, 'lifecontent.html', context=context)

def localcontent(request,id):
    list = LocalNews.objects.get(pk=id)
    context = {'list': list}
    return render(request, 'lifecontent.html', context=context)

def mediacontent(request,id):
    list = MediaNews.objects.get(pk=id)
    context = {'list': list}
    return render(request, 'lifecontent.html', context=context)



