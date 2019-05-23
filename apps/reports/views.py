# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import JsonResponse
from users.utils.verify import *
from operations.models import *
from scanhosts.lib.utils import prpcrypt
from detail.utils.machines import *
from detail.utils.handdles import *
from detail.models import *
from detail.utils.handdles import *
import re
import os
import time
import platform


def base(request):
    return render(request, 'base.html', {})


def report(request):
    context = {'title': '报表平台'}
    return render(request, 'reports/report.html', context)


def histogram(request):
    """柱状图"""
    # for e in StatisticsRecord.objects.filter(id=1):
    #     pyh_count = e.pyh_count
    #     vmx_count = e.vmx_count
    #     kvm_count = e.kvm_count
    #     docker_count = e.docker_count
    #     net_count = e.net_count
    #     other_count = e.other_count

    e = StatisticsRecord.objects.last()
    print(e.pyh_count,e.other_count)
    e.v_count = e.vmx_count + e.kvm_count + e.docker_count
    list = [e.pyh_count, e.v_count, e.net_count, e.other_count]
    return render(request, 'reports/histogram.html', {'List': json.dumps(list)})


def rack(request):
    """机柜布置图"""
    item = CabinetInfo.objects.all()
    list=[]
    for x in item:
       list.append([x.cab_x,x.cab_y,   x.cab_name])
    return render(request, 'reports/rack.html', {'List': json.dumps(list)})


@login
@level
def cab_add(request):
    """手动添加机柜"""
    cab_num = request.POST.get("cab_num")
    cab_u = request.POST.get("cab_u")
    cab_high = request.POST.get("cab_high")
    cab_width = request.POST.get("cab_width")
    cab_deep = request.POST.get("cab_deep")
    cab_x = request.POST.get("cab_x")
    cab_y = request.POST.get("cab_y")

    cab_info = CabinetInfo()
    cab_area = float(cab_width)*float(cab_deep)
    print(cab_width, cab_deep, cab_area, "*************************")
    cab_info.cab_name = cab_num
    cab_info.cab_lever = cab_u
    cab_info.cab_high = cab_high
    cab_info.cab_width = cab_width
    cab_info.cab_deep = cab_deep
    cab_info.cab_area = cab_area
    cab_info.cab_x = cab_x
    cab_info.cab_y = cab_y
    cab_info.save()
    return render(request, 'detail/cab_list.html', {})


@login
@level
def phy_add(request):
    """手动添加物理服务器"""
    server_ip = request.POST.get("server_ip")
    machine_brand = request.POST.get("machine_brand")
    system_ver = request.POST.get("system_ver")
    sys_hostname = request.POST.get("sys_hostname")
    mac = request.POST.get("mac")
    ser_cabin = request.POST.get("ser_cabin")
    phy_u = request.POST.get("phy_u")

    phy_info = PhysicalServerInfo()
    # cab = CabinetInfo.objects.get(cab_name=ser_cabin)
    phy_info.ser_cabin_id = ser_cabin
    phy_info.server_ip = server_ip
    phy_info.machine_brand = machine_brand
    phy_info.system_ver = system_ver
    phy_info.sys_hostname = sys_hostname
    phy_info.mac = mac
    phy_info.phy_u = phy_u
    phy_info.save()
    return render(request, 'detail/index.html', {})
