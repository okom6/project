from django.shortcuts import render
from django.http import HttpResponse
from .app1 import app

def index(request, num="1"):
    #name=request.GET.get("name")
    return HttpResponse("Hello World!")
    #return HttpResponse(name)

    return render(request, 'app1/template.html', {})

#def index(request, num="1"):
    #if(num!="1"):
        #print(num)
