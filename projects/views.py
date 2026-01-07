from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def projects(request):
    projects=Project.objects.all()
    context={"projects":projects}
    return render (request,"products.html",context)

def project(request,pk):
    projectsObj=Project.objects.get(id=pk)
    tags=projectsObj.tags.all()
    return render(request,"single_products.html",{'project': projectsObj,'tags': tags})
