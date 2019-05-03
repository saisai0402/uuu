from django.urls import path, include, re_path
from .views import IndexView

app_name = 'index'

urlpatterns = [
    # 首页
    path('', IndexView.as_view(), name='index'),
]
