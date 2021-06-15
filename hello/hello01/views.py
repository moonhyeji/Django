from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1><a href="/hello01/test">여기는 hello  안의 Hello01의 뷰야!, django</a></h1>')
#요청이 들어오면 views.py에 요청을 연결해주는파일 : urls.py ->이거 만들어주기

def test(request):
    return HttpResponse('<h1><a href="/hello01"> return </a></h1>') 

