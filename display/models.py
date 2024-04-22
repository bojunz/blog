from django.db import models

# Create your models here.

class BlogModel(models.Model):
    #blank表示填写name表单字段的时候可以为空
    name = models.CharField(max_length=10,blank=True)
    sku = models.CharField(max_length=30,blank=True)
    number = models.IntegerField(max_length=50)


