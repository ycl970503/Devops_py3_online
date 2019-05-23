# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-12 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cab_name', models.CharField(max_length=10, unique=True, verbose_name='机柜编号')),
                ('cab_lever', models.IntegerField(verbose_name='机器U数,1-10分别代表1~10层')),
                ('cab_width', models.FloatField(default=0.8, max_length=3, verbose_name='机柜宽度(米)')),
                ('cab_high', models.FloatField(default=2.2, max_length=3, verbose_name='机柜高度(米)')),
                ('cab_deep', models.FloatField(default=1, max_length=3, verbose_name='机柜深度(米)')),
                ('cab_area', models.FloatField(default=0.8, max_length=3, verbose_name='占地面积(平方米)')),
                ('cab_x', models.FloatField(max_length=5, verbose_name='x轴位置')),
                ('cab_y', models.FloatField(max_length=5, verbose_name='y轴位置')),
            ],
            options={
                'verbose_name': '机柜信息表',
                'verbose_name_plural': '机柜信息表',
                'db_table': 'cabinetinfo',
            },
        ),
        migrations.CreateModel(
            name='ConnectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssh_username', models.CharField(default='', max_length=10, null=True, verbose_name='ssh用户名')),
                ('ssh_userpasswd', models.CharField(default='', max_length=40, null=True, verbose_name='ssh用户密码')),
                ('ssh_hostip', models.CharField(default='', max_length=40, null=True, verbose_name='ssh登录的ip')),
                ('ssh_host_port', models.CharField(default='', max_length=10, null=True, verbose_name='ssh登录的端口')),
                ('ssh_rsa', models.CharField(default='', max_length=64, verbose_name='ssh私钥')),
                ('rsa_pass', models.CharField(default='', max_length=64, verbose_name='私钥的密钥')),
                ('ssh_status', models.IntegerField(default=0, verbose_name='用户连接状态,0-登录失败,1-登录成功')),
                ('ssh_type', models.IntegerField(default=0, verbose_name='用户连接类型, 1-rsa登录,2-dsa登录,3-ssh_rsa登录,4-docker成功,5-docker无法登录')),
                ('sn_key', models.CharField(default='', max_length=256, verbose_name='唯一设备ID')),
            ],
            options={
                'verbose_name': '用户登录信息表',
                'verbose_name_plural': '用户登录信息表',
                'db_table': 'connectioninfo',
            },
        ),
        migrations.CreateModel(
            name='NetConnectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_username', models.CharField(default='', max_length=10, null=True, verbose_name='用户名')),
                ('tel_userpasswd', models.CharField(default='', max_length=40, null=True, verbose_name='设备用户密码')),
                ('tel_enpasswd', models.CharField(default='', max_length=40, null=True, verbose_name='设备超级用户密码')),
                ('tel_host_port', models.CharField(default='', max_length=10, null=True, verbose_name='设备登录的端口')),
                ('tel_hostip', models.CharField(default='', max_length=40, null=True, verbose_name='设备登录的ip')),
                ('tel_status', models.IntegerField(default=0, verbose_name='用户连接状态,0-登录失败,1-登录成功')),
                ('tel_type', models.IntegerField(default=0, verbose_name='用户连接类型, 1-普通用户可登录,2-超级用户可登录')),
                ('sn_key', models.CharField(default='', max_length=256, verbose_name='唯一设备ID')),
            ],
            options={
                'verbose_name': '网络设备用户登录信息',
                'verbose_name_plural': '网络设备用户登录信息',
                'db_table': 'netconnectioninfo',
            },
        ),
        migrations.CreateModel(
            name='NetWorkInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=40, verbose_name='网络设备ip')),
                ('host_name', models.CharField(max_length=10, verbose_name='网络设备名')),
                ('u_lev', models.IntegerField(default='', verbose_name='设备安放U数')),
                ('net_cab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CabinetInfo')),
            ],
            options={
                'verbose_name': '网络设备表',
                'verbose_name_plural': '网络设备表',
                'db_table': 'networkinfo',
            },
        ),
        migrations.CreateModel(
            name='OtherMachineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40, verbose_name='设备ip')),
                ('sn_key', models.CharField(max_length=256, verbose_name='设备的唯一标识')),
                ('machine_name', models.CharField(max_length=20, verbose_name='设备名称')),
                ('remark', models.TextField(default='', verbose_name='备注')),
                ('reson_str', models.CharField(default='', max_length=128, verbose_name='归纳原因')),
                ('oth_cab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CabinetInfo')),
            ],
            options={
                'verbose_name': '其它设备表',
                'verbose_name_plural': '其它设备表',
                'db_table': 'othermachineinfo',
            },
        ),
        migrations.CreateModel(
            name='PhysicalServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.CharField(max_length=40, verbose_name='服务器IP')),
                ('machine_brand', models.CharField(default='--', max_length=60, verbose_name='服务器品牌')),
                ('system_ver', models.CharField(default='', max_length=30, verbose_name='操作系统版本')),
                ('sys_hostname', models.CharField(max_length=15, verbose_name='操作系统主机名')),
                ('mac', models.CharField(default='', max_length=512, verbose_name='MAC地址')),
                ('sn', models.CharField(default='', max_length=256, verbose_name='SN-主机的唯一标识')),
                ('vir_type', models.CharField(default='', max_length=2, verbose_name='宿主机类型')),
                ('phy_u', models.IntegerField(verbose_name='安装层数')),
                ('ser_cabin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CabinetInfo', to_field='cab_name')),
            ],
            options={
                'verbose_name': '物理服务器信息表',
                'verbose_name_plural': '物理服务器信息表',
                'db_table': 'physicalserverinfo',
            },
        ),
        migrations.CreateModel(
            name='StatisticsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField(default='2019-05-12', verbose_name='更新时间')),
                ('all_count', models.IntegerField(default=0, verbose_name='所有设备数量')),
                ('pyh_count', models.IntegerField(default=0, verbose_name='物理设备数量')),
                ('net_count', models.IntegerField(default=0, verbose_name='网络设备数量')),
                ('other_count', models.IntegerField(default=0, verbose_name='其他设备数量')),
                ('kvm_count', models.IntegerField(default=0, verbose_name='KVM设备数量')),
                ('docker_count', models.IntegerField(default=0, verbose_name='Docker设备数量')),
                ('vmx_count', models.IntegerField(default=0, verbose_name='VMX设备数量')),
            ],
            options={
                'verbose_name': '扫描后的汇总硬件统计信息',
                'verbose_name_plural': '扫描后的汇总硬件统计信息',
                'db_table': 'statisticsrecord',
            },
        ),
        migrations.CreateModel(
            name='VirtualServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.CharField(max_length=40, verbose_name='服务器IP')),
                ('server_type', models.CharField(default='', max_length=80, verbose_name='服务器类型:kvm,Vmware,Docker,others')),
                ('system_ver', models.CharField(default='', max_length=30, verbose_name='操作系统版本')),
                ('sys_hostname', models.CharField(max_length=80, verbose_name='操作系统主机名')),
                ('mac', models.CharField(default='', max_length=512, verbose_name='MAC地址')),
                ('sn', models.CharField(default='', max_length=256, verbose_name='SN-主机的唯一标识')),
                ('conn_vir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.ConnectionInfo')),
                ('vir_phy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.PhysicalServerInfo')),
            ],
            options={
                'verbose_name': '虚拟设备表',
                'verbose_name_plural': '虚拟设备表',
                'db_table': 'virtualserverinfo',
            },
        ),
        migrations.AddField(
            model_name='netconnectioninfo',
            name='dev_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.NetWorkInfo'),
        ),
    ]
