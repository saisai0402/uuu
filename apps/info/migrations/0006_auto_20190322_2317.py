# Generated by Django 2.1.4 on 2019-03-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20190322_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
        migrations.AddField(
            model_name='img',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='img',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='background_image/%Y/%m/%d/', verbose_name='背景图片'),
        ),
    ]