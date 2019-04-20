import xadmin

from .models import Category, Tag, Tui, Article


class CategoryAdmin(object):
    # 显示的列
    list_display = ['name']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['name']


class TagAdmin(object):
    # 显示的列
    list_display = ['name']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['name']


class TuiAdmin(object):
    # 显示的列
    list_display = ['name']
    # 搜索的字段
    search_fields = ['name']
    # 过滤
    list_filter = ['name']


class ArticleAdmin(object):
    # 显示的列
    list_display = ['title', 'category', 'tags', 'user', 'views', 'tui', 'created_time',
                    'modified_time']
    # 搜索的字段
    search_fields = ['title', 'excerpt', 'category', 'tags', 'img', 'user', 'views', 'tui', 'created_time',
                     'modified_time']
    # 过滤
    list_filter = ['title', 'excerpt', 'category', 'tags', 'img', 'user', 'views', 'tui', 'created_time',
                   'modified_time']
    # 修改文章
    list_editable = ['title', 'excerpt', 'category', 'tags', 'img', 'tui']
    # 满50条数据就自动分页
    list_per_page = 50
    # 后台数据列表排序方式
    ordering = ['-created_time']
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ['title', 'excerpt', 'category']


# 将后台管理器与models进行关联注册。
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Tui, TuiAdmin)
xadmin.site.register(Article, ArticleAdmin)
