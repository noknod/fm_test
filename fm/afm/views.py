# -*- coding: utf-8 -*- 
from django.shortcuts import render, HttpResponse

from django.core.context_processors import csrf
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from afm.models import WordNoun, WordAdjective, Product, ProductDetail, \
    Ingredient
from afm.dao.word import WordDAO, ProductDAO, IngredientDAO
from afm.consts import RE_ONLY_ALPHA_AND_SPACE

word_dao = WordDAO(WordNoun, WordAdjective)
product_dao = ProductDAO(Product, ProductDetail)
ingredient_dao = IngredientDAO(Ingredient)


def index(request):
    template = 'fm_index.html'
    context = {}
    return render(request, template, context)


def ings_choose(request):
    if request.method == 'POST':
        method = request.POST.get('_method', None)
        if  method == 'DELETE':
            if 'reg_speciality' in request.session:
                del request.session['reg_speciality']
            return HttpResponseRedirect('/clinic/')
        else:
            reg_speciality = request.POST.get('speciality')
            if reg_speciality == BLANK_CHOICE[0]:
                request.session['reg_speciality'] = reg_speciality
                return HttpResponseRedirect('/clinic/registration/speciality/')
            request.session['reg_speciality'] = reg_speciality
            return HttpResponseRedirect('/clinic/registration/date/')
    else:
        template = 'fm_ings_choose.html'
        #if 'reg_speciality' in request.session:
        #    speciality = request.session['reg_speciality']
        #else:
        #    speciality = BLANK_CHOICE[0]
        #form = SpecialityChooseForm(FIND_ADMISSION_DAYS_AHEAD, 
        #        initial={'speciality': speciality})
        context = {}#'form': form}
        context.update(csrf(request))
        return render(request, template, context)


def ings_search(request):
    """ """
    if not request.is_ajax():
        return HttpResponse(status=400)
    if request.method != 'POST':
        return JsonResponse(data={"error": "Bad Request"}, status=400)
    data = request.POST.get('params', None)
    content = {'data': []}
    if data:
        params = []
        for astr in data.split(','):
            params.append(RE_ONLY_ALPHA_AND_SPACE.sub('', astr.lower()).split(' '))
        params_ids = word_dao.search(params)
        products = product_dao.search(params_ids)
        ingredient_list = []
        for product in products:
            ingredient_list.append(product['product'])
        dummy_ingredients = set(ingredient_list)
        ingredients = ingredient_dao.search(dummy_ingredients)
        for ingredient in ingredients:
            content['data'].append(ingredient)
    return JsonResponse(data=content, status=200)
