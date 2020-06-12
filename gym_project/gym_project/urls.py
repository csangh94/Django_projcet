from django.contrib import admin
from django.urls import path, include
import member.urls
import gyminfo.urls
import food.urls
from member.views import *
from Post.views import *
from django.conf.urls.static import static
from django.conf import settings
import Post.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include(member.urls)),
    path('post/', include(Post.urls)),
    path('', Main, name='main'),
    path('gym/', include(gyminfo.urls)),
    path('food/', include(food.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
