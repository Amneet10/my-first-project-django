from django.shortcuts import render
from django.HttpResponse import HttpResponse

def learn_django(request):
    return HttpResponse('hello django')
    
    
def learn_python(request):
    return HttpResponse('hello python')
    
