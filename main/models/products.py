from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    given_money = models.FloatField(verbose_name='Given money')
    description = models.TextField(verbose_name='Description')
    kindergarten_id = models.ForeignKey('main.Kindergarten', on_delete=models.CASCADE, verbose_name='Kindergarten ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
