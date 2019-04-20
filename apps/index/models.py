from django.db import models
from datetime import datetime



class IndexSeo(models.Model):
    '''首页SEO'''
    title = models.CharField('标题', max_length=100)
    keywords = models.CharField('关键词', max_length=200)
    description = models.TextField('描述', max_length=500)
    add_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '首页SEO'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    '''首页幻灯片'''
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y%m', max_length=100)
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', auto_now=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

class Link(models.Model):
    '''友情链接'''
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)
    add_time = models.DateTimeField('添加时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
