from django.urls import path
from Post import views

urlpatterns = [
    path('list/', views.PostLV.as_view(), name='post_list'),
    path('detail/<int:pk>', views.PostDV.as_view(), name='post_detail'),  # 디테일뷰
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    #path('', views.index, name='index'),
    # logout/라는 경로로 접근했을 때 logout이 호출된다.
    # url(r'^login/$', views.signin, name='login'),
    # 게시물 제목을 클릭해서 들어갈때는 게시물 번호를 통해 들어가고, 게시물 번호는 자동으로 pk값으로 지정되어
    # 있기 때문에 post/<int:pk>/" 기입
]
