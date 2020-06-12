from django.contrib.auth.models import User
from django.urls import *
from django.utils import timezone

from member.models import *


class Post(models.Model):
    user_id = models.ForeignKey(GymMember, db_column='user_id',
                                on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='TITLE', max_length=100, null=False)
    content = models.TextField('CONTENT', default='')
    Pub_date = models.DateTimeField(default=timezone.now)  # 생성 시 시각
    mod_date = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        verbose_name = 'post'  # 사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에 표시된다. # 단수형
        verbose_name_plural = 'posts'  # 복수형
        db_table = 'post_post'
        ordering = ('-mod_date',)  # 게시물수정필드  내림차순 정렬

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.id,))
        # reverse()함수는 url패턴을 만들어주는 내장 함수 이다.
        # 장고는 urls.py변경을 통해 각 뷰에 대한 url이 변경되는 유연한 시스템을 가지고 이어
        # url이 변경되더라고 url reverse가 변경된 url을 추적한다.

    def get_previous(self):
        return self.get_previous_by_mod_date()

    def get_next(self):
        return self.get_next_by_mod_date()
