from django.contrib.auth.models import User

from django.db import models

# Create your models here.

# 짐 정보 등록 테이블 / author = 관리자 , photo = 관련 사진, text = 소개 글,

class GymInfo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos') # 관리자
    gym_title = models.CharField(max_length=50)                                            # 짐 이름
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',default='photos/no_image.png')   # 관련 사진
    home_page = models.CharField(max_length=50)                                            # 업체 사이트
    phone = models.CharField(max_length=20)                                                # 업체 번호
    open_time = models.TextField(default='')                                               # 영업 시간
    created = models.DateTimeField(auto_now_add=True)                                      # 등록 시 시간 등록
    updated = models.DateTimeField(auto_now=True)                                          # 수정 시 시간
    text = models.TextField(default='')                                                    # 소개 글
    class Meta:
        # ordering = ['updated']  # 오름차순
        ordering = ['-updated']   # 내림차순

    def __str__(self):
        return self.gym_title+" " + self.created.strftime('%Y-%m-%d %H:%M:%S')             # 짐 이름, 등록 시간
