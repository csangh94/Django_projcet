from django.urls import path, include
from member.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('memberlist/', MemberList.as_view(), name='list'),
    path('membercreate/', memberCreate, name='create'),
    path('membercreate2/', memberCreate2, name='create2'),
    path('memberupdate/<pk>', MemberUpdate.as_view(), name='update'),
    path('memberdelete/<pk>', memberDelete, name='delete'),
    path('memberdetail/<pk>', MemberDetail.as_view(), name='detail'),
    path('login/', login, name='login'),
    path('loginCheck/', loginCheck, name='loginCheck'),
    path('logout/', logout, name='logout'),
    # path('checkid', checkid, name='checkid'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


