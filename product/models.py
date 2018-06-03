from django.db import models

# Create your models here.
class Housekeeping(models.Model):

    content = models.TextField(verbose_name='内容')

    tel = models.CharField(max_length=15,verbose_name='联系电话')

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.tel

    class Meta:
        verbose_name = '家政服务'
        verbose_name_plural = '家政服务'

class Car(models.Model):

    content = models.TextField(verbose_name='内容')

    tel = models.CharField(max_length=15,verbose_name='联系电话')

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.tel

    class Meta:
        verbose_name = '汽车维修'
        verbose_name_plural = '汽车维修'

class People(models.Model):

    content = models.TextField(verbose_name='内容')

    tel = models.CharField(max_length=15,verbose_name='联系电话')

    def __unicode__(self):
        return self.content

    def __unicode__(self):
        return self.tel

    class Meta:
        verbose_name = '便民维修'
        verbose_name_plural = '便民维修'
