from email.policy import default
from re import T
from django.db import models
from django.contrib.auth.models import User
from photo.fields import ThumbnailImageField


# Create your models here.
class Cate(models.Model):
    cate_name = models.CharField('NAME', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.cate_name

    
    


class Market(models.Model):
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField('NAME', max_length=100, blank=True)
    url = models.URLField('URL', unique = True)
    # item = models.CharField('ITEM', max_length=100, blank=True)
    image = ThumbnailImageField(upload_to='market/%Y/%m',  blank=True, null=True)
    price = models.CharField('PRICE', max_length=100, blank=True)

    class Meta:
        verbose_name = 'market'
        verbose_name_plural = 'markets'
        # db_table = 'blog_posts'


    