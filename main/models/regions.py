from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Title')

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.title
