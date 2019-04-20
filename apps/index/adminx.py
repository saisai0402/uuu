import xadmin

from .models import Banner, Link, IndexSeo


class IndexSeoAdmin(object):
    '''首页SEO'''
    # 显示的列
    list_display = ['title', 'keywords', 'description', 'add_time']
    # 搜索的字段
    search_fields = ['title', 'keywords', 'description', 'add_time']
    # 过滤
    list_filter = ['title', 'keywords', 'description', 'add_time']
    # 时间倒序
    ordering = ['-add_time']


    def has_add_permission(self):
        return False

    def has_delete_permission(self, obj=None):
        return obj is None or obj.pk != 1


class BannerAdmin(object):
    '''首页幻灯片'''
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    ordering = ['-add_time']


class LinkAdmin(object):
    '''友情链接'''
    list_display = ['name', 'link_url', 'add_time']
    search_fields = ['name', 'link_url', 'add_time']
    list_filter = ['name', 'link_url', 'add_time']
    ordering = ['-add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Link, LinkAdmin)
xadmin.site.register(IndexSeo, IndexSeoAdmin)
