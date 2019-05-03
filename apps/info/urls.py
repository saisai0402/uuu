from django.urls import path, include, re_path
from .views import ArticleView, CategoryView

app_name = 'info'

urlpatterns = [
    # 首页
    path('article/<int:article_id>', ArticleView.as_view(), name='article'),
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),
    # path('', ImgView.as_view(), name='img'),
]
