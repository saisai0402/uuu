import xadmin

from .models import EmailVerifyRecord
from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = False
    use_bootswatch = False


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '悠游日记'
    # 修改footer
    site_footer = '悠游日记'
    # 收起菜单
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    '''xadmin中这里是继承object，不再是继承admin'''
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)
