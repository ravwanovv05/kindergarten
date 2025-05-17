from django.db import models


class ConsumedProduct(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    chef_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Chef ID')
    kindergarten_id = models.ForeignKey('main.Kindergarten', on_delete=models.CASCADE, verbose_name='Kindergarten ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Consumed Product'
        verbose_name_plural = 'Consumed Products'

    def __str__(self):
        return self.title
