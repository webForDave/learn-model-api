from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.title