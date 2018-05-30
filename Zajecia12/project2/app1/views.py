from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index(request):
    name=request.GET.get("name")
    surname=request.GET.get("surname")
    #Person.objects.create(name, surname)
    student=Person.objects.all()
    return render(request, 'app1/templates.html', {'student':student})

    #name=request.GET.get("name")
    #return HttpResponse("Hello World!")
    #return HttpResponse(name)
