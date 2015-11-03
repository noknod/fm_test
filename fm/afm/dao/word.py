# -*- coding: utf-8 -*- 
#from afm.models import WordNoun, WordAdjective


class WordDAO(object):
    """ """

    def __init__(self, nouns, adjectives):
        """ """
        self.nouns = nouns
        self.adjectives = adjectives

    def search(self, search_param_list):
        """ """
        result = []
        for param in search_param_list:
            dummy = {}
            for word in self.nouns.objects.filter(noun__in=param):
                dummy[word.noun] = {'id': word.noun_id, 'type': 'noun'}
            for word in self.adjectives.objects.filter(adjective__in=param):
                dummy[word.adjective] = {'id': word.adjective_id, 
                    'type': 'adjective'}
            result.append(dummy)
        return result


class ProductDAO(object):
    """ """

    def __init__(self, products, details):
        """ """
        self.products = products
        self.details = details

    def search(self, noun_adjective_list):
        """ """
        result = []
        for words in noun_adjective_list:
            noun = None
            adjectives = []
            for word, info in words.items():
                if info['type'] == 'noun':
                    noun = info['id']
                else:
                    adjectives.append(info['id'])
            products = self.products.objects.filter(noun_id=noun)
            for product in products:
                good = True
                for adjective in adjectives:
                    if len(self.details.objects.filter(
                            product_id=product, adjective_id=adjective)) == 0:
                        good = False
                        break
                if good:
                    result.append({'params': words, 'product': product.product_id})
        return result


class IngredientDAO(object):
    """ """

    def __init__(self, ingredients):
        """ """
        self.ingredients = ingredients

    def search(self, ingredient_list):
        """ """
        ingredients = set(ingredient_list)
        result = []
        for ingredient in ingredients:
            info = self.ingredients.objects.filter(product_id=ingredient, is_abstract=False)
            for dummy in info:
                result.append({'id': dummy.product_id, 'ingredient': dummy.ingredient})
        return result