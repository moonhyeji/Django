from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone



def index(request):
    return render(request, 'index.html', {'list':MyBoard.objects.all()})



def detail(request, id):                                        #컬럼 id = 넘어온 값id (파라미터의 id)
    return render(request,'detail.html', {'dto':MyBoard.objects.get(id=id)})



def update_form(request, id):
    return render(request, 'update.html', {'dto':MyBoard.objects.get(id=id)})



def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    
    myboard = MyBoard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    
    if result_title + result_content == 2:
        return redirect('detail/' + id)
    else: 
        return redirect('updateform/'+id)
    
    
def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()
    
    
    if result_delete[0] == 1:
        return redirect('index')
    else :
        return redirect('delete/'+id)
    
def insert_form(request):
    return render(request, 'insert.html')


def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    
    
    result = MyBoard.objects.create(myname = myname,
                                    mytitle=mytitle,
                                    mycontent=mycontent,
                                    mydate=timezone.now())
    
    if result:
        return redirect('index')
    else:
        return redirect('insertform')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    