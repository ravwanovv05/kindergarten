from django.db import models

from main.models.regions import Region


class Kindergarten(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    number_of_children = models.PositiveBigIntegerField(verbose_name='Number of children')
    district_id = models.ForeignKey('main.District', on_delete=models.CASCADE, verbose_name='District')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region')

    class Meta:
        verbose_name = 'Kindergarten'
        verbose_name_plural = 'Kindergartens'

    def __str__(self):
        return self.title


