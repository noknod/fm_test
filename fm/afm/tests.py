from django.test import TestCase

# Create your tests here.

#import django

from afm.models import WordNoun, WordAdjective, Product, ProductDetail, \
    Ingredient
from afm.dao.word import WordDAO, ProductDAO, IngredientDAO


word_dao = WordDAO(WordNoun, WordAdjective)
product_dao = ProductDAO(Product, ProductDetail)
ingredient_dao = IngredientDAO(Ingredient)

s1 = set(['перец', 'красный'])
s2 = set(['перец', 'чёрный', 'молотый'])
params = [s1, s2]

print('\nСлова')
params_ids = word_dao.search(params)
for params_id in params_ids:
   print(params_ids)

print('\nТовары')
products = product_dao.search(params_ids)
ingredient_list = []
for product in products:
   print(product)
   ingredient_list.append(product['product'])

print('\nИнгредиенты')
dummy_ingredients = set(ingredient_list)
ingredients = ingredient_dao.search(dummy_ingredients)
for ingredient in ingredients:
   print(ingredient)