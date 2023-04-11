from django.db import models


class URLMapping(models.Model):
    short_url = models.CharField(max_length=10, unique=True)
    original_url = models.URLField()

    def __str__(self):
        return f'{self.short_url} -> {self.original_url}'
