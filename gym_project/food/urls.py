from django.urls import path
from food.views import *

urlpatterns = [
    path('foodinput', inputfood, name="input"),
    path('test/', test, name="test"),
    path('find', test2, name="test2"),
    path('test3/', test3, name="test3"),
    path('session_end/', session_end, name="session_end"),
    path('session_in/', session_in, name="session_in"),

]
