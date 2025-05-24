from django.db import models

class CivilServantModela(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)

    def __str__(self):
        return self.name
