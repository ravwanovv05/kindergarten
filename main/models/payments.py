from django.db import models


class Payment(models.Model):
    TYPE_CHOICES = (
        ('cash', 'Cash'),
        ('card', 'Card'),

    )
    amount = models.FloatField(verbose_name='Amount')
    type_of_payment = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Type of Payment')
    month = models.CharField(max_length=50, verbose_name='Month')
    description = models.TextField(verbose_name='Description')
    kindergarten_id = models.ForeignKey('main.Kindergarten', on_delete=models.CASCADE)
    child_id = models.ForeignKey('main.Child', on_delete=models.CASCADE, verbose_name='Child ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.month

