from django.db import models


class Child(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    date_of_birth = models.DateField(verbose_name='Date of birth')
    payment_status = models.BooleanField(default=False, verbose_name='Payment status')
    parent_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Parent ID')
    group_id = models.ForeignKey('main.Group', on_delete=models.CASCADE, verbose_name='Group ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Child'
        verbose_name_plural = 'Children'

    def __str__(self):
        return self.first_name
