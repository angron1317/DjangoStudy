
'''
###第一种方法，直接在本文件中写html
from django.http import HttpResponse

def index(request): #django要求第一个参数
    html='Hello Word!'
    return HttpResponse(html)
 '''

from django.shortcuts import render
from block.models import Block

def index(request):
    # block_infos=[
    #     {"name":"运维专区","desc":"运维人员技术讨论茶园","manager":"block_infos"},
    #     {"name": "Django专区", "desc": "Djangoer讨论区", "manager": "Django姓名"},
    #     {"name": "部落专区", "desc": "部落建设讨论", "manager": "admin"}
    # ]

    # block_infos=Block.objects.all().order_by("-id") # 所有行

    block_infos = Block.objects.filter(status=0).order_by("-id")
    return render(request, "index.html", {"blocks": block_infos})
