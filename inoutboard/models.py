from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=200)
    last_mod = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False, verbose_name='last modified')
    status = models.BooleanField()
    message = models.TextField()

