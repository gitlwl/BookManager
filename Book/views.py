from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#视图函数定义在这里

def index(request):
    #进行处理
    return HttpResponse("JAVAandPython君在此")