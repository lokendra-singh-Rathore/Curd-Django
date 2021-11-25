from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from db.models import details
from db.forms import detailsfrom


def index(request):
    obs=details.objects.all()
    context={'obs':obs}
    
    return render(request,'index.html',context)

def addmember(request):
    form=detailsfrom
    if request.method=='POST':
        form=detailsfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context={'form':form}
    return render(request,'add_member.html',context)

def update(request,pk):
    form=detailsfrom
    member=details.objects.get(id=pk)
    if request.method == 'POST':
        form=detailsfrom(request.POST , instance=member)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={'form':form}
    return render(request,'add_member.html',context)

def delete(request,pk):
    member=details.objects.get(id=pk)
    member.delete()
    return redirect('index')
    