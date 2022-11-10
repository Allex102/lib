import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Readers(models.Model):
    fullname = models.CharField(max_length=200, verbose_name='ФИО',blank=True)
    address = models.CharField(max_length=200, verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=200, verbose_name='Номер телефона', blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
        ordering  = ['fullname']

class Authors(models.Model):
    fullname = models.CharField(max_length=200, verbose_name='ФИО автора', blank=True)
    img = models.ImageField(verbose_name='Изображение автора', blank=True, upload_to='authors/%Y-%m-%D')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['fullname']


class Books(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', blank=True)
    year = models.DateField(verbose_name='Год выпуска', blank=True)
    count = models.IntegerField(verbose_name='Количество', blank=True,)
    author_id = models.ForeignKey(to=Authors, on_delete=models.PROTECT, related_name='books', verbose_name='id автора')
    slug = models.SlugField(max_length=250, verbose_name='url', unique=True)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Изображение', upload_to='%Y-%m-%D', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']


class Outs(models.Model):
    date_out = models.DateField(verbose_name='Дата выдачи', blank=True)
    date_in = models.DateField(verbose_name='Дата сдачи', blank=True)
    readers_id = models.ForeignKey(to=Readers, on_delete=models.PROTECT, related_name='outs', verbose_name='id читателя')
    books_id = models.ForeignKey(to=Books, on_delete=models.PROTECT, related_name='outs', verbose_name='id книги')

    def __str__(self):
        return f'Выдача от {self.date_out}'

    class Meta:
        verbose_name = 'Выдача'
        verbose_name_plural = 'Выдачи'
        ordering = ['date_out']