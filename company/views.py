from django.shortcuts import render
from .models import CompanyStructure,CompanyMemorabilia,CompanyTeam,CompanyCulture,CompanyProfile

# Create your views here.
def Idlen(n,list):
    l = len(list)
    if l-n<0:
        return 0
    else:
        return l-n

def company(request):

    list = CompanyProfile.objects.all()
    profile_list = list[Idlen(3, list):]

    list = CompanyStructure.objects.all()
    structure_list = list[Idlen(3, list):]

    list= CompanyCulture.objects.all()
    culture_list = list[Idlen(3, list):]

    list = CompanyTeam.objects.all()
    team_list = list[Idlen(3, list):]

    list = CompanyMemorabilia.objects.all()
    memorabilia_list = list[Idlen(3, list):]

    context = {'profile_list':profile_list,'structure_list':structure_list,'culture_list':culture_list,'team_list':team_list,'memorabilia_list':memorabilia_list}
    return render(request,'company.html',context=context)

