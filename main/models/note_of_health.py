from django.db import models


class NoteOfHealth(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    nurse_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='Nurse ID')
    child_id = models.ForeignKey('main.Child', on_delete=models.CASCADE, verbose_name='Child ID')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Added at')

    class Meta:
        verbose_name = 'Note of Health'
        verbose_name_plural = 'Note of Health'

    def __str__(self):
        return self.title
