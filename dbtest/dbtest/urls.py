"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


#path 설정 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),  #아무것도 안들어오면 views의 index로 가고 이름은 index로 간다.
    path('detail/<int:id>', views.detail, name ='detail'),  #detail 이라고 요청이들어오는데 int값 (이름은 id)가 넘어옴. , views.detail 에 넘겨줄거야. 
    path('updateform/<int:id>',views.update_form, name='updateform'),
    path('updateres',views.update_res),
    path('delete/<int:id>',views.delete),
    path('insertform', views.insert_form , name="insertform"),
    path('insertres',views.insert_res),
]















