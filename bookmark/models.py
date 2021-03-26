from django.db import models
import datetime

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField("TITLE", max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    date = models.DateTimeField('DATETIME', default=datetime.datetime.now, null=True, blank=True)

    def __str__(self):
        return self.title
