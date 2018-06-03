from django.db import models
from system.storage import ImageStorage
# Create your models here.

#创建模型类,公司新闻类，定义字段及类型
class CompanyProfile(models.Model):

    content = models.TextField(verbose_name='内容')
    # 内容

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '公司简介'
        verbose_name_plural = '公司简介'


class CompanyCulture(models.Model):

    content = models.TextField(verbose_name='内容')
    # 内容

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '企业文化'
        verbose_name_plural = '企业文化'


class CompanyTeam(models.Model):

    content = models.TextField(verbose_name='内容')

    def __unicode__(self):
        return self.content


    class Meta:
        verbose_name = '团队建设'
        verbose_name_plural = '团队建设'



class CompanyMemorabilia(models.Model):

    content = models.TextField(verbose_name='内容')
    # 内容
    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '大事迹'
        verbose_name_plural = '大事迹'


class CompanyStructure(models.Model):

    content = models.TextField(verbose_name='内容')

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '组织架构'
        verbose_name_plural = '组织架构'




