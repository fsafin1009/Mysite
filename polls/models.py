import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Владелец статьи", blank=True, null = True )
    title = models.CharField(max_length=15, verbose_name="Названия статьи")
    content = models.TextField(verbose_name="Описание статьи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликована?")
    data_published = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Стаья"
        verbose_name_plural = "Cтатьи"




