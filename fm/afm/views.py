# -*- coding: utf-8 -*- 
from django.shortcuts import render

from django.core.context_processors import csrf


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