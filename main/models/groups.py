from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')
    number_of_children = models.PositiveIntegerField(verbose_name='Number of children')
    nursery_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Nursery ID')
    kindergarten_id = models.ForeignKey('main.Kindergarten', on_delete=models.CASCADE, verbose_name='Kindergarten ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.title
