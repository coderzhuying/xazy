from django.db import models
from system.storage import ImageStorage

# Create your models here.

class Notice(models.Model):

    title = models.CharField(max_length=40,verbose_name='标题')
    # 新闻,最多不能超过40个字符
    content = models.TextField(verbose_name='内容')
    # 内容
    pub_date = models.DateTimeField(auto_now=True,verbose_name='发布时间')
    # 发布时间，自动保存为最后的修改时间


    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.pub_date

    class Meta:
        verbose_name = '通知公告'
        verbose_name_plural = '通知公告'

class BigImage(models.Model):

    bigimg1 = models.ImageField(upload_to='index/bigimg1', storage=ImageStorage(),verbose_name='图片1')
    bigimg2 = models.ImageField(upload_to='index/bigimg2', storage=ImageStorage(),verbose_name='图片2')
    bigimg3 = models.ImageField(upload_to='index/bigimg3', storage=ImageStorage(),verbose_name='图片3')

    class Meta:
        verbose_name = '封面大图'
        verbose_name_plural = '封面大图'

class SamllImage(models.Model):
    samllimg1 = models.ImageField(upload_to='index/samllimg1', storage=ImageStorage(),verbose_name='图片1')
    samllimg2 = models.ImageField(upload_to='index/samllimg2', storage=ImageStorage(),verbose_name='图片2')
    samllimg3 = models.ImageField(upload_to='index/samllimg3', storage=ImageStorage(),verbose_name='图片3')
    samllimg4 = models.ImageField(upload_to='index/samllimg4', storage=ImageStorage(),verbose_name='图片4')
    samllimg5 = models.ImageField(upload_to='index/samllimg5', storage=ImageStorage(),verbose_name='图片5')
    samllimg6 = models.ImageField(upload_to='index/samllimg6', storage=ImageStorage(),verbose_name='图片6')

    class Meta:
        verbose_name = '小轮播图'
        verbose_name_plural = '小轮播图'



