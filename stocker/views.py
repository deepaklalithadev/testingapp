from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Nursery


def home(request):
    nursery_list = Nursery.objects.all()
    context = {'nursery_list': nursery_list}
    return render(request,'stocker/home.html',context)


def detail(request,nid):
    target = Nursery.objects.get(id=nid)
    return render(request,'stocker/detail.html',{'target': target})


def add_nur(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        district = request.POST.get('district',)
        taluka = request.POST.get('taluka',)
        incharge = request.POST.get('incharge',)
        mobile = request.POST.get('mobile',)
        photo = request.FILES['photo']
        newnur = Nursery(name=name,district=district,taluka=taluka,incharge=incharge,mobile=mobile,photo=photo)
        newnur.save()
    return render(request,'stocker/add.html')