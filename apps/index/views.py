from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import IndexSeo


class IndexView(View):
    '''首页'''

    def get(self, request):
        # 设置首页SEO
        index_seo = IndexSeo.objects.all()[0]
        # 获取服务器时间
        nt = datetime.now()

        local_time = nt.strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年', m='月', d='日')
        return render(request, 'index.html', {
            'index_seo': index_seo,
            'local_time': local_time,
        })
