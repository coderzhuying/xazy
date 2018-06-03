from django.db import models
from system.storage import ImageStorage
# Create your models here.
class House(models.Model):

    title = models.CharField(max_length=40, verbose_name='标题')
    # 最多不能超过40个字符
    content = models.TextField(verbose_name='内容')
    # 内容
    pub_date = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    # 发布时间，自动保存为最后的修改时间
    author = models.CharField(max_length=20, verbose_name='发布人')
    # 发布人
    img = models.ImageField(upload_to='life', verbose_name='图片',null=True,blank=True)

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.author

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.pub_date


    class Meta:
        verbose_name = '业主之家'
        verbose_name_plural = '业主之家'