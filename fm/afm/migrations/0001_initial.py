# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngsCategory',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Первичный ключ')),
                ('category', models.CharField(max_length=250, verbose_name='Категория ингредиента')),
            ],
            options={
                'managed': False,
                'verbose_name_plural': 'Категории ингредиентов',
                'db_table': 'ings_category',
                'ordering': ['category'],
                'verbose_name': 'Категории ингредиентов',
            },
        ),
    ]
