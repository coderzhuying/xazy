from django.db import models

# Create your models here.

#创建模型类,公司新闻类，定义字段及类型
class CompanyNews(models.Model):

    title = models.CharField(max_length=40,verbose_name='标题')
    # 新闻,最多不能超过40个字符
    content = models.TextField(verbose_name='内容')
    # 内容
    pub_date = models.DateTimeField(auto_now=True,verbose_name='发布时间')
    # 发布时间，自动保存为最后的修改时间
    author = models.CharField(max_length=20,verbose_name='发布人')
    # 发布人
    img = models.ImageField(upload_to='company/', verbose_name='图片', null=True, blank=True)


    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.author

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.pub_date

    class Meta:
        verbose_name = '公司新闻'
        verbose_name_plural = '公司新闻'


#创建模型类，地方新闻类,定义字段及类型
class LocalNews(models.Model):
    title = models.CharField(max_length=40, verbose_name='标题')
    # 新闻,最多不能超过40个字符
    content = models.TextField(verbose_name='内容')
    # 内容
    pub_date = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    # 发布时间，自动保存为最后的修改时间
    author = models.CharField(max_length=20, verbose_name='发布人')
    # 发布人
    img = models.ImageField(upload_to='local/', verbose_name='图片', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.author

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.pub_date

    class Meta:
        verbose_name = '地方动态'
        verbose_name_plural = '地方动态'


#创建模型类，媒体新闻类,定义字段及类型
class MediaNews(models.Model):

    title = models.CharField(max_length=40, verbose_name='标题')
    # 新闻,最多不能超过40个字符
    content = models.TextField(verbose_name='内容')
    # 内容
    pub_date = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    # 发布时间，自动保存为最后的修改时间
    author = models.CharField(max_length=20, verbose_name='发布人')
    # 发布人
    img = models.ImageField(upload_to='media/', verbose_name='图片', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.author

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.pub_date

    class Meta:
        verbose_name = '媒体新闻'
        verbose_name_plural = '媒体新闻'
