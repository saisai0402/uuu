from django.db import models
from users.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField


# 文章分类
class Category(models.Model):
    name = models.CharField('内容分类', max_length=100)

    class Meta:
        verbose_name = '内容分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = RichTextUploadingField(verbose_name='文章详情')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    """
    文章作者，这里User是从重构的users.models导入的。这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
