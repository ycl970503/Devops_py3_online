# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-09 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15, verbose_name='用户名')),
                ('user_passwd', models.CharField(max_length=40, verbose_name='密码')),
                ('user_level', models.CharField(choices=[('0', '普通用户'), ('1', '后台管理员'), ('2', '超级管理员')], default='0', max_length=2, verbose_name='用户权限等级')),
                ('user_email', models.CharField(max_length=40, verbose_name='邮箱地址')),
            ],
            options={
                'verbose_name': '注册用户表',
                'verbose_name_plural': '注册用户表',
                'db_table': 'userinfo',
            },
        ),
    ]
