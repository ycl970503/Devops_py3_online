# coding=utf-8
import datetime
from hashlib import sha1
from django.shortcuts import render, redirect
from .models import UserInfo




def base(request):
    return render(request, 'base.html', {})


def register(request):
    context = {'title': '注册'}
    return render(request, 'users/register.html', context=context)
#
# def register_haddle(request):
#     if request.method == "POST":
#         register_form = RegisterForm(request.POST)
#         message = "请检查填写的内容！"
#         if register_form.is_valid():  # 获取数据
#             user_name = register_form.cleaned_data['user_name']
#             user_passwd1 = register_form.cleaned_data['user_passwd1']
#             user_passwd2 = register_form.cleaned_data['user_passwd2']
#             user_email = register_form.cleaned_data['user_email']
#             if user_passwd1 != user_passwd2:  # 判断两次密码是否相同
#                 message = "两次输入的密码不同！"
#                 return render(request, 'users/register.html', locals())
#             else:
#                 same_name_user = UserInfo.objects.filter(user_name=user_name)
#                 if same_name_user:  # 用户名唯一
#                     message = '用户已经存在，请重新选择用户名！'
#                     return render(request, 'users/register.html', locals())
#                 same_email_user = UserInfo.objects.filter(user_email=user_email)
#                 if same_email_user:  # 邮箱地址唯一
#                     message = '该邮箱地址已被注册，请使用别的邮箱！'
#                     return render(request, 'users/register.html', locals())  # 当一切都OK的情况下，创建新用户
#                 user_pass_sha1 = (hashlib.sha1(user_passwd1.encode('utf-8'))).hexdigest
#                 new_user = UserInfo.objects.create()
#                 new_user.user_name = user_name
#                 new_user.user_passwd = user_pass_sha1
#                 new_user.user_email = user_email
#                 new_user.save()
#                 return redirect('users/login.html')  # 自动跳转到登录页面
#     register_form = RegisterForm()
#     return render(request, 'login/register.html', locals())
#



def login(request):
    context = {'title': '登录'}
    return render(request, 'users/login.html', context=context)


def login_haddle(request):
    post = request.POST
    user_name = post.get('user_name')
    user_passwd = post.get('user_passwd')
    remember_uname = post.get('remember_uname', '0')
    passwd_sha1 = sha1()
    passwd_sha1.update(user_passwd.encode("utf8"))
    user_passwd_sha1 = passwd_sha1.hexdigest()
    user_names = UserInfo.objects.filter(user_name=user_name)
    context = {'title': '登录', 'user_name': user_name, 'user_passwd': user_passwd}
    if len(user_names) >= 1:
        if user_names[0].user_passwd == user_passwd_sha1:
            request.session['uid'] = user_names[0].id
            request.session['user_name'] = user_name
            request.session['user_level'] = user_names[0].user_level
            path = request.session.get('path', '/')
            response = redirect(path)
            if remember_uname == '1':
                response.set_cookie('user_name', user_name,expires=(datetime.datetime.now()+datetime.timedelta(days=7)))
            else:
                response.set_cookie('user_name', '', max_age=-1)
            return response
        else:
            context['error_passwd'] = '1'
            return render(request, 'users/login.html', context)
    else:
        context['error_name'] = '1'
        return render(request, 'users/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/user/login/')

def user_center(request):

    """获取当前用户信息"""
    user_name = request.session["user_name"]
    # user_level = UserInfo.objects.values('user_level').filter(user_name=user_name)
    # user_email = UserInfo.objects.values('user_email').filter(user_name=user_name)

    for e in UserInfo.objects.filter(user_name=user_name):
        user_level = e.user_level
        user_email = e.user_email
    if user_level == '0':
        user_level = "普通用户"
    elif user_level == '1':
        user_level = "后台管理员"
    elif user_level == '2':
        user_level = "超级管理员"
    context = {'title': "用户中心", 'user_name': user_name, 'user_level': user_level, 'user_email': user_email}
    return render(request, 'users/user_center.html', context)
