from django.shortcuts import render
from django.views.generic.base import View
from .models import Article, Tag


class InfoView(View):
    '''文章详情页'''

    def get(self, request, article_id):
        # 文章详情
        content = Article.objects.get(id=int(article_id))
        content.views += 1
        content.save()
        previous_content = Article.objects.filter(created_time__gt=content.created_time,
                                                  category=content.category.id).first()
        next_content = Article.objects.filter(created_time__lt=content.created_time,
                                              category=content.category.id).last()
        # 取出文章对应标签所有标签
        tags = content.tags.all()
        relate_articles = Article.objects.all().order_by('?')[0:10]
        # 旅游指南是多对多查询
        guide_articles = Article.objects.prefetch_related('tags').order_by('?')[:10]
        hot_articles = Article.objects.all().order_by('-views')[0:10]
        return render(request, 'info.html', {
            'content': content,
            'previous_content': previous_content,
            'next_content': next_content,
            'relate_articles': relate_articles,
            'guide_articles': guide_articles,
            'hot_articles': hot_articles,
            'tags': tags
        })
