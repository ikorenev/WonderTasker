from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    date = models.DateTimeField('Дедлайн')
    task = models.TextField('Описание')
    is_complete = models.BooleanField('Задание выполнено', default=False)
    is_moder = models.BooleanField('Задание отправлено на проверку', default=False)
#    priority =

def __str__(self):
    return self.title


class Meta:
    verbose_name = 'Задачи'
    verbose_name_plural = 'Задачи'
