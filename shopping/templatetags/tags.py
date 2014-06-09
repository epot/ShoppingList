'''
Created on 8 juin 2014

@author: epot
'''

import re

from django import template

register = template.Library()

@register.simple_tag()
def active(current_path, pattern):
    print '-----'
    print "path=" + current_path
    print "pattern=" + pattern
    if re.search(pattern, current_path):
        print 'slip'
        return 'active'
    return ''