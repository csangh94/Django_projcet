from django.urls import path

from gyminfo.views import *

urlpatterns = [
    path('gyminsert/', GymInsert.as_view(), name='gm_insert'),
    path('gymlist/',selectAll,name='gm_list'),
    path('gymdetail/<int:pk>',Gm_detail.as_view(),name='gm_detail'),
    path('gymupdate/<int:pk>', GymUpdate.as_view(), name='gm_update'),
    path('gymdelete/<int:pk>', GymDelete.as_view(), name='gm_delete'),
]
