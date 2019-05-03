from django.shortcuts import render
from django.views.generic.base import View
from .models import Article, Tag, Category


class ArticleView(View):
    '''文章详情页'''

    def get(self, request, article_id):
        # 文章详情
        article = Article.objects.get(id=int(article_id))
        article.views += 1
        article.save()
        previous_article = Article.objects.filter(created_time__gt=article.created_time,
                                                  category=article.category.id).first()
        next_article = Article.objects.filter(created_time__lt=article.created_time,
                                              category=article.category.id).last()
        # 取出文章对应标签所有标签
        tags = article.tags.all()
        relate_articles = Article.objects.all().order_by('?')[0:10]
        # 旅游指南是多对多查询
        guide_articles = Article.objects.prefetch_related('tags').order_by('?')[:10]
        hot_articles = Article.objects.all().order_by('-views')[0:10]
        return render(request, 'article.html', {
            'article': article,
            'previous_article': previous_article,
            'next_article': next_article,
            'relate_articles': relate_articles,
            'guide_articles': guide_articles,
            'hot_articles': hot_articles,
            'tags': tags
        })


class CategoryView(View):
    '''文章分类页'''

    def get(self, request, category_id):
        category = Category.objects.get(id=int(category_id))
        new_articles = Article.objects.prefetch_related('category').order_by('-modified_time')[:10]
        return render(request, 'category.html', {
            'category': category,
            'new_articles' : new_articles

        })
