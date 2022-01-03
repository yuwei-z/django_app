from django.shortcuts import render


def index(request):     # 一定有一个参数是request
    return render(request, "multiterminals/web.html")   # 地址从templates/开始， render的第一个参数是request
