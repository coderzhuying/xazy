from django.shortcuts import render
from .models import Recruitment
# Create your views here.
def join(request):
    Recruitment_list = Recruitment.objects.all()
    context = {'Recruitment_list':Recruitment_list}
    return render(request,'join.html',context)

