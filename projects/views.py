from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):

    message= "Wow! you are here"
    Age = 20
    context={"msg":message,"number":Age,"projects":projectsList}
    return render (request,"products.html",context)

def project(request,pk):
    projectsObj=None
    for i in projectsList:
        if i['id']==pk:
            projectsObj=i

    return render(request,"single_products.html",{'project':projectsObj})
