from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<a href="play/">进入游戏界面</a>'
    line3 = '<img src="https://img0.baidu.com/it/u=4035339947,1492935398&fm=26&fmt=auto" width=2000>'
    return HttpResponse(line1 + line2 + line3)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<a href="">回到首页</a>'
    line3 = '<img src="https://img0.baidu.com/it/u=418569545,82599050&fm=26&fmt=auto" width=2000>'
    return HttpResponse(line1 + line2 + line3)
