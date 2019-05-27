# coding=utf-8
from detail.models import *
from django.shortcuts import redirect
from detail.utils.machines import *
import json
import scanhosts.lib.J_do
from django.shortcuts import render
from django.http import JsonResponse
from users.utils.verify import *
from operations.models import *
from scanhosts.lib.utils import prpcrypt
from detail.utils.machines import *
from detail.utils.handdles import *
from detail.utils.handdles import *
import time
import scanhosts.lib.J_do
from django.http import StreamingHttpResponse
from django.utils.timezone import now
import pexpect,datetime
import re
import os
import time
import platform
from collections import defaultdict




def state_handdle(request):
    """状态修改"""
    detail_type = request.GET.get('detail_type')
    # 注：when detail_type='o' or 'n'时，下面conn_sn_key为设备序列号，并非用户连接的唯一设备标识或者id
    # 注：when detail_type='p' or 'v'时，下面conn_sn_key为与用户关联的id，并非唯一设备标识或者设备序列号
    conn_sn_key = request.POST.get('conn_id')
    state = request.POST.get('state')
    state_dict = {u'已报废': 0, u'测试使用': 1, u'线上运行': 2, u'下线': 3}
    if detail_type == ('p' or 'v'):
        conn_sn_key = Machines().filter_machines(ConnectionInfo, pk=conn_sn_key)[0].sn_key
    machine = Machines().filter_operations(SN=conn_sn_key)[0]
    machine.state = state_dict[state]
    machine.save()
    return redirect(request.session.get('path', '/'))

def module_deploy(request):
    item = ConnectionInfo.objects.all()
    list = []
    ip = []
    for x in item:
       list.append(x.ssh_hostip)
    return render(request, 'operations/module_deploy.html', {'List': json.dumps(list)})

def module_operate(request):
    operate_ip = request.POST.get("operate_ip")
    operate_order = request.POST.get("operate_order")
    ip = operate_ip.split(',')
    for i in ip:
        a = ip(i)
        print(a)
    return render(request, 'operations/module_operate.html', {})

def revise_net(request,param):

    list= param
    return render(request, 'operations/revise_net.html', {'list': list})

def revisee_net(request):
    server_ip = request.POST.get("list")
    net_cab = request.POST.get("net_cab")
    net_u = request.POST.get("net_u")

    print(list)

    for e in NetWorkInfo.objects.all():
        if e.host_ip==server_ip:
            if net_cab!='':
                a = CabinetInfo.objects.get(cab_name=net_cab)
                cab_id = a.id
                e.net_cab_id = cab_id
            if net_u!='':
                e.u_lev = net_u
            e.save()
        else:
            e.save()

    return render(request, 'operations/revise_net.html', {})

def snmpWalk(host, community, oid):
    """利用os模块打开一个管道运行snmpwalk工具结合host，团体字符串，OID获取交换机路由器状态"""
    result = os.popen('snmpwalk -v 2c -c ' + community + ' '+ host + ' ' + oid).read().split('\n')[:-1]
    return result


def getPortDevices(host, community):
    """获取端口信息"""

    device_mib = snmpWalk(host, community, 'RFC1213-MIB::ifDescr')
    device_list = []
    for item in device_mib:
        device_list.append(item.split(':')[3].strip())
    print(device_list)
    return device_list


def getPortStatus(host, community):
    """获取端口状态信息"""
    device_mib = snmpWalk(host, community, 'RFC1213-MIB::ifOperStatus')
    device_list = []
    for item in device_mib:
        device_list.append(item.split(':')[3].strip())
    return device_list

def getPortIP(host, community):
    """获取端口IP信息"""
    device_mib = snmpWalk(host, community, 'RFC1213-MIB::ipAdEntAddr')
    device_list = []
    for item in device_mib:
        device_list.append(item.split(':')[3].strip())
    print(device_list)
    return device_list

def getPortMAC(host, community):
    """获取端口MAC信息"""
    device_mib = snmpWalk(host, community, 'RFC1213-MIB::ifPhysAddress')
    # print("MAC Address", device_mib)
    device_list = []
    for item in device_mib:
        if len(item) < 40:
            device_list.append('Null')
        else :
            device_list.append(item.split(':')[3].strip())
    return device_list


#只是执行查看端口的函数
def login(request,param):
    community = "public"
    print('=' * 10 + param + '=' * 10)
    start = time.time()
    print("system info")
    # dict = defaultdict(list)
    dict={}
    DeviceList = getPortDevices(param, community)
    DeviceStatus = getPortStatus(param, community)
    DeviceMac = getPortMAC(param, community)
    for item in DeviceList:
        sta_index = DeviceList.index(item)
        print("Port:" + item + " Status:" + DeviceStatus[sta_index]+"MACCCCCCCCCCCC :  "+DeviceMac[sta_index])
        dict.setdefault(item,[]).append(DeviceStatus[sta_index])
        dict.setdefault(item, []).append(DeviceMac[sta_index])
        print(dict)
    return render(request, 'operations/login.html', {'dict': dict})



#真正执行登录的函数
def  login1(request,param):

    net_login_dct = {}
    with open("%s/conf/net_dev.pass" % BASE_DIR, 'r') as f:
        for item in f.readlines():
            ip, username, passwd, en_passwd = re.split("\s+", item)[:4]
            if ip == param:
                net_login_dct[ip] = (username, passwd, en_passwd)

    for ip, login_info in net_login_dct.items():
        jn = J_net_do(param, login_info)
        res = jn.cisco_login()

    return render(request, 'operations/login1.html', {})