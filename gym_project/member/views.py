from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
# 컨트롤러 역할
from django.urls import reverse_lazy
from django.views.generic import *

from Post.models import Post
from gyminfo.models import GymInfo
from .models import GymMember

from django.contrib.auth.models import User

from django.contrib import auth

# AuthenticationForm 모델폼 import
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def Main(request):
    list=GymInfo.objects.all()

    return render(request, 'member/main.html',{"list":list})


class MemberList(ListView):
    model = GymMember
    # template 파일명 : 모델명_list.html


class MemberDetail(DetailView):
    model = GymMember
    success_url = reverse_lazy('list')


class MemberUpdate(UpdateView):
    model = GymMember
    fields = ['user_id', 'user_pw', 'user_name', 'user_tel', 'membership']
    template_name_suffix = '_update'
    success_url = reverse_lazy('main')


def memberCreate(request):
    return render(request, 'member/gymmember_create.html')


def memberCreate2(request):
    member = GymMember()
    member.user_id = request.POST['user_id']
    member.user_pw = request.POST['user_pw']
    member.user_name = request.POST['user_name']
    member.user_tel = request.POST['user_tel']
    member.membership = request.POST['membership']

    member.save()
    return render(request, 'member/main.html')


def loginok(request):
    return render(request, 'member/main.html')


def index(request, user_id, user_pw, user_name, user_tel, membership):
    return HttpResponse('received user_id: ' + user_id + '<br>' + \
                        'receiced user_pw: ' + user_pw + '<br>' + \
                        'receiced user_name: ' + user_name + '<br>' + \
                        'receiced user_tel: ' + user_tel + '<br>' + \
                        'receiced membership' + membership)


from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
# jango.contrib.auth 내 함수 login을 import함.
# (views.py 내 정의한 함수 login과 구분하기 위해 auth_log로 재 명명함)
# Session Create

# def checkid(request):
#    user_id = request.POST.get('user_id')
#    rows = GymMember.objects.distinct('user_id')

# def checkid(request):
#     try:
#         member = GymMember.objects.get(user_id=request.GET['user_id'])
#     except Exception as e:
#         member = None
#     result = {
#         'result': 'success',
#         # 'data': model_to_dict(planner)
#         'data': "not exist" if member is None else "exist"
#     }
#     return JsonResponse(result)

def login(request):
    return render(request, 'member/login.html')


def loginCheck(request):
    user_id = request.POST.get('user_id')
    user_pw = request.POST.get('user_pw')
    print(user_id, '================================')
    row = GymMember.objects.filter(user_id=user_id, user_pw=user_pw).exists()
    print(row)
    # 로그인 ok
    if row == True:
        request.session['user_id'] = user_id
        return redirect('main')
    else:
        return redirect('login')


def logout(request):
    del request.session['user_id']
    # auth_logout(request)
    return redirect('main')


# 회원 탈퇴
def memberDelete(request, pk):
    fb = GymMember.objects.get(user_id=pk)
    fb.delete()
    del request.session['user_id']
    return redirect('main')



# def memberCreate2(request):
#     post = Post()
#     post.user_id = request.POST['user_id']
#     post.title = request.POST['title']
#     post.content = request.POST['content']
#     post.save()
#     return redirect('main')

