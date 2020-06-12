from django.db import models


# Create your models here.

class GymMember(models.Model):
    # 파이썬의 변수, DB테이블의 항목
    # 프라이머리 키 없으면 자동으로 id 생기고 오토인크리먼트
    user_id = models.CharField(max_length=100, primary_key=True)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=100)
    membership = models.CharField(max_length=100)
