# -*- coding: utf-8 -*- 
from django.db import models

from afm.utils import str_clean_and_lowcase


class IngsCategory(models.Model):
    """ Таблица категорий ингедиентов """

    class Meta:
        db_table = 'ings_category'
        managed = False
        verbose_name = 'Категории ингредиентов'
        verbose_name_plural = 'Категории ингредиентов'
        ordering = ['category']

    # Поле: Первичный ключ
    category_id = models.IntegerField(
            primary_key=True, 
            null=False,
            verbose_name='Первичный ключ',
            help_text='',
            )

    # Поле: Категория ингредиента
    category = models.CharField(
            max_length=250,
            null=False,
            unique=True, 
            verbose_name='Категория ингредиента',
            help_text='',
            )

    def save(self, *args, **kwargs):
        """ 
        Переопределение: приведение поля category к нижнему регистру
        """
        self.category = str_clean_and_lowcase(self.category)

        # Вызов метода-предка
        super(IngsCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category + ' (' + str(self.category_id) + ')'