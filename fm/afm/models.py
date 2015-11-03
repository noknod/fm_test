# -*- coding: utf-8 -*- 
from django.db import models

from afm.utils import str_clean_and_lowcase


class WordNoun(models.Model):
    """ Таблица-словарь существительных """

    class Meta:
        db_table = 'data_word_noun'
        managed = False
        verbose_name = 'Словарь существительных'
        verbose_name_plural = 'Словарь существительных'
        ordering = ['noun']

    # Поле: Первичный ключ
    noun_id = models.IntegerField(
            primary_key=True, 
            null=False,
            verbose_name='Первичный ключ',
            help_text='',
            )

    # Поле: Существительное
    noun = models.CharField(
            max_length=50,
            null=False,
            unique=True, 
            verbose_name='Существительное',
            help_text='',
            )

    def save(self, *args, **kwargs):
        """ 
        Переопределение: запрещение изменения таблицы data_word_noun
        """
        raise Exception('Запрещено изменение таблицы data_word_noun!')

    def __str__(self):
        return self.noun + ' (' + str(self.noun_id) + ')'


class WordAdjective(models.Model):
    """ Таблица-словарь прилагательных """

    class Meta:
        db_table = 'data_word_adjective'
        managed = False
        verbose_name = 'Словарь прилагательных'
        verbose_name_plural = 'Словарь прилагательных'
        ordering = ['adjective']

    # Поле: Первичный ключ
    adjective_id = models.IntegerField(
            primary_key=True, 
            null=False,
            verbose_name='Первичный ключ',
            help_text='',
            )

    # Поле: Прилагательное
    adjective = models.CharField(
            max_length=50,
            null=False,
            unique=True, 
            verbose_name='Прилагательное',
            help_text='',
            )

    def save(self, *args, **kwargs):
        """ 
        Переопределение: запрещение изменения таблицы data_word_adjective
        """
        raise Exception('Запрещено изменение таблицы data_word_adjective!')

    def __str__(self):
        return self.adjective + ' (' + str(self.adjective_id) + ')'


class Product(models.Model):
    """ Таблица-словарь товаров """

    class Meta:
        db_table = 'data_product'
        managed = False
        verbose_name = 'Словарь товаров'
        verbose_name_plural = 'Словарь товаров'
        #ordering = ['']

    # Поле: Первичный ключ
    product_id = models.IntegerField(
            primary_key=True, 
            null=False,
            verbose_name='Первичный ключ',
            help_text='',
            )

    # Поле: Внешний ключ: существительное
    noun_id = models.ForeignKey(
            WordNoun, 
            db_column='noun_id', 
            null=False,
            verbose_name='Внешний ключ: существительное',
            help_text='',
            )

    def save(self, *args, **kwargs):
        """ 
        Переопределение: запрещение изменения таблицы data_word_product
        """
        raise Exception('Запрещено изменение таблицы data_word_product!')

    def __str__(self):
        return self.noun_id.noun + ' (' + str(self.product_id) + ')'


class ProductDetail(models.Model):
    """ Таблица-словарь товаров """

    class Meta:
        db_table = 'data_product_detail'
        managed = False
        verbose_name = 'Словарь товаров'
        verbose_name_plural = 'Словарь товаров'
        #unique_together = (('product_id', 'adjective_id',),)
        #ordering = ['']

    # Поле: Внешний ключ: товар
    product_id = models.ForeignKey(
            Product, 
            primary_key=True, 
            db_column='product_id', 
            null=False,
            verbose_name='Внешний ключ: товар',
            help_text='',
            )

    # Поле: Внешний ключ: прилагательное
    adjective_id = models.ForeignKey(
            WordAdjective, 
            primary_key=True, 
            db_column='adjective_id', 
            null=False,
            verbose_name='Внешний ключ: прилагательное',
            help_text='',
            )

    def save(self, *args, **kwargs):
        """ 
        Переопределение: запрещение изменения таблицы data_product_detail
        """
        raise Exception('Запрещено изменение таблицы data_product_detail!')

    def __str__(self):
        return self.product_id.noun_id.noun + ' ' + self.adjective_id.adjective + ' (' + str(self.product_id) + ')'


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


class Ingredient(models.Model):
    """ Таблица ингедиентов """

    class Meta:
        db_table = 'ings_product'
        managed = False
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['category_id', 'product_id']

    # Поле: Первичный ключ
    product_id = models.IntegerField(
            primary_key=True, 
            db_column='product_id', 
            null=False,
            verbose_name='Первичный ключ',
            help_text='',
            )

    # Поле: Внешний ключ: категория
    category_id = models.ForeignKey(
            IngsCategory, 
            db_column='category_id', 
            null=False,
            verbose_name='Внешний ключ: категория',
            help_text='',
            )

    # Поле: Ингредиент
    ingredient = models.CharField(
            max_length=500,
            null=False,
            unique=True, 
            verbose_name='Ингредиент',
            help_text='',
            )

    # Поле: Внешний ключ: родитель
    parent_id = models.ForeignKey(
            'self', 
            db_column='parent_id', 
            null=False,
            related_name='parent',
            verbose_name='Внешний ключ: родитель',
            help_text='',
            )

    # Поле: Признак абстрактного ингредиента для наследования
    is_abstract = models.BooleanField(
            null=False,
            default=False, 
            verbose_name='Признак абстрактного ингредиента для наследования',
            help_text='',
            )

    def save(self, *args, **kwargs):
        """ 
        Переопределение: запрещение изменения таблицы ings_product
        """
        raise Exception('Запрещено изменение таблицы ings_product!')

    def __str__(self):
        return self.ingredient + ' (абс.: ' + str(self.is_abstract) + ' ' + str(self.product_id) + ')'