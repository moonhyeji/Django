from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.hello, name='index'),   #name 에 index를 넣어놓으니까 a 태그에서 해당 name으로 감! 경로를 이름으로 바꿈. 
    path('var01',views.var01),
    path('var02',views.var02),
    path('for', views.forLoop),
    path('if01', views.if01),
    path('if02', views.if02),
    path('href', views.href),
]