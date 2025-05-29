from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
class Region(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=120, unique=True, verbose_name='Title')

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.title
