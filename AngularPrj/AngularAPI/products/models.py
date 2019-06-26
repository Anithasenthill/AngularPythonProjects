from django.db import models

# Create your models here.
from django.db.models import ImageField


class Product(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    price = models.IntegerField(blank=False, default=1)
    desc = models.CharField(max_length=70, blank=True, default='')
    # img = models.ImageField()


    def __str__(self):
        return self.name

    # def image_img(self):
    #     if self.img:
    #         return u'<img src="%s" width="50" height="50" />' % self.img.url
    #     else:
    #         return '(Retryyyy)'



