from django.db import models

# Create your models here.

class Information(models.Model):

    telephone = models.CharField(max_length=15,verbose_name='联系电话')

    address = models.CharField(max_length=15, verbose_name='联系地址')

    person = models.CharField(max_length=15, verbose_name='联系人')

    def __unicode__(self):
        return self.telephone

    def __unicode__(self):
        return self.address

    def __unicode__(self):
        return self.person

    class Meta:
        verbose_name = '联系方式'
        verbose_name_plural = '联系方式'
