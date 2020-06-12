from django.contrib.auth.models import User
from django.db import models


# 칼로리 정보 검색

class Info_Kal(models.Model):
    code = models.CharField(max_length=20, primary_key=True)  # 음식 코드
    food_name = models.CharField(max_length=100)     # 음식 이름
    food_source = models.CharField(max_length=100)   # 음식 출처/원산지
    serving_size = models.CharField(max_length=10)   # 1회 제공량
    unit = models.CharField(max_length=5)            # 제공량 단위
    food_kal = models.DecimalField(max_digits=5,decimal_places=2)          # 칼로리

    def __str__(self):
        return self.food_name + " ( " + self.code + ") : " +str(self.food_kal)+ "kcal"
