from django.shortcuts import render
from .models import Notice,BigImage,SamllImage
from news.models import CompanyNews,LocalNews,MediaNews
from product.models import People

# Create your views here.
def Idlen(n,list):
    l = len(list)
    if l-n<0:
        return 0
    else:
        return l-n

def index(request):
    list = Notice.objects.all()
    Notice_list = list[Idlen(4,list):]

    list = CompanyNews.objects.all()
    CompanyNews_list = list[Idlen(3,list):]



    list = MediaNews.objects.all()
    MediaNews_list = list[Idlen(3,list):]

    context = {'Notice_list': Notice_list,'CompanyNews_list':CompanyNews_list,'MediaNews_list':MediaNews_list}
    return render(request,'index.html',context=context)

def content(request,id):
    list = Notice.objects.get(pk=id)
    context = {'list': list}
    return render(request, 'noticecontent.html', context=context)