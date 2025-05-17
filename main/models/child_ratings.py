from django.db import models


class ChildRating(models.Model):
    grade = models.IntegerField(verbose_name='Grade')
    comment = models.TextField(verbose_name='Comment')
    nursery_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Nursery ID')
    child_id = models.ForeignKey('main.Child', on_delete=models.CASCADE, verbose_name='Child ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Child Rating'
        verbose_name_plural = 'Child Ratings'

    def __str__(self):
        return self.child_id.first_name


