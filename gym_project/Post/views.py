from django.urls import reverse_lazy
from django.views.generic import *
from Post.models import Post


class PostLV(ListView):
    model = Post
    context_object_name = 'posts'
    # 디폴트 변수명지정함, post쓰는 변수가 많아서 다르게 설정해줌
    paginate_by = 2  # 한페이지에 보여줄 오브젝트 갯수


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'mod_date'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    # 성공시 'post_list' url로 이동


class PostCreate(CreateView):  # 모델 , 사용할 필드, 성공URL이 필요하다
    model = Post
    fields = ['id', 'title', 'content', 'user_id']
    # 게시물 작성에 필요한 필드기입
    #   입력하는 tmeplate필요,  지정!
    template_name_suffix = '_create'

    # 성공했으면 어느 페이지로 연결할지 설정
    # 호출했던 페이지의 위치에 상관없이 list라
    # 명명된 페이지를 호출해준다.
    success_url = reverse_lazy('post_list')


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update'
    success_url = reverse_lazy('post_list')
