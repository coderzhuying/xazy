from django.db import models

# Create your models here.

class Recruitment(models.Model):
    position = models.CharField(max_length=40,verbose_name='岗位')
    requirements = models.TextField(verbose_name='岗位要求')
    salary = models.CharField(max_length=40,verbose_name='薪资')
    place = models.TextField(verbose_name='工作地')

    def __unicode__(self):
        return self.position

    def __unicode__(self):
        return self.requirements

    def __unicode__(self):
        return self.salary

    def __unicode__(self):
        return self.place

    class Meta:
        verbose_name = '招聘信息'
        verbose_name_plural = '招聘信息'


