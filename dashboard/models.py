from django.db import models


class Function(models.Model):
    function = models.CharField('Функция', max_length=255)
    graph = models.ImageField(upload_to='graphs/',
        blank=True,
        null=True,
        verbose_name='График')
    interval = models.IntegerField('Интервал')
    dt = models.IntegerField('Шаг')
    processing_date = models.DateTimeField('Дата обработки', auto_now_add=True)
