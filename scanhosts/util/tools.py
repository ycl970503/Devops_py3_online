#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.core.mail import send_mail
import time

class sendmail():
    def __init__(self,receive_addr,sub_info,content_info):
        sub_data = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        self.receive_addr =  receive_addr
        self.sub_info = sub_info + sub_data
        self.content_info = content_info
        print("收到邮件了！！！！！")
    def send(self):
        print("准备发送了！！！！！")
        try:
            send_mail(
                subject=self.sub_info,
                message=self.content_info,
                # subject='this is a new test',
                # message='WHYYYYYYYYYYYY',
                from_email='yangchenluu@163.com',
                # recipient_list=self.receive_addr,
                recipient_list=['921881662@qq.com'],
                fail_silently=False,
            )
            return True
        except Exception as e:
            print(e)
            return False