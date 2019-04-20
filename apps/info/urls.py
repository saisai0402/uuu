from django.urls import path, include, re_path
from .views import InfoView

app_name = 'users'

urlpatterns = [
    # 首页
    path('<int:article_id>/', InfoView.as_view(), name='info'),
    # path('', ImgView.as_view(), name='img'),
]
