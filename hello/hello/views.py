from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, world! </h1>')

#index는 8000에 아무것도 없으면 인덱스가 응답될거야 라고 써놓음.  




def mytest(request):
    return HttpResponse('<h1>hello, Django</h1>')