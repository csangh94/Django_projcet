from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from food.dao import *

def session_in(request):
    rank = serch_rank()
    rank_list = []
    for x in rank:
        rank_dic = {}
        rank_dic['name'] = x[0]
        rank_dic['count'] = x[1]
        rank_list.append(rank_dic)
    request.session['rank'] = rank_list
    return redirect('main')

def session_end(request):
    del request.session['rank'],request.session['kal']
    return redirect('main')
def inputfood(request):
    return render(request, 'food/food_input.html')


def test(request):
    data = request.GET.get('food')
    data_list = data.split(",")
    file = open("검색 정보.txt", "a", encoding="utf8")
    for x in data_list:
        file.write(x + "\n")
    file.close()
    b = ''
    c= []
    sum2=0.0
    for x in data_list:
        food_info = fooddao(x)
        if food_info != None:
            y = food_info
            sum2 = sum2+float(y[5])
            b = b + str(y[1]+"의 1회 제공량 "+y[3]+y[4]+"/ "+y[5]+"kal<br>")
            c.append(str(y[1]+"의 1회 제공량 "+y[3]+y[4]+"/ "+y[5]+"kal"))
    test_a = sum2/50
    c.append("총 칼로리>>"+str(sum2)+"kal")
    c.append("소비시간 >>런닝머신 6km/h "+str(int(test_a))+"0분 달리기")
    request.session['kal']=c
    if b =='':
        return HttpResponse("<span style=color:red>정확히 입력해 주세요</span>")
    else:
        return HttpResponse(b+"총 칼로리>>"+str(sum2)+"kal<br>소비시간 >>런닝머신 6km/h "+str(int(test_a))+"0분 달리기")

def test2(request):
    test_list = facility()
    dic_list = []
    for x in test_list:
        dic_test = {}
        dic_test['division'] = x[1]
        dic_test['name'] = x[2]
        dic_test['address'] = x[3]
        dic_test['latitude'] = x[4]
        dic_test['longitude'] = x[5]
        dic_test['tel'] = x[6]
        dic_test['home'] = x[8]
        dic_test['storm'] = x[9]
        dic_test['inout'] = x[10]
        dic_test['parking'] = x[11]
        dic_list.append(dic_test)
    return render(request, 'food/food_input.html', {"test_list": dic_list})


def test3(request):
    data = request.GET.get('division')
    test_list = test_facility(data)
    dic_list = []
    for x in test_list:
        dic_test = {}
        dic_test['division'] = x[1]
        dic_test['name'] = x[2]
        dic_test['address'] = x[3]
        dic_test['latitude'] = x[4]
        dic_test['longitude'] = x[5]
        dic_test['tel'] = x[6]
        dic_test['home'] = x[8]
        dic_test['storm'] = x[9]
        dic_test['inout'] = x[10]
        dic_test['parking'] = x[11]
        dic_list.append(dic_test)
    return render(request, 'food/map_list.html', {"se_list": dic_list})
