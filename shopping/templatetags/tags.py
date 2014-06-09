'''
Created on 8 juin 2014

@author: epot
'''

import re

from django import template

register = template.Library()

@register.simple_tag()
def active(current_path, pattern):
    if re.search(pattern, current_path):
        return 'active'
    return ''