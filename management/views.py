# coding: utf-8

import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .models import MyUser, Book, Img, Bookcure, Bookcheck, Bookhealth, Bookdange, Booksituation, Bookchange, Bookdiagnose, Booktime, \
#     SSD
from .models import *
from django.core.urlresolvers import reverse
from .utils import permission_check
from datetime import datetime



# def index(request):
#     return render(request, 'backend.html')



def new_page(request):
    return render(request, 'add_person_info.html')


# def index(request):
#     user = request.user if request.user.is_authenticated() else None
#     content = {
#         'active_menu': 'homepage',
#         'user': user,
#     }
#     return render(request, 'management/index.html', content)


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=post.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=post.get('nickname', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'management/signup.html', content)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'management/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/set_password.html', content)


#@user_passes_test(permission_check)

# def add_book00(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_book00 = SSD(
#                 name=post.get('name', ''),
#
#
#                 numble=post.get('numble'),
#                 idnumble=post.get('idnumble'),
#
#         )
#         new_book00.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book00',
#         'state': state,
#     }
#     return render(request, 'management/add_book00.html', content)




def add_book(request):
    #user = request.user
    state = None
    if request.method == 'POST':

        post = json.loads(request.body)
        # 添加联系人信息...
        try:
            new_book = Book(
                    conname=post.get('conname',''),
                    conrelation=post.get('conrelation',''),
                    conphone=int(post.get('conphone')) if post.get('conphone') else 0,
                    nowprovince=post.get('city_picker_select')[0],
                    nowcity=post.get('city_picker_select')[1],
                    nowcounty=post.get('city_picker_select')[2],
                    nowstreet=post.get('nowstreet',''),
                    birthprovince=post.get('city_picker_select_1')[0],
                    birthcity=post.get('city_picker_select_1')[1],
                    birtharea=post.get('city_picker_select_1')[2],
                    birthstreet=post.get('birthstreet',''),
                    healthtype=post.get('healthtype',''),
            )
            new_book.save()
        except Exception as e:
            print e

        # 血管再开通治疗
        try:
            new_bookcure = Bookcure(
                b1=int(post.get('b1')) if post.get('b1') else 0,
                b2=datetime.strptime(post.get('b2'), "%Y-%m-%dT%H:%M"),
                b3=post.get('b3', ''),
                b4=datetime.strptime(post.get('b4'), "%Y-%m-%dT%H:%M"),
                b5=post.get('b5_list', ''),
                b51=post.get('b51_list', ''),
                b5a11=int(post.get('b5a11')) if post.get('b5a11') else 0,
                b5a12=datetime.strptime(post.get('b5a12'), "%Y-%m-%dT%H:%M"),
                b5a13=int(post.get('b5a13')) if post.get('b5a13') else 0,
                b5a14=post.get('b5a14', ''),
                b5a15=int(post.get('b5a15')) if post.get('b5a15') else 0,
                b5a16=float(post.get('b5a16', 0.0)),
                b5a17=float(post.get('b5a17', 0.0)),
                b5a18=int(post.get('b5a18')) if post.get('b5a18') else 0,
                b5a19=int(post.get('b5a19')) if post.get('b5a19') else 0,
                b5a110=int(post.get('b5a110')) if post.get('b5a110') else 0,
                b5a111=post.get('b5a111', ''),
                b5a112=post.get('b5a112_list', ''),
                b5a113=post.get('b5a113', ''),
                b5a21=int(post.get('b5a21')) if post.get('b5a21') else 0,
                b5a22=datetime.strptime(post.get('b5a22'), "%H:%M"),
                b5a23=int(post.get('b5a23')) if post.get('b5a23') else 0,
                b5a24=float(post.get('b5a24', 0.0)),
                b5a25=float(post.get('b5a25', 0.0)),
                b5a26=int(post.get('b5a26')) if post.get('b5a26') else 0,
                b5a27=int(post.get('b5a27')) if post.get('b5a27') else 0,
                b5a28=post.get('b5a28', ''),
                b5a31=int(post.get('b5a31')) if post.get('b5a31') else 0,
                b5a32=datetime.strptime(post.get('b5a32'), "%H:%M"),
                b5a33=int(post.get('b5a33')) if post.get('b5a33') else 0,
                b5a34=int(post.get('b5a34')) if post.get('b5a34') else 0,
                b5a35=post.get('b5a35', ''),
                b5a41=int(post.get('b5a41')) if post.get('b5a41') else 0,
                b5a42=datetime.strptime(post.get('b5a42'), "%H:%M"),
                b5a43=int(post.get('b5a43')) if post.get('b5a43') else 0,
            )
            new_bookcure.save()
        except Exception as e:
            print e

        # 首次评估及化验检查，意识选择
        try:
            new_bookcheck = Bookcheck(
                c1=int(post.get('c1')) if post.get('c1') else 0,
                c1a1=int(post.get('c1a1')) if post.get('c1a1') else 0,
                c2=post.get('c2_list', ''),
                c2a1=post.get('c2a1', ''),
                c2a2=int(post.get('c2a2')) if post.get('c2a2') else 0,
                c3=float(post.get('c3')) if post.get('c3') else 0.0,
                c4a1=int(post.get('c4a1')) if post.get('c4a1') else 0,
                c4a2=int(post.get('c4a2')) if post.get('c4a2') else 0,
                c5a1=float(post.get('c5a1')) if post.get('c5a1') else 0.0,
                c5a2=float(post.get('c5a2')) if post.get('c5a2') else 0.0,
                c5a3=float(post.get('c5a3')) if post.get('c5a3') else 0.0,
                c5a4=float(post.get('c5a4')) if post.get('c5a4') else 0.0,
                c6a1=float(post.get('c6a1')) if post.get('c6a1') else 0.0,
                c6a2=float(post.get('c6a2')) if post.get('c6a2') else 0.0,
                c6a3=float(post.get('c6a3')) if post.get('c6a3') else 0.0,
                c6a4=float(post.get('c6a4')) if post.get('c6a4') else 0.0,
                c7a1=float(post.get('c7a1')) if post.get('c7a1') else 0.0,
                c7a2=float(post.get('c7a2')) if post.get('c7a2') else 0.0,
                c7a3=float(post.get('c7a3')) if post.get('c7a3') else 0.0,
                c7a4=float(post.get('c7a4')) if post.get('c7a4') else 0.0,
                c8=float(post.get('c8')) if post.get('c8') else 0.0,
                c9=float(post.get('c9')) if post.get('c9') else 0.0,
                c10=float(post.get('c10')) if post.get('c10') else 0.0,
                c11=post.get('c11_list', ''),
                c12a1=int(post.get('c12a1')) if post.get('c12a1') else 0,
                c12a2=post.get('c12a2_list', ''),
                c12a3=post.get('c12a3', ''),
                # c13a1=post.get('c13a1', ''),
                # c13a2=post.getlist('c13a2', ''),
                # c13a3=post.getlist('c13a3', ''),
                c14a1=int(post.get('c14a1')) if post.get('c14a1') else 0,
                c14a2=post.get('c14a2', ''),
                c15=float(post.get('c15')) if post.get('c15') else 0.0,
            )
            new_bookcheck.save()
            state = True
        except Exception as e:
            state = False
            print e

        # 入院后治疗
        try:
            new_bookhealth = Bookhealth(
                d1a10=int(post.get('d1a10')) if post.get('d1a10') else 0,
                d1a11=int(post.get('d1a11')) if post.get('d1a11') else 0,
                d1a12=float(post.get('d1a12')) if post.get('d1a12') else 0.0,
                d1a13=float(post.get('d1a13')) if post.get('d1a13') else 0.0,
                d1a14=float(post.get('d1a14')) if post.get('d1a14') else 0.0,
                d1a15=float(post.get('d1a15')) if post.get('d1a15') else 0.0,
                d1a20=int(post.get('d1a20')) if post.get('d1a20') else 0,
                d1a21=int(post.get('d1a21')) if post.get('d1a21') else 0,
                d1a22=float(post.get('d1a22')) if post.get('d1a22') else 0.0,
                d1a23=post.get('d1a23', ''),
                d1a30=int(post.get('d1a30')) if post.get('d1a30') else 0,
                d1a31=post.get('d1a31_list', ''),
                d1a32=int(post.get('d1a32')) if post.get('d1a32') else 0,
                d1a33=post.get('d1a33', ''),
                d1a34=float(post.get('d1a34')) if post.get('d1a34') else 0.0,
                d1a35=int(post.get('d1a35')) if post.get('d1a35') else 0,
                d1a36=post.get('d1a36', ''),
                d1a37=float(post.get('d1a37')) if post.get('d1a37') else 0.0,
                d1a38=int(post.get('d1a38')) if post.get('d1a38') else 0,
                d1a39=post.get('d1a39', ''),
                d1a310=float(post.get('d1a310')) if post.get('d1a310') else 0.0,
                d1a311=int(post.get('d1a311')) if post.get('d1a311') else 0,
                d1a312=post.get('d1a312', ''),
                d1a313=float(post.get('d1a313')) if post.get('d1a313') else 0.0,
                d1a314=int(post.get('d1a314')) if post.get('d1a314') else 0,
                d1a315=post.get('d1a315', ''),
                d1a316=float(post.get('d1a316')) if post.get('d1a316') else 0.0,
                d1a317=post.get('d1a317', ''),
                d1a318=float(post.get('d1a318')) if post.get('d1a318') else 0.0,
                d1a40=int(post.get('d1a40')) if post.get('d1a40') else 0,
                d1a41=post.get('d1a41_list', ''),
                d1a42=float(post.get('d1a42')) if post.get('d1a42') else 0.0,
                d1a43=float(post.get('d1a43')) if post.get('d1a43') else 0.0,
                d1a44=float(post.get('d1a44')) if post.get('d1a44') else 0.0,
                d1a45=float(post.get('d1a45')) if post.get('d1a45') else 0.0,
                d1a46=float(post.get('d1a46')) if post.get('d1a46') else 0.0,
                d1a47=float(post.get('d1a47')) if post.get('d1a47') else 0.0,
                d1a48=post.get('d1a48', ""),
                d1a49=float(post.get('d1a49')) if post.get('d1a49') else 0.0,
                d1a51=post.get('d1a51', ''),
                d1a52=post.get('d1a52', ''),
                d1a53=post.get('d1a53', ''),
                d1a54=post.get('d1a54', ''),
                d1a55=post.get('d1a55', ''),
                d1a56=float(post.get('d1a56')) if post.get('d1a56') else 0.0,
                d1a57=float(post.get('d1a57')) if post.get('d1a57') else 0.0,
                d1a58=float(post.get('d1a58')) if post.get('d1a58') else 0.0,
                d1a59=float(post.get('d1a59')) if post.get('d1a59') else 0.0,
                d1a510=float(post.get('d1a510')) if post.get('d1a510') else 0.0,
                d1a511=post.get('d1a511', ''),
                d1a512=post.get('d1a512', ''),
                d1a570=post.get('d1a570', ''),
                d1a571=post.get('d1a571', ''),
                d1a572=post.get('d1a572', ''),


                d1a513=float(post.get('d1a513')) if post.get('d1a513') else 0.0,
                d1a514=float(post.get('d1a514')) if post.get('d1a514') else 0.0,
                d1a573=float(post.get('d1a573')) if post.get('d1a573') else 0.0,
                d1a574=float(post.get('d1a574')) if post.get('d1a574') else 0.0,
                d1a575=float(post.get('d1a575')) if post.get('d1a575') else 0.0,

                d1a515=post.get('d1a515_list', ''),
                d1a516=float(post.get('d1a516')) if post.get('d1a516') else 0.0,
                d1a517=float(post.get('d1a517')) if post.get('d1a517') else 0.0,
                d1a518=float(post.get('d1a518')) if post.get('d1a518') else 0.0,
                d1a519=float(post.get('d1a519')) if post.get('d1a519') else 0.0,
                d1a520=post.get('d1a520', ''),
                d1a521=float(post.get('d1a521')) if post.get('d1a521') else 0.0,
                d1a522=post.get('d1a522_list', ''),
                d1a523=float(post.get('d1a523')) if post.get('d1a523') else 0.0,
                d1a524=float(post.get('d1a524')) if post.get('d1a524') else 0.0,
                d1a525=float(post.get('d1a525')) if post.get('d1a525') else 0.0,
                d1a526=float(post.get('d1a526')) if post.get('d1a526') else 0.0,
                d1a527=float(post.get('d1a527')) if post.get('d1a527') else 0.0,
                d1a528=float(post.get('d1a528')) if post.get('d1a528') else 0.0,
                d1a529=post.get('d1a529', ''),
                d1a530=float(post.get('d1a530')) if post.get('d1a530') else 0.0,
                d1a531=post.get('d1a531', ''),
                d1a532=post.get('d1a532', ''),
                d1a533=float(post.get('d1a533')) if post.get('d1a533') else 0.0,
                d1a534=float(post.get('d1a534')) if post.get('d1a534') else 0.0,
                d1a535=float(post.get('d1a535')) if post.get('d1a535') else 0.0,
                d1a536=float(post.get('d1a536')) if post.get('d1a536') else 0.0,
                d1a537=float(post.get('d1a537')) if post.get('d1a537') else 0.0,
                d1a538=float(post.get('d1a538')) if post.get('d1a538') else 0.0,
                d1a539=float(post.get('d1a539')) if post.get('d1a539') else 0.0,
                d1a540=float(post.get('d1a540')) if post.get('d1a540') else 0.0,
                d1a541=float(post.get('d1a541')) if post.get('d1a541') else 0.0,
                d1a542=float(post.get('d1a542')) if post.get('d1a542') else 0.0,
                d1a543=post.get('d1a543', ''),
                d1a544=float(post.get('d1a544')) if post.get('d1a544') else 0.0,
                d1a545=int(post.get('d1a545')) if post.get('d1a545') else 0,
                d1a546=post.get('d1a546', ''),
                d1a547=float(post.get('d1a547')) if post.get('d1a547') else 0.0,
                d1a548=int(post.get('d1a548')) if post.get('d1a548') else 0,
                d1a549=post.get('d1a549', ''),
                d1a550=float(post.get('d1a550')) if post.get('d1a550') else 0.0,
                d1a551=int(post.get('d1a551')) if post.get('d1a551') else 0,
                d1a552=post.get('d1a552', ''),
                d1a553=float(post.get('d1a553')) if post.get('d1a553') else 0.0,
                d1a554=int(post.get('d1a554')) if post.get('d1a554') else 0,
                d1a555=post.get('d1a555', ''),
                d1a556=float(post.get('d1a556')) if post.get('d1a556') else 0.0,
                d1a557=int(post.get('d1a557')) if post.get('d1a557') else 0,
                d1a558=post.get('d1a558', ''),
                d1a559=float(post.get('d1a559')) if post.get('d1a559') else 0.0,
                d1a560=int(post.get('d1a560')) if post.get('d1a560') else 0,
                d1a561=post.get('d1a561', ''),
                d1a562=float(post.get('d1a562')) if post.get('d1a562') else 0.0,
                d1a563=int(post.get('d1a563')) if post.get('d1a563') else 0,
                d1a564=post.get('d1a564', ''),
                d1a565=float(post.get('d1a565')) if post.get('d1a565') else 0.0,
                d1a566=post.get('d1a566', ''),
                d1a567=float(post.get('d1a567')) if post.get('d1a567') else 0.0,


                d1a6=post.get('d1a6', ''),
                d1a7=post.get('d1a7', ''),
                d2a10=int(post.get('d2a10')) if post.get('d2a10') else 0,
                d2a11=post.get('d2a11_list', ''),
                d2a12=float(post.get('d2a12')) if post.get('d2a12') else 0.0,
                d2a13=float(post.get('d2a13')) if post.get('d2a13') else 0.0,
                d2a14=float(post.get('d2a14')) if post.get('d2a14') else 0.0,
                d2a15=float(post.get('d2a15')) if post.get('d2a15') else 0.0,
                d2a16=post.get('d2a16', ''),
                d2a17=float(post.get('d2a17')) if post.get('d2a17') else 0.0,
                d2a20=int(post.get('d2a20')) if post.get('d2a20') else 0,
                d2a21=post.get('d2a21_list', ''),
                d2a22=float(post.get('d2a22')) if post.get('d2a22') else 0.0,
                d2a23=float(post.get('d2a23')) if post.get('d2a23') else 0.0,
                d2a24=float(post.get('d2a24')) if post.get('d2a24') else 0.0,
                d2a25=float(post.get('d2a25')) if post.get('d2a25') else 0.0,
                d2a26=float(post.get('d2a26')) if post.get('d2a26') else 0.0,
                d2a27=float(post.get('d2a27')) if post.get('d2a27') else 0.0,
                d2a28=post.get('d2a28', ''),
                d2a29=float(post.get('d2a29')) if post.get('d2a29') else 0.0,
                d2a31=post.get('d2a31', ''),
                d2a32=post.get('d2a32', ''),
                d2a33=post.get('d2a33', ''),
                d2a34=post.get('d2a34', ''),
                d2a35=post.get('d2a35', ''),
                d2a36=float(post.get('d2a36')) if post.get('d2a36') else 0.0,
                d2a37=float(post.get('d2a37')) if post.get('d2a37') else 0.0,
                d2a38=float(post.get('d2a38')) if post.get('d2a38') else 0.0,
                d2a39=float(post.get('d2a39')) if post.get('d2a39') else 0.0,
                d2a310=float(post.get('d2a310')) if post.get('d2a310') else 0.0,
                d2a311=post.get('d2a311', ''),
                d2a312=post.get('d2a312', ''),
                d2a315=post.get('d2a315', ''),
                d2a316=post.get('d2a316', ''),
                d2a317=post.get('d2a317', ''),

                d2a313=float(post.get('d2a313')) if post.get('d2a313') else 0.0,
                d2a314=float(post.get('d2a314')) if post.get('d2a314') else 0.0,
                d2a318=float(post.get('d2a318')) if post.get('d2a318') else 0.0,
                d2a319=float(post.get('d2a319')) if post.get('d2a319') else 0.0,
                d2a3110=float(post.get('d2a3110')) if post.get('d2a3110') else 0.0,
                d2a331=post.get('d2a331', ''),
                d2a332=post.get('d2a332', ''),
                d2a333=float(post.get('d2a333')) if post.get('d2a333') else 0.0,
                d2a334=float(post.get('d2a334')) if post.get('d2a334') else 0.0,
                d2a335=float(post.get('d2a335')) if post.get('d2a335') else 0.0,
                d2a336=float(post.get('d2a336')) if post.get('d2a336') else 0.0,
                d2a337=float(post.get('d2a337')) if post.get('d2a337') else 0.0,
                d2a338=float(post.get('d2a338')) if post.get('d2a338') else 0.0,
                d2a339=float(post.get('d2a339')) if post.get('d2a339') else 0.0,
                d2a340=float(post.get('d2a340')) if post.get('d2a340') else 0.0,
                d2a341=float(post.get('d2a341')) if post.get('d2a341') else 0.0,
                d2a342=float(post.get('d2a342')) if post.get('d2a342') else 0.0,
                d2a343=post.get('d2a343', ''),
                d2a344=float(post.get('d2a344')) if post.get('d2a344') else 0.0,
                d2a345=int(post.get('d2a345')) if post.get('d2a345') else 0,
                d2a346=post.get('d2a346', ''),
                d2a347=float(post.get('d2a347')) if post.get('d2a347') else 0.0,
                d2a348=int(post.get('d2a348')) if post.get('d2a348') else 0,
                d2a349=post.get('d2a349', ''),
                d2a350=float(post.get('d2a350')) if post.get('d2a350') else 0.0,
                d2a351=int(post.get('d2a351', 0.0)),
                d2a352=post.get('d2a352', ''),
                d2a353=float(post.get('d2a353')) if post.get('d2a353') else 0.0,
                d2a354=int(post.get('d2a354')) if post.get('d2a354') else 0,
                d2a355=post.get('d2a355', ''),
                d2a356=float(post.get('d2a356')) if post.get('d2a356') else 0.0,
                d2a357=int(post.get('d2a357')) if post.get('d2a357') else 0,
                d2a358=post.get('d2a358', ''),
                d2a359=float(post.get('d2a359')) if post.get('d2a359') else 0.0,
                d2a360=int(post.get('d2a360')) if post.get('d2a360') else 0,
                d2a361=post.get('d2a361', ''),
                d2a362=float(post.get('d2a362')) if post.get('d2a362') else 0.0,
                d2a363=int(post.get('d2a363')) if post.get('d2a363') else 0,
                d2a364=post.get('d2a364', ''),
                d2a365=float(post.get('d2a365')) if post.get('d2a365') else 0.0,
                d2a366=post.get('d2a366', ''),
                d2a367=float(post.get('d2a367')) if post.get('d2a367') else 0.0,
                d2a4=post.get('d2a4', ''),
                d2a5=post.get('d2a5', ''),
            )
            new_bookhealth.save()
            state = True
        except Exception as e:
            state = False
            print e

        # 危险因素
        try:
            new_bookdang = Bookdange(
                e1=post.get('e1_list', ''),
            )
            new_bookdang.save()
        except Exception as e:
            state = False
            print e

        # 住院1周内病情变化
        try:
            new_bookchange = Bookchange(
                f1=post.get('f1', ''),
            )
            new_bookchange.save()
            state = True
        except Exception as e:
            state = False
            print e


        # 出院情况
        try:
            new_booksituation = Booksituation(
                g1=post.get('g1', ''),
                g2=int(post.get('g2')) if post.get('g2') else 0,
            )
            new_booksituation.save()
            state = True
        except Exception as e:
            state = False
            print e

        # 出院诊断
        try:
            new_bookdiagnose = Bookdiagnose(
                h1=post.get('h1_list', ''),
                h2=post.get('h2_list', ''),
                h3=post.get('h3', ''),
                h4=post.get('h4', ''),
            )
            new_bookdiagnose.save()
            state = True
        except Exception as e:
            state = False
            print e

        # 住院时间
        try:
            new_booktime = Booktime(
                i1=int(post.get('i1')) if post.get('i1') else 0,
                i2=int(post.get('i2')) if post.get('i2') else 0,
                i3=int(post.get('i3')) if post.get('i3') else 0,
                i4=int(post.get('i4')) if post.get('i4') else 0,

            )
            new_booktime.save()
            state = True
        except Exception as e:
            state = False
            print e

        # 保存所有信息
        try:
            ssd = SSD(
                name=post.get('name', ''),
                numble=int(post.get('numble')) if post.get('numble') else 0,
                idnumble=post.get('idnumble', ''),
                book=new_book,
                bookcure=new_bookcure,
                bookcheck=new_bookcheck,
                bookhealth=new_bookhealth,
                bookdange=new_bookdang,
                bookchange=new_bookchange,
                booksituation=new_booksituation,
                bookdiagnose=new_bookdiagnose,
                booktime=new_booktime,
            )
            ssd.save()
            state = True
        except Exception as e:
            state = False
            print e

    if state:
        txt = "success"
    else:
        txt = "fail"

    content = {
        'user': 'test',
        'active_menu': 'add_book',
        'state': txt
    }
    return JsonResponse(content)


# def add_book2(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_bookcure = Bookcure(
#                 b1=post.get('b1'),
#                 b2=post.get('b2'),
#                 b3=post.get('b3', ''),
#                 b4=post.get('b4', ''),
#                 b5=post.getlist('b5', ''),
#                 b51=post.getlist('b51', ''),
#                 b5a11=post.get('b5a11'),
#                 b5a12=post.get('b5a12', ''),
#                 b5a13=post.get('b5a13'),
#                 b5a14=post.get('b5a14', ''),
#                 b5a15=post.get('b5a15'),
#                 b5a16=post.get('b5a16'),
#                 b5a17=post.get('b5a17'),
#                 b5a18=post.get('b5a18'),
#                 b5a19=post.get('b5a19'),
#                 b5a110=post.get('b5a110'),
#                 b5a111=post.get('b5a111', ''),
#                 b5a112=post.getlist('b5a112', ''),
#                 b5a113=post.get('b5a113', ''),
#                 b5a21=post.get('b5a21'),
#                 b5a22=post.get('b5a22', ''),
#                 b5a23=post.get('b5a23'),
#                 b5a24=post.get('b5a24'),
#                 b5a25=post.get('b5a25'),
#                 b5a26=post.get('b5a26'),
#                 b5a27=post.get('b5a27'),
#                 b5a28=post.get('b5a28', ''),
#                 b5a31=post.get('b5a31'),
#                 b5a32=post.get('b5a32', ''),
#                 b5a33=post.get('b5a33'),
#                 b5a34=post.get('b5a34'),
#                 b5a35=post.get('b5a35', ''),
#                 b5a41=post.get('b5a41'),
#                 b5a42=post.get('b5a42', ''),
#                 b5a43=post.get('b5a43'),
#         )
#         new_bookcure.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book2',
#         'state': state,
#     }
#     return render(request, 'management/add_book2.html', content)


# def add_book3(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_bookcheck = Bookcheck(
#                 c1=post.get('c1'),
#                 c1a1=post.get('c1a1'),
#                 c2=post.getlist('c2', ''),
#                 c2a1=post.get('c2a1', ''),
#                 c2a2=post.get('c2a2'),
#                 c3=post.get('c3'),
#                 c4a1=post.get('c4a1'),
#                 c4a2=post.get('c4a2'),
#                 c5a1=post.get('c5a1'),
#                 c5a2=post.get('c5a2'),
#                 c5a3=post.get('c5a3'),
#                 c5a4=post.get('c5a4'),
#                 c6a1=post.get('c6a1'),
#                 c6a2=post.get('c6a2'),
#                 c6a3=post.get('c6a3'),
#                 c6a4=post.get('c6a4'),
#                 c7a1=post.get('c7a1'),
#                 c7a2=post.get('c7a2'),
#                 c7a3=post.get('c7a3'),
#                 c7a4=post.get('c7a4'),
#                 c8=post.get('c8'),
#                 c9=post.get('c9'),
#                 c10=post.get('c10'),
#                 c11=post.getlist('c11', ''),
#                 c12a1=post.get('c12a1'),
#                 c12a2=post.getlist('c12a2', ''),
#                 c12a3=post.get('c12a3', ''),
#                 # c13a1=post.get('c13a1', ''),
#                 # c13a2=post.getlist('c13a2', ''),
#                 # c13a3=post.getlist('c13a3', ''),
#                 c14a1=post.get('c14a1'),
#                 c14a2=post.get('c14a2', ''),
#         )
#         new_bookcheck.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book3',
#         'state': state,
#     }
#     return render(request, 'management/add_book3.html', content)


# def add_book4(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_bookhealth = Bookhealth(
#                 d1a10=post.get('d1a10'),
#                 d1a11=post.get('d1a11'),
#                 d1a12=post.get('d1a12'),
#                 d1a13=post.get('d1a13'),
#                 d1a14=post.get('d1a14'),
#                 d1a15=post.get('d1a15'),
#                 d1a20=post.get('d1a20'),
#                 d1a21=post.get('d1a21'),
#                 d1a22=post.get('d1a22'),
#                 d1a23=post.get('d1a23', ''),
#                 d1a30=post.get('d1a30'),
#                 d1a31=post.getlist('d1a31', ''),
#                 d1a32=post.get('d1a32'),
#                 d1a33=post.get('d1a33', ''),
#                 d1a34=post.get('d1a34'),
#                 d1a35=post.get('d1a35'),
#                 d1a36=post.get('d1a36', ''),
#                 d1a37=post.get('d1a37'),
#                 d1a38=post.get('d1a38'),
#                 d1a39=post.get('d1a39', ''),
#                 d1a310=post.get('d1a310'),
#                 d1a311=post.get('d1a311'),
#                 d1a312=post.get('d1a312', ''),
#                 d1a313=post.get('d1a313'),
#                 d1a314=post.get('d1a314'),
#                 d1a315=post.get('d1a315', ''),
#                 d1a316=post.get('d1a316'),
#                 d1a317=post.get('d1a317', ''),
#                 d1a318=post.get('d1a318'),
#                 d1a40=post.get('d1a40'),
#                 d1a41=post.getlist('d1a41', ''),
#                 d1a42=post.get('d1a42'),
#                 d1a43=post.get('d1a43'),
#                 d1a44=post.get('d1a44'),
#                 d1a45=post.get('d1a45'),
#                 d1a46=post.get('d1a46'),
#                 d1a47=post.get('d1a47'),
#                 d1a48=post.get('d1a48', ''),
#                 d1a49=post.get('d1a49'),
#                 d1a51=post.get('d1a51', ''),
#                 d1a52=post.get('d1a52', ''),
#                 d1a53=post.get('d1a53', ''),
#                 d1a54=post.get('d1a54', ''),
#                 d1a55=post.get('d1a55', ''),
#                 d1a56=post.get('d1a56'),
#                 d1a57=post.get('d1a57'),
#                 d1a58=post.get('d1a58'),
#                 d1a59=post.get('d1a59'),
#                 d1a510=post.get('d1a510'),
#                 d1a511=post.get('d1a511', ''),
#                 d1a512=post.get('d1a512', ''),
#                 d1a513=post.get('d1a513'),
#                 d1a514=post.get('d1a514'),
#                 d1a515=post.getlist('d1a515', ''),
#                 d1a516=post.get('d1a516'),
#                 d1a517=post.get('d1a517'),
#                 d1a518=post.get('d1a518'),
#                 d1a519=post.get('d1a519'),
#                 d1a520=post.get('d1a520', ''),
#                 d1a521=post.get('d1a521'),
#                 d1a522=post.getlist('d1a522', ''),
#                 d1a523=post.get('d1a523'),
#                 d1a524=post.get('d1a524'),
#                 d1a525=post.get('d1a525'),
#                 d1a526=post.get('d1a526'),
#                 d1a527=post.get('d1a527'),
#                 d1a528=post.get('d1a528'),
#                 d1a529=post.get('d1a529', ''),
#                 d1a530=post.get('d1a530'),
#                 d1a531=post.get('d1a531', ''),
#                 d1a532=post.get('d1a532', ''),
#                 d1a533=post.get('d1a533'),
#                 d1a534=post.get('d1a534'),
#                 d1a535=post.get('d1a535'),
#                 d1a536=post.get('d1a536'),
#                 d1a537=post.get('d1a537'),
#                 d1a538=post.get('d1a538'),
#                 d1a539=post.get('d1a539'),
#                 d1a540=post.get('d1a540'),
#                 d1a541=post.get('d1a541'),
#                 d1a542=post.get('d1a542'),
#                 d1a543=post.get('d1a543', ''),
#                 d1a544=post.get('d1a544'),
#                 d1a545=post.get('d1a545'),
#                 d1a546=post.get('d1a546', ''),
#                 d1a547=post.get('d1a547'),
#                 d1a548=post.get('d1a548'),
#                 d1a549=post.get('d1a549', ''),
#                 d1a550=post.get('d1a550'),
#                 d1a551=post.get('d1a551'),
#                 d1a552=post.get('d1a552', ''),
#                 d1a553=post.get('d1a553'),
#                 d1a554=post.get('d1a554'),
#                 d1a555=post.get('d1a555', ''),
#                 d1a556=post.get('d1a556'),
#                 d1a557=post.get('d1a557'),
#                 d1a558=post.get('d1a558', ''),
#                 d1a559=post.get('d1a559'),
#                 d1a560=post.get('d1a560'),
#                 d1a561=post.get('d1a561', ''),
#                 d1a562=post.get('d1a562'),
#                 d1a563=post.get('d1a563'),
#                 d1a564=post.get('d1a564', ''),
#                 d1a565=post.get('d1a565'),
#                 d1a566=post.get('d1a566', ''),
#                 d1a567=post.get('d1a567'),
#                 d1a6=post.get('d1a6', ''),
#                 d1a7=post.get('d1a7', ''),
#                 d2a10=post.get('d2a10'),
#                 d2a11=post.getlist('d2a11', ''),
#                 d2a12=post.get('d2a12'),
#                 d2a13=post.get('d2a13'),
#                 d2a14=post.get('d2a14'),
#                 d2a15=post.get('d2a15'),
#                 d2a16=post.get('d2a16', ''),
#                 d2a17=post.get('d2a17'),
#                 d2a20=post.get('d2a20'),
#                 d2a21=post.getlist('d2a21', ''),
#                 d2a22=post.get('d2a22'),
#                 d2a23=post.get('d2a23'),
#                 d2a24=post.get('d2a24'),
#                 d2a25=post.get('d2a25'),
#                 d2a26=post.get('d2a26'),
#                 d2a27=post.get('d2a27'),
#                 d2a28=post.get('d2a28', ''),
#                 d2a29=post.get('d2a29'),
#                 d2a31=post.get('d2a31', ''),
#                 d2a32=post.get('d2a32', ''),
#                 d2a33=post.get('d2a33', ''),
#                 d2a34=post.get('d2a34', ''),
#                 d2a35=post.get('d2a35', ''),
#                 d2a36=post.get('d2a36'),
#                 d2a37=post.get('d2a37'),
#                 d2a38=post.get('d2a38'),
#                 d2a39=post.get('d2a39'),
#                 d2a310=post.get('d2a310'),
#                 d2a311=post.get('d2a311', ''),
#                 d2a312=post.get('d2a312', ''),
#                 d2a313=post.get('d2a313'),
#                 d2a314=post.get('d2a314'),
#                 d2a331=post.get('d2a331', ''),
#                 d2a332=post.get('d2a332', ''),
#                 d2a333=post.get('d2a333'),
#                 d2a334=post.get('d2a334'),
#                 d2a335=post.get('d2a335'),
#                 d2a336=post.get('d2a336'),
#                 d2a337=post.get('d2a337'),
#                 d2a338=post.get('d2a338'),
#                 d2a339=post.get('d2a339'),
#                 d2a340=post.get('d2a340'),
#                 d2a341=post.get('d2a341'),
#                 d2a342=post.get('d2a342'),
#                 d2a343=post.get('d2a343', ''),
#                 d2a344=post.get('d2a344'),
#                 d2a345=post.get('d2a345'),
#                 d2a346=post.get('d2a346', ''),
#                 d2a347=post.get('d2a347'),
#                 d2a348=post.get('d2a348'),
#                 d2a349=post.get('d2a349', ''),
#                 d2a350=post.get('d2a350'),
#                 d2a351=post.get('d2a351'),
#                 d2a352=post.get('d2a352', ''),
#                 d2a353=post.get('d2a353'),
#                 d2a354=post.get('d2a354'),
#                 d2a355=post.get('d2a355', ''),
#                 d2a356=post.get('d2a356'),
#                 d2a357=post.get('d2a357'),
#                 d2a358=post.get('d2a358', ''),
#                 d2a359=post.get('d2a359'),
#                 d2a360=post.get('d2a360'),
#                 d2a361=post.get('d2a361', ''),
#                 d2a362=post.get('d2a362'),
#                 d2a363=post.get('d2a363'),
#                 d2a364=post.get('d2a364', ''),
#                 d2a365=post.get('d2a365'),
#                 d2a366=post.get('d2a366', ''),
#                 d2a367=post.get('d2a367'),
#                 d2a4=post.get('d2a4', ''),
#                 d2a5=post.get('d2a5', ''),
#         )
#         new_bookhealth.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book4',
#         'state': state,
#     }
#     return render(request, 'management/add_book4.html', content)


# def add_book5(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_bookdang = Bookdange(
#                 e1=post.getlist('e1', ''),
#         )
#         new_bookdang.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book5',
#         'state': state,
#     }
#     return render(request, 'management/add_book5.html', content)


# def add_book6(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_bookchange = Bookchange(
#                 f1=post.get('f1', ''),
#         )
#         new_bookchange.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book6',
#         'state': state,
#     }
#     return render(request, 'management/add_book6.html', content)



# def add_book7(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_booksituation = Booksituation(
#                 g1=post.get('g1', ''),
#                 g2=post.get('g2'),
#         )
#         new_booksituation.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book7',
#         'state': state,
#     }
#     return render(request, 'management/add_book7.html', content)
#
#
# def add_book8(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_bookdiagnose = Bookdiagnose(
#                 h1=post.getlist('h1', ''),
#                 h2=post.getlist('h2', ''),
#                 h3=post.get('h3', ''),
#                 h4=post.get('h4', ''),
#         )
#         new_bookdiagnose.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book8',
#         'state': state,
#     }
#     return render(request, 'management/add_book8.html', content)
#
#
# def add_book9(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         new_booktime = Booktime(
#                 i1=post.get('i1'),
#                 i2=post.get('i2'),
#                 i3=post.get('i3'),
#                 i4=post.get('i4'),
#
#         )
#         new_booktime.save()
#         state = 'success'
#     content = {
#         'user': user,
#         'active_menu': 'add_book9',
#         'state': state,
#     }
#     return render(request, 'management/add_book9.html', content)

# def view_book_list(request):
#     user = request.user if request.user.is_authenticated() else None
#     category_list = Book.objects.values_list('category', flat=True).distinct()
#     query_category = request.GET.get('category', 'all')
#     if (not query_category) or Book.objects.filter(category=query_category).count() is 0:
#         query_category = 'all'
#         book_list = Book.objects.all()
#     else:
#         book_list = Book.objects.filter(category=query_category)
#
#     if request.method == 'POST':
#         keyword = post.get('keyword', '')
#         book_list = Book.objects.filter(name__contains=keyword)
#         query_category = 'all'
#
#     paginator = Paginator(book_list, 5)
#     page = request.GET.get('page')
#     try:
#         book_list = paginator.page(page)
#     except PageNotAnInteger:
#         book_list = paginator.page(1)
#     except EmptyPage:
#         book_list = paginator.page(paginator.num_pages)
#     content = {
#         'user': user,
#         'active_menu': 'view_book',
#         'category_list': category_list,
#         'query_category': query_category,
#         'book_list': book_list,
#     }
#     return render(request, 'management/view_book_list.html', content)
#
#
# def detail(request):
#     user = request.user if request.user.is_authenticated() else None
#     book_id = request.GET.get('id', '')
#     if book_id == '':
#         return HttpResponseRedirect(reverse('view_book_list'))
#     try:
#         book = Book.objects.get(pk=book_id)
#     except Book.DoesNotExist:
#         return HttpResponseRedirect(reverse('view_book_list'))
#     content = {
#         'user': user,
#         'active_menu': 'view_book',
#         'book': book,
#     }
#     return render(request, 'management/detail.html', content)
#
#
# @user_passes_test(permission_check)
# def add_img(request):
#     user = request.user
#     state = None
#     if request.method == 'POST':
#         try:
#             new_img = Img(
#                     name=post.get('name', ''),
#                     description=post.get('description', ''),
#                     img=request.FILES.get('img', ''),
#                     book=Book.objects.get(pk=post.get('book', ''))
#             )
#             new_img.save()
#         except Book.DoesNotExist as e:
#             state = 'error'
#             print(e)
#         else:
#             state = 'success'
#     content = {
#         'user': user,
#         'state': state,
#         'book_list': Book.objects.all(),
#         'active_menu': 'add_img',
#     }
#     return render(request, 'management/add_img.html', content)


