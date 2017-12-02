# -*- encoding:utf-8 -*-
from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers
from models import *
import json
import decimal
import datetime

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.time):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

def trans(obj):
    return json.dumps(obj, cls=MyEncoder)

def backend(request):
    current_user = request.user
    return render(request, 'backend.html', locals())


# @login_required()
def show_ssd(request):
    # 页面展示
    ssds = SSD.objects.all().order_by('-id').select_related().values()
    records = []
    for ssd in ssds:
        try:
            ssd['book'] = trans(Book.objects.filter(id=ssd['book_id']).values()[0])
            ssd['bookcure'] = trans(Bookcure.objects.filter(id=ssd['bookcure_id']).values()[0])
            ssd['bcheck'] = trans(Bookcheck.objects.filter(id=ssd['bookcheck_id']).values()[0])
            ssd['bhealth'] = trans(Bookhealth.objects.filter(id=ssd['bookhealth_id']).values()[0])
            ssd['bdange'] = trans(Bookdange.objects.filter(id=ssd['bookdange_id']).values()[0])
            ssd['bchange'] = trans(Bookchange.objects.filter(id=ssd['bookchange_id']).values()[0])
            ssd['bsituation'] = trans(Booksituation.objects.filter(id=ssd['booksituation_id']).values()[0])
            ssd['bdiagnose'] = trans(Bookdiagnose.objects.filter(id=ssd['bookdiagnose_id']).values()[0])
            ssd['btime'] = trans(Booktime.objects.filter(id=ssd['booktime_id']).values()[0])
            records.append(ssd)
        except Exception as e:
            print(str(e))
    data = {}
    data['res'] = json.dumps(records)
    data['total'] = ssds.count()
    return JsonResponse(data)

def get_ssd_by_id(request):
    ids = request.GET.get('id')
    ids = json.loads(ids)
    if ids:
        id = ids[0]
        info = SSD.objects.filter(id=id).values()[0]
        print info
        return JsonResponse(info)

@csrf_exempt
def save_ssd(request):
    if request.method == 'POST':
        data = request.POST
        ids = data['id']
        name = data['name']
        idnumble = data['idnumble']
        ids = json.loads(ids)
        if not ids:
            return None
        SSD.objects.filter(id=ids[0]).update(name=name,idnumble=idnumble)
        return HttpResponse('ok')



@csrf_exempt
def delete_ssd(request):
    if request.method == 'POST':
        '''
        删除
        '''
        id_list = request.POST.get('id',[]).encode('utf-8')
        ids = json.loads(id_list)
        if not ids:
            return None
        try:
            for id in ids:
                s = SSD.objects.select_related().get(id=id)
                s.delete()

                #此处可以考虑级联删除,一键删除  此处未做

                #删除外建表book
                book_id = s.book_id
                Book.objects.filter(id=book_id).delete()

                # 删除外建表bookcuew
                bookcure_id = s.bookcure_id
                Bookcure.objects.filter(id=bookcure_id).delete()

                # 删除外建表bookhealth
                bookhealth_id = s.bookhealth_id
                Bookhealth.objects.filter(id=bookhealth_id).delete()

                # 删除外建表bookcheck
                bookcheck_id = s.bookcheck_id

                Bookcheck.objects.filter(id=bookcheck_id).delete()

                # 删除外建表bookchange
                bookchange_id = s.bookchange_id
                Bookchange.objects.filter(id=bookchange_id).delete()

                # 删除外建表bookdange
                bookdange_id = s.bookdange_id
                Bookdange.objects.filter(id=bookdange_id).delete()

                # 删除外建表booksituation
                booksituation_id = s.booksituation_id
                Booksituation.objects.filter(id=booksituation_id).delete()

                # 删除外建表bookdiagnose
                bookdiagnose_id = s.bookdiagnose_id
                Bookdiagnose.objects.filter(id=bookdiagnose_id).delete()

                # 删除外建表bbooktime
                booktime_id = s.booktime_id
                Booktime.objects.filter(id=booktime_id).delete()
                return HttpResponse('ok')
        except Exception as e:
            print('delete error:',str(e))
            return HttpResponse('error')