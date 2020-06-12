from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from gyminfo.models import GymInfo



def selectAll(request):
    list = GymInfo.objects.all()
    return render(request, 'gyminfo/gyminfo_list.html',{"list":list})
class GymInsert(CreateView):
    model = GymInfo
    fields = ['author','gym_title','home_page','open_time','phone','photo','text']
    template_name = 'gyminfo/gym_insert.html'
    success_url = reverse_lazy('gm_list')

class Gm_detail(DetailView):
    model = GymInfo
    template_name = "gyminfo/gm_detail.html"

class GymUpdate(UpdateView):
    model = GymInfo
    fields = ['author','gym_title','home_page','open_time','phone','photo','text']
    template_name_suffix = '_update'
    success_url = reverse_lazy('gm_list')

class GymDelete(DeleteView):
    model = GymInfo
    success_url = reverse_lazy('gm_list')