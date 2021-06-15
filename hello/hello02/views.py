
from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.
def hello(request):
    return render(request, 'hello02.html',{'name':'파이썬'})
      #request 받아서, hello02.html을 그려줄건데 name 이 파이썬일거야.
      
      
def var01(request):
    lst = ['python', 'Django', 'Template']
    return render(request, 'variable01.html', {'lst':lst})


def var02(request):
    dct = { 'class': 'qclass', 'name':'혜지'}
    return render(request, 'variable02.html', {'dct':dct})


def forLoop(request):
    return render(request, 'for.html',{'numbers': range(1,10)})


def if01(request):
    return render(request, 'if01.html', {'user': {'id':'qclass', 'name':'혜지 '}})    
# http://127.0.0.1:8000/hello02/if01



def if02(request):
    return render(request, 'if02.html', {'role': 'boss'})


def href(request):
    return render(request, 'href.html')















