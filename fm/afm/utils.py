# -*- coding: utf-8 -*- 


#import re
#import traceback

#from django.db import transaction

from afm.consts import RE_ONLY_ALPHA_AND_SPACE, RE_ONLY_ONE_SPACE


def str_clean_and_lowcase(astr):
    """ Очистка и преобразование строки к нижнему регистру """
    astr = RE_ONLY_ONE_SPACE.sub(' ', 
                RE_ONLY_ALPHA_AND_SPACE.sub('', astr.lower()))
    return astr.strip()
