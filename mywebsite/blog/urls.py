from django.urls import path
from blog import views

urlpatterns = [ # 처리규칙임.
    path("", views.index, name="index"),
]
