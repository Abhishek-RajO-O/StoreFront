from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tags(models.Model):
    lable = models.CharField(max_length=255)


# genric relationship using content types

class TaggedItem(models.Model):
    """what tag applied to what object"""
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)
    # type  (product , video , article )
    # ID
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE)
    # if id is a GID then this will not work . this is the limitation       
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


