from django.db import models


class Attendance(models.Model):
    attended = models.BooleanField(verbose_name='Attended')
    admin_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Administrator ID')
    child_id = models.ForeignKey('main.Child', on_delete=models.CASCADE, verbose_name='Child ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return self.child_id.first_name

