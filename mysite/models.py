from django.db import models
from datetime import datetime
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField

class Post(models.Model):
    title: str = models.CharField(max_length=200)
    slug:  str = models.CharField(max_length=200)
    body:  str = models.TextField()
    pub_date: datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-pub_date",)
    def __str__(self) ->str:
        return self.title
