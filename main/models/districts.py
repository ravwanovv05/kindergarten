from django.db import models


class District(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    region_id = models.ForeignKey('main.Region', on_delete=models.CASCADE, verbose_name='Region ID')

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return self.title
